from textblob import TextBlob
from newspaper import Article
import nltk


url = 'https://abcnews.go.com/US/laken-riley-suspect-guilty-murder/story?id=116030068'
article = Article(url)

article.download()
article.parse()
article.nlp()


text = article.summary

print(text)
blob = TextBlob(text)
sentiment = blob.sentiment.polarity #score from -1 to 1
print(sentiment)