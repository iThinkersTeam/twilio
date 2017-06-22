from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant

# Substitute your Twilio AccountSid and ApiKey details
ACCOUNT_SID = 'ACdad27b69d50ee7f3ae16151c463fa590'
API_KEY_SID = 'SK4b99e19ad029d728d6a54fb0c7938d1a'
API_KEY_SECRET = 'l9z6OW2DrTrOntf7xr8iW5ZHTbww16nV'

# Create an Access Token
token = AccessToken(ACCOUNT_SID, API_KEY_SID, API_KEY_SECRET)

# Set the Identity of this token
token.identity = 'example-user'

# Grant access to Video
grant = VideoGrant(room='cool room')
token.add_grant(grant)

# Serialize the token as a JWT
jwt = token.to_jwt()
print(jwt)
