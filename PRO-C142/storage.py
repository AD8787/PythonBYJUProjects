import csv

all_articles = []

with open("PROC138_datasets/shared_articles.csv", encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
not_liked_articles = []