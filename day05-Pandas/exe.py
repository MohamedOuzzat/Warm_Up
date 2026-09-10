import pandas as pd

df = pd.read_csv("file/data.csv")

# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.columns)
# print(df.index)
# print(df.dtypes)
# print(df.info())
# print(df.describe())

# cat_cols = df.select_dtypes(include=['str', 'category']).columns
# num_cols = df.select_dtypes(include=['number']).columns
# print(cat_cols)
# print(num_cols)

# print(df["ville"].unique())

# no_uniq=df['ville'].nunique()
# print(no_uniq)



# print(df.isnull())
# print(df[df.isnull()])

# result=df.groupby('ville')['client_id'].count()


# print(result)
print(df)





