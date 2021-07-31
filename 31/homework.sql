# First task
SELECT supplier FROM suppliers
WHERE id IN (
  SELECT supplier_id FROM actions
    WHERE Year(action_date) = 2016
    GROUP BY supplier_id
    HAVING SUM(qty*price) > (
    SELECT SUM(qty*price)
        FROM actions
        WHERE Year(action_date) = 2016
        AND supplier_id = (
      SELECT id FROM suppliers
            WHERE supplier = 'IDT'
        )
    )
);

#Second task
SELECT product
FROM products
WHERE NOT EXISTS (SELECT product_id FROM actions WHERE actions.product_id = products.id AND supplier_id IN
    (SELECT id FROM suppliers WHERE supplier = 'IDT'));


#Third task
SELECT category FROM categories WHERE id IN
    (SELECT category_id FROM products WHERE id IN
        (SELECT product_id FROM actions WHERE
            MONTH(action_date) BETWEEN 6 AND 8 AND YEAR(action_date) = 2016 AND supplier_id IN
                (SELECT id FROM suppliers WHERE supplier = 'IDT')));