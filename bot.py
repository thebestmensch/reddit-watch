#!/usr/bin/env python
"""
RedditBot file

@author     james@temboinc.com
@since      2015-04-21
"""

import praw
import time
from multiprocessing import Process


def controller(keywords, subreddits):
	"""
	"""
	# instantiate praw and request reddit login
	r = praw.Reddit('Reddit-Watch RedditBot')
	r.login()

	# the process queue
	jobs = []
	for subreddit in subreddits:
		p = Process(target=run, args=(r, keywords, subreddit))
		jobs.append(p)
		p.start()

def run(reddit, keywords, subreddit):
	"""
	"""
	# list of searched posts
	already_done = []

	# the subreddit watcher
	while True:
		print subreddit
		subreddit = reddit.get_subreddit(subreddit)
		for post in subreddit.get_new(limit=10):
			# get post body and title
			op_body = post.selftext.lower()
			op_title = post.title.lower()
			op = op_body + " " + op_title

			# check if post title or body has a search value 
			has_search = any(string in op for string in keywords)
			if post.id not in already_done and has_search:
				# create and send message
				msg = '[%s](%s)' % (op_title, post.short_link)
				#reddit.send_message('Menschy28', op_title, msg)
				print msg
				already_done.append(post.id)
		# wait for 15mins
		time.sleep(900)

controller(['uniqlo', 'nordstrom'], ['frugalmalefashion', 'malefashionadvice'])