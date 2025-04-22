# N8N, Python enabled

https://gitpod.io/#https://github.com/aknip/N8N

- based on https://www.npmjs.com/package/n8n-nodes-python-runtime
- installs latest version of n8n (change in Dockerfile)

## Start
- docker-compose up -d


## Install latest version of n8n manually, eg. in gitpod
- npm install n8n -g
- n8n start

## Notes

### Alternative Python integration
see https://github.com/naskio/docker-n8n-python => seems not to work?

### Local Directories
directories "n8n_data" and "local-files" can be deleted to start from scratch

### Docker Compose with ngrok
https://github.com/Joffcom/n8n-ngrok/tree/main

### Copy from repo config to local gitpod config
- rm -rf /home/gitpod/.n8n
- cp -r ./n8n_data /home/gitpod/.n8n

### Copy from local gitpod config to repo config
- rm -rf ./n8n_data
- cp -r /home/gitpod/.n8n ./n8n_data

this is appended text 1

this is appended text 2

this is appended text 1

this is appended text 2

this is appended text 1

this is appended text 2