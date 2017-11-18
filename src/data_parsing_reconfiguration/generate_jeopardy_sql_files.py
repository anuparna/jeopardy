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


if __name__ == '__main__':
    # Parse command line arguments
    input_config, output_config = ap.argument_parser()

    # Read SCV files and parse
    # Retrieve questions.csv location from the config
    questions_csv_location = input_config.get('files', 'questions')
    #print(os.path.realpath(questions_csv_location))

    # Request dataframe of questions.csv
    questions_df = csvr.get_dataframe(questions_csv_location)
    #print(questions_df.describe())

    # Retrieve contestants.csv location from the config
    contestants_csv_location = input_config.get('files', 'contestants')

    # Request data-frame of contestants.csv
    contestants_df = csvr.get_dataframe(contestants_csv_location)
    rc.generate_contestant(contestants_df, input_config, output_config)
