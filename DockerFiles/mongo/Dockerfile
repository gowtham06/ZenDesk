FROM mongo:3.2.12

RUN mkdir -p /Data

COPY Data/ /Data

RUN (mongod --fork --syslog && \
     mongoimport --db zendesk --jsonArray --collection users --file /Data/users.json && \
     mongoimport --db zendesk --jsonArray --collection organizations --file /Data/organizations.json && \
     mongoimport --db zendesk --jsonArray --collection tickets --file /Data/tickets.json)
