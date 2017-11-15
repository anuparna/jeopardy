import pandas


def generate_contestant(df_contestant):
    """

    @param df_contestant:
    @return:
    """

    # Generate group of customers with the same occupation.
    contestants_groups = df_contestant.groupby(df_contestant['occupation'])
    for occupation, group in contestants_groups:
        # print occupation
        print(occupation)
        # print the data of that regiment
        print(group)
