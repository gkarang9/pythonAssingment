statical={'batsman':{'virat':{'matches':'5000','run':'11000','average':'80','highscore':'264'},
                   'mahi':{'matches':'6001','run':'20000','average':'70','highscore':'169'},
                   'rohit':{'matches':'4000','run':'10324','average':'104','highscore':'232'}}}
	
high=[]
for id in statical.keys():
	for nextid in statical[id].keys():
		c.append(statical[id][nextid]['highscore'])
print("Highscore=",max(high))		