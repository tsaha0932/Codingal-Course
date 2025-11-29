CREATE TABLE students (
    roll_no INT PRIMARY KEY,
    name VARCHAR(50),
    course VARCHAR(50),
    marks INT
);

INSERT INTO students VALUES
(1, 'Amit', 'BCA', 85),
(2, 'Riya', 'BBA', 78),
(3, 'John', 'BCA', 92),
(4, 'Sara', 'BCom', 88),
(5, 'Mike', 'BBA', 60);

UPDATE students
SET marks = 95
WHERE roll_no = 3;

DELETE FROM students
WHERE marks < 65;

SELECT *
FROM students
WHERE course = 'BCA';

SELECT *
FROM students
ORDER BY marks DESC;

SELECT name, course, marks
FROM students
WHERE marks > 80
ORDER BY marks DESC;