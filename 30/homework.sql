#First task
SELECT YEAR(action_date) as year, CASE Month(action_date)
WHEN 1 then 'январь'
WHEN 2 then 'февраль'
WHEN 3 then 'март'
WHEN 4 then 'апрель'
WHEN 5 then 'май'
WHEN 6 then 'июнь'
WHEN 7 then 'июль'
WHEN 8 then 'август'
WHEN 9 then 'сентябрь'
WHEN 10 then 'октябрь'
WHEN 11 then 'ноябрь'
WHEN 12 then 'декабрь'
END AS
 month, DATE(action_date) as date, SUM(price * qty) as total
FROM actions GROUP BY year, month, date ORDER BY date;

#Second task
SELECT s.supplier, '' as year, '' as category, SUM(qty * price) as price FROM actions INNER JOIN suppliers s on actions.supplier_id = s.id
GROUP BY s.supplier
UNION
SELECT s.supplier, YEAR(action_date) as year, '' as category, SUM(price * qty) as price FROM actions INNER JOIN suppliers s on actions.supplier_id = s.id
GROUP BY s.supplier, YEAR(action_date)
UNION
SELECT s.supplier, YEAR(action_date) as year, c.category as category, SUM(actions.price * qty) as price FROM actions INNER JOIN suppliers s on actions.supplier_id = s.id
INNER JOIN products p on actions.product_id = p.id INNER JOIN categories c on p.category_id = c.id
GROUP BY s.supplier, YEAR(action_date), category ORDER BY year;
