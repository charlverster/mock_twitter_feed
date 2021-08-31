# Mock Twitter Feed

This Python program is a simple mock twitter feed, displayed in the console. 

## Description

* The program looks for two text files inside the folder `files` in the working directory, named `user.txt` and `tweet.txt`.

* `user.txt` containts a list of users and the people they follow. `tweet.txt` contains a list of tweets posted by the users. 

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

## Getting Started

### Dependencies

- To combat [Works On My Machine](https://www.leadingagile.com/2017/03/works-on-my-machine/) the python app runs from a dockerized Ubuntu container. Install Docker Desktop for your host machine from [the Docker website](https://www.docker.com/products/docker-desktop).
- Docker-compose is required.

### Installing

- Clone this repository to your machine.
- In your terminal, navigate to the `mysql_docker` folder. Build the dockerfile with:
```
docker build -t mysqlserver .
```
- Navigate to the `src` folder and build Ubuntu dockerfile with:
```
docker build -t ubuntu_container .
```
- Run the docker containers with:
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
-`{user_file}` is the text file containing the user data (such as `user.txt` in the example).
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
