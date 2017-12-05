# column names of CSV
PLAYER_ID = 'player_id'
PLAYER_ID_X = 'player_id_x'
PLAYER_ID_Y = 'player_id_y'
OCCUPATION = 'occupation'
PLAYER_FIRST_NAME = 'player_first_name'
PLAYER_LAST_NAME = 'player_last_name'
HOMETOWN_CITY = 'hometown_city'
HOMETOWN_STATE = 'hometown_state'
GAME_ID = 'game_id'
SEASON = 'season'
SEASON_Y = 'season_y'
SEAT_LOCATION = 'seat_location'
ROUND = 'round'
QUESTION_TEXT = 'question_text'
CORRECT_RESPONDENT= 'correct_respondent'
CORRECT = 'correct'
POSITION = 'position'
QUESTION_ID = 'question_id'
ANSWER = 'answer'
CATEGORY_ID = 'category_id'
ROUND_NAME = 'round_name'
DOLLAR_VALUE = 'dollar_value'
IS_DAILY_DOUBLE = 'is_daily_double'
QUESTION_INDEX = 'question_index'
FILE_LOCATION = 'file_location'
VALUE_X = 'value_x'

# criteria on columns used for matching rows in CSVs
NON_DUPLICATED_PLAYER_CRITERIA_COLUMNS = ['player_first_name',
                                          'player_last_name',
                                          'hometown_city',
                                          'hometown_state',
                                          'occupation']
QUESTION_TREND_COMMON_COLUMNS_CRITERIA = [GAME_ID,
                                          'row',
                                          'column',
                                          ROUND]


# input config file names
CONTESTANTS = 'contestants'
OCCUPATIONS = 'occupations'
CONTESTANT = 'contestant'
GAME = 'game'
CONTESTANT_LOCATION = 'contestant_location'
QUESTIONS = 'questions'
QUESTION = 'question'
CATEGORY = 'category'
CORRECT_RESPONSE = 'correct_response'

