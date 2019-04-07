### STAGE 1: Build ###

FROM node:10-alpine as builder

COPY package.json package-lock.json ./

RUN npm install

## Storing node modules on a separate layer will prevent unnecessary npm installs at each build
RUN mkdir /frontend && mv ./node_modules ./frontend

WORKDIR /frontend

COPY . .

RUN npm run ng build -- --prod --output-path=dist

### STAGE 2: Setup ###

FROM nginx:1.14.1-alpine

COPY nginx/default.conf /etc/nginx/conf.d/

RUN rm -rf /usr/share/nginx/html/*

COPY --from=builder /frontend/dist /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]
