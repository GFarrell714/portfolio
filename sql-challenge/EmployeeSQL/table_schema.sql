drop table Titles;

create table Titles (
		create_title_id varchar(50) primary key,
		title varchar(50) not null
);

select * from Titles;

drop table employees;

create table employees (
		emp_no int primary key,
        emp_title_id varchar(50) not null,
		birth_date date,
		first_name varchar(255),
		last_name varchar(255),
		sex varchar(20),
		hire_date date,
		foreign key (emp_title_id) references Titles (create_title_id)
);


select * from employees

drop table departments;

create table departments (
		dept_no varchar(50) primary key,
		dept_name varchar(50)
);

select * from departments;

drop table Department_Employees;

create table Department_Employees (
		emp_no int,
		dept_no varchar(50),
		foreign key (dept_no) references departments (dept_no)
);

select * from Department_Employees;

drop table Salaries;

create table Salaries (
		emp_no int primary key,
		salary int
);

select * from Salaries;

drop table Departmnent_Managers;

create table Department_Managers (
		dept_no varchar(50),
		emp_no int,
		foreign key (dept_no) references departments (dept_no)
);

select * from Department_Managers;