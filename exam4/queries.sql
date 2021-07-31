use tracker_ap4_ilyas_zinollin;
#1
SELECT p.name as project, SUM(i.fact_time) as sum FROM IssueStatus
INNER JOIN issues i on IssueStatus.issue_id = i.id
INNER JOIN projects p on i.project_id = p.id
WHERE i.executor_id = 2 AND status_id = 3 GROUP BY project ORDER BY sum DESC;


#2
SELECT t.type as type, SUM(i.fact_time) as sum FROM IssueStatus
INNER JOIN issues i on IssueStatus.issue_id = i.id
INNER JOIN type t on i.type_id = t.id
WHERE i.executor_id = 2 AND i.project_id = 4 AND status_id = 3 GROUP BY type ORDER BY sum DESC;

#3
SELECT e.name as name, SUM(i.fact_time) as sum FROM IssueStatus
INNER JOIN issues i on IssueStatus.issue_id = i.id
INNER JOIN employees e on i.executor_id = e.id
INNER JOIN EmployeesProjects EP on e.id = EP.employee_id
WHERE i.project_id = 1 AND EP.start_date >= '2020-01-01' AND EP.end_date <= '2020-03-15' AND status_id = 3
GROUP BY name ORDER BY sum DESC;

#4
SELECT p.name as project, SUM(i.fact_time) as hours FROM IssueStatus
INNER JOIN issues i on IssueStatus.issue_id = i.id
INNER JOIN projects p on i.project_id = p.id
GROUP BY project ORDER BY hours DESC LIMIT 3;

#5
SELECT p.name as project, COUNT(*) as qty FROM issues
INNER JOIN projects p on issues.project_id = p.id
GROUP BY project ORDER BY qty DESC;

#11
SELECT e.name as name, AVG(fact_time) as average_time FROM issues
INNER JOIN employees e on issues.executor_id = e.id
WHERE project_id = 4 GROUP BY name ORDER BY average_time DESC;