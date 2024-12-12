from typing import List

from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import and_, or_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload, selectinload

import models
import serializers
from db import Base, engine, get_db

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],  # Allows all origins. Specify domains for more control.
    allow_credentials=True,  # Allows cookies to be included in requests
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


# Initialize database tables
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Task 1
@app.get("/api/departments/", response_model=List[str])
async def get_department_codes(db: AsyncSession = Depends(get_db)):
    # replace with your code...
    return []


# Task 2
# Note: replace response_model=object with response_model=User once you've got this working
@app.get("/api/users/{username}", response_model=object)
async def get_users_by_username(
    username: str, db: AsyncSession = Depends(get_db)
):
    # replace with your code...
    return {}


# Task 3
@app.get("/api/courses/", response_model=List[serializers.Course])
async def get_courses(
    title: str = Query(None),
    instructor: str = Query(None),
    department: str = Query(None),
    hours: int = Query(None),
    db: AsyncSession = Depends(get_db),
):

    # base query to "courses" table that also asks SQLAlchemy
    # to join to the "instructors" and "locations" table.
    query = select(models.Course).options(
        selectinload(models.Course.instructors),
        selectinload(models.Course.location),
    )

    # includes a "title" filter if specified:
    if title:
        query = query.where(models.Course.title.ilike(f"%{title}%"))

    # includes a "department" filter if specified:
    if department:
        query = query.where(models.Course.department == department)

    # includes an "hours" filter if specified:
    if hours:
        query = query.where(models.Course.hours == hours)

    # includes an "instructors" filter if specified:
    if instructor:
        query = query.join(models.Course.instructors).where(
            or_(
                models.Instructor.last_name.ilike(f"%{instructor}%"),
                models.Instructor.first_name.ilike(f"%{instructor}%"),
            )
        )

    result = await db.execute(
        query.order_by(models.Course.department, models.Course.code)
    )
    courses = result.scalars().all()
    return courses


@app.delete(
    "/api/schedules/{schedule_id}/courses/{course_crn}",
    response_model=serializers.Schedule,
)
async def delete_course_from_schedule(
    schedule_id: int,
    course_crn: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(models.ScheduleCourse).where(
            and_(
                models.ScheduleCourse.course_crn == course_crn,
                models.ScheduleCourse.schedule_id == schedule_id,
            )
        )
    )
    schedule_course = result.scalar_one_or_none()
    if schedule_course is None:
        raise HTTPException(status_code=404, detail="Schedule not found")

    await db.delete(schedule_course)
    await db.commit()

    result = await db.execute(
        select(models.Schedule)
        .where(models.Schedule.id == schedule_id)
        .options(
            # also query for corresponding course data:
            selectinload(models.Schedule.courses).options(
                joinedload(models.Course.location),
                selectinload(models.Course.instructors),
            )
        )
    )
    schedule = result.scalar_one_or_none()
    return schedule


@app.get("/api/instructors/", response_model=List[serializers.Instructor])
async def get_instructors(db: AsyncSession = Depends(get_db)):

    result = await db.execute(
        select(models.Instructor).order_by(models.Instructor.last_name)
    )
    instructors = result.scalars().all()
    return instructors


@app.get("/api/users/", response_model=List[serializers.User])
async def get_users(db: AsyncSession = Depends(get_db)):

    result = await db.execute(
        select(models.User).order_by(models.User.username)
    )
    users = result.scalars().all()  # Extract distinct department names
    return users


@app.get("/api/schedules/", response_model=List[serializers.Schedule])
async def read_schedule(db: AsyncSession = Depends(get_db)):

    # this query is tricky. It's basically saying that when you query
    # the schedules table, also query for the cooresponding courses and
    # also the location and instructors associated with those courses:
    result = await db.execute(
        select(models.Schedule).options(
            selectinload(models.Schedule.courses).options(
                joinedload(models.Course.location),
                selectinload(models.Course.instructors),
            )
        )
    )
    schedules = result.scalars().all()
    return schedules


# @app.post("/api/schedules/", response_model=serializers.Schedule)
# async def create_schedule(
#     schedule: serializers.ScheduleCreate,
#     user_id: int,
#     db: AsyncSession = Depends(get_db),
# ):
#     # Fetch the user
#     result = await db.execute(
#         select(models.User).where(models.User.id == user_id)
#     )
#     user = result.scalar_one_or_none()
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")

#     # Create a new schedule
#     new_schedule = models.Schedule(name=schedule.name, user_id=user_id)
#     db.add(new_schedule)

#     await db.commit()
#     return new_schedule


@app.get("/api/schedules/{username}", response_model=serializers.Schedule)
async def read_schedule_by_username(
    username: str, db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(models.Schedule)
        .join(models.Schedule.user)  # Join the related User table
        .where(models.User.username == username)  # Filter by username
        .options(
            # also query for corresponding course data:
            selectinload(models.Schedule.courses).options(
                joinedload(models.Course.location),
                selectinload(models.Course.instructors),
            )
        )
    )
    schedule = result.scalar_one_or_none()
    if schedule is None:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return schedule


@app.post(
    "/api/schedules/{schedule_id}/courses", response_model=serializers.Schedule
)
async def add_course_to_schedule(
    schedule_id: int,
    course_data: serializers.SchedulCourseCreate,
    db: AsyncSession = Depends(get_db),
):

    # 1. Validate schedule exists
    schedule_result = await db.execute(
        select(models.Schedule).where(models.Schedule.id == schedule_id)
    )
    schedule = schedule_result.scalar_one_or_none()
    if schedule is None:
        raise HTTPException(status_code=404, detail="Schedule not found")

    # 2. Validate course exists
    course_result = await db.execute(
        select(models.Course).where(models.Course.crn == course_data.crn)
    )
    course = course_result.scalar_one_or_none()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    # 3. Check if the course is already in the schedule
    schedule_course_result = await db.execute(
        select(models.ScheduleCourse).where(
            models.ScheduleCourse.schedule_id == schedule_id,
            models.ScheduleCourse.course_crn == course_data.crn,
        )
    )
    existing_schedule_course = schedule_course_result.scalar_one_or_none()
    if existing_schedule_course:
        raise HTTPException(
            status_code=400, detail="Course already in schedule"
        )

    # Create new ScheduleCourse entry
    new_schedule_course = models.ScheduleCourse(
        schedule_id=schedule_id,
        course_crn=course_data.crn,
    )
    db.add(new_schedule_course)
    await db.commit()

    # Reload schedule with courses
    result = await db.execute(
        select(models.Schedule)
        .where(models.Schedule.id == schedule_id)
        .options(
            # also query for corresponding course data:
            selectinload(models.Schedule.courses).options(
                joinedload(models.Course.location),
                selectinload(models.Course.instructors),
            )
        )
    )
    schedule = result.scalar_one_or_none()
    return schedule
