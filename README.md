# Data science portfolio by Hye Seung Lee
This portfolio is a compilation of notebooks which I created for data analysis or for exploration of machine learning algorithms. Please browse through each section to see each project.

## UvA Data Science Master's thesis project

### Introduction

People are motivated to resist persuasion in many situations. In recent years, scholars have identified and categorized several resistance strategies in the field of Communication Science. Yet, resistance to persuasion has been difficult to measure due to certain
response biases, such as social desirability. This study aims to fill the academic gap by automating the measurement of resistance
strategies towards persuasion by answering the first research question:

a) Can resistance attempts and strategies be adequately classified?

By reaching an adequate level of automated classification for the strategies, this study further seeks to gain the practical understanding of how everyday people use different ways to resist persuasion depending on domains and types of information. Thus,
another substantial research question is: 

b) Do people use resistance strategies more or less depending on certain domains and types of online news? 

Using a manually structured dataset of online news comments, multiple supervised machine learning classifiers were trained and tested. In a stepwise method, the comments were first classified according to the presence or absence of a resistance attempt. Second-level classification was based on the extent of the three resistance strategies: "contesting," "empowerment," and "negative affect." Results show that the best performing model for the first and second-level classifications of contesting, empowering, and negative affect strategies achieved F1 scores of .78, .75, .78, .79, respectively. Moreover, people’s use of resistance strategies was found to depend on domains (politics & economy vs. lifestyle & health) and types of news (regular vs. opinion).

### Data Collection

#### Web Scraping

#### Manual Annotation

#### Inter-coder Reliability Test

#### Internet Argument Corpus (IAC)

### Variables

### Infrastructure

All the steps from pre-processing to machine learning modeling were executed on Google’s cloud computing instance with 16 CPU cores and 60GB of memory with 2 NVIDIA K80 GPUs.

### Pre-processing

The scraped texts of comments are assumed to be unclean as they usually have punctuation, Emojis, URLs, and typos. To clean the texts, the NLTK library were used to filter out stopwords and lemmatize the words.

### Feature Extraction

#### A. Term Frequency-Inverse Document Frequency (TF-IDF)
#### B. Sentiment Analysis
#### C. Word Embedding Techniques

### Learning Algorithms

Multinomial Naïve Bayes, Support Vector Machines, Decision Trees, Stochastic Gradient Descent, Perceptron, AdaBoost, Majority Voting classifiers were tested.

### Performance Evaluation Metrics

For performance evaluation of the supervised machine learning algorithms, the following metrics are considered and reported: precision,
recall, F1, and AUC measure. Precision represents the ratio of the number of comments correctly labeled as positive to the total number of positively classified comments. Recall represents the ratio of the total number of positively labeled comments to the total comments which are truly positive. The F1 measurement is the mean of precision and recall, where an F1 score reaches its best value at 1. The Area Under the Curve (AUC) measurement represents the probability that the algorithms will rank a randomly chosen positive comment higher than a randomly chosen negative comment.

