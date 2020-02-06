const tmi = require('tmi.js');
const { config } = require('./config.js')
const fetch = require('node-fetch');

// Define configuration options
const opts = {
  identity: {
    username: config.botName,
    password: config.authToken
  },
  channels: config.channels
};
// Create a client with our options
const client = new tmi.client(opts);

// Register our event handlers (defined below)
client.on('message', onMessageHandler);
client.on('connected', onConnectedHandler);

// Connect to Twitch:
client.connect();

// Called every time a message comes in
function onMessageHandler (target, context, msg, self) {

  const query = `mutation ($message: String, $channelName: String){ createMessage (input: { message:$message channelName:$channelName }) { message { id message timestamp channelName } } }`
  const vars = {
    message: msg.trim(),
    channelName: target
  }

  fetch('http://localhost:5000/graphql', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query: query, variables: vars }),
  })
    .then(res => res.json());
}

// Called every time the bot connects to Twitch chat
function onConnectedHandler (addr, port) {
  console.log(`* Connected to ${addr}:${port}`);
}