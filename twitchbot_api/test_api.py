import json
import unittest

from app import app
# set our application to testing mode
app.testing = True


class TestApi(unittest.TestCase):

    def test_messages(self):
        with app.test_client() as client:
            query = """mutation {
                 createMessage (input: { message:"Hello" channelName:"World!" }) 
                 {
                      message { 
                          id 
                          message 
                          timestamp 
                          channelName 
                          } 
                } 
            }"""
            # send data as POST form to endpoint
            result = client.post(
                '/graphql',
                data=json.dumps({'query': query}),
                headers={"Content-Type": "application/json"}
            )
            # check result from server with expected data
            self.assertEqual(
                result.json['data']['createMessage']['message']['message'],
                'Hello'
            )
            self.assertEqual(
                result.json['data']['createMessage']['message']['channelName'],
                'World!'
            )
    
    def test_channel_rate(self):
        with app.test_client() as client:

            # send data as POST form to endpoint
            result = client.post(
                '/channel_rate',
                data=json.dumps({'channelName': "World!"}),
                headers={"Content-Type": "application/json"}
            )
            assert result.json['total_messages']
            assert result.json['message_rate_minutes']
            assert result.json['message_rate_seconds']

def test_channel_mood(self):
        with app.test_client() as client:

            # send data as POST form to endpoint
            result = client.post(
                '/channel_mood',
                data=json.dumps({'channelName': "World!"}),
                headers={"Content-Type": "application/json"}
            )
            assert result.json['recent_pogchamps']