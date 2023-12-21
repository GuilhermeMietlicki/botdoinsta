from instabot import Bot, utils

bot = Bot()




#login na conta do instagram
bot.login(username="email", password= "senha")

#coletar o nome das pessoas que vc segue mas nao te seguem de volta
file = utils.file("config/non-followers.txt")

non_followers = set(bot.following) - set(bot.followers) - bot.friends_file.set
non_followers = list(non_followers)
non_followers_name = []

for user in non_followers:
    name = bot.get_username_from_user_id(user)
    non_followers_name.append(name)
    print(name)
    bot.snall_delay()

#Salvar num txt.
    file.save_list(non_followers_name)

    #python main.py