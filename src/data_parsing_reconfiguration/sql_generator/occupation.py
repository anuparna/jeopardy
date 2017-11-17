class Occupation(object):
    """
    Occupation entity with details of the occupation of contestants.
    Attributes:
        occupation_id: Primary Id of the occupation
        occupation_name : name of the occupation
    """

    sql_file = '../sql/insert_scripts/occupation.sql'

    def __init__(self, occupation_id, occupation_name):
        """
        Create a new instance of occupation
        @param occupation_id: Primary Id of the occupation
        @param occupation_name: Name of the occupation
        """
        self.occupation_id = occupation_id
        self.occupation_name = occupation_name

    def generate_sql(self):
        """
        Generates the Insert query for occupation
        @return: query: String query generated
        """
        file = open(self.sql_file, "a")
        query = 'INSERT INTO ' \
                'occupation(occupation_id, occupation_name) ' \
                'VALUES ({0}, \'{1}\');\n'
        query = query.format(self.occupation_id, self.occupation_name)

        file.write(query)
        file.close()
        return query
