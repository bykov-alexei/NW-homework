CREATE USER IF NOT EXISTS images@localhost IDENTIFIED BY 'images';
DROP DATABASE images;
CREATE DATABASE images;
GRANT ALL PRIVILEGES ON images.* TO images@localhost;

USE images;
CREATE TABLE images (
    `id` INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `filename` VARCHAR(255) NOT NULL,
    `server` VARCHAR(255) NOT NULL
);

INSERT INTO images (`filename`, `server`) VALUES
    ('img1.jpg', 's1'),
    ('img2.jpeg', 's1'),
    ('img3.jpg', 's2'),
    ('img4.jpeg', 's2'),
    ('img5.jpeg', 's3'),
    ('img6.jpg', 's3');