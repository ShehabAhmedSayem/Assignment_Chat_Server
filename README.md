# Assignment_Chat_Server

You need to first run the message_server from this repo:
[Message Server](https://github.com/ShehabAhmedSayem/Assignmet_Message_Server)

First build and run the docker container for Message Server.

Now run the following command to build this container.
```
docker build -t chat_server .
```
And to start a single chat server run the following command
```
docker run --name client_1 --network assignment_message_server_message-service chat_server
```

Here the network is mandatory as this was created during the message server building and named as assignment_message_server_message-service.

After running, we can see the messages in the console that will be sent automatically after every 20 sec to message_server.
We can create multiple chat server using the previous docker run command by changing the name.

You can also pass 2 env variable to control the frequency of sending message and whether the reply should be auto or in interactive mode(Will send auto after time out). 
```
AUTO_REPLY=0 or AUTO_REPLY=1 
MESSAGE_SENDING_GAP_IN_SECONDS=10 
```
Run the following command

```
docker run -it --name client_2 --network assignment_message_server_message-service -e AUTO_REPLY=0 -e MESSAGE_SENDING_GAP_IN_SECONDS=10 chat_server
```
