# FastAPI-MYSQL-DOCKER
### About this FastAPI app
This app is using FastAPI python framework to connect to the MySQL database
to do CRUD actions on USER and ITEM tables on database.

#### How to run the app

mv .env-example .env

edit .env and provide the values for the variables as you want.

docker-compose up --build -d

go to the browser and enter http://localhost:8080/docs

#### How to kill the app

docker-compose down