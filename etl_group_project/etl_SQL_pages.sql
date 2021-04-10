CREATE TABLE new_blockbuster (
    title TEXT PRIMARY KEY, 
    genre TEXT,
    rating TEXT,
    release_year INT,
    studio TEXT,
    worldwide_gross FLOAT
);
SELECT release_year, worldwide_gross
FROM new_blockbuster
LIMIT 10;
-- CREATE imdb TABLE
--------------------
CREATE TABLE new_imdb (
    title TEXT PRIMARY KEY,
    director TEXT,
    actors TEXT,
    rating FLOAT,
    votes INT,
    revenue_millions FLOAT,
    metascore FLOAT
);
SELECT title, revenue_millions
FROM new_imdb
LIMIT 10;
-- CREATE tmdb TABLE
--------------------
CREATE TABLE new_tmdb (
    title TEXT PRIMARY KEY,
    original_title TEXT,
    budget INT
);
SELECT title, budget
FROM new_tmdb
LIMIT 10;

SELECT b.title, b.genre, i.director, t.budget,
    b.release_year, b.worldwide_gross
FROM new_blockbuster b
INNER JOIN new_imdb i 
ON b.title = i.title
INNER JOIN new_tmdb t
ON i.title = t.title
ORDER BY b.worldwide_gross DESC
LIMIT 10;