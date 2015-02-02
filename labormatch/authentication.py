#for linkedin
#yanan
#not working yet

from linkedin.linkedin import (LinkedInAuthentication, LinkedInApplication,
                               PERMISSIONS)


if __name__ == '__main__':
    API_KEY = '77t43u3loazvrz'
    API_SECRET = 'b95o3WkJj7vbNWMj'
    RETURN_URL = 'http://localhost:8000'
    authentication = LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL,
                                            PERMISSIONS.enums.values())
    print authentication.authorization_url
    application = LinkedInApplication(authentication)
