CREATE TABLE correct_response (
    FOREIGN KEY (contestant_id) REFERENCES contestant(contestant_id) ON DELETE CASCADE,
    FOREIGN KEY (question_id) REFERENCES question(question_id) ON DELETE CASCADE
    );
