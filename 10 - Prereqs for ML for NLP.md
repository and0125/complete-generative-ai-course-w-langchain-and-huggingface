# Notes

**NOTE**: I started taking these notes somewhere else, but found this orignal location again. Some of the notes on tokenization, stemming, and lemmas are likely somewhere else.

## Lemmatization for Text Preprocessing

Lemmatizing is a process that's like stemming, but the process of lemmatization is to produce a `lemma` which is the root word, instead of the root of the word. These are close, but slightly different. `lemmas` shouldn't change the meaning of the word, in the way that stems would. A lemma is a meaningful word, and not a root of a word that could change the meaning.

example:

```python
from nltk.stem import WordNetLemmatizer


lemmatizer=WordNetLemmatizer()

lemmatizer.lemmatize("going",pos="a")
```

The `pos` argument is the part of speech; which would be:

```text
Noun = n
verb = v
adjective = a
adverb = r
```

You can then use lemmatizion to remove words that are repetitive or to make sure you are understanding the root word, and getting whole words each time, instead of partial fragments of words like stemming results in.

So lemmatizing provides a meaningful word while providing meaningful word as output.

Use the `WordNetLemmatizer()` most of the time; it will take time for larger bodies of text.

Lemmatization is a great step for Q&A, Chatbot functionalities, text summarization, etc.

## StopWords

This is another text pre-processing technique.

These are helpful for making sure our text is cleaned, so that we can transform those clean text into vectors for performing the machine learning.

Stop words happen in natural language. These are words like `I`, `the`, `why`, `we` etc. These words won't play a large role in translating text, or summarizing a text; these have less of a role. But words like `not` are very powerful when doing summarization.

So when we have a body of text, we can remove stopwords alone, or combine it with stemming, which is a useful technique.

**NOTE**: stopwords are different in every language.

```python
form nltk.stem import PorterStemmer
from nltk.corpus import stopwords

# downloading the data to use; especially for the stop words
import nltk
nltk.download("stopwords") # this will have all the stop words from all the languages in nltk

# to get the one's in english
stopwords = stopwords.words("english") # returns a list of all the stop words
```

We can also create our own list of stopwords ourselves; some of the nltk words included should still be included, like before and after, not, etc.

There are some languages that aren't included in this naturally.

```python
# imagine there is a speech text in a variable called
speech = "..."

from nltk.stem import PorterStemmer

stemmer=PorterStemmer()

sentences = nltk.sent_tokenize(speech)

stopwords = stopwords.words("english")

# we apply stop words and filter
for i in range(len(sentences)):
    # grabbing each sentence as words
    words = nltk.word_tokenize(sentence[i])

    # gets only the words not in the stopwords; and makes sure the stop words are unique just in case
    words = [ stemmer.stem(word) for word in words if word not in set(stopwords)]

    sentences[i] = ' '.join(words)# converting back to a sentence

# see output
print(sentences) # will have transformed sentences
```

You can also do this with the snowball stemmer for better results; would still have capital letters in porterstemmer, and snowball makes sure these are lower case.

And to get better root words, use a lemmatizer:

```python
lemmatizer = WordNetLemmatizer()

for i in range(len(sentences)):

    words = nltk.word_tokenize(sentence[i])

    words = [ lemmatizer.lemmatize(word.lower()) for word in words if word not in set(stopwords)]

    sentences[i] = ' '.join(words)

print(sentences)
```

This creates great shortened sentences. Also remember you can add the `pos` tag to the lemmatize() function this can be even more effective; you can generalliy use `pos='v'` to treat words like verbs, which can be helpful to translate to the root word. This gives back individual words that are unique and meaningful for each sentence.

You can also include the lowercasing as a pre-check before starting to manipulate the strings with `words.lower()`.

This is the text pre-processing; you can also do regex pre-processing.

## Parts of Speech Tagging

This is important for lemmatization; because if you have a word that's a verb or a noun, you can get to the correct root word.

We'll see all the parts of speech, and then, with the help of the text pre-processing, we can consider and tag each word with its proper part of speech.

There are several options that can be used for the `pos` value, and there are 35 different types that nltk can assign to each word.

He's using the same speech example:

```python
paragraph = "..."

import nltk

sentences = nltk.sent_tokenize(paragraph)

```
