
import requests

import datetime
import telepot

class BotHandler:

    def __init__(self, token):

            self.token = token

            self.api_url = "https://api.telegram.org/bot{}/".format(token)



    #url = "https://api.telegram.org/bot<token>/"



    def get_updates(self, offset=0, timeout=15):

        method = 'getUpdates'

        params = {'timeout': timeout, 'offset': offset}

        resp = requests.get(self.api_url + method, params)

        result_json = resp.json()['result']

        return result_json





    def send_message(self, chat_id, text):

        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}

        method = 'sendMessage'

        resp = requests.post(self.api_url + method, params)

        return resp



    def get_first_update(self):

        get_result = self.get_updates()



        if len(get_result) > 0:

            last_update = get_result[0]

        else:

            last_update = None



        return last_update



    def send_photo(self,chat_id,photo,cap="None"):

        method = 'sendPhoto'

        params = {'chat_id': chat_id, 'photo': photo, 'caption':cap}


        resp = requests.post(self.api_url + method, params)

        return resp






token = ' ' #Token of your bot

magnito_bot = BotHandler(token) #Your bot's name







def main():

    new_offset = 0

    print('Launching the B6 Group Manger Bot...')



    while True:

        all_updates=magnito_bot.get_updates(new_offset)



        if len(all_updates) > 0:

            for current_update in all_updates:

                print(current_update)

                first_update_id = current_update['update_id']

                if 'text' not in current_update['message']:

                    first_chat_text='Hi'

                else:

                    first_chat_text = current_update['message']['text']

                first_chat_id = current_update['message']['chat']['id']
                #getting the first_chat_name
                if 'first_name' in current_update['message']:

                    first_chat_name = current_update['message']['chat']['first_name']

                elif 'new_chat_member' in current_update['message']:
                    first_chat_name = current_update['message']['new_chat_member']['first_name']
                    #first_chat_name = current_update['message']['new_chat_member']['username']

                elif 'from' in current_update['message']:

                    first_chat_name = current_update['message']['from']['first_name']

                else:

                    first_chat_name = "unknown"

                new_offset = first_update_id + 1
                #printing several messages

                if 'text' in current_update['message']:
                    chat_text = current_update['message']['text']
                else:
                    chat_text='/hi'

                if chat_text=='/hi':
                    magnito_bot.send_message(first_chat_id,"Hey there!")
                elif chat_text== '/badges':

                    magnito_bot.send_message(first_chat_id,"Badges look somewhat like this")
                    magnito_bot.send_photo(first_chat_id,'https://drive.google.com/file/d/1PE90MGakKXUEPnQ9s3ErAwU-rJkKIELZ/view?usp=sharing')
                    magnito_bot.send_message(first_chat_id,"I will be issuing you badges\n Badges issued to you will be posted on the group")
                    magnito_bot.send_message(first_chat_id,"If you have more than 2 badges you will be made an ADMIN of the group")

                elif chat_text=="/tell_me_about_your_creator":
                    magnito_bot.send_message(first_chat_id,"I have been created by TheAppInnovator")
                    magnito_bot.send_message(first_chat_id,"My creator will be inserting more changes soon into me")


                elif chat_text=='/security':

                    magnito_bot.send_message(first_chat_id,"Your messages are completely secure with me\nOur Conversation is private\nOnly messages you FORWARD will be sent to the owner of the group")

                elif chat_text=='/forward_my_message':

                    magnito_bot.send_message(first_chat_id,"Forwading message.....")
                    magnito_bot.send_message((first_chat_id,"Now, please type in you message"))
                    chat_text =current_update['message']['text']
                    magnito_bot.send_message(524425359,"Message forwarded from: "+first_chat_name+" is here\n"+chat_text)

                elif chat_text=='/what_else':
                    magnito_bot.send_message(first_chat_id,first_chat_name+",All my features will be unlocked soon\nMy creator will be soon working on me\n I can always help with you all day")
                    magnito_bot.send_message(first_chat_id,"If you find anything suspicious while using telegram or someone in the group or some unknown, please do not hesitate to forward your grievance")
                    magnito_bot.send_message(first_chat_id,"ALWAYS HAPPY TO SERVE!!!")

                elif chat_text=='/make_me_admin':
                    magnito_bot.send_message(first_chat_id,"If you meet the following requirements, I will make you an admin after checking for the following details with my fellow bots\n1.Profile Photo\n2.Your Own Name\n3.Active Participant of the Groupt\n4.Not Banned")
                    magnito_bot.send_message(524425359, "MAKE ME ADMIN message from:" + first_chat_name)

                else:


                    magnito_bot.send_message(524425359,"Message from:" +first_chat_name+"\nThe message is:"+chat_text)



'''
hi-Hello
badges-information about badges
tell_me_about_your_creator-TheAppInnovator
security-encryption enabled
forward_my_message-forwards the message you type
what_else-my capabilities
make_me_admin-admin criteria
'''






if __name__ == '__main__':

    try:

        main()

    except KeyboardInterrupt:

        exit()