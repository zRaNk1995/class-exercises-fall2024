## SQL Questions
1. SELECT - Retrieving Data. Write a query to list the titles and release years of all movies in the film table.




2. WHERE - Filtering Data. Write a query to find all customers whose last name starts with the letter 'S'.




3. ORDER BY - Sorting Results. List all films titles and their durations, sorted by their rental duration in descending order. If two films have the same rental duration, sort them alphabetically by title.




4. JOIN - Combining Tables. Write a query to list all films along with their categories. Show the film title and category name.




5. AGGREGATE FUNCTIONS - Summarizing Data. Write a query to find the average rental duration for movies in each category.




6. COUNT - Counting Rows. Write a query to count how many films are in the Action category.




7. INSERT - Adding Data. Insert a new customer into the customer table. The new customer should have a first name, last name, email, and be linked to an existing store.




8. UPDATE - Modifying Data. Update the rental rate of all films in the Comedy category, increasing it by 10%.




9. DELETE - Removing Data. Write a query to delete all films that have never been rented. Make sure to use a subquery to identify the films that haven't been rented.



10. CREATE TABLE & ALTER TABLE - Managing Database Structure. Create a new table called movie_reviews with columns for review_id, film_id, reviewer_name, rating, and comments. Then, add a foreign key constraint linking film_id to the film table.




## SQLAlchemy Questions

1. Understanding SQLAlchemy Automap: How do you think the `AutoModels` class works to dynamically generate SQLAlchemy ORM models from the database schema?



2. Async Database Operations: Explain the use of asynchronous database sessions in this script. Why does the script use AsyncSession instead of a regular Session, and how does this improve the efficiency of database operations?



3. SQLAlchemy Query Construction: In the `model_examples` function, there is a query that selects all customers whose last names start with the letter "P". See if you can write another questy that selects customers whose first name ends with the letters "n" or "a" using SQLAlchemy syntax.



4. In the `raw_sql_examples` function, there are two ways to execute SQL queries: directly via the engine using conn.execute() and using an ORM session with session.execute(). Discuss the pros and cons of executing raw SQL directly compared to using SQLAlchemy’s ORM methods.
Hint: Consider the trade-offs in terms of readability, safety (e.g., SQL injection risks), and flexibility when using raw SQL versus ORM abstractions.