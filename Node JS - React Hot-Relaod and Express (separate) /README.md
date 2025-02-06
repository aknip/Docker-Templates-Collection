# Nodejs React and Express (separate)

2 containers:
- React frontend with hot reload and scripts for dev, build, test => see myblog/README.md
- Node.js expess backend with hot reload

docker-compose up

http://localhost:3000
http://localhost:4000


# Source:
- https://github.com/pinaki3majumder/dockerized-react-node-app-with-hot-reload
- alternative approach, ideas: https://medium.com/@elifront/best-next-js-docker-compose-hot-reload-production-ready-docker-setup-28a9125ba1dc







# Dockerized React-Node App with Hot Reload

This project demonstrates how to Dockerize a React-Node application with hot reload functionality.

## Features

- React frontend with hot reload
- Node.js backend
- Dockerized development environment

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Docker installed on your machine. You can download and install Docker from [here](https://www.docker.com/get-started).
- Node.js installed on your machine. You can download and install Node.js from [here](https://nodejs.org/).
- React installed globally. You can install React globally using npm:

  ```bash
  npm install -g create-react-app
  ```
## Getting Started

In the project directory, you can run:

  ```bash
  docker compose up
  ```