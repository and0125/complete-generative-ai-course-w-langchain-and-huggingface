# Streamlit

streamlit is a way to create beautiful websites for displaying data easily especially from LLMs and to power applications.

this is an open-source app framework for ML and DS projects. enables you to create beautiful applications for your projects.

He installs the following packages in a virtual env to use streamlit:

```text
# requirements.txt
ipykernel
numpy
pandas
matplotlib
seaborn
flask
memory_profiler
streamlit
```

Then you can create a file to write your code; this is `lesson-33.py`. You can load the title to the streamlit program, and you can run `python lesson-33.py` to setup a server on `localhost:8501` for streamlit, and can see this in your browser.

We created a project that displays text, a title, and a DataFrame, and creates a graph as well.

This becomes a great way to display a quick PoC in front of any boss.

We also use a `widgets.py` file to understand how to work with widgets in streamlit, which give us the ability to accept and adjust based on user interactions.

Use streamlit.io to look at other components within streamlit you can play with; there are many different charts and graphs to do this.

You can use this to create the entire web application you require.

Next class demos an ML application within Streamlit.

## Creating a Web App with Streamlit

We'll create a classification project with streamlit.

**NOTE**: there are deployment options for streamlit inside of snowflake, and within a streamlit community edition.

This app creates a sidebar with a slider to show predictions of the species of flower based on four factors.
