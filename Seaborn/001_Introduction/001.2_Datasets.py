import seaborn as sns
print(sns.get_dataset_names())

df = sns.load_dataset("titanic")
print(df.head())