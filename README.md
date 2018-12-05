# Data science portfolio by Hye Seung Lee
This portfolio is a compilation of notebooks which I created for data analysis or for exploration of machine learning algorithms. Please browse through each section to see each project.

## UvA Data Science Master's thesis project

### Motivations & Hypotheses

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

## UvA Communication Research Science Master's thesis project
