CREATE TABLE IF NOT EXITS movies (
  MOVIE_NAME TEXT,
  GENRE TEXT,
  RATING REAL 
);

INSERT INTO movies ( MOVIE_NAME, GENRE, RATING) VALUES
 ('The Fault in our Stars', 'Romance', 4),
 ('My Oxford Year', 'Romance', 4),
 ('Goosebumps', 'Horror', 3),
 ('The Tearsmith', 'Drama', 3),
 ('The Idea of You', 'Romance', 4),
 ('The Woman in Cabin 10', 'Thriller', 3.5);

SELECT * FROM movies;

