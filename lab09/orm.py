import asyncio

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from sqlalchemy.schema import MetaData
from sqlalchemy.sql import text

PORT = "5433"


class AutoModels:
    def __init__(self, engine):
        self._base = None
        self._engine = engine

    async def get(self, table_name: str):
        if not self._base:
            await AutoModels._async_init()
        return getattr(self._base.classes, table_name, None)

    async def _async_init(self):
        async with self._engine.connect() as conn:
            metadata = MetaData()
            await conn.run_sync(metadata.reflect)
            self._base = automap_base(metadata=metadata)
            self._base.prepare()

    @staticmethod
    async def create(engine):
        instance = AutoModels(engine)
        await instance._async_init()
        return instance


async def model_examples(engine):
    auto_models = await AutoModels.create(engine)

    # These are now data models (aka "classes") with which you can
    # interact
    # Actor = await auto_models.get("actor")
    # Address = await auto_models.get("address")
    # Category = await auto_models.get("category")
    # City = await auto_models.get("city")
    # Country = await auto_models.get("country")
    # FilmCategory = await auto_models.get("film_category")
    # Inventory = await auto_models.get("inventory")
    # Language = await auto_models.get("language")
    # Payment = await auto_models.get("payment")
    # Rental = await auto_models.get("rental")
    # Staff = await auto_models.get("staff")
    # Store = await auto_models.get("store")

    Customer = await auto_models.get("customer")
    Film = await auto_models.get("film")
    FilmActor = await auto_models.get("film_actor")

    # Print the title and description of every film in the database
    async with AsyncSession(engine) as session:
        films = await session.execute(select(Film))
        for film in films.scalars().all():
            print(f"{film.title}: {film.description}")

    # Print the last_name of all customers whose last name starts
    # with "P"
    async with AsyncSession(engine) as session:
        customers = await session.execute(
            select(Customer).where(Customer.last_name.startswith("P"))
        )
        for customer in customers.scalars().all():
            print(customer.last_name)

    # Print the email address of the first active user we find
    async with AsyncSession(engine) as session:
        customers = await session.execute(
            select(Customer).where(Customer.active == 1)
        )
        first_customer = customers.scalars().first()
        print(first_customer.email)

    # Print the name and phone number of all the inactive customers
    async with AsyncSession(engine) as session:
        customers = await session.execute(
            select(Customer)
            .options(joinedload(Customer.address))
            .where(Customer.active == 0)
        )
        for customer in customers.scalars().all():
            print(
                f"{customer.first_name} {customer.last_name}: {customer.address.phone}"
            )

    # List the actors/actresses in 5 films
    async with AsyncSession(engine) as session:
        films = await session.execute(
            select(Film)
            .options(
                joinedload(Film.film_actor_collection).joinedload(
                    FilmActor.actor
                )
            )
            .limit(5)
        )

        for film in films.scalars().unique():
            print(f"{film.title}:")
            for film_actor in film.film_actor_collection:
                print(
                    f"   {film_actor.actor.first_name} {film_actor.actor.last_name}"
                )

    # Print the name and city of all inactive customers
    # Print the name and description of all the horror movies


async def raw_sql_examples(engine):
    # Basic async SQL query directly via the engine
    async with engine.connect() as conn:
        results = await conn.execute(
            text("SELECT first_name FROM customer LIMIT 10")
        )
        # print the first data field value for the first 5 results:
        for result in results[5]:
            print(result[0])

    # Basic async SQL query via the ORM session
    stmt = text(
        "SELECT * FROM customer WHERE first_name > 'a' AND first_name < 'b'"
    )
    async with AsyncSession(engine) as session:
        results = await session.execute(stmt)
        # print first 5 results:
        for result in results[:5]:
            print(result)


async def main():
    # set echo=True if you want to see how your queries are being
    # translated into SQL
    engine = create_async_engine(
        f"postgresql+asyncpg://postgres:postgres@localhost:{PORT}/dvdrental"
    )

    # await raw_sql_examples(engine)
    await model_examples(engine)


if __name__ == "__main__":
    asyncio.run(main())
