CREATE TABLE question (
    question_id INT(5) NOT NULL PRIMARY KEY,
    question_text TEXT NOT NULL,
    answer TEXT NOT NULL,
    dollar_value INT(10),
    question_index INT(2),
    is_daily_double BIT, 
    round_name ENUM('jeopardy', 'double jeopardy', 'final'),
    category_id INT(5),
    FOREIGN KEY (category_id) REFERENCES category(category_id) ON DELETE CASCADE
    game_id INT(5), 
    FOREIGN KEY (game_id) REFERENCES game(game_id) ON DELETE CASCADE  
);
