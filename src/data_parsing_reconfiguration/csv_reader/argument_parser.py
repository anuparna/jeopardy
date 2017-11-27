import argparse
import configparser


def argument_parser():
    """
    Function used to validate and read the command line arguments passed during the execution of
    generate_jeopardy_sql_files.py
    @return input_config: ConfigParser - A Python object representing the elements of the input_config.ini
    @return output_config: ConfigParser - A Python object representing the elements of the output_config.ini
    """

    arg_parser = argparse.ArgumentParser(add_help=False)

    # Add an string argument 'input_config' and 'output_config'
    required_parameters = arg_parser.add_argument_group('required named arguments')
    required_parameters.add_argument("-i", "--input_config", dest='input_config_file', default='input_config.ini', type=str,
                                     help='Input Configuration file provides details of the '
                                          'locations of the required CSV files',
                                     required=True)
    required_parameters.add_argument("-o", "--output_config", dest='output_config_file', default='output_config.ini', type=str,
                                     help='Output Configuration file provides details of the '
                                          'locations of the generated .sql files containing insert statements'
                                          ' for the Jeopardy database tables',
                                     required=True)

    # Add an string argument 'help'
    arg_parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                            help='This Python script reads CSV files and '
                                 'creates .sql files to insert in database. '
                                 'The project is meant to be used for creating a Jeopardy database.')

    # Parse command line
    args = arg_parser.parse_args()

    # Read config file
    input_config_file = args.input_config_file
    output_config_file = args.output_config_file

    input_config = configparser.ConfigParser()
    output_config = configparser.ConfigParser()

    input_config.read(input_config_file)
    output_config.read(output_config_file)

    return input_config, output_config
