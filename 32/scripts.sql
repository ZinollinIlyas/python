use educational_center;
#1
SELECT COUNT(*) as students_qty, c.name as course, '' as groupp FROM StudentsCourses
INNER JOIN groupps g on StudentsCourses.group_id = g.id INNER JOIN courses c on g.course_id = c.id
WHERE c.id = 1 AND start_date = '2021-03-22' AND end_date IS NULL
UNION
SELECT COUNT(*) as students_qty, c.name as course, g.name as groupp FROM StudentsCourses
INNER JOIN groupps g on StudentsCourses.group_id = g.id INNER JOIN courses c on g.course_id = c.id
WHERE c.id = 1 AND start_date = '2021-03-22' AND end_date IS NULL GROUP BY g.name ORDER BY groupp;

#2
SELECT c.name as course, COUNT(*) as qty, g.name as groupp FROM StudentsCourses
INNER JOIN groupps g on StudentsCourses.group_id = g.id
INNER JOIN courses c on g.course_id = c.id
WHERE c.id = 1 AND is_finished = 0 and start_date = '2021-03-22' AND end_date < '2022-03-22' GROUP BY groupp;

#3
SELECT c.name as course, COUNT(*) as qty FROM StudentsCourses
INNER JOIN groupps g on StudentsCourses.group_id = g.id
INNER JOIN courses c on g.course_id = c.id WHERE start_date between '2020-01-01' AND '2022-12-31'
GROUP BY course ORDER BY course;

#4
SELECT g.name as groupp, COUNT(*) as qty FROM StudentsCourses
INNER JOIN groupps g on StudentsCourses.group_id = g.id
INNER JOIN courses c on g.course_id = c.id
WHERE c.id = 1 AND start_date BETWEEN '2020-01-01' AND '2022-12-31' GROUP BY groupp ORDER BY groupp;

#5
SELECT g.name as groupp, COUNT(*) as qty FROM StudentsCourses
INNER JOIN groupps g on StudentsCourses.group_id = g.id
WHERE g.id = 1
AND start_date < '2021-04-15' AND (end_date > '2021-04-15' OR end_date IS NULL) AND is_finished = 0
GROUP BY groupp ORDER BY groupp;

#6
SELECT c.name as course, g.name as groupp, COUNT(*) as qty FROM StudentsCourses
INNER JOIN groupps g on StudentsCourses.group_id = g.id
INNER JOIN courses c on g.course_id = c.id
WHERE is_finished = 0 AND end_date IS NOT NULL
GROUP BY groupp, course ORDER BY groupp;

#7
SELECT g.name as groupp, COUNT(*) as qty FROM StudentsCourses
INNER JOIN groupps g on StudentsCourses.group_id = g.id
INNER JOIN courses c on g.course_id = c.id
WHERE c.id = 2 AND is_finished = 1 AND end_date < '2022-01-01' GROUP BY groupp ORDER BY groupp;

#8
SELECT s.name as name, s.surname as surname, c.name as course, g.name as groupp, start_date, end_date FROM StudentsCourses
INNER JOIN groupps g on StudentsCourses.group_id = g.id
INNER JOIN courses c on g.course_id = c.id
INNER JOIN students s on student_id = s.id
INNER JOIN (Select student_id from StudentsCourses GROUP BY student_id HAVING COUNT(student_id)>1)
    as b ON b.student_id = s.id
WHERE start_date <= '2020-01-20' AND end_date >= '2020-01-20';

#9
SELECT g.name as groupp, c.name as course, COUNT(*) as qty FROM StudentsCourses
INNER JOIN groupps g on StudentsCourses.group_id = g.id
INNER JOIN courses c on g.course_id = c.id
WHERE is_finished = 0 AND end_date IS NOT NULL AND start_date < '2021-07-16' GROUP BY course, groupp;

#10
SELECT c.name as course, COUNT(*) as qty FROM StudentsCourses
INNER JOIN groupps g on StudentsCourses.group_id = g.id
INNER JOIN courses c on g.course_id = c.id
WHERE is_finished = 1 AND end_date < '2021-07-16' GROUP BY course;