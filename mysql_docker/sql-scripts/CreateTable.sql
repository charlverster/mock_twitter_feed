-- Create the users table
CREATE TABLE users 
(
    username VARCHAR(30) PRIMARY KEY
    -- Use user name as primary key. 
    -- Assuming all user names are unique
    -- Assuming names are no longer than 30 characters
);

-- Create the follows table
CREATE TABLE follows
(
    username VARCHAR(30) NOT NULL REFERENCES users(username),   -- User name
    follows_user VARCHAR(30) NOT NULL REFERENCES users(username), -- Name of friend they follow
    PRIMARY KEY (username, follows_user)
);

-- Create the posts table
CREATE TABLE posts
(
    post_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(30) NOT NULL REFERENCES users(username),
    post VARCHAR(140)
) ;