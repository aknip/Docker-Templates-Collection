# n8n (Python enabled) 

https://gitpod.io/#https://github.com/aknip/N8N

- based on https://www.npmjs.com/package/n8n-nodes-python-runtime
- installs latest version of n8n (change in Dockerfile)
- n8n: Folder n8n_local-files can be used for file exchange

## Important!
Before first startup do:
chown -R 1000:1000 ./n8n_data/
chown -R 1000:1000 ./n8n_local-files/

## Start n8n 
- docker-compose up -d
- http://localhost:5678

## n8n extensions
n8n-nodes-python-runtime


## Use terminal in docker
- docker-compose exec n8n-python ash


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


/home/node/.n8n/config