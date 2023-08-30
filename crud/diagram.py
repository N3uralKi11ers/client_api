import pandas as pd
import ast

from schemas import Diagram

def print_values_for_diagram(user_name):
    dat = pd.read_csv('data/bd.csv').set_index('Name').loc[user_name]
    col = [item for sublist in pd.read_csv('data/category.csv', index_col='Unnamed: 0').values for item in sublist]
    value = ast.literal_eval(dat.iloc[1])
    return value, col


def diagram_allocation(user_name) -> Diagram:
    shares, shares_titles = print_values_for_diagram(user_name)
    return Diagram(shares=shares, shares_titles=shares_titles)