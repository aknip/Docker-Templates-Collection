# Docker Development Environments

A collection of repos with Docker templates.

### Execute commands inside Docker
- Use `run` for a single one-off execution and starting a container.
- Use `exec` for executing a command in a running container.
Examples => XXX is Docker container name / service name:
- docker-compose run XXX bash
- docker-compose run XXX python3 --version
- docker-compose exec XXX bash
- docker-compose exec XXX python src/marimoapp.py



## Sources:

1. Collection of Docker Compose templates for Python, NodeJS, Java ...
Instant Development for Docker-based Applications with Docker Volumes (Plug & Play Hot Reload)
- https://jerichosiahaya.medium.com/instant-development-for-docker-based-applications-with-docker-volumes-plug-play-hot-reload-57c331d53de2
- https://github.com/singgihdwindaru/docker-instant-development/tree/main

2. Docker volumes in detail
- https://therahulsarkar.medium.com/understanding-docker-volumes-a-comprehensive-guide-46339aa9ac53
- Fixing "node_modules" problems with volumes (anonymous volumes): https://medium.com/@jkpeyi/the-struggles-with-docker-compose-volumes-section-176cbe722987

2. Docker compose
- https://medium.com/@abderraoufbenchoubane/setup-a-python-environment-with-docker-a4e38811e0d3
- https://github.com/Abderraouf99/medium-article-source-code/tree/main/docker-env


3. VScode and the Dev Containers extension.
- https://towardsdatascience.com/setting-a-dockerized-python-environment-the-elegant-way-f716ef85571d



