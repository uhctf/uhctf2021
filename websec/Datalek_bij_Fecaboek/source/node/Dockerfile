FROM node:15.14.0-alpine3.10

WORKDIR /home/node/app

COPY package*.json ./

RUN npm install
RUN npm ci --only=production

COPY ./src/ ./

USER node
CMD [ "node", "index.js" ]