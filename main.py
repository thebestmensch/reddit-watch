"""
CLI file for subreddit search and notification bot

@author     james@temboinc.com
@since      2015-04-23
"""

import optparse
from bot import controller

def main():
	desc = "Reddit-Watch: a subreddit search and notification bot"
	# the cli
	p = optparse.OptionParser(description=desc)
	p.add_option('-s', '--subs', default=[], help="subreddits to search", action="append", dest="subs")
	p.add_option('-k', '--keywords', default=[], help="keywords to search for", action="append", dest="keys")
	p.add_option('-u', '--username', default=[], help="username to send notification", action="store", dest="username")
	
	opts, args = p.parse_args()

	# check required params
	if not opts.subs:
		p.error('Please enter a subreddit to watch.')
	if not opts.keys:
		p.error('Please enter a keyword for watch for.')
	if not opts.username:
		p.error('Please enter a username to send the notification.')

	controller(opts.keys, opts.subs, opts.username)
if __name__ == '__main__':
	main()