FROM node:14
WORKDIR /usr/src/app
COPY package*.json ./

RUN npm install
RUN npm install express request@2.81.0 dotenv cors body-parser nodemon avsc cassandra-driver uuid
COPY . .
EXPOSE 3000
CMD [ "npm", "start" ]
