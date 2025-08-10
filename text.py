from textblob import TextBlob

text = "I really love learning Python, but sometimes debugging can be frustrating."
blob = TextBlob(text)

polarity = blob.sentiment.polarity
subjectivity = blob.sentiment.subjectivity
word_count = len(blob.words)

print("Text:", text)
print("Word Count:", word_count)
print("Polarity:", polarity)
print("Subjectivity:", subjectivity)

misspelled = "I havv a speling errror."
corrected = TextBlob(misspelled).correct()

print("\nOriginal:", misspelled)
print("Corrected:", corrected)
