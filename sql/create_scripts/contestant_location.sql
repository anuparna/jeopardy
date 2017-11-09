CREATE TABLE contestant_location (
    FOREIGN KEY (game_id) REFERENCES game(game_id) ON DELETE CASCADE,
    FOREIGN KEY (contestant_id) REFERENCES contestant(contestant_id) ON DELETE CASCADE,
    seat_location ENUM('right', 'middle', 'returning_champion')
    );
