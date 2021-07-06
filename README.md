# discord_gateway
Server that uses a bot to interact with discord
  
# Usage
### Send message to channel
`POST` `<host>:<port>/api/v1/channel/message`  
###### Headers
``` 
{
    "Authorization": "Secret <environment variable SERVER_AUTHORIZATION_SECRET>"
}
```
###### Body
```
{
  "message": string,
  "channel_id": int
}
```
if the bot has been added to the guild (server in the UI) and the channel exists in the guild the message will be sent by the bot to the channel
### Health Check
`GET` `<host>:<port>/api/v1/health`  

Will respond with a `200`
  
# Deployment
Check `.example.env` for required environment variables

# Inspiration
[icco's](https://github.com/icco) [relay](https://github.com/icco/relay)
