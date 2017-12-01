import constants
from enum import Enum


class Round(Enum):
    J = 'Jeopardy'
    DJ = 'Double Jeopardy'
    final = 'Final'


class Question(object):
    """
    Question entity with details of the questions asked in a game.
    """

    def __init__(self, **question_arguments):
        """
        Create a instance of Question
        @param question_arguments: map of named arguments - variables used for instantiation
        """
        self.question_id = question_arguments.get('question_id')
        self.question_text = question_arguments.get('question_text')
        self.answer = question_arguments.get('answer')
        self.dollar_value = question_arguments.get('dollar_value')
        self.question_index = question_arguments.get('question_index')
        self.is_daily_double = question_arguments.get('is_daily_double')
        # ENUM('jeopardy', 'double jeopardy', 'final')
        self.round_name = (Round[question_arguments.get('round_name')]).value
        self.category_id = question_arguments.get('category_id')
        self.game_id = question_arguments.get('game_id')
        self.sql_file = question_arguments.get('file_location')

    def generate_sql(self, entity_definition):
        """
        Generates the SQL for Question and writes the SQL in a file
        @param entity_definition: Entity definition - table (columns...) from the input configuration
        @return query : String query generated
        """
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

        with open(self.sql_file, 'a', encoding='utf-8') as file:
            print(query, file=file)

        file.close()
        return query
