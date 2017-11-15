import argparse
import configparser


def argument_parser():
    """
    Function used to validate and read the command line arguments passed during the execution of create_database_insert_sql.py
    @return: ConfigParser - A Python object representing the elements of the config.ini
    """
    arg_parser = argparse.ArgumentParser(add_help=False)

    # Add an string argument 'config'
    required_parameters = arg_parser.add_argument_group('required named arguments')
    required_parameters.add_argument("-c", "--config", dest='config_file', default='config.ini', type=str,
                                     help='Config file provides details of the locations of the required CSV files',
                                     required=True)

    # Add an string argument 'help'
    arg_parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                            help='This Python script reads CSV files and '
                                 'creates .sql files to insert in database. '
                                 'The project is meant to be used for creating a Jeopardy database.')

    # Parse command line
    args = arg_parser.parse_args()

    # Read config file
    config_file = args.config_file
    config = configparser.ConfigParser()
    config.read(config_file)
    return config
