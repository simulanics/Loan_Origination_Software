-- Load initial data for the Users table
\copy Users FROM 'users.csv' WITH DELIMITER ',' CSV HEADER;

-- Similarly for other tables
\copy Borrowers FROM 'borrowers.csv' WITH DELIMITER ',' CSV HEADER;
\copy Properties FROM 'properties.csv' WITH DELIMITER ',' CSV HEADER;
\copy Loans FROM 'loans.csv' WITH DELIMITER ',' CSV HEADER;
\copy Conditions FROM 'conditions.csv' WITH DELIMITER ',' CSV HEADER;
\copy Liabilities FROM 'liabilities.csv' WITH DELIMITER ',' CSV HEADER;
