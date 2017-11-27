CREATE TABLE question (
    question_id INT(6) NOT NULL PRIMARY KEY,
    question_text TEXT NOT NULL,
    answer TEXT NOT NULL,
    dollar_value INT(10),
    question_index INT(2),
    is_daily_double BIT, 
    round_name ENUM('Jeopardy', 'Double Jeopardy', 'Final'),
    category_id INT(5) UNSIGNED,
    game_id INT(4) UNSIGNED NOT NULL,
    FOREIGN KEY(category_id) REFERENCES category(category_id) ON DELETE CASCADE,
    FOREIGN KEY(game_id) REFERENCES game(game_id) ON DELETE CASCADE );
