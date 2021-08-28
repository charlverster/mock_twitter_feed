-- Create a user that can access the database remotely
CREATE USER 'db_engineer'@'%' IDENTIFIED BY 'twitter_password';
-- Grant the user permissions
GRANT ALL PRIVILEGES ON twitter. * TO 'db_engineer'@'%';