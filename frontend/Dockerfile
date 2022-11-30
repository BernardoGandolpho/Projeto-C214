FROM node:16-alpine

WORKDIR /urs/src/poke-front

COPY ./package.json ./
COPY ./package-lock.json ./

COPY . .

RUN npm install
