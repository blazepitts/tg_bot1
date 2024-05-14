import telebot, postgres
import pyperclip as ppc
from telebot import types as tps


def show_jira_replies(bot,message):
    jira = tps.InlineKeyboardMarkup()
    cannotCancelPVZ = tps.InlineKeyboardButton("Не можем отменить ПВЗ",callback_data="cannotCancelPVZ")
    cannotCancelPostRF = tps.InlineKeyboardButton("Не можем отменить Почта РФ",callback_data="cannotCancelPostRF")
    jira31day = tps.InlineKeyboardButton("31 день на отмену",callback_data="jira31day")
    jiraInDoc = tps.InlineKeyboardButton("Список др. жир",callback_data="jiraInDoc")
    anotherWorkerResponse = tps.InlineKeyboardButton("Ответил_др. оператор",callback_data="anotherWorkerResponse")
    jira.row(cannotCancelPVZ,cannotCancelPostRF,jira31day,jiraInDoc,anotherWorkerResponse)

    orderBanLifted = tps.InlineKeyboardButton("Снят запрет заказа",callback_data="orderBanLifted")
    noCertificate = tps.InlineKeyboardButton("Сертификата нет/ скрытие товара",callback_data="noCertificate")
    certificateIssuance = tps.InlineKeyboardButton("Выдача сертификата",callback_data="certificateIssuance")
    answerIsDouble = tps.InlineKeyboardButton("Ответ в задании: дубль",callback_data="answerIsDouble")
    courierDelivered = tps.InlineKeyboardButton("Доставлен-не-получен: курьер доставил",callback_data="courierDelivered")
    jira.row(orderBanLifted,noCertificate,certificateIssuance,answerIsDouble,courierDelivered)
    bot.send_message(message.chat.id, f"_", reply_markup=jira)

def btn_process(bot,call):
    def plus():
        bot.send_message(chat_id=call.message.chat.id, text=f'`+`', parse_mode="Markdown")
        
    def full_response(subject):
        chat,closing_jira,category = postgres.obj.take_jira_full(subject)
        if subject == 'jiraInDoc':
            bot.send_message(chat_id=call.message.chat.id, text=f'{chat}\n\n{closing_jira}')
        else:
            ppc.copy(f'{chat}'); bot.send_message(chat_id=call.message.chat.id, text=f'`{closing_jira}`\n\n`{category}`', parse_mode="Markdown")
    
    def chat_only(subject):
        chat = postgres.obj.take_jira_chat_only(subject); ppc.copy(f'{chat}'); plus()

    def no_need_response(subject):
        template = postgres.obj.take_no_need_response(subject)
        ppc.copy('{}'.format(template)); plus()
                

    switcher = {
        "cannotCancelPVZ":lambda:full_response('cannotCancelPVZ'),
        "cannotCancelPostRF":lambda:full_response('cannotCancelPostRF'),
        "jira31day":lambda:full_response('jira31day'),
        "jiraInDoc":lambda:full_response('jiraInDoc'),
        "anotherWorkerResponse":lambda:no_need_response('anotherWorkerResponse'),
        "orderBanLifted":lambda:full_response('orderBanLifted'),
        "noCertificate":lambda:full_response('noCertificate'),
        "certificateIssuance":lambda:full_response('certificateIssuance'),
        "answerIsDouble":lambda:chat_only('answerIsDouble'),
        "courierDelivered":lambda:full_response('courierDelivered')
        }

    switcher[call.data]()


