# Import the textgetter function from the textgetter.py file
from textgetter import textgetter
# import nltk
# nltk.download('punkt')

# URL to test
test_url = "https://whitepaper.apeironnft.com/apeironnft/ascension-introduction-to-apeiron/a-new-kind-of-god-game"  # Replace this with the actual URL you want to test

# Call the textgetter function with the test URL
results = textgetter(test_url)

for result in results:
    print(result)