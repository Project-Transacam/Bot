from telethon.sync import TelegramClient, events
from telethon.tl.types import ReplyInlineMarkup,KeyboardButtonRow
from telethon.tl.types import ReplyKeyboardMarkup,KeyboardButtonCallback
from telethon import Button
# import requests

host = "localhost"
port=8000

api_id=20518797
api_hash="903f959827fe5d6f92f1fa764f1539ae"
bot_token = '5754027807:AAHeMCWbKZvauwJqbK-j4zoksaJZUmsXRcY'


bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@bot.on(events.NewMessage)
async def my_event_handler(event):
    print("bot is running")
    if 'hello' in event.raw_text.lower():
        # markup = bot.build_reply_markup(Button.inline('hi'))
        # await bot.action(event.sender_id, 'cancel')
        await event.reply("Hi")                               
        # await bot.send_message(event.sender_id, 'click me', buttons=markup)
    elif 'start' in event.raw_text.lower():
        chat = await event.get_chat()
        print("username",chat.first_name + chat.last_name)
        if chat.first_name !="" and chat.last_name != "":
            await event.reply(f"Welcome {chat.last_name}")
            message = await bot.send_message(
            event.sender_id,
            'This message has **bold**, `code`, __italics__ and '
            'a [nice website](https://example.com)!',
            link_preview=False)
        else:
            await event.reply(f"Welcome aboard!!")
        # sender = await event.get_sender()
        # print("sender",sender)
        # chat_id = event.chat_id
        # print('chart_id',chat_id)
        # sender_id = event.sender_id
        # print("sender_id",sender_id)

        # ReplyInlineMarkup(
        #         rows=[
        #                 KeyboardButtonRow(
        #                         buttons=[
        #                                 KeyboardButtonCallback(
        #                                         text='⇱ Main balance',
        #                                         data=b'main_balance',
        #                                         requires_password=False
        #                                 ),
        #                                 KeyboardButtonCallback(
        #                                         text='↵ Back',
        #                                         data=b'back',
        #                                         requires_password=False
        #                                 ),
        #                         ]
        #                 ),
        #         ]
        # ),
        # await event.reply(reply_markup)
        #check if user has been registered if no, register user
        # message = await bot.send_message(
        # 'me',
        # 'This message has **bold**, `code`, __italics__ and '
        # 'a [nice website](https://example.com)!',
        # link_preview=False)
    elif 'send' in event.raw_text.lower():
        #send user input field to enter reciepient number of choose from favourite
        await event.reply('To which number!')
    elif 'balance' in event.raw_text.lower():
        #request for users pin and validate and send user his balance
        await event.reply(f'{5000} frs')
    elif 'faq' in event.raw_text.lower():
        await event.reply("""
        welcome to UB microfinance we are at your service.\n
        1:how to my account balance\n
        2:how to reset my pin \n
        3:what is **transackam**\n
        4:how can i delete my account
        """
        )
    elif 'history' in event.raw_text.lower():
        #last 10 recent transactions after authenticating with user pin
        await event.reply(f'you spent {1000}frs this month')
    elif 'help' in event.raw_text.lower():
        await event.reply('pay fees\n and others')
    elif 'withdraw' in event.raw_text.lower():
        await event.reply('choose a network: \n 1:MTN \n 2:Orange\n ')
    elif 'change pin' in event.raw_text.lower():
        #enter old pin, validate and enter new pin
        await event.reply('enter old pin\n')
    else:
        await event.reply("Invalid command")

bot.run_until_disconnected()
