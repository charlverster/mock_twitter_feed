# Mock Twitter Feed

This program is a simple mock twitter feed, displayed in the console. 

## Description

* The app looks for two files 7-bit ASCII files in the working directory named `user.txt` and `tweet.txt`.

* `user.txt` containts a list of users and the people they follow. `tweet.txt` contains a list of tweets posted by the users. 

* The app extracts the list of users and tweets, and then prints to console each user's name, their tweets and their followers tweets in the following format:

```
user
    @user: Tweet
    @followee: Tweet
```
*"Followee" is someone the user follows.*

## Getting Started

### Dependencies

- This software requires Docker. Install Docker Desktop for your host machine from [the Docker website](https://www.docker.com/products/docker-desktop).
- To combat [Works On My Machine](https://www.leadingagile.com/2017/03/works-on-my-machine/) the python app runs from a dockerized Ubuntu container. 

### Installing (TBC)

- Clone this repository.
- Open the terminal and navigate to the `mysql_docker` folder. Build the dockerfile using `docker build -t mysqlserver .`
- Navigate to the `src` folder and build ubuntu dockerfile `docker build -t ubuntu_container .`
- Run `docker-compose up -d` to create docker containers in their own network
- Run `docker exec -it ubuntu-container bash` to open a console within the ubuntu container.


```
python3 app/main.py user.txt tweet.txt
```


### Executing program (TBC)

- Run the python app with `python3 app/main.py {user_file} {tweet_file}` where 
    `{user_file}` is the text file containing the user data (such as `user.txt` in the example) and `{tweet_file}` is the text file containing the tweets (such as `tweet.txt` in the example).

## Help (TBC)

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Charl Verster\
Contact me at [email][mailto:verstercpf@gmail.com] or on [LinkedIn](https://www.linkedin.com/in/verstercpf/)

## Version History


* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

Readme template:
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
