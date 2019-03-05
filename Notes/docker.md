#Docker Tutorial
Docker is like a lightweight Virtual Machine called a container.
It can be run on any OS.
The containers typically run a single app.

##Running a container
    $docker container run -it -p 80:80 nginx
    - run in interactive mode
    - publish
    - map CLIENT port 80 to CONTAINER port 80
    - Use nginx (web server) image
        - If it's not on the system, it will be pulled from DockerHub
Now the server is running and I can get to it by going localhost:80
The container image comes from DockerHub and is saved
    $ docker container run -d -p  8080:80 --name mynginx nginx
    - run a container detached (doesn't log the container)

##Bash into Container
    $ docker container exec -it mynginx bash
    - Like sshing into the container

##Shutting it down
    $ docker container ls -a
    - to see all of the containers running or not running
    $ docker container rm [CONTAINER ID]
    - Removes the container
    $ docker images
    - Shows a list of all the stored images
    $ docker image rm [IMAGE ID]
    - removes the image from memory

##Bind Mount
Run the container and have it map to a file on the local machine
    $ docker container run -d -p 8080:80 -v $(pwd):/usr/share/nginx/html --name nginx-website nginx
    - $(pwd) spits out the current dir

##Creating a docker file
FROM nginx:latest

WORKDIR /usr/share/nginx/html

COPY . .

1. bases your image off the nginx image, latest one
2. set the working directory in the container
3. copies all the files in the current directory

###Build Image from the file
$ docker image build -t bacchusjackson/nginx-website .

###Build the container from the image
$ docker container run -d -p 8082:80 bacchusjackson/nginx-website

##Running Multiple Interactive Containers
FROM node:10

WORKDIR /usr/src/app

COPY package\*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]

##Docker Compose file
Does all of the $ docker container run stuff for you

version: '3'
services:
    app:
        container_name: docker-node-mongo
        restart: always
        build: .
        ports:
            - '80:3000'
        links:
            - mongo
    mongo:
        container_name: mongo
        image: mongo
        ports:
            - '27017:27017'

###.dockerignore
works the same as a .gitignore 

### Start it up
    $ docker-compose up
