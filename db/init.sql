use W2A;

CREATE TABLE UserInfo (
	id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	username VARCHAR(30) NOT NULL,
	hashed_password VARCHAR(255) NOT NULL,
	email VARCHAR(50) NOT NULL,
	UNIQUE KEY EMAIL (email));
