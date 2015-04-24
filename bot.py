#!/usr/bin/env python
"""
RedditBot file

@author     james@temboinc.com
@since      2015-04-21
"""

import praw
import time
import datetime
from multiprocessing import Process

def controller(keywords, subreddits, username):
	"""
	"""
	# instantiate praw and request reddit login
	r = praw.Reddit('Reddit-Watch RedditBot')
	r.login()

	# the process queue
	jobs = []
	for subreddit in subreddits:
		p = Process(target=run, args=(r, keywords, subreddit, username))
		jobs.append(p)
		p.start()

def run(reddit, keywords, subreddit, username):
	"""
	"""
	# list of searched posts
	already_done = []

	# the subreddit watcher
	while True:
		subreddit = reddit.get_subreddit(subreddit)
		print "watching %s..." % subreddit
		# for newest 100 posts
		for post in subreddit.get_new(limit=100):
			# get post body and title
			op_body = post.selftext.lower()
			op_title = post.title.lower()
			op = op_body + " " + op_title

			# check if post title or body has a search value 
			if post.id not in already_done:
				for keyword in keywords:
					if keyword in op:
						# create and send message
						msg = '[%s](%s)' % (op_title, post.short_link)
						title = '[Reddit-Watch]['+datetime.datetime.now().strftime("%Y-%m-%d")+'] ' + keyword
						reddit.send_message(username, title, msg)
						already_done.append(post.id)
		# wait for 15mins
		time.sleep(900)

