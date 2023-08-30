import pandas as pd
import ast

# read cashback by username
def print_name_cashback(user_name):
    dat = pd.read_csv('data/bd.csv').set_index('Name').loc[user_name]
    col = [item for sublist in pd.read_csv('data/category.csv', index_col='Unnamed: 0').values for item in sublist]
    value = ast.literal_eval(dat.iloc[0])
    sorted_indices = sorted(range(len(value)), key=lambda i: value[i], reverse=True)[:3]

    result = [col[i] for i in sorted_indices]
    return result[0], result[1], result[2]


def get_cashback(user_name):
    return print_name_cashback(user_name)