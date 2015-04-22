#!/usr/bin/env python
"""
Bot file

@author     james@temboinc.com
@since      2015-04-22
"""
import os
import sys
import praw
import time
from pprint import pprint

r = praw.Reddit('test')
r.login()

search = ['uniqlo', 'nordstrom']
already_done = []

while True:
	subreddit = r.get_subreddit('frugalmalefashion')
	for submission in subreddit.get_new(limit=10):
		op_body = submission.selftext.lower()
		op_title = submission.title.lower()
		op = op_body + " " + op_title
		has_search = any(string in op for string in search)
		if submission.id not in already_done and has_search:
			print submission.short_link
			already_done.append(submission.id)
	time.sleep(1800)