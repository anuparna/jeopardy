CREATE TABLE wager (
	contestant_id INT(5) UNSIGNED NOT NULL FOREIGN KEY REFEReNCES Contestant(contestant_id),
  	question_id INT(5) UNSIGNED NOT NULL FOREIGN KEY REFERENCES Question(question_id), 
  	wager_amount INT,
	);
