CREATE TABLE question (
    question_id INT(5) NOT NULL PRIMARY KEY,
    question_text TEXT NOT NULL,
    answer TEXT NOT NULL,
    dollar_value INT(10),
    question_index INT(2),
    is_daily_double BIT, 
    round_name ENUM('jeopardy', 'double jeopardy', 'final'),
    category_id INT(5),
    
    game_id INT(5), 
    
);
