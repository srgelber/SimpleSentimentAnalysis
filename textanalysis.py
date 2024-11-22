from textblob import TextBlob


with open('mytext.txt','r') as f:
    text = f.read()

print(text)
blob = TextBlob(text)
sentiment = blob.sentiment.polarity #score from -1 to 1
print(sentiment)