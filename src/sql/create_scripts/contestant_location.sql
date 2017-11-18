CREATE TABLE contestant_location (
    game_id INT(4) UNSIGNED NOT NULL,
    contestant_id INT(5) UNSIGNED NOT NULL,
    seat_location ENUM('right', 'middle', 'returning_champ'),
    FOREIGN KEY (game_id) REFERENCES game(game_id) ON DELETE CASCADE,
    FOREIGN KEY (contestant_id) REFERENCES contestant(contestant_id) ON DELETE CASCADE
    );
