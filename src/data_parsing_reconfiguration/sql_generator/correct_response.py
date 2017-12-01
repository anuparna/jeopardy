import constants


class CorrectResponse(object):
    """
    CorrectResponse entity with details of the contestants who responded correctly to questions.
    Attributes:
        contestant_id: Primary Id of the contestant
        question_id : Primary Id of the question
    """

    def __init__(self, contestant_id, question_id, file_location):
        """
        Create a new instance of occupation
        @param contestant_id: Primary Id of the contestant
        @param question_id: Primary Id of the question
        @param file_location: Location of the .sql file generated from the instance
        """
        self.contestant_id = contestant_id
        self.question_id = question_id
        self.sql_file = file_location

    def generate_sql(self, entity_definition):
        """
        Generates the Insert query for occupation
        @param entity_definition: definition of correct_response entity from input configuration
        @return: query: String query generated
        """
        file = open(self.sql_file, "a")
        query = constants.INSERT_INTO + entity_definition + ' VALUES (\'{0}\', \'{1}\');\n'
        query = query.format(self.contestant_id, self.question_id)

        file.write(query)
        file.close()
        return query
