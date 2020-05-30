from twitch_listener import listener

user, client, oauth = open('twitch_auth.txt').read().split(' ')

bot = listener.connect_twitch(user, client, oauth)
bot.listen('Michaelalfox', 5)