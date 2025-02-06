# Node js

docker-compose up --build

Folder src can be edited 

### Execute commands inside Docker
- Use `run` for a single one-off execution and starting a container.
- Use `exec` for executing a command in a running container.
Examples:
- docker-compose run nodejs bash
- docker-compose run nodejs python3 --version
- docker-compose exec nodejs bash
- docker-compose exec nodejs python src/marimoapp.py


## Docker
docker build -t my_nodejs .
docker run -p 80:80 -it my_nodejs


## fly.io
- Install CLI: brew install flyctl

- Init existing app (first deploy): fly launch --now
- Update: fly deploy





    # Source
    - https://medium.com/geekculture/deploy-docker-images-on-fly-io-free-tier-afbfb1d390b1
    - https://github.com/fly-apps