-- script that creates the database hbtn_0c_0
DROP DATABASE IF EXISTS `second_table`;

CREATE TABLE first_table (
    id INT NOT NULL, name VARCHAR(256), score INT
)

INSERT INTO
    `second_table` (id, name, score)
VALUES (1, "John", 10),
    (2, "Alex", 3),
    (3, "Bod", 14),
    (4, "George", 8);