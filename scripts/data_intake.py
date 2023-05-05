# This code is used to reguraly intake REDDIT post data using the PRAW api

import pandas as pd
import praw
from datetime import datetime

date = datetime.today().strftime('%Y-%m-%d')

reddit = praw.Reddit()

#ask_doc_reddit = reddit.subreddit('askdocs')
#home_improve_reddit = reddit.subreddit('homeimprovement')

subreddits = []

def reddit_data(sub_name):
    subreddit = reddit.subreddit(sub_name)
    subreddit_data = []

    for post in subreddit.new(limit=1000):
        if not post.stickied:
            post.comments.replace_more(limit=5)
            if len(post.comments) > 0:
                for comment in post.comments:
                    subreddit_comment = {}
                    subreddit_comment['post_id'] = post.id
                    subreddit_comment['title'] = post.title
                    subreddit_comment['self_text'] = post.selftext
                    subreddit_comment['subreddit'] = post.subreddit
                    
                    if not comment.stickied:
                        subreddit_comment['comment'] = comment.body
                        subreddit_comment['comment_id'] = comment.id
                    else:
                        subreddit_comment['comment'] = None
                        subreddit_comment['comment_id'] = None
                    subreddits.append(subreddit_comment)
            else:
                subreddit_comment = {}
                subreddit_comment['post_id'] = post.id
                subreddit_comment['title'] = post.title
                subreddit_comment['self_text'] = post.selftext
                subreddit_comment['comment'] = None
                subreddit_comment['comment_id'] = None
                subreddit_comment['subreddit'] = post.subreddit
                subreddits.append(subreddit_comment)
    return subreddit_data

subreddits += reddit_data('askdocs')
subreddits += reddit_data('homeimprovement')

df = pd.DataFrame(subreddits)

df.to_csv(f'../data/reddit_submissions_{date}.csv')