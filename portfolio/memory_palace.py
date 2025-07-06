#User creates memory item
# e.g. memory_text = "Remember to call mom"
#pick random location = "Kitchen table"
# Generating prompt = "An elephant sitting on a kitchen table is making a phone call with a giant green telephone in his lab and calling mom"

from faker import Faker
import spacy

# Load the language model
nlp = spacy.load("en_core_web_sm")

# Process text
text = "Call Mom"
doc = nlp(text)

    # Extract different parts
    for token in doc:
    if token.pos_ == "VERB":
        print(token)
    print(f"{token.text} | {token.pos_} | {token.dep_}")


#Libraries:
'''Text Processing & Analysis
spaCy - Excellent for extracting nouns, verbs, and understanding sentence structure. Great for identifying what's actually important in user input.
TextBlob or VADER - Simple sentiment analysis to detect if something is urgent/emotional vs routine.
wordnet (from NLTK) - Find synonyms, related words, and word associations automatically. Perfect for "milk → cow → farm" chains.
Random Generation & Templates
Faker - Generates realistic random data (names, places, objects) that you can mix into descriptions.
Text-to-Speech (for later)
pyttsx3 - Offline text-to-speech, works everywhere, customizable voices.
gTTS - Google's text-to-speech API, higher quality but requires internet.
Data Storage
TinyDB - Lightweight JSON database for storing palaces and user progress without database complexity.
pickle (built-in) - Simple object serialization for saving user data.'''


