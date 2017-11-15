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

    sql_file = 'contestant.sql'

    def __init__(self, first_name, last_name, home_city, country_or_state, occupation_id):
        """
        Initialize an instance of contestant
        @param first_name:
        @param last_name:
        @param home_city:
        @param country_or_state:
        @param occupation_id:
        """
        self.first_name = first_name
        self.last_name = last_name
        self.home_city = home_city
        self.country_or_state = country_or_state
        self.occupation_id = occupation_id

    def generate_sql(self):
        query = 'INSERT INTO contestant(first_name, last_name, home_city, country_or_state, occupation_id ) VALUES' \
                '(' + self.first_name + ',' + self.last_name + ',' + self.home_city + ',' + self.country_or_state + \
                ','+self.occupation_id+');'
        return query
