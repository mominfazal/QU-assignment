from flask import *
import requests
import json
import sys
import tweepy #https://github.com/tweepy/tweepy
import re

# We are not using any scraping tools (like scrapy) because Both the sites CNN and Twitter both provides us easy to fetch content.
# Above imported library "requests" is a tool which can fetch all the printed contents of a URL, we are using this to retrive JSON from CNN
# Twitter is not scrapable, it will start blocking IPs after several hits. However, twitter is open to give us the data hence they have provided us APIs to fetch the content.
# tweepy is the one of many pyhton libraries which provides us fetching data from twitter apis easily. Why I choose this is because it provides user timelines details also.

app = Flask(__name__)
@app.route('/')
def home():
	return render_template('index.html')

@app.route('/get_data_from_twitter',methods=['POST'])
def get_twitter():
	query = request.form.get('query')
	tweetID = request.form.get('tweetID')  # This variable will be set only if we click on Show more about tweet button.
	response = get_data_from_twitter(query,tweetID)
	return jsonify(response)


@app.route('/get_data_from_cnn',methods=['POST'])
def get_cnn():
	start = request.form.get('startfrom') # This variable is used to keep track of news which are already loaded on page.
	query = request.form.get('query') # This variable is the key word according to which our news api will return news.
	response = get_data_from_cnn(query,start)
	return jsonify(response)

def get_data_from_twitter(query,tweetID):
	dataToSend = {}

	# Secret Credentials for Twitter. Read only.
	consumer_key = '49uNBkqNHzWxvR3Z4JDbRASmi'
	consumer_secret = 'g2zSEMgxczfEwfL6SWtomTXXPoK3Fg68Kr9U1kchZ1bbk3dy4Z'
	access_token_key = '847013729187352576-X0FIKTAd6VzJwCOnxxfKwgtTiKjZd2X'
	access_token_secret = 'UKIcmA6MRuiUAL6QBrq3UvDK4hSMuAgbYPldYQdoR5ViT'

	try:
		#Getting a connection with twitter using above credentials
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token_key, access_token_secret)
		api = tweepy.API(auth)

		# fetching complete timeline of the user
		# api.user_timeline('TwitterHandle Here')
		if(query is None):
			query = 'realDonaldTrump' # Incase text box is blank

		userData = api.user_timeline(query,count=25,tweet_mode="extended")    # To make this task generic we just need to make 'TwitterHandle' field dynamic
		# dataToSend is the variable which will be returned to the User Interface
		dataToSend['total_tweets'] = len(userData)
		dataToSend['results'] = []

	# else: # We are not including this part due to time crunch
	# 	tweetData = api.get_status(tweetID)
	# 	dataToSend['total_tweets'] = len(tweetData)
	# 	dataToSend['results'] = []
	except:
		dataToSend['error_message'] = 'Coudnt connect to twitter'

	for eachData in userData:
		try:
			singleData = {}
			singleData['twitter_text'] = re.sub(r'[^\x00-\x7f]',r'', eachData.full_text.encode("utf-8")) # remove hexadecimal characters
			singleData['url'] = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', singleData['twitter_text']) #find all URLS - iframe URLS in this case
			singleData['created_at'] = str(eachData.created_at.date())
			singleData['id'] = str(eachData.id_str.encode("utf-8"))
			for url in singleData['url']:
				singleData['twitter_text'] = singleData['twitter_text'].replace(url,'').strip()  # Remove all URLS from text as we wont display it.
			dataToSend['results'].append(singleData)

		except:
			print(sys.exc_info()[0])

	return dataToSend

def get_data_from_cnn(query,start):
	dataToSend = {}
	if start is None:
		start = 1
	if query is None:
			query = 'donald trump'
	if start == 1:  # for Load more logic this will hit for the first occurance only
		url = 'https://search.api.cnn.io/content?q='+query+'&size=25'  # Before scraping! I decided to analyse the request flow of the CNN website and there I found this API which fetches first part(ie size=25) of the news data for the page.
	else:
		fromNo = ((int(start)-1)*25)+1
		url = 'https://search.api.cnn.io/content?q='+query+'&size=25&page='+str(start)+'&from='+str(fromNo) # This is the load more api.
	try:
		query_data = requests.get(url)  #Simple Http request to fetch data from CNN
		query_data = json.loads(query_data.content)  #Fetching it as Json
		dataToSend['meta'] = query_data['meta']    
		dataToSend['results'] = []
	except: 
		dataToSend['error_message'] = 'Coudnt connect to twitter'

	# print query_data['result']
	# sys.exit(0)

	for eachData in query_data['result']:
		try:
			singleData = {}
			singleData['desc_text'] = str(eachData['body'].encode("utf-8"))
			singleData['headline'] = str(eachData['headline'])
			singleData['firstPublishDate'] = str(eachData['firstPublishDate'][:10])
			singleData['detailsUrl'] = str(eachData['url'])
			dataToSend['results'].append(singleData)
		except:
			print(sys.exc_info()[0])
			
	return dataToSend

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = False)
