import constants
from enum import Enum


class Round(Enum):
    JP = 'jeopardy'
    DJ = 'double jeopardy'
    F = 'final'


class Question(object):
    """
    Question entity with details of the questions asked in a game.
    """

    def __init__(self, **kwargs):
        """
        Create a instance of Question
        @param kwargs: map of named arguments - variables used for instantiation
        """
        self.question_id = kwargs.get('question_id')
        self.question_text = kwargs.get('question_text')
        self.answer = kwargs.get('answer')
        self.dollar_value = kwargs.get('dollar_value')
        self.question_index = kwargs.get('question_index')
        self.is_daily_double = kwargs.get('is_daily_double')
        self.round_name = Round(kwargs.get('round_name'))
        # ENUM('jeopardy', 'double jeopardy', 'final'),
        self.category_id = kwargs.get('category_id')
        self.game_id = kwargs.get('game_id')
        self.sql_file = kwargs.get('file_location')

    def generate_sql(self, entity_definition):
        """
        Generates the SQL for Question and writes the SQL in a file
        @param entity_definition: Entity definition - table (columns...) from the input configuration
        @return query : String query generated
        """
        file = open(self.sql_file, "a")

        query = constants.INSERT_INTO + entity_definition + ' VALUES ({0}, \'{1}\', \'{2}\', {3}, {4},' \
                                                            ' \'{5}\', \'{6}\', {7}, {8}' + ');\n'
        query = query.format(self.question_id,
                             self.question_text,
                             self.answer,
                             self.dollar_value,
                             self.question_index,
                             self.is_daily_double,
                             self.round_name,
                             self.category_id,
                             self.game_id)

        file.write(query)
        file.close()
        return query
