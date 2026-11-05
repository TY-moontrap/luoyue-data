import pandas as pd

def load_data(path='data/data.csv'):
    """读 CSV，返回一张表。参数 path 可以换文件。"""
    df = pd.read_csv(path, encoding='utf-8')
    return df

def count_by_type(df):
    """按 type 列计数，返回从多到少的序列。"""
    return df['type'].value_counts()
