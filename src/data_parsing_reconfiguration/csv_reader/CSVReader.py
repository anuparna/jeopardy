import pandas as pd


def get_dataframe(csv_location):
    """
    Function to read CSV file and convert into a Pandas dataframe for further manipulation
    @param csv_location: filepath of the CSV file to be read
    @return: df: Pandas dataframe - can be used for reconfiguration
    """
    df = pd.read_csv(filepath_or_buffer=csv_location, delimiter=',')
    return df
