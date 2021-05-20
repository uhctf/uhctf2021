FROM node:15.14.0-alpine3.11

WORKDIR /home/node/app

COPY package*.json ./
COPY ./src/ ./src/
COPY ./public/ ./public/

RUN npm install --only=prod

USER node

CMD [ "node", "src/index.js" ]