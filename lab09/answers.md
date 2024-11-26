## SQL Questions
1. SELECT - Retrieving Data. Write a query to list the titles and release years of all movies in the film table.

SELECT title, release_year
FROM film;




2. WHERE - Filtering Data. Write a query to find all customers whose last name starts with the letter 'S'.

SELECT *
FROM customer
WHERE last_name LIKE 'S%';



3. ORDER BY - Sorting Results. List all films titles and their durations, sorted by their rental duration in descending order. If two films have the same rental duration, sort them alphabetically by title.

SELECT title, rental_duration
FROM film
ORDER BY rental_duration DESC, title ASC;



4. JOIN - Combining Tables. Write a query to list all films along with their categories. Show the film title and category name.

SELECT f.title, c.name AS category_name
FROM film f
INNER JOIN film_category fc ON f.film_id = fc.film_id
INNER JOIN category c ON fc.category_id = c.category_id;



5. AGGREGATE FUNCTIONS - Summarizing Data. Write a query to find the average rental duration for movies in each category.

SELECT c.name AS category_name, AVG(f.rental_duration) AS average_rental_duration
FROM film f
INNER JOIN film_category fc ON f.film_id = fc.film_id
INNER JOIN category c ON fc.category_id = c.category_id
GROUP BY c.name;



6. COUNT - Counting Rows. Write a query to count how many films are in the Action category.

SELECT COUNT(*) AS action_films_count
FROM film f
INNER JOIN film_category fc ON f.film_id = fc.film_id
INNER JOIN category c ON fc.category_id = c.category_id
WHERE c.name = 'Action';



7. INSERT - Adding Data. Insert a new customer into the customer table. The new customer should have a first name, last name, email, and be linked to an existing store.

INSERT INTO customer (first_name, last_name, email, store_id, create_date)
VALUES ('John', 'Doe', 'johndoe@example.com', 1, CURRENT_TIMESTAMP);



8. UPDATE - Modifying Data. Update the rental rate of all films in the Comedy category, increasing it by 10%.

UPDATE film
SET rental_rate = rental_rate * 1.10
WHERE film_id IN (
    SELECT f.film_id
    FROM film f
    INNER JOIN film_category fc ON f.film_id = fc.film_id
    INNER JOIN category c ON fc.category_id = c.category_id
    WHERE c.name = 'Comedy'
);



9. DELETE - Removing Data. Write a query to delete all films that have never been rented. Make sure to use a subquery to identify the films that haven't been rented.

DELETE FROM film
WHERE film_id NOT IN (
    SELECT DISTINCT film_id
    FROM inventory i
    INNER JOIN rental r ON i.inventory_id = r.inventory_id
);


10. CREATE TABLE & ALTER TABLE - Managing Database Structure. Create a new table called movie_reviews with columns for review_id, film_id, reviewer_name, rating, and comments. Then, add a foreign key constraint linking film_id to the film table.

-- Create the table
CREATE TABLE movie_reviews (
    review_id SERIAL PRIMARY KEY,
    film_id INT NOT NULL,
    reviewer_name VARCHAR(100),
    rating INT CHECK (rating BETWEEN 1 AND 5),
    comments TEXT
);

-- Add a foreign key constraint
ALTER TABLE movie_reviews
ADD CONSTRAINT fk_film
FOREIGN KEY (film_id)
REFERENCES film (film_id);



## SQLAlchemy Questions

1. Understanding SQLAlchemy Automap: How do you think the `AutoModels` class works to dynamically generate SQLAlchemy ORM models from the database schema?

 The AutomapBase.prepare() method queries the database for metadata, such as table names, columns, and relationships. It generates Python classes corresponding to the tables, populating attributes and relationships based on the schema.


2. Async Database Operations: Explain the use of asynchronous database sessions in this script. Why does the script use AsyncSession instead of a regular Session, and how does this improve the efficiency of database operations?

Asynchronous database sessions enable non-blocking interaction with the database. Asynchronous operations such as queries allow other tasks to execute while waiting for the database response, improving scalability in I/O-bound applications like web servers.
The script uses AsyncSession over a regular Session because it’s designed for applications needing efficient resource usage and concurrency, such as those with high request volumes. It avoids blocking the event loop during database operations.


3. SQLAlchemy Query Construction: In the `model_examples` function, there is a query that selects all customers whose last names start with the letter "P". See if you can write another questy that selects customers whose first name ends with the letters "n" or "a" using SQLAlchemy syntax.




4. In the `raw_sql_examples` function, there are two ways to execute SQL queries: directly via the engine using conn.execute() and using an ORM session with session.execute(). Discuss the pros and cons of executing raw SQL directly compared to using SQLAlchemy’s ORM methods.
Hint: Consider the trade-offs in terms of readability, safety (e.g., SQL injection risks), and flexibility when using raw SQL versus ORM abstractions.
Executing SQL queries via conn.execute() (raw SQL) and session.execute() (ORM) represents two approaches with distinct trade-offs:

Raw SQL via conn.execute()
Pros:
Direct control over the SQL, enabling execution of complex queries, stored procedures, or database-specific features.
Useful for tasks that are cumbersome to express in ORM.
Cons:
Higher risk of SQL injection if user input isn’t sanitized properly.
Less portable since the query might rely on database-specific syntax.
ORM Abstractions via session.execute()
Pros:
Abstracts SQL generation, making queries more readable and maintainable.
Safer from SQL injection as SQLAlchemy automatically handles parameterized queries.
Integrates well with the ORM’s features, like session management and relationships.
Cons:
Slightly less flexibility for extremely complex or database-specific queries.
Potential performance overhead compared to raw SQL in certain cases.
Trade-offs: Use ORM for most queries due to its readability and safety, but leverage raw SQL for specific cases requiring direct database interaction or advanced optimization.
