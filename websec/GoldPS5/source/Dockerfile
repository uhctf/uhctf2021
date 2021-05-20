FROM node:15.14.0-alpine3.10

WORKDIR /home/node/app

COPY package*.json ./

ENV NODE_ENV production

RUN npm install --only=prod
RUN npm ci --only=prod

COPY ./src/ ./

USER node
CMD [ "npm", "run", "prod" ]