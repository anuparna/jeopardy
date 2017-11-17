CREATE TABLE contestant (
	contestant_id INT(5) UNSIGNED NOT NULL PRIMARY KEY,
	first_name TINYTEXT NOT NULL,
	last_name TINYTEXT,
	home_city TINYTEXT,
	country_or_state TINYTEXT,
	occupation_id INT(5) UNSIGNED,
	FOREIGN KEY (occupation_id) REFERENCES occupation(occupation_id) ON DELETE CASCADE
	);