# NLP In Machine Learning

## Overview

ML solves two types of problems; supervised and unsupervised learning.

Most of the supervised learning problems solve classification and regression problems. If we have a lot of features, they might be called independent features that are input features.

Your output feature is the dependent feature.

The aim of a supervised ML model is to predict the output based on the input value. The main aim is to create a model, train it with the data provided, and this model should be capable to make predictions of the output data based on new data that has the input data.

There are cases where some features are completely made up of text, like doing spam classification. So we'd get emails and then try to determine if its spam or not. Then you might have features like email subject, email body, etc. And you'd want to output whether or not the email is spam or not. The output could be boolean, binary, or two text strings too.

There are techniques like one hot encoding to change the data feature set, but if you need to learn from a specific word or phrase, the model can't learn from the natural language.

A model can't understand the particular text, but you can convert the text into meaningful `vectors`, which represent meaningful input for language. And we use NLP to make the text useful for predictions.

NLP is popular because there are plenty of automated devices that are able to understand natural language. Google is coming up with amazing things in this area.

## Roadmap

Bottom to top approach to learning this:

- Step 0: learning a programming language (ours is python)
- Step 1: text pre-processing: starts with cleaning text to make it useful; cleaning the input. like tokenization (pg to sentence, sentence to words, etc.), stemming, lemmatization, stop words, etc.
- Step 2: text preprocessing pt 2: converting cleaned text into vectors; learning topics like bag of words, TF IDF, unigrams, bigrams, etc. These vectors should make sure the context of the statement is captured.
- Step 3: Text preprocessing pt 3: this uses more advanced techniques like word2vec, average word2vec; other techniques to convert input text to vectors. Going from 2 to 3, the approach you are using are better, and we need to understand if the step 2 is sufficient for our use cases or not.
- Step 4: RNN LSTM RNN, GRU RNN: these are deep learning techniques for solving text related problems. These are neural networks to understand, and are a part of deep learning.
- Step 5: text pre-processing pt 4: word embeddings which use some amount of word2vec, but we can have more control here.
- Step 6: transformers: this is an advanced technique.
- Step 7: BERT; another advanced technique.

Going with this pattern is great to see how the techniques improve. As you go up, the accuracy increases, but the model size also increases.

We'll focus on the first 3 steps to start; then the next 4 steps as a part of the deep learning portion. We'll use packages like NLTK and Spacy for these advanced NLP works.

NLTK will be our focus. For deep learning we'll use tensorflow and pytorch (Google and facebook, respectively).

You have to do some intense pre-processing to get the data to be useful, and then pick the right type of model for the accuracy you need.