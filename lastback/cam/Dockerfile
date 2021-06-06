FROM node:lts-stretch
RUN mkdir =p /node
ADD . /node
WORKDIR /node
RUN npm install
RUN yarn install
CMD ["node", "server.js"]
