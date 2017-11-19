from sql_generator import contestant
from sql_generator import occupation
from copy import deepcopy
import pandas as pd


def find_contestant_id_from_dup_records(contestant_id):
    """
    Since there exists duplicate records in the csv for contestants.
    Given a contestant_id, find the unique_id used for insertion in the database.
    @param contestant_id: Player id retrieved from the csv
    @return: contestant_id used for database insertion.
    """
    if any(df_non_duplicate_contestants['player_id'] == contestant_id):
        return contestant_id
    else:
        if any(df_duplicate_contestants['player_id'] == contestant_id):
            temp_contestant_df = df_duplicate_contestants.loc[df_duplicate_contestants['player_id']
                                                              == contestant_id]            
            first_row = temp_contestant_df.head(1)

            non_dup_contestants = df_non_duplicate_contestants
            non_duplicated_player_df_with_criteria = pd.merge(non_dup_contestants, first_row, how='inner',
                                                              on=['player_first_name', 'player_last_name',
                                                                  'hometown_city', 'hometown_state', 'occupation'])
            if len(non_duplicated_player_df_with_criteria) == 1:
                return non_duplicated_player_df_with_criteria['player_id_x'].item()
        return ''


def generate_contestant_and_occupation(df_contestant, input_config, output_config):
    """
    Collect contestant and occupation information from contestants.csv
    @param df_contestant: Contestant data-frame used for reconfiguration
    @param input_config: Input configuration
    @param output_config: Output configuration
    """

    # get location of output files
    contestants_sql_location = output_config.get('files', 'contestants')
    occupation_sql_location = output_config.get('files', 'occupations')

    # reset the sql files
    open(contestants_sql_location, 'w').close()
    open(occupation_sql_location, 'w').close()

    # get entity definition
    contestant_entity_definition = input_config.get('entities', 'contestant')
    occupation_entity_definition = input_config.get('entities', 'occupation')

    # remove duplicate player_id rows and clean data
    global df_duplicate_contestants
    df_contestant = df_contestant.fillna('')
    df_duplicate_contestants = deepcopy(df_contestant)
    df_contestant = df_contestant.drop_duplicates(subset=['player_id'], keep='first')
    df_contestant = df_contestant.drop_duplicates(df_contestant.columns.difference(['player_id']),
                                                  keep='first')
    global df_non_duplicate_contestants
    df_non_duplicate_contestants = df_contestant
    print(df_duplicate_contestants.shape, df_non_duplicate_contestants.shape )

    # Generate group of customers with the same occupation.
    contestants_groups = df_contestant.groupby(df_contestant['occupation'])
    occupation_id = 0
    contestant_count = 0
    for occupation_name, group in contestants_groups:
        # Generate SQL for Occupation
        occupation_id = occupation_id + 1

        if occupation_name:
            occupation_name = (occupation_name.strip()).replace("'", "\\'")
            contestant_occupation = occupation.Occupation(occupation_id, occupation_name,
                                                          file_location=occupation_sql_location)
            contestant_occupation.generate_sql(entity_definition=occupation_entity_definition)

        # Generate SQL for contestant
        no_of_contestants = len(group)
        for index in range(no_of_contestants):
            csv_player = group.iloc[index]
            contestant_id = csv_player['player_id']

            first_name = (csv_player['player_first_name'].strip()).replace("'", "\\'")
            last_name = (csv_player['player_last_name'].strip()).replace("'", "\\'")
            home_city = (csv_player['hometown_city'].strip()).replace("'", "\\'")
            country_or_state = (csv_player['hometown_state'].strip()).replace("'", "\\'")

            if occupation_name:
                player = contestant.Contestant(contestant_id=contestant_id,
                                               first_name=first_name,
                                               last_name=last_name,
                                               home_city=home_city,
                                               country_or_state=country_or_state,
                                               occupation_id=occupation_id,
                                               file_location=contestants_sql_location)
                player.generate_sql(entity_definition=contestant_entity_definition)
                contestant_count += 1
            else:
                player = contestant.Contestant(contestant_id=contestant_id,
                                               first_name=first_name,
                                               last_name=last_name,
                                               home_city=home_city,
                                               country_or_state=country_or_state,
                                               occupation_id=None,
                                               file_location=contestants_sql_location)
                player.generate_sql(entity_definition=contestant_entity_definition)
                contestant_count += 1

    print(" No. of occupations to be inserted : ", occupation_id-1)
    print(" No. of contestants to be inserted : ", contestant_count)