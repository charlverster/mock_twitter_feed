CREATE TABLE users
(
    UserID INT NOT NULL PRIMARY KEY,
    UserName text
);
CREATE TABLE follows
(
    UserID INT NOT NULL REFERENCES Users(UserID),
    FollowsID INT NOT NULL REFERENCES Users(UserID),
    PRIMARY KEY (UserID, FollowsID)
);
CREATE TABLE posts
(
    PostID INT PRIMARY KEY,
    UserID INT NOT NULL REFERENCES Users(UserID),
    Content text
) ;