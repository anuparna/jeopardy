import constants


class ContestantLocation(object):
    """
        ContestantLocation entity definition - Represents location of a contestant in a game
        Attributes: game_id, contestant_id, seat_location
    """
    def __init__(self, game_id, contestant_id, seat_location, file_location):
        """
        Create a new instance of ContestantLocation (Database table: contestant_location)
        @param game_id: Unique id of an episode
        @param contestant_id: Unique id of a contestant
        @param seat_location: Enum location of the contestant
        @param file_location: .sql file location for insert sql statements
        """
        self.game_id = game_id
        self.contestant_id = contestant_id
        self.seat_location = seat_location
        self.sql_file = file_location

    def generate_sql(self, entity_definition):
        """
        Generates the SQL for Game and writes the SQL in a file
        @param entity_definition: Entity definition - table (columns...) from the input configuration
        @return query : String query generated
        """
        file = open(self.sql_file, "a")
        query = constants.INSERT_INTO + entity_definition + ' VALUES ({0}, {1}, \'{2}\');\n'
        query = query.format(self.game_id, self.contestant_id, self.seat_location)

        file.write(query)
        file.close()
        return query
