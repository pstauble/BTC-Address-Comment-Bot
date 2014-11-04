

import time
import praw
import requests

username="btcbottest"
password="x9x6x3.."

subreddit="bottesting"

already_done=[]

r=praw.Reddit(user_agent="Bitcoin Balance Bot")
r.login(username,password)

#Code still needs tidying up.

subreddit=r.get_subreddit(subreddit)

for submission in subreddit.get_hot(limit=10):
	comments=praw.helpers.flatten_tree(submission.comments)
	for comment in comments:
		
		if comment.body == "GetWallet:" and comment.id not in already_done:
			adress=comment.text.split("GetWallet:")[1]
			adress=adress[0:35] #gets the first 36 characters after GetWallet
			if adress[0]==" ": #If the first value is a space
				adress=adress[1:] #If first is space then removes space
				adress=adress.split(" ")[0] #If theres a space after adress it keeps only the adress
				print adress
			else:
				adress=adress.split(" ")[0] #If theres no space take only adress before
				print adress
			
			if len(adress)>	34 or len(adress)<26:
				break
			
			else:
				value=requests.get("https://blockchain.info/q/addressbalance/"+adress)
			
				comment.reply("The wallet in your comment contains %s BTC.") %value
		
		else:
			pass
		
		already_done.append(comment.id)			
		
			
			#12DQohP4zon4DZdFsFD3f7YNb9ePiHzSVN
			
			
