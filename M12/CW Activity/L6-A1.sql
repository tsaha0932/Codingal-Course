---Create the nomnom table if it does not exist
CREATE TABLE IF NOT EXISTS nomnom (
  NAME TEXT,
  NEIGHBOURHOOD TEXT,
  CUISNE TEXT,
  REVIEW REAL,
  PRICE TEXT,
  HEALTH TEXT 
);

--Insert sample data into the nomnom table
INSERT INTO nomnom (NAME, NEIGHBOURHOOD, CUISNE, REVIEW, PRICE, HEALTH) VALUES
 ('Peter', 'Brooklyn', 'Steak', 4.4, '$$$$', 'A'),
 ('Jongro', 'Midtown', 'Korean', 3.5, '$$', 'A'),
 ('Pocha', 'Midtown', 'Pizza', 4, '$$$', 'B'),
 ('Lighthouse', 'Queens', 'Chinese', 3.9, '$', 'A'),
 ('Minica', 'Downtown', 'American', 4.6, '$$$', ''),
 ('Marea', 'Chinatown', 'Chinese', 3.0, '$$', ''),
 ('Dirty Candy', 'Uptown', 'Italian', 4.9, '$$$$', 'B'),
 ('Di Fara Pizza', 'Brooklyn', 'Pizza', 3.8, '$$$', 'A'),
 ('Golden Unicorn', 'Uptown', 'Italian', 3.8, '$$', 'A');

--Select all records from the nomnom table
SELECT * FROM nomnom;

--Select distinct neighbourhoods from the nomnom table
SELECT DISTINCT NEIGHBOURHOOD FROM nomnom;

--Select distinct cuisines from the nomnom table
SELECT DISTINCT CUISNE FROM nomnom;

--Select all records with Chinese cuisine
SELECT * FROM nomnom WHERE CUISINE = 'Chinese';

--Select all records with a review rating of 4 or higher
SELECT * FROM nomnom WHERE REVIEW >= 4;

--Select all records with italian cuisine and $$$ price
SELECT * FROM nomnom WHERE CUISNE = 'Italian' AND PRICE = '$$$';

--Select all records where the name contains 'Candy'
SELECT * FROM nomnom WHERE NAME LIKE '%Candy%';

--Select all records where the neighbourhood is Midtown, Downtown, or Chinatown
SELECT * FROM nomnom
WHERE NEIGHBOURHOOD IN ('Midtown', 'Downtown', 'Chinatown');

--Select the top 4 records ordered by review rating in descending order
SELECT * FROM nomnom ORDER BY REVIEW DESC LIMIT 4;