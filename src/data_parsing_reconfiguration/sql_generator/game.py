import constants


class Game(object):
    """
        Game entity definition - Represents an episode of the game
        Attributes: game_id, season_number
    """
    def __init__(self, game_id, season_num, file_location):
        """
        Create a new instance of game
        @param game_id: Unique game id - represents every episode
        @param season_num: Season when the game was aired
        @param file_location: Location of .sql file
        """
        self.game_id = game_id
        self.season_number = season_num
        self.sql_file = file_location

    def generate_sql(self, entity_definition):
        """
        Generates the SQL for Game and writes the SQL in a file
        @param entity_definition: Entity definition - table (columns...) from the input configuration
        @return query : String query generated
        """
        file = open(self.sql_file, "a")
        query = constants.INSERT_INTO + entity_definition + ' VALUES ({0}, {1});\n'
        query = query.format(self.game_id, self.season_number)

        file.write(query)
        file.close()
        return query
