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
		# get post body and title
		op_body = submission.selftext.lower()
		op_title = submission.title.lower()
		op = op_body + " " + op_title

		# check if post title or body has a search value 
		has_search = any(string in op for string in search)
		if submission.id not in already_done and has_search:
			# create and send message
			msg = '[%s](%s)' % (op_title, submission.short_link)
			r.send_message('Menschy28', op_title, msg)
			already_done.append(submission.id)
	# wait for 15mins
	time.sleep(900)