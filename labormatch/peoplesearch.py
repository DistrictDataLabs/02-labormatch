import oauth2 as oauth
import httplib2
import time, os, simplejson
 
# Fill the keys and secrets you retrieved after registering your app
consumer_key      =   '77t43u3loazvrz'
consumer_secret  =   'b95o3WkJj7vbNWMj'
user_token           =   'd77d38f5-6f3e-422a-9a6a-6fe985ae8c54'
user_secret          =   '01027166-7044-4c73-988a-61896e12dd82'

 
# Use your API key and secret to instantiate consumer object
consumer = oauth.Consumer(consumer_key, consumer_secret)
 
# Use the consumer object to initialize the client object
client = oauth.Client(consumer)
 
# Use your developer token and secret to instantiate access token object
access_token = oauth.Token(key=user_token, secret=user_secret)
 
client = oauth.Client(consumer, access_token)
 
#---------examples--------#
## Make call to LinkedIn to retrieve your own profile
#resp,content = client.request("https://api.linkedin.com/v1/people/~", "GET", "")
 
## By default, the LinkedIn API responses are in XML format. If you prefer JSON, simply specify the format in your call
## resp,content = client.request("https://api.linkedin.com/v1/people/~?format=json", "GET", "")
#--------end of example---------#


joburl = "https://api.linkedin.com/v1/job-search?job-title=Software+Engineer"
resp,content = client.request(joburl, "GET", "")

pplurl = "https://api.linkedin.com/v1/people-search?school-name=Shermer%20High%20School&current-school=false"
resp,content = client.request(pplurl, "GET", "")

