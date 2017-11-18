from sql_generator import game
from sql_generator import contestant_location


def generate_game(df_contestant_loc, input_config, output_config):
    """
    Generate SQL for the entity game based on the data available for contestant_location
    @param df_contestant_loc: Pandas data-frame representing locations.csv
    @param input_config: Input configuration
    @param output_config: Output configuration, primarily used to retrieve the location of the .sql file to be generated
    @return: game_counter: count of the no. of rows to be inserted in the entity game
    """
    game_counter = 0

    # get location of output files
    game_sql_location = output_config.get('files', 'game')

    # get entity definition
    game_entity_definition = input_config.get('entities', 'game')

    # select columns required for game and clean data
    df_game = df_contestant_loc[['game_id', 'season']]
    df_game = df_game.drop_duplicates(keep='first')

    # generate sql for game
    for index, row in df_game.iterrows():
        game_counter += 1
        episode = game.Game(game_id=row['game_id'],
                            season_num=row['season'],
                            file_location=game_sql_location)
        episode.generate_sql(game_entity_definition)

    return game_counter


def generate_contestant_location(df_contestant_loc, input_config, output_config):
    """
    Generate SQL for the entity game based on the data available for contestant_location
    @param df_contestant_loc: Pandas data-frame representing locations.csv
    @param input_config: Input configuration
    @param output_config: Output configuration, primarily used to retrieve the location of the .sql file to be generated
    @return: loc_counter: count of the no. of rows to be inserted in the entity contestant_location
    """
    loc_counter = 0

    # get location of output files
    contestant_loc_sql_location = output_config.get('files', 'contestant_location')

    # get entity definition
    contestant_loc_entity_definition = input_config.get('entities', 'contestant_location')

    # select columns required for game and clean data
    df_player_loc = df_contestant_loc[['game_id', 'player_id', 'seat_location']]
    df_player_loc = df_player_loc.drop_duplicates(keep='first')

    # generate sql for game
    for index, row in df_player_loc.iterrows():
        location = contestant_location.ContestantLocation(game_id=row['game_id'],
                                                          contestant_id=row['player_id'],
                                                          seat_location=row['seat_location'].strip(),
                                                          file_location=contestant_loc_sql_location)
        location.generate_sql(contestant_loc_entity_definition)
        loc_counter += 1

    return loc_counter


def generate_sql_statements(df_contestant_loc, input_config, output_config):
    """
    Generate SQL insert statements for entities, Game and Contestant_location.
    @param df_contestant_loc: Pandas data-frame representing contestant location information
    @param input_config: Input Configuration
    @param output_config: Output Configuration
    @return:
    """
    no_of_games = generate_game(df_contestant_loc=df_contestant_loc,
                                input_config=input_config,
                                output_config=output_config)
    print(" No. of games to be inserted : ", no_of_games)

    no_of_contestant_locations = generate_contestant_location(df_contestant_loc=df_contestant_loc,
                                                              input_config=input_config,
                                                              output_config=output_config)
    print(" No. of contestant locations to be inserted : ", no_of_contestant_locations)
