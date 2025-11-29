CREATE TABLE employees (
    emp_id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER 
);

INSERT INTO employees VALUES
(1, 'Amit', 'HR', 30000),
(2, 'Riya', 'HR', 35000),
(3, 'John', 'IT', 50000),
(4, 'Sara', 'IT', 55000),
(5, 'Mike', 'Finance', 45000);

SELECT 
    COUNT(*) AS total_employees,
    SUM(salary) AS total_salary,
    AVG(salary) AS average_salary,
    MAX(salary) AS highest_salary,
    MIN(salary) AS lowest_salary
FROM employees;

SELECT
    department,
    COUNT(*) AS emp_count,
    SUM(salary) AS total_salary,
    AVG(salary) AS avg_salary
FROM employees
GROUP BY department;