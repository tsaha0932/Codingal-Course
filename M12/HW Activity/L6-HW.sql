CREATE TABLE Employees (
    EmpID INT,
    EmpName VARCHAR(50),
    Department VARCHAR(50),
    City VARCHAR(50),
    Salary INT
);

SELECT DISTINCT EmpName, City, Salary
FROM Employees
WHERE City LIKE '%a%'            
  AND Salary BETWEEN 40000 AND 90000
  AND EmpName LIKE '_a%'        
ORDER BY Salary ASC, EmpName;
