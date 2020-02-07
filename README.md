# TwitchBot
### Initial Setup
Running this app will require 2 instances of terminal running (one for the JS TwitchBot and another for the Python API) \
In one of the terminals, run the following commands: \
`npm install` \
`node twitchBot.js`

In the other terminal run the following commands: \
(Recommend to use a virtual environment, but not necessary)
Requires Python 3.5
`pip install -r requirements.txt` \
Navigate into the `twitchbot_api` directory and run the following commands: \
`flask db init` \
`flask db upgrade` \
Once your database is initialized, then you can begin the Python API by running: \
`flask run`

You can change the Twitch Channel to trace in the config.js file (as well as use your own Twitch Creds instead of the ones provided)

### Testing
To Test the API (from root directory):

`python3 -m unittest twitchbot_api/test_api.py`

### Features
__0001__ - As a developer, I want the initial application setup \
__0002__ - As a developer, I want to have the database created via flask and the necessary tables created via flask-migrate \
__0003__ - As a user, I want to be able to post messages to the database \
__0004__ - As a twitchBot, I want to be able to connect to a twitch channel and post messages to the application database as they come in \
__0005__ - As a user, I want to pull a channel's message rate (per minute and per second) \
__0006__ - As a user, I want to be able to pull down a Twitch Channel's mood \
__0007__ - As a developer, I want the twitchBot and flask API to have sufficient testing coverage