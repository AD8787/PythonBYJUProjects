import pandas as pd
import numpy as np

df1 = pd.read_csv("PROC138_datasets/shared_articles.csv")
print(df1.head())

df2 = pd.read_csv("PROC138_datasets/users_interactions.csv")
print(df2.head())

df1 = df1[df1["eventType"] == "CONTENT SHARED"]
df1.head()

def totalEvents(df1_row):
  totalLikes = df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"] == "LIKE")].shape[0]
  totalViews = df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"] == "VIEW")].shape[0]
  totalBookmarks = df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"] == "BOOKMARK")].shape[0]
  totalLFollows = df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"] == "FOLLOW")].shape[0]
  totalComments = df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"] == "COMMENT CREATED")].shape[0]
  return totalLikes + totalViews + totalBookmarks + totalLFollows + totalComments
df1["total_events"] = df1.apply(totalEvents,axis = 1)
df1.head()

df1 = df1.sort_values(["total_events"], ascending = False)

def convert(x):
  if isinstance(x, str):
    return x.lower()

  else:
    return ""

df1["title"] = df1["title"].apply(convert)

df1.head()

from sklearn.feature_extraction.text import CountVectorizer
count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df1['title'])

from sklearn.metrics.pairwise import cosine_similarity
cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

df1 = df1.reset_index()
indices = pd.Series(df1.index, index=df1['contentId'])

def get_recommendations(contentId, cosine_sim):
    idx = indices[contentId]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return df1['contentId'].iloc[movie_indices]

get_recommendations(-4029704725707465084, cosine_sim2)

