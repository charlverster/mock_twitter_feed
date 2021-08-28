# Use official Mysql image
FROM mysql/mysql-server

# Copy .sql scipts into container. Scripts are automatically run on startup
COPY ./sql-scripts/ /docker-entrypoint-initdb.d/

# Expose port
EXPOSE 3306