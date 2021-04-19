--list the following details of each employee: employee number, lasrt name, first name, sex, and salary.
SELECT e.emp_no, e.last_name, e.first_name, e.sex, s.salary
From employees as e
JOIN Salaries as s
ON e.emp_no=s.emp_no;


--List first name, last name, and hire date for employees who were hired in 1986.
SELECT first_name, last_name, hire_date
FROM employees
WHERE DATE_PART('year', hire_date) = 1986
GROUP BY first_name, last_name, hire_date;


--. List the manager of each department with the following information: 
--department number, department name, the manager's employee number, last name, first name.
SELECT dm.dept_no, dm.emp_no, d.dept_name, e.first_name, e.last_name
FROM Department_Managers as dm
LEFT JOIN departments as d 
ON dm.dept_no=d.dept_no
LEFT JOIN employees as e
ON dm.emp_no=e.emp_no;


--List the department of each employee with the following information: 
--employee number, last name, first name, and department name.
SELECT e.emp_no, e.last_name, e.first_name, de.dept_no, d.dept_name
FROM employees as e
INNER JOIN Department_Employees as de
ON e.emp_no=de.emp_no
INNER JOIN departments as d
ON d.dept_no=de.dept_no
GROUP BY dept_name, de.dept_no, e.emp_no, last_name, first_name;


--. List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."
SELECT first_name, last_name, sex FROM employees
WHERE first_name = 'Hercules' AND last_name like 'B%'
GROUP BY first_name, last_name, sex;


--List all employees in the Sales department, including their employee number, last name, first name, and department name.
SELECT e.emp_no, e.first_name, e.last_name, de.dept_no
FROM employees as e
LEFT JOIN Department_Employees as de
ON e.emp_no=de.emp_no
INNER JOIN departments as d
ON d.dept_no=de.dept_no
WHERE d.dept_name = 'Sales';



--List all employees in the Sales and Development departments, including their 
--employee number, last name, first name, and department name.
SELECT e.emp_no, e.first_name, e.last_name, de.dept_no
FROM employees as e
LEFT JOIN Department_Employees as de
ON e.emp_no=de.emp_no
INNER JOIN departments as d
ON d.dept_no=de.dept_no
WHERE d.dept_name in ('Sales', 'Development');


--In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
SELECT last_name, COUNT(*) AS freq_count
FROM employees
GROUP BY last_name
ORDER BY freq_count DESC;
