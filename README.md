# Poli_KOL_Detection
A tweet analysis project based on NLP(LDA modeling) and Network Analysis

## Introduction
In China, the influences of social media have widely permeated through people’s lives and the emergence of key opinion leaders (KOLs) in cyberspace greatly strengthens the information-spreading effects via social media. This project discerns the strategies taken by political key opinion leaders (KOLs) to shape their community influences from the politics-related forum section on Weibo, one of the biggest social media in China. Based on the latent Dirichlet allocation (LDA) modeling, relevant tweets under this section were integrated to construct a tweet corpus, from which 9 topics were derived. Meanwhile, community detection was further performed to find out the top 10 most influential KOLs under the section. Combining topic modeling and community detection, the strategy that was taken by the KOLs to shape their influences was fathomed based on qualitative analyses: On one hand, KOLs particularly concentrated on ongoing political affairs related to bilateral politics with clear biases to express their opinions. On the other hand, topics that were chosen by these key opinion leaders are close to the daily lives of normal people, ensuring strong realisticity and understandability to immerse target users in the discussion.

## Data Preprocessing
41,848 tweets between 2011-2016 were selected for the purpose to establish a corpus for tweet topic detection, which were drawn under the politics-related forum section from Sina Weibo, one of the biggest Chinese social media. 

Original data is: text_dta.csv

Cleaned data is: dta_cleaned.csv (Which is generated by clean.py)

Both files can be found under "data" directory.

Under "utils" a "tokenize.py" file is provided. This file is used to tokenize the tweets to get prepared for subsequent NLP analysis.

## Model Construction
The process of model construction is presented in the Jupyter Notebook file "analysis_model.ipynb" .

## To go through the whole process, these modules are needed:

```
pandas
jieba
zhon
gensim
pyLDAvis
IPython
pickle
re
```
