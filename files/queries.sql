CREATE TABLE companies (
company_id SERIAL PRIMARY KEY,
company_name VARCHAR(100) NOT NULL
);

CREATE TABLE vacancies (
vacancy_id SERIAL PRIMARY KEY,
company_id INTEGER REFERENCES companies (company_id) ON DELETE CASCADE,
vacancy_name VARCHAR(100) NOT NULL,
vacancy_url VARCHAR(100) NOT NULL,
vacancy_salary_from INT,
vacancy_salary_to INT,
vacancy_address VARCHAR(100),
CONSTRAINT chk_salary_from CHECK(vacancy_salary_from >= 0),
CONSTRAINT chk_salary_to CHECK(vacancy_salary_to >= 0)
);

SELECT company_name, COUNT(*) FROM companies
INNER JOIN vacancies USING (company_id)
GROUP BY company_name
ORDER BY company_name;

SELECT company_name, vacancy_name,
vacancy_salary_from, vacancy_salary_to, vacancy_url  FROM vacancies
INNER JOIN companies USING (company_id)
ORDER BY company_name;

SELECT AVG(vacancy_salary_from)::numeric(10,0) FROM vacancies;

SELECT vacancy_name, vacancy_salary_from FROM vacancies
WHERE vacancies.vacancy_salary_from <> 0 AND vacancy_salary_from > (SELECT AVG(vacancy_salary_from) FROM vacancies)
ORDER BY vacancy_salary_from DESC;

SELECT * FROM vacancies
WHERE vacancy_name LIKE '%python%';