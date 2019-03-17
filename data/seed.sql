drop table if exists user;
drop table if exists recipe;
drop table if exists cocktail;

CREATE TABLE test (
	name text
);

-- create table user (
--  ... ?
-- );
CREATE TABLE user (
	id INTEGER PRIMARY KEY AUTOINCREMENT, 
	username VARCHAR(255) NOT NULL,
	password VARCHAR(255) NOT NULL
	);


-- create table recipe (
-- ... ?
-- );
CREATE TABLE "recipes" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"name"	VARCHAR(255) NOT NULL,
	"description"	TEXT NOT NULL,
	"ingredients"	TEXT NOT NULL,
	"image"	TEXT NOT NULL,
	"user_id"	INTEGER,
	FOREIGN KEY("user_id") REFERENCES "users"("id")
);

-- insert into user 
-- ... ?
insert into user
(name)
VALUES("")
(password)
VALUES("")
;