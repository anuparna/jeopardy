import constants


class Contestant(object):
    """
        A contestant of the Jeopardy game show
        Attributes:
            first_name: First name of the contestant
            last_name: Last name of the contestant
            home_city: Home city of the contestant
            country_or_state: Country or state of the contestant
            occupation_id: Occupation id of the contestant, depends on occupation master table
    """

    def __init__(self, contestant_id, first_name, last_name, home_city, country_or_state, occupation_id, file_location):
        """
        Initialize an instance of contestant
        @param contestant_id: Player id from the CSV
        @param first_name: First name of the contestant
        @param last_name: Last name of the contestant
        @param home_city: Home city
        @param country_or_state: Country for contestants outside US. State for US residents
        @param occupation_id: Occupation id generated in occupation table
        @param file_location: Location of the .sql file
        """
        self.contestant_id = contestant_id
        self.first_name = first_name
        self.last_name = last_name
        self.home_city = home_city
        self.country_or_state = country_or_state
        self.occupation_id = occupation_id
        self.sql_file = file_location

    def generate_sql(self, entity_definition):
        """
        Generates the SQL for Contestant and writes the SQL in a file
        @param entity_definition: Entity definition - table (columns...) from the input configuration
        @return query : String query generated
        """
        file = open(self.sql_file, "a")
        query = constants.INSERT_INTO + entity_definition + ' VALUES ({0}, \'{1}\', \'{2}\', \'{3}\', \'{4}\', {5});\n'
        if self.occupation_id is None:
            query = query.format(self.contestant_id, self.first_name, self.last_name,
                                 self.home_city, self.country_or_state, 'null')
        else:
            query = query.format(self.contestant_id, self.first_name, self.last_name,
                                 self.home_city, self.country_or_state, self.occupation_id)

        file.write(query)
        file.close()
        return query
