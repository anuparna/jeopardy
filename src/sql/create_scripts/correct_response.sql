CREATE TABLE correct_response (
    contestant_id INT(5) UNSIGNED NOT NULL,
    question_id INT(6) NOT NULL,
    FOREIGN KEY (contestant_id) REFERENCES contestant(contestant_id) ON DELETE CASCADE,
    FOREIGN KEY (question_id) REFERENCES question(question_id) ON DELETE CASCADE
    );
