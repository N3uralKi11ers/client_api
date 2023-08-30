import pandas as pd
import ast

from schemas import TransactionBase


# read user history
def print_users_history(user_name):
    data = pd.read_csv('data/Peop_Hist.csv', index_col='Unnamed: 0').set_index('Name').loc[user_name]
    return data.values


# read transactions
def get_transactions(user_name) -> [TransactionBase]:
    transactions: [TransactionBase] = []
    df = print_users_history(user_name)
    for product_title, amount, dt in df:
        transaction = TransactionBase(
            product_title=product_title,
            price=amount,
            datetime=dt,
        )
        transactions.append(transaction)

        
    return transactions