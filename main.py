from mytools import load_data, count_by_type

df = load_data()
print('行数 =', len(df))
print(count_by_type(df))
