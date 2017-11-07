CREATE TABLE wager (
	contestant_id INT(5) UNSIGNED NOT NULL, 
	FOREIGN KEY (contestant_id) REFERENCES contestant(contestant_id) ON DELETE CASCADE 
  	question_id INT(5) UNSIGNED NOT NULL, 
	FOREIGN KEY (question_id) REFERENCES question(question_id) ON DELETE CASCADE  	
	wager_amount INT(10),
	);
