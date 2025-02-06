FROM node:alpine

COPY package.json .

RUN npm install

WORKDIR /app

COPY . .

# required for docker desktop port mapping
EXPOSE 3000

CMD ["npm", "start"]