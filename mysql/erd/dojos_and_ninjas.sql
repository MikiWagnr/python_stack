
-- Query: Create 3 new dojos

INSERT INTO dojos (name) 
VALUES('New York');
INSERT INTO dojos (name) 
VALUES('California');
INSERT INTO dojos (name) 
VALUES('Mountain');

-- Query: Delete the 3 dojos you just created

DELETE FROM dojos WHERE id = 1;
DELETE FROM dojos WHERE id = 2;
DELETE FROM dojos WHERE id = 3;


-- Query: Create 3 more dojos

INSERT INTO dojos (name) 
VALUES('New York');
INSERT INTO dojos (name) 
VALUES('California');
INSERT INTO dojos (name) 
VALUES('Mountain');


-- Query: Create 3 ninjas that belong to the first dojo

INSERT INTO ninjas (first_name, last_name, age ,dojo_id) 
VALUES('Tom', 'hiddlenston', 29, 1);
INSERT INTO ninjas (first_name, last_name, age ,dojo_id) 
VALUES('luke', 'skywalker', 20, 1);
INSERT INTO ninjas (first_name, last_name, age ,dojo_id) 
VALUES('charles', 'xavier', 59, 1);

-- Query: Create 3 ninjas that belong to the second dojo

INSERT INTO ninjas (first_name, last_name, age ,dojo_id) 
VALUES('wanda', 'maximmof', 29, 2);
INSERT INTO ninjas (first_name, last_name, age ,dojo_id) 
VALUES('Annakin', 'skywalker', 20, 2);
INSERT INTO ninjas (first_name, last_name, age ,dojo_id) 
VALUES('miki', 'minach', 59, 2);

-- Query: Create 3 ninjas that belong to the third dojo

INSERT INTO ninjas (first_name, last_name, age ,dojo_id) 
VALUES('harold', 'hiddlenston', 29, 3);
INSERT INTO ninjas (first_name, last_name, age ,dojo_id) 
VALUES('peter', 'parker', 20, 3);
INSERT INTO ninjas (first_name, last_name, age ,dojo_id) 
VALUES('essraa', 'valeria', 59, 3);

-- Query: Retrieve all the ninjas from the first dojo

SELECT * FROM ninjas WHERE dojo_id = 1;

-- Query: Retrieve all the ninjas from the last dojo

SELECT * FROM ninjas WHERE dojo_id = 3;

-- Query: Retrieve the last ninja's dojo

SELECT * FROM dojos 
JOIN ninjas ON dojos.id = ninjas.dojo_id
WHERE ninjas.id = (SELECT id FROM ninjas ORDER BY id DESC LIMIT 1);



