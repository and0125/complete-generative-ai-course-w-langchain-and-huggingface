# What is Generative AI

from 2022 until now, generative AI is the big thing. How is generative AI different from AI, ML, and DL?

- AI: these are applications that can perform a task without human intervention. For instance, Netflix's recommendation system presents movies that are personalized to a user, without a human manually recommending these films.
  - AI engineers are people who are creating an AI product, which may be integrated with a software product itself. AI products would be a mobile or web, or IoT application that uses AI for automated tasks.
- ML: machine learning is a subset of AI which uses statistical tools to perform various tasks, like analysis visualization, prediction, and forecasting. This requires a full ML lifecycle - data cleaning, cleansing, feature engineering, etc. These analyses are performed on and the ML makes decisions about data records, which helps you to understand the data to derive insights.
- DL: deep learning started in the 1950s, but only became technically feasible more recently. This is a subset of ML that mimics the human brain's function, and how we learn. This is where multi-layer neural networks come into play. 3 main features to learn for Deep Learning: ANN works for how the model is trained, CNN and object detection for computer vision, RNN and its variants for text related or time series use cases. From RNNs we get the transformer and BERT architecture.
- Gen AI: transformers and BERT are the backbone of generative AI. These are the most advanced techniques for mimicking the human brain. There are two types of model training: discriminative and generative models. Deep learning models are of two types: discriminative models and generative models. Generative AI is more about these generative models, which generate new content based on what the model has been trained on. Discriminative models are meant for classification, prediction sort of problems. The discriminiative use cases also require a model trained on labeled data. Also, we need Generative models to be trained on a large amount of data to be effective.
  - two types of Models for Generative AI: LLM for large language models; and large image models.
  - Generative AI has models that are already trained on huge amounts of data, and can respond with respect to the data its been trained on.

Companies like Open AI, Meta, Google, Anthropic, Vercel. These are GPT4, Llama, Gemma, Claude, and these are known as foundation or pre-trained models. This is because they are trained on the entire internet's worth of data at a specific time. Stability is a company working on LIMs.

You can then fine tune these foundational models for specific tasks, with LoRA and QLoRA. The idea is to get the best foundation model and then use it to fine tune for your domain specific task. You can fine tune with your own custom data set.

Langchain is a framework for working with each particular model; we'll use this to build several applications.

**NOTE**: it is likely not possible to train a full LLM model on your own, but we can understand the process for training these LLMs, and its just not possible to do practically, but we can understand this conceptually.

## How LLMs are trained

Stage 0: thinking through the internet data used to train the model
Stage 1: train a generative pre-trained model to create a GPT like model
Stage 2: use supervised fine tuning to make the data domain specific
Stage 3: perform reinforcement learning over time to prevent drift, from human feedback

This is the big steps of a GPT model.

Say you are learning about dogs:

- you read 500 books on dogs
- you are asked a question about dogs
- you respond with the answers from the books you know

This is the mental model to keep in mind.

### Stage 1

You pass internet data into your transformer, and this data trains the transformers and creates a GPT-like base model. This would be able to do:

- language translation,
- text summarization,
- text completion,
- and sentiment analysis.

All those tasks can be easily implemented once you have this transformer trained.

However we want to use this model for a conversational chatbot. We want this functionality where we give a request and get a response; which is a combination of the four tasks above.

To get to this chat feature, we do the next stage.

### Stage 2

For a real conversation, we model this as one person saying something, then another responses, and you build on the responses. This is the essence of how chat bots function.

Having the requests and responses continually is important to get captured.

This response and request cycle is turned into an SFT(supervised fine tuning) training data corpus for a conversation.

We'll create a training data set based on the request having the conversation history, and the response giving an ideal response.

This training data set is used to train the base GPT model, using stochastic gradient descent.

So you'll be able to get this chat functionality after this second stage.

This SFT Chat GPT model will give output based on the data it was trained with; but if you ask questions that aren't in the training data, you'll get hallucinations.

### Stage 3

Reinforcement learning helps to prevent and create boundaries for hallucinations by using human feedback to help direct the chatbot to the correct answers.

The first two stages have a standard and best practices, but this third stage is the latest addition that is cutting edge.

So you send a request, and obtain a response or several responses. Based on the responses, you can use a human to rank the responses to see which is the most suitable response. Based on the response ranking, you create a reward model for the model, so that each response has a score, and the ranking determines the quality of the response.

Mental model:

- you ask a chef for a vegan dish with certain ingredients
- the chef doesn't know, but will ask their other chef friends for their best recipes
- the responses will come in from the friends
- the chef will then rank the particular recipes (the reward model)
- and based on the recipe the chef thinks is best, the chef will send it to you
- you will evaluate if the recipe is good for you
- you tell the chef, and the chef adjusts based on the new info, and goes through the process again (reinforcement)

this way the chef's response improves over time, and if someone else asked the chef for a vegan recipe with the same ingredients, the chef should be quicker at providing a satisfactory answer.

So stage 1 and stage 2 are standardized, the data set for stage 2 could be created as well.

Bu this third stage requires a huge amount of data and human responses to get right.

## LLM Analysis

check out [this website](artificalanalysis.ai) which compares the different AI models for their quality, speed, and price. on April 2nd 2025, Gemini 2.5 pro is leading on all these deminsions. Claude is middle to bottom of the pack; GPT is mid to last.

So Gemini 2.5 Pro is going to be the best model to work with for the time being; see `gemini.google.com` for use. has a paid tier and a free tier too.
