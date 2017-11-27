import constants


class Category(object):
    """
    Category entity with details of the different categories of questions.
    Attributes:
        category_id: Primary Id of the category
        category_name : name of the category
    """

    def __init__(self, category_id, category_name, file_location):
        """
        Create a new instance of occupation
        @param category_id: Primary Id of the category
        @param category_name: Name of the category
        @param file_location: Location of the .sql file generated from the instance
        """
        self.category_id = category_id
        self.category_name = category_name
        self.sql_file = file_location

    def generate_sql(self, entity_definition):
        """
        Generates the Insert query for occupation
        @param entity_definition: definition of Occupation entity from input configuration
        @return: query: String query generated
        """
        query = constants.INSERT_INTO + entity_definition + ' VALUES ({0}, \'{1}\');\n'
        query = query.format(self.category_id, self.category_name)

        with open(self.sql_file, 'a', encoding='utf-8') as file:
            print(query, file=file)

        file.close()
        return query
