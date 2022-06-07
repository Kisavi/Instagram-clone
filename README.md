### PROJECT  NAME 
 +  Instagram clone


## Description

This is a simple web clone of the instagram website. A user can create an account and sign into it. The site supports uploading images,liking and commenting on images as well as following other users. Logged in users can view photos uploaded by other users in the home page of app.

## Author
Denis Kisavi

## BDD

>Signup inputs

| Inputs |  Description |
| :---         |          ---: |
| Username  | Account username, ``eg johndoe``|
| Email  | User email, ``eg johndoe@testmail.com``|
| Password  | Account password, ``eg password123``|
| Confirm Password  | Account password, ``eg password123``|

>Login Inputs

| Inputs |  Description |
| :---         |          ---: |
| Username  |Account username, ``eg johndoe``|
| Password  | Account password, ``eg 12345678``|

## User Story

- User can sign up if they have no account.

- User can login to their account.

- User can follow other users or unfollow them.

- User can post a picture.

- User can like or unlike a picture and also leave a comment.

- User can view their profile and edit their profile information.

- User can visit other peoples profiles and see their posts.

- User can logout of the application.


## <a href=" https://safaritours.herokuapp.com/">Live preview of the site</a>

## Set up instructions and installations

### Prerequisites

- python3.8

- python virtual environment ~ to create one run the following command `python3.8 -m venv --without-pip virtual`

- python pip ~ to install pip activate virtual environment `source virtual/bin/activate` then run `curl https://bootstrap.pypa.io/get-pip.py | python`

- Postgres ~ to install follow the following commands in your home directory:
    - `sudo apt-get update`
    - `sudo apt-get install postgresql postgresql-contrib libpq-dev`
    - `sudo service postgresql start`
    - `sudo -u postgres createuser --superuser $USER`
    - `sudo -u postgres createdb $USER`
    - `touch .psql_history`

### Installation instructions

- Clone the repo ~ `git clone https://github.com/Kisavi/Instagram-clone.git`

- Activate virtual environment: 
   `python3.6 -m venv --without-pip virtual` then `source virtual/bin/activate`

- Install all the dependancies in the requirements.txt file to get a development env running
   `pip3 install -r requirements.txt`

- Create a database 
  ```bash
  psql
  CREATE DATABASE 'your database name';
  ```

- Create .env file and paste the following filing where appropriate:
  ```python
  SECRET_KEY = '<Secret_key>'
  DBNAME = '<your db name>'
  USER = '<Username>'
  PASSWORD = '<password>'
  DEBUG = True
  ```

- Run initial migration
  ``` bash
  python3 manage.py makemigrations
  python3 manage.py migrate
  ```

- Run the app

   - `python3 manage.py runserver`

- Open the `localhost:8000` to check if the app is running successfully.

## Development
#### Want to make a contribution to enhance an existing module or fix a bug? Great!
* Fork the repo
* Create a new branch (git checkout -b improve-feature)
* Make the appropriate changes in the files
* Add changes to reflect the changes made
* Commit your changes (git commit -am 'Improve feature')
* Push to the branch (git push origin improve-feature)
* Create a Pull Request

## Technologies used

    - python3.8
    - Django4.0.4
    - Bootstrap
    - Postgresql

## Known Bugs
Some functionality not fully implemented
#### 
If you find a bug (the website couldn't handle the query and or gave undesired results), kindly open an issue here by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue here. Please include sample queries and their corresponding results.
## Contact Information
* For any inqueries feel free to write to me through
  + denis.kagunda@student.moringaschool.com

## Licence
* MIT License
* Copyright (c) 2022 Denis Kagunda






