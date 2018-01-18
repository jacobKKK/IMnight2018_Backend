import re
import json
# import logging
from channels import Group
from channels.sessions import channel_session

from human.models import Relationship
from human.chat.models import Message

from django.contrib.auth.models import User

# log = logging.getLogger('console-logger')


@channel_session
# Connected to websocket.connect
def ws_connect(message):
    # the message path is /chat/{label}/
    # get prefix -> "chat"
    # get label -> "{label}"
    try:
        prefix, prefix2, label = message['path'].strip("/").split("/")
        if prefix != 'human' and prefix2 != 'chat':
            log.error('invalid ws path=%s', message['path'])
            return
        room = Relationship.objects.get(label=label)
    except ValueError:
        # log.error('invalid ws path=%s', message['path'])
        return
    except Relationship.DoesNotExist:
        # log.error('ws room does not exist label=%s', label)
        return

    # log.info('chat connect room=%s client=%s:%s',
        # room.label, message['client'][0], message['client'][1])

    # Accept the incoming connection
    message.reply_channel.send({'accept': True})

    message.channel_session['room'] = room.label

    # Add this client to the "chat-{label}" group
    Group('chat-' + label,
          channel_layer=message.channel_layer).add(message.reply_channel)


@channel_session
# Connected to websocket.receive
def ws_receive(message):
    # Look up the room from the channel session, bailing if it doesn't exist
    try:
        label = message.channel_session['room']
        room = Relationship.objects.get(label=label)
    except KeyError:
        # log.error('no room in channel_session')
        return
    except Relationship.DoesNotExist:
        # log.error('recieved message, buy room does not exist label=%s', label)
        return

    # Parse out a chat message from the content text, bailing if it doesn't
    try:
        data = json.loads(message.content['text'])
    except ValueError:
        # log.error("ws message isn't json text=%s", text)
        return

    # conform to the expected message format.
    if set(data.keys()) != set(('handle', 'message')):
        # log.error("ws message unexpected format data=%s", data)
        return

    if data:
        # log.error('chat message room=%s handle=%s message=%s',
                  # room.label, data['handle'], data['message'])
        handle = data["handle"]
        user = User.objects.get(username=handle)
        msg = data["message"]
        m = Message.objects.create(room=room, handle=user, message=msg)

        # send the massage to the clients in Group
        Group('chat-' + label,
              channel_layer=message.channel_layer).send({
                  # error here is that as_dict() cant convert User object to json
                  # 'text': json.dumps(m.as_dict())
                  'text': json.dumps(data)
              })


@channel_session
# Connected to websocket.disconnect
def ws_disconnect(message):
    try:
        label = message.channel_session['room']
        room = Relationship.objects.get(label=label)

        # remove this client from Group
        Group('chat-' + label,
              channel_layer=message.channel_layer).discard(message.reply_channel)
    except Relationship.DoesNotExist:
        # log.error('recieved message, buy room does not exist label=%s', label)
        return
