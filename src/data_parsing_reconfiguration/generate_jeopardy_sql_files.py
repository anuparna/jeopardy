# The entire process starts from here
# The input_config.ini is required to execute this program

import sys
import os

sys.path.insert(0, os.path.realpath('./csv_reader'))
sys.path.insert(0, os.path.realpath('./data_reconfiguration'))
sys.path.insert(0, os.path.realpath('./sql_generator'))

from csv_reader import argument_parser as ap
from csv_reader import CSVReader as csvr
from data_reconfiguration import reconfigure_contestants_data as rc
from data_reconfiguration import reconfigure_question_data as rcq
from data_reconfiguration import reconfigure_game_contestant_location_data as rc_game_player_loc


if __name__ == '__main__':
    # Parse command line arguments
    input_config, output_config = ap.argument_parser()

    # Retrieve csv locations from the config
    contestants_csv_location = input_config.get('files', 'contestants')
    game_contestant_csv_location = input_config.get('files', 'locations')
    questions_csv_location = input_config.get('files', 'questions')
    trend_csv_location = input_config.get('files', 'trend')

    # Request data-frame from CSVs
    contestants_df = csvr.get_dataframe(contestants_csv_location)
    game_contestant_df = csvr.get_dataframe(game_contestant_csv_location)
    questions_df = csvr.get_dataframe(questions_csv_location)
    trend_df = csvr.get_dataframe(trend_csv_location)

    # Reconfiguration
    rc.generate_contestant_and_occupation(contestants_df, input_config, output_config)
    rc_game_player_loc.generate_sql_statements(game_contestant_df, input_config, output_config, rc)

    # Reconfiguration of questions
    rcq.generate_sql_statements(questions_df, trend_df, input_config, output_config)