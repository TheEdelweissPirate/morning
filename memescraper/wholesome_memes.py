import requests
import os

savePath= "C:\\Users\\Hari kumar\\Desktop\\morning\\memescraper\\test_meme_folder"
				
import praw

reddit = praw.Reddit(	client_id = 'atKWAVmqcTN2tw', 
						client_secret = 'OPspkFyWhvEv8We9kzBkafYE288', 
						username = 'TheEdelweissPirate', 
						password = 'pearlsbeforeswine', 
						user_agent = 'TheEdelweissPiratev1')

subreddit = reddit.subreddit('wholesomememes')
hot_wholesomememes = subreddit.hot(limit = 20)
print(hot_wholesomememes)
img_counter=0
for submission in hot_wholesomememes:
	if not submission.stickied:
		print(submission.url)
		r = requests.get(str(submission.url))
		print(r)
		# fileName = os.path.join(savePath,"meme "+str(img_counter)+".png")
		# with open(fileName,'wb') as f:
  #       			f.write(r.content)
  #       			img_counter+=1


