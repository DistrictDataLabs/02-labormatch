#for linkedin
#yanan
#not working yet

from linkedin import linkedin # pip install python-linkedin

# OAuth 1.0a
# Define CONSUMER_KEY, CONSUMER_SECRET,  
# USER_TOKEN, and USER_SECRET from the credentials 
# provided in your LinkedIn application


CONSUMER_KEY = '77t43u3loazvrz'
CONSUMER_SECRET = 'b95o3WkJj7vbNWMj'

USER_TOKEN = 'd77d38f5-6f3e-422a-9a6a-6fe985ae8c54'
USER_SECRET = '01027166-7044-4c73-988a-61896e12dd82'

RETURN_URL = 'http://ysun1.github.io/labormatch/' # Not required for developer authentication

# Instantiate the developer authentication class

auth = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET, 
                                USER_TOKEN, USER_SECRET, 
                                RETURN_URL, 
                                permissions=linkedin.PERMISSIONS.enums.values())

# Pass it in to the app...

app = linkedin.LinkedInApplication(auth)

# Use the app...

app.get_profile()
