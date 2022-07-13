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