CREATE TABLE sales (
    sale_id INTEGER,
    product TEXT,
    category TEXT,
    quantity INTEGER,
    price INTEGER
);

INSERT INTO sales VALUES
(1, 'Laptop', 'Electronics', 2, 40000),
(2, 'Mouse', 'Electronics', 5, 500),
(3, 'Shirt', 'Clothing', 3, 1200),
(4, 'Jeans', 'Clothing', 2, 2500),
(5, 'Headphones', 'Electronics', 4, 1500),
(6, 'Shoes', 'Footwear', 2, 3000),
(7, 'Sandals', 'Footwear', 3, 1200);

SELECT
    category,
    SUM(quantity) AS total_quantity,
    SUM(price * quantity) AS total_sales,
    AVG(price) AS avg_price,
    MAX(price) AS max_price
FROM sales
WHERE price > 1000                   
GROUP BY category                      
HAVING SUM(price * quantity) > 5000  
ORDER BY total_sales DESC;         