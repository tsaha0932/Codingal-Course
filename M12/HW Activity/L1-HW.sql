CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT,
    Department TEXT,
    Salary REAL
);

INSERT INTO Employees (EmployeeID, FirstName, LastName, Department, Salary)
VALUES
(1, 'John', 'Doe', 'HR', 50000),
(2, 'Jane', 'Smith', 'IT', 70000),
(3, 'Bob', 'Johnson', 'IT', 65000),
(4, 'Alice', 'Brown', 'Finance', 60000);

SELECT * FROM Employees;

SELECT *
FROM Employees
WHERE Department = 'IT';
