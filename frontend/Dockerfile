# build
FROM node:22 AS build
WORKDIR /app
ENV PATH=/app/node_modules/.bin:$PATH
COPY ./frontend/package.json ./frontend/yarn.lock ./

RUN corepack enable
COPY ./frontend/ ./
RUN yarn install --frozen-lockfile
RUN yarn build

# prod
FROM nginx:stable-alpine
RUN rm /etc/nginx/conf.d/default.conf
COPY ./frontend/nginx.conf /etc/nginx/conf.d
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
