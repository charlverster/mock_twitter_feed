# Use official Mysql image
FROM mysql/mysql-server

# Set a password
# ENV MYSQL_ROOT_PASSWORD twitter_password

# # Add a database
# ENV MYSQL_DATABASE twitter

# Add the content of the sql-scripts/ directory to your image
# All scripts in docker-entrypoint-initdb.d/ are automatically
# executed during container startup

COPY ./sql-scripts/ /docker-entrypoint-initdb.d/

EXPOSE 3306