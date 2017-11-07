CREATE TABLE wager (
	contestant_id INT(5) UNSIGNED NOT NULL, 
	FOREIGN KEY (contestant_id) REFERENCES contestant(contestant_id),
  	question_id INT(5) UNSIGNED NOT NULL, 
	FOREIGN KEY (question_id) REFERENCES question(question_id),  	
	wager_amount INT,
	);
