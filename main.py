"""
CLI file for subreddit search and notification bot

@author     james@temboinc.com
@since      2015-04-23
"""

import optparse

def main():
	desc = "Reddit-Watch: a subreddit search and notification bot"
	# the cli
	p = optparse.OptionParser(description=desc)
	p.add_option('-s', '--subs', default=False, help="subreddits to search", action="store", dest="subs")
	p.add_option('-k', '--keywords', default=False, help="keywords to search for", action="store", dest="keys")
	
	opts, args = p.parse_args()

	# check required params
	if not opts.subs:
		p.error('Please enter a subreddit to watch.')
	if not opts.keys:
		p.error('Please enter a keyword for watch for.')

if __name__ == '__main__':
	main()