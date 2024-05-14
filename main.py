import telebot
import expected_date, photo_and_jira, cancel_and_return,shorts_clar_another,jira_replies, feedback
import postgres
from telebot import types as tps
import pyperclip as ppc


class Btns_chosen:
    def __init__(self):
        self.btns_chosen = ''
    def getBtns_chosen(self):
        return self.btns_chosen

btns = Btns_chosen()



api_token = "5504305892:AAEEDAuidnKOG1refLzWJ9aQvsIV7YW5iRg"
bot = telebot.TeleBot(api_token, parse_mode=None)

if __name__ == "__main__":
    @bot.message_handler(func=lambda message: message.text == "11")
    def pressed_ru(message):
        res = postgres.obj.how_namy_times_pressed("ru")
        bot.send_message(message.chat.id, f"Here what I've got\n\n{res}")
        

    @bot.message_handler(func=lambda message: message.text == "00")
    def pressed_en(message):
        res = postgres.obj.how_namy_times_pressed("en")
        bot.send_message(message.chat.id, f"Here what I've got\n\n{res}")

    
    @bot.message_handler(func=lambda message: True)
    def handle_message(message):
        if message.text == "/feedback":
            btns.btns_chosen = "feedback"
            feedback.show_feedback(bot,message)
        elif message.text == "/jira_replies":
            btns.btns_chosen = "jira_replies"
            jira_replies.show_jira_replies(bot,message)
        elif message.text.lower() == "/expetced_and_violated":
            btns.btns_chosen = "expetced_and_violated"
            expected_date.show_expected(bot,message)                   
        elif message.text.lower() == "/photo_and_jira":
            btns.btns_chosen = "photo_and_jira"
            photo_and_jira.show_jira_and_photo(bot,message)                   
        elif message.text.lower() == "/cancel_and_return": 
            btns.btns_chosen = "cancel_and_return"
            cancel_and_return.show_cancel_and_return(bot,message)                   
        elif message.text.lower() == "/shorts_clar_another":
            btns.btns_chosen = "shorts_clar_another"
            shorts_clar_another.show_shorts_and_clar(bot,message)
        elif message.text.lower() == "зк":
            bot.send_message(message.chat.id, f'`Если возникнут дополнительные вопросы, обращайтесь к нам в чат.`', parse_mode="Markdown")
        elif message.text.lower() == "от":
            bot.send_message(message.chat.id, f'`Здравствуйте, XXX. Благодарю за ожидание.`', parse_mode="Markdown")
        elif message:
            ppc.copy(f'Здравствуйте, XXX. Благодарю за ожидание.\n\n{message.text}\n\nЕсли возникнут дополнительные вопросы, обращайтесь к нам в чат.')
            bot.send_message(message.chat.id, f'`Здравствуйте, XXX. Благодарю за ожидание.\n\n{message.text}\n\nЕсли возникнут дополнительные вопросы, обращайтесь к нам в чат.`', parse_mode="Markdown")
            bot.send_message(message.chat.id, f"/start  TEXT COPIED",parse_mode="Markdown")   
        '''        
        edit commands (bot father)
        jira_replies - обработка жир и шорты 
        feedback - отзывы
        shorts_clar_another - уточнения, коротыши, другое
        cancel_and_return - отмена и возвраты
        expetced_and_violated - ожидаемая и нарушены
        photo_and_jira - фото и жиры
        '''
    @bot.callback_query_handler(func=lambda call: True)
    def btn_handler(call):
        chosen = btns.getBtns_chosen()
        if chosen == "expetced_and_violated":
            expected_date.btn_process(bot,call)
        elif chosen == "photo_and_jira":
            photo_and_jira.btn_process(bot,call)
        elif chosen == "shorts_clar_another":
            shorts_clar_another.btn_process(bot,call)
        elif chosen == "cancel_and_return":
            cancel_and_return.btn_process(bot,call)
        elif chosen == "feedback":
            feedback.btn_process(bot,call)
        elif chosen == "jira_replies":
            jira_replies.btn_process(bot,call)

                                
                                                                                                                                

    bot.polling()