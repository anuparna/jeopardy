from sql_generator import Question
from sql_generator import Round
from sql_generator import Category
from sql_generator import CorrectResponse
import pandas as pd


def generate_sql_statements(questions_df,
                            trend_df,
                            final_results_df,
                            player_location_df,
                            input_config,
                            output_config):
    """
    Generate sql statements for question, category, correct_response and wager
    @param questions_df: Pandas data-frame from questions.csv
    @param trend_df:  Pandas data-frame from trend.csv
    @param final_results_df:  Pandas data-frame from final_results.csv
    @param player_location_df: Player information with seat-location, game_id and contestant_id
    @param input_config: Input configuration
    @param output_config: Output configuration
    @return: None
    """
    # get location of output files
    question_sql_location = output_config.get('files', 'questions')
    category_sql_location = output_config.get('files', 'category')
    correct_response_sql_location = output_config.get('files', 'correct_response')

    # reset the sql files
    open(question_sql_location, 'w').close()
    open(category_sql_location, 'w').close()
    open(correct_response_sql_location, 'w').close()

    # get entity definition
    question_entity_definition = input_config.get('entities', 'question')
    category_entity_definition = input_config.get('entities', 'category')
    correct_response_entity_definition = input_config.get('entities', 'correct_response')

    # get data from multiple CSVs - questions and trend - for 2 rounds - J and DJ
    questions_trend_df = pd.merge(questions_df,
                                  trend_df,
                                  how='outer',
                                  on=['game_id', 'row', 'column', 'round'])
    questions_trend_contestant_df = pd.merge(questions_trend_df,
                                             player_location_df,
                                             how='outer',
                                             left_on=['correct_respondent', 'game_id'],
                                             right_on=['seat_location', 'game_id'])

    # collect correct responses for final round questions
    final_round_questions_df = questions_trend_contestant_df.loc[questions_trend_contestant_df['round'] == Round.final.name]
    # find player associated with the seat location of the correct respondent of final round questions
    final_results_df = pd.merge(player_location_df,
                                final_results_df,
                                how='inner',
                                left_on=['seat_location', 'game_id'],
                                right_on=['position', 'game_id'])
    final_results_df = final_results_df.loc[final_results_df['correct'] == True] # collect only correct respondents
    # find matches
    final_question_correct_responses_df = pd.merge(final_round_questions_df,
                                                   final_results_df,
                                                   how='outer',
                                                   on=['game_id'])


    # generate SQL files
    no_of_questions, no_of_question_categories, no_of_correct_responses \
        = generate_questions(questions_trend_contestant_df,
                             final_question_correct_responses_df,
                             question_sql_location,
                             question_entity_definition,
                             category_sql_location,
                             category_entity_definition,
                             correct_response_sql_location,
                             correct_response_entity_definition)

    print(" No. of question categories to be inserted : ", no_of_question_categories)
    print(" No. of questions to be inserted : ", no_of_questions)
    print(" No. of correct responses to be inserted : ", no_of_correct_responses)


def generate_categories(category_id, category_name, category_sql_location, category_entity_definition):
    """
    Generate SQL statements for Category
    @param category_id: Id of the Category
    @param category_name: Name of the category
    @param category_sql_location: Location of category.sql to be generated
    @param category_entity_definition: Entity definition of Category
    @return: None
    """
    if category_name:
        category = (category_name.strip()).replace("'", "\\'")
        question_category = Category(category_id,
                                     category,
                                     file_location=category_sql_location)
        question_category.generate_sql(entity_definition=category_entity_definition)


def generate_questions(questions_trend_contestant_df,
                       final_question_correct_responses_df,
                       question_sql_location,
                       question_entity_definition,
                       category_sql_location,
                       category_entity_definition,
                       correct_response_sql_location,
                       correct_response_entity_definition):
    """
    Generates SQL statements for category and question entities
    @param questions_trend_contestant_df: Combination of questions csv, trend csv and
                                          contestant seat location based on the game in the
                                          form of Pandas data-frame
    @param final_question_correct_responses_df: Pandas data-frame containing contestants who responded perfectly
                                                to questions asked in the final round
    @param question_sql_location: SQL file location of the to-be generated questions
    @param question_entity_definition: Entity definition of the SQL entity - question
    @param category_sql_location: SQL file location of the to-be generated question - categories
    @param category_entity_definition: Entity definition of the SQL entity - category
    @param correct_response_sql_location: SQL file location of the to-be generated question - correct_response
    @param correct_response_entity_definition: Entity definition of the SQL entity - correct_response
    @return question_counter: Total no. of questions to be inserted
    @return category_counter: Total no. of question categories to be inserted
    @return correct_responses_counter: Total no. of correct responses to be inserted
    """
    question_counter = 0
    category_counter = 0
    correct_responses_counter = 0
    questions_param = {}
    # Generate group of customers with the same occupation
    question_groups = questions_trend_contestant_df.groupby(questions_trend_contestant_df['category'])
    for category, question_rows in question_groups:
        # Generate SQL for category
        if category:
            category_counter = category_counter + 1
            generate_categories(category_id=category_counter,
                                category_name=category,
                                category_sql_location=category_sql_location,
                                category_entity_definition=category_entity_definition)

            # Generate SQL for question
            no_of_questions = len(question_rows)
            for index in range(no_of_questions):
                question_row = question_rows.iloc[index]
                question_counter += 1
                questions_param['question_id'] = question_counter

                question_text = (question_row['question_text'].strip())
                question_text = question_text.replace('"', '\\"')
                question_text = question_text.replace("'", "\\'")
                question_text = question_text.replace("\\\\'", "\\'")
                questions_param['question_text'] = question_text

                answer = (question_row['answer'].strip())
                answer = answer.replace('"', '\\"')
                answer = answer.replace("'", "\\'")
                answer = answer.replace("\\\\'", "\\'")
                questions_param['answer'] = answer

                questions_param['dollar_value'] = question_row['value_x']
                questions_param['file_location'] = question_sql_location
                questions_param['game_id'] = question_row['game_id']
                questions_param['round_name'] = (question_row['round'].strip()).replace("'", "\\'")
                questions_param['category_id'] = category_counter

                if pd.notnull(question_row['season_y']):
                    if pd.notnull(question_row['wager']):
                        questions_param['is_daily_double'] = 1
                    else:
                        questions_param['is_daily_double'] = 0
                    questions_param['question_index'] = question_row['question_index']

                question = Question(**questions_param)
                question.generate_sql(question_entity_definition)

                # insert data for correct respondent to the question
                if question_row['round'] == Round.final.name:
                    # Final round questions can have multiple correct respondents.
                    # select those rows
                    question_game_id = question_row['game_id']
                    final_round_correct_respondents = \
                        final_question_correct_responses_df.loc[final_question_correct_responses_df['game_id']
                                                                == question_game_id]

                    for final_round_correct_responses_counter, final_round_responses_row \
                            in final_round_correct_respondents.iterrows():
                        if pd.notnull(final_round_responses_row['player_id_y']):
                            correct_responses_counter += 1
                            generate_correct_respondent(contestant_id=final_round_responses_row['player_id_y'],
                                                        question_id=question_counter,
                                                        correct_response_sql_location=correct_response_sql_location,
                                                        correct_response_entity_definition=
                                                        correct_response_entity_definition)
                elif pd.notnull(question_row['player_id']):
                    # Insert correct respondents for Jeopardy and Double Jeopardy rounds
                    correct_responses_counter += 1
                    generate_correct_respondent(contestant_id=question_row['player_id'],
                                                question_id=question_counter,
                                                correct_response_sql_location=correct_response_sql_location,
                                                correct_response_entity_definition=correct_response_entity_definition)

    return question_counter, category_counter, correct_responses_counter


def generate_correct_respondent(contestant_id,
                                question_id,
                                correct_response_sql_location,
                                correct_response_entity_definition):
    """
    Create SQL statements for Correct Response
    @param contestant_id: Unique Id of the contestant
    @param question_id: Unique Id of the question
    @param correct_response_sql_location: SQL file location of the to-be generated correct-response
    @param correct_response_entity_definition: Entity definition of correct_response
    @return: None
    """
    contestant_correct_response = CorrectResponse(contestant_id,
                                                  question_id,
                                                  file_location=correct_response_sql_location)
    contestant_correct_response.generate_sql(entity_definition=correct_response_entity_definition)
