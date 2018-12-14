CREATE DATABASE warsztat_war_pyt_s_12;


CREATE TABLE users (
id serial,
email VARCHAR(255) unique,
username VARCHAR(255),
hashed_password VARCHAR(80),
PRIMARY KEY(id)
);


