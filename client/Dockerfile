FROM node:alpine

WORKDIR /app

COPY . .

RUN npm install -g @angular/cli

RUN npm install

CMD ["npm", "run", "start:all"]