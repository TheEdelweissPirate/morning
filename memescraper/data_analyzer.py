import pandas as pd
subreddits = pd.read_csv("subreddits_public.csv")
print(subreddits.head())
subreddits = subreddits.dropna() 
#pd.Series(subreddits).astype(int)
df_filtered = subreddits[(subreddits["subscribers_count"]).astype(int) >= 1000] 
  
# Print the new dataframe 
print(df_filtered.head(15))
  
# Print the shape of the dataframe 
print(df_filtered.shape)

