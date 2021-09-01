# Mock Twitter Feed

This is a Python program that imitates twitter and displayed a mock twitter feed in the console. 

## Description

* The program looks for two text files inside the folder `files` in the working directory, such as `user.txt` and `tweet.txt`. 

* `user.txt` containts a list of users and the people they follow. 
```
Ward follows Alan
Alan follows Martin
Ward follows Martin, Alan
```
`tweet.txt` contains a list of tweets posted by the users. 
```
Alan> If you have a procedure with 10 parameters, you probably missed some.
Ward> There are only two hard things in Computer Science: cache invalidation, naming things and off-by-1 errors.
Alan> Random numbers should not be generated with a method chosen at random.

```

* The program extracts the list of users and tweets, and then prints to console each user's name, their tweets and their followers tweets in the format:

```
user_A
    @user_A: Post
    @followee_A: Post
user_B
    @followee_B: Post
    @followee_B: Post
    @userB: Post
```
where:
* "Followee" is someone the user follows,
* Users are sorted alphabetically, and
* Posts are sorted in the order they appear in the file.

The user and tweet data is stored in a MySQL database that runs in a separate docker container. 

## Getting Started

### Dependencies

- To combat [Works On My Machine](https://www.leadingagile.com/2017/03/works-on-my-machine/) the python app runs from a dockerized Ubuntu container. Install Docker Desktop for your host machine from [the Docker website](https://www.docker.com/products/docker-desktop).
- Docker-compose is required.

### Installing

- Clone this repository to your machine.
- In your terminal, navigate to the `mysql_docker` folder where the `Dockerfile` is and build the dockerfile with:
```
docker build -t mysqlserver .
```
This builds the MySql docker image and runs the scripts inside the `mysql_docker/sql-scripts` folder to set up the MySQL database. 

- In your terminal, navigate to the `src` folder where the `Dockerfile` is and build Ubuntu dockerfile with:
```
docker build -t ubuntu_container .
```

- In your terminal, navigate back to the main directory where the `docker-compose.yml` file is and run the docker containers with:
```
docker-compose up -d
``` 
- The docker-compose file creates a folder `files` in the current working directory and maps it to the docker container. Place the `user.txt` and `tweet.txt` files you would like to use as input files in this directory. 
- Sample files are included. 

### Executing program

- Run the python app with: 
```
python3 app/main.py {user_file} {tweet_file}
```
where
- `{user_file}` is the text file containing the user data (such as `user.txt` in the example).
- `{tweet_file}` is the text file containing the tweets (such as `tweet.txt` in the example).

### Output

- When run with the sample input files `user.txt` and `tweet.txt`, the output is:
```
Alan
        @Alan: If you have a procedure with 10 parameters, you probably missed some.
        @Alan: Random numbers should not be generated with a method chosen at random.
Martin
Ward
        @Alan: If you have a procedure with 10 parameters, you probably missed some.
        @Ward: There are only two hard things in Computer Science: cache invalidation, naming things and off-by-1 errors.
        @Alan: Random numbers should not be generated with a method chosen at random.
```
## Unit test

- Unit tests are included in the program. Unit tests are located in the `app` directory and prepended by `test_`.
- Run unit tests by running the `test_*.py` files with python3. For example to run `test_main.py`:
```
python3 app/test_main.py
```
- The following unit test files are included:
```
test_main.py
test_read_text_files.py
```
## Authors

Charl Verster\
Contact me at [email][mailto:verstercpf@gmail.com] or on [LinkedIn](https://www.linkedin.com/in/verstercpf/)

## Version History

* 0.1 - Initial release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

This README.md is loosly based on [awesome-readme](https://github.com/matiassingers/awesome-readme).
