from sql_generator import question
import pandas as pd


def generate_questions(questions_df, trend_df,
                       input_config, output_config):
    # get location of output files
    question_sql_location = output_config.get('files', 'questions')

    # reset the sql files
    open(question_sql_location, 'w').close()

    # get entity definition
    question_entity_definition = input_config.get('entities', 'question')

    question_counter = 0
    questions_trend_df = pd.merge(questions_df, trend_df,
                                  how='inner',
                                  on=['game_id', 'row', 'column'])
    print(questions_df.columns)
