# Langchain

## Langchain Overview

Langchain is the most common framework to build AI applications.

When Open AI and HuggingFace, these were the first two companies to come up with the LLM concept; other companies were doing this but these were the first to market. Open AI came up with GPT model.

When this started, the developers started exploring; and OpenAI had different libraries, like the transformer API for developing pipelines. Also API keys were needed for things like fine-tuning.

But as more companies came to market, different libraries were getting created for each of these models.

Langchain as a company came up with a common framework to develop Gen AI applications. these were libraries they could provide access to; and when you have this open source code, it makes it easy to create from open source models and make these applications.

If you create a Gen AI application, and you may be using an open source or paid LLM, but how do you make sure you can do LLMOps, like:

- debugging
- monitoring
- evaluation
- playground

Langchain created an eco-system for these activities, which now can be done with a library called LangSmith.

The main thing it does was create this other libraries to work with.

Also there is LangServe for creating the chains as a rest APIs.

This is an eco-system because LangChain is the core for interacting with the model. And the course will cover the entire services available.

Also will cover deployment to AWS and Hugging Face.

Initially langchain came and was able to work with a number of different models.

Also Langchain-Community you can access the open source models, but the paid models require an API keys. You can use retrieval for loading documents, a vector store for working with text as a chatbot (there are a variety of these databases).

We'll focus on the entire lifecycle of a generative AI product.

## Virtual Environment

Created a new folder for this project (each end to end project will have its own folder).

Always needed to do a virtual env, and we'll add a specific set of packages in this venv.

He recommended using python 3.10 for these uses.

```text
# requirements.txt
langchain
jupyter
notebook
```

installing happened, then you're good to start projects in langchain. We'll do most of the beginning coding in a jupyter notebook, then move to files once we go through the basics.

Need to have at least $5 for using the OpenAI API, which is useful for just getting the fundamentals of working with these APIs.

Langchain is an open source framework for developing a Gen AI application. You actually need to create an account to use some of these modules. This enables you to create projects. 
