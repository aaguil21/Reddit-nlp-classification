### Contents:
- [Problem Stament](#Background)
- [File Structure](#Data-Import-and-Cleaning)
- [Feature Engineering](#Feature-Engineering)
- [Modeling](#Modeling)
- [Conclusion](#Conclusion)

# Problem Statement

Two common types of questions are those related to our health and our homes. The subreddits of r/AskDocs and r/HomeImprovement ask each of these type of questions respectively. As a data scientist, I want to explore the classification of these posts and creating a model that can determine to which subreddit a post belongs. This model can have multiple use cases, such as redirecting questions from the internet to proper medical outlets. 

When evaluating the model and it's use cases, an accuracy of at least 99% to reduce the amount of misclassified questions. A focus on the cases where medical questions are not misclassified would be prefered for the severity of the cases that could be involved.



# File Structure

```
├── presentation.pdf
├── README.md
├── scripts                                         # Contains script to read data from reddit API
├── notebooks                                       # Contains notebooks for dadta science workflow
    ├──Data_Cleaning_and_EDA.ipynb
    ├──Data_Preprocessing.ipynb
    └──Modeling.ipynb
├── imgs                                            # Collection of visualizations from data analysis 
└── data                                            # Includes original and clean/processed datasets
```

# Data Dictionary 

| Feature    | Data Type | Description                                                              |
|------------|-----------|--------------------------------------------------------------------------|
| post_id    | string    | ID associated with submission post                                       |
| title      | string    | Title for a subreddit post                                               |
| self_text  | string    | Body of text for subreddit post                                          |
| subreddit  | string    | The subreddit the post has been posted in: {r/AskDocs, r/HomeImprovement |
| comment    | string    | Top threaded comments from each of the posts                             |
| comment_id | string    | Id associate with the comment submission                                 |


# Feature Engineering



# Modeling

The types of models used to classify text to subreddits were:

    - Logistic Regression
    - Random Forest Classifier
    - AdaBoost Classifier
    - Bagging Classifier
    - Stacking Classifier

# Conclusion

While the best scoring models had an accuracy of 97%, this is below the treshold that I found acceptable for the number of posts that are given in a day to each subreddit. A average number of 500 posts are made to each subreddit a day, so then the model would be incorrectly determining around 15 posts that could be of serious nature. Applying this model to a pipeline where a larger input amount could result in delays for hundreds of user for serious medical questions. 

I do want to add that many stringent features where applied to the model to create a more general model. Without these restirctions, the models where able to determine above 98% accuracy. But, the flaws in these models would be that they would be harder to generalize to texts that are not of the nature of the two subreddits. 

