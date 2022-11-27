from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
import campay



class Bot(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("all good here")
    def post(self, request, *args, **kwargs):
        return HttpResponse("all good here")




# async def main():
    # Getting information about yourself
    # me = await bot.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    # print(me.stringify())

    # When you print something, you see a representation of it.
    # You can access all attributes of Telegram objects with
    # the dot operator. For example, to get the username:
    # username = me.username
    # print(username)
    # print(me.phone)

    # You can print all the dialogs/conversations that you are part of:
    # async for dialog in bot.iter_dialogs():
    #     print(dialog.name, 'has ID', dialog.id)

    # You can send messages to yourself...
    # await bot.send_message('me', 'Hello, myself!')
    # ...to some chat ID
    # await bot.send_message(-100123456, 'Hello, group!')
    # ...to your contacts
    # await bot.send_message(680278409, 'Hello, friend!')
    # await bot.send_message('+237680278409', 'Hello, friend!')
    # ...or even to any username
    # await bot.send_message('Che Bernice', 'Testing Telethon!')
    # await bot.send_message('username', 'Testing Telethon!')

    # You can, of course, use markdown in your messages:
    # message = await bot.send_message(
    #     'me',
    #     'This message has **bold**, `code`, __italics__ and '
    #     'a [nice website](https://example.com)!',
    #     link_preview=False
    # )

    # Sending a message returns the sent message object, which you can use
    # print(message.raw_text)

    # You can reply to messages directly if you have a message object
    # await message.reply('Cool!')

    # Or send files, songs, documents, albums...
    # await bot.send_file('me', '/home/me/Pictures/holidays.jpg')

    # You can print the message history of any chat:
    # async for message in bot.iter_messages('me'):
    #     print(message.id, message.text)

        # You can download media from messages, too!
        # The method will return the path where the file was saved.
        # if message.photo:
        #     path = await message.download_media()
        #     print('File saved to', path)  # printed after download is done

# with bot:
#     bot.loop.run_until_complete(main())
