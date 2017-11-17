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

    sql_file = '../sql/insert_scripts/contestant.sql'

    def __init__(self, contestant_id, first_name, last_name, home_city, country_or_state, occupation_id):
        """
        Initialize an instance of contestant
        @param contestant_id: Player id from the CSV
        @param first_name:
        @param last_name:
        @param home_city:
        @param country_or_state:
        @param occupation_id:
        """
        self.contestant_id = contestant_id
        self.first_name = first_name
        self.last_name = last_name
        self.home_city = home_city
        self.country_or_state = country_or_state
        self.occupation_id = occupation_id

    def generate_sql(self):
        """
        Generates the SQL for Contestant and writes the SQL in a file
        @return: query : String query generated
        """
        file = open(self.sql_file, "a")
        query = 'INSERT INTO ' \
                'contestant(contestant_id, first_name, last_name, home_city, country_or_state, occupation_id) ' \
                'VALUES ({0}, \'{1}\', \'{2}\', \'{3}\', \'{4}\', {5});\n'
        if self.occupation_id is None:
            query = query.format(self.contestant_id, self.first_name, self.last_name,
                                 self.home_city, self.country_or_state, 'null')
        else:
            query = query.format(self.contestant_id, self.first_name, self.last_name,
                                 self.home_city, self.country_or_state, self.occupation_id)

        file.write(query)
        file.close()
        return query
