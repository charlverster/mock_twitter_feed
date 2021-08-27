
CREATE USER 'db_engineer'@'%' IDENTIFIED BY 'twitter_password';

GRANT ALL PRIVILEGES ON twitter. * TO 'db_engineer'@'%';