FROM node:9.5.0-alpine

WORKDIR /client

COPY package*.json ./

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh && npm i

COPY . .

RUN npm run build
EXPOSE 8000
CMD ["node", "server.js"]