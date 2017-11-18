import constants


class Occupation(object):
    """
    Occupation entity with details of the occupation of contestants.
    Attributes:
        occupation_id: Primary Id of the occupation
        occupation_name : name of the occupation
    """

    def __init__(self, occupation_id, occupation_name, file_location):
        """
        Create a new instance of occupation
        @param occupation_id: Primary Id of the occupation
        @param occupation_name: Name of the occupation
        @param file_location: Location of the .sql file generated from the instance
        """
        self.occupation_id = occupation_id
        self.occupation_name = occupation_name
        self.sql_file = file_location

    def generate_sql(self, entity_definition):
        """
        Generates the Insert query for occupation
        @param entity_definition: definition of Occupation entity from input configuration
        @return: query: String query generated
        """
        file = open(self.sql_file, "a")
        query = constants.INSERT_INTO + entity_definition + ' VALUES ({0}, \'{1}\');\n'
        query = query.format(self.occupation_id, self.occupation_name)

        file.write(query)
        file.close()
        return query
