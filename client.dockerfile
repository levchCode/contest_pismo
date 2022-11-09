FROM nginx

WORKDIR /usr/share/react

RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
RUN apt-get install -y nodejs

COPY ./pismo/package*.json ./

RUN npm install --legacy-peer-deps
COPY ./pismo .

RUN npm run build

RUN rm -r /usr/share/nginx/html/*

RUN cp -a ./dist/* /usr/share/nginx/html/

COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf


ENTRYPOINT ["nginx", "-g", "daemon off;"]
