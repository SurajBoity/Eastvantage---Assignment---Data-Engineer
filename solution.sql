SELECT 
    c.customer_id AS Customer,
    c.age AS Age,
    i.item AS Item,
    SUM(i.quantity) AS Quantity
FROM customers c
JOIN sales s ON c.customer_id = s.customer_id
JOIN items i ON s.sale_id = i.sale_id
WHERE c.age BETWEEN 18 AND 35
  AND i.quantity IS NOT NULL
GROUP BY c.customer_id, c.age, i.item
HAVING SUM(i.quantity) > 0
ORDER BY c.customer_id, i.item;
