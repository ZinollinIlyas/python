USE study_database;

# First task
SELECT product, date(action_date) as date, qty as quantity, (actions.price * actions.qty) as sum FROM actions
INNER JOIN products ON product_id = products.id INNER JOIN categories ON products.category_id = categories.id
WHERE categories.category = 'Monitors' AND action_date < '2017/01/01' ORDER BY qty DESC LIMIT 5;

# Second task
SELECT action_date as date, product, supplier, qty as quantity, actions.price FROM actions
INNER JOIN products on actions.product_id = products.id
INNER JOIN suppliers on actions.supplier_id = suppliers.id
WHERE action_date BETWEEN '2016/01/01' AND '2016/01/31' ORDER BY action_date DESC;

# Third task
SELECT DISTINCT product FROM products INNER JOIN actions a on products.id = a.product_id
WHERE a.action_date BETWEEN '2017/01/01' AND '2017/12/31';