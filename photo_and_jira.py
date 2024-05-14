import telebot
import pyperclip as ppc
from telebot import types as tps
api_token = "5504305892:AAEEDAuidnKOG1refLzWJ9aQvsIV7YW5iRg"
bot = telebot.TeleBot(api_token, parse_mode=None)

def show_jira_and_photo(bot,message):
    jira_photo = tps.InlineKeyboardMarkup()
    jiraForOrder = tps.InlineKeyboardButton("Жира по заказу",callback_data="jiraForOrder")
    jiraForQuestion = tps.InlineKeyboardButton("Жира по вопросу",callback_data="jiraForQuestion")
    currentlyWorking = tps.InlineKeyboardButton("Пока что занимаются вопросом",callback_data="currentlyWorking")
    jiraLong = tps.InlineKeyboardButton("Жира больше срока",callback_data="jiraLong")
    certificateLong = tps.InlineKeyboardButton("Сертиф. больше срока",callback_data="certificateLong")
    certificateReq = tps.InlineKeyboardButton("Запрос сертификата",callback_data="certificateReq")
    jira_photo.row(jiraForOrder,jiraForQuestion,currentlyWorking,jiraLong,certificateLong,certificateReq)
    
    photoReply = tps.InlineKeyboardButton("Фото ответ",callback_data="photoReply")
    photoOne = tps.InlineKeyboardButton("Фото одно",callback_data="photoOne")
    textReply = tps.InlineKeyboardButton("Текстовый ответ",callback_data="textReply")
    photoAndText = tps.InlineKeyboardButton("Фото и текст",callback_data="photoAndText")
    photoDispute = tps.InlineKeyboardButton("Фото и спор",callback_data="photoDispute")
    re_registration = tps.InlineKeyboardButton("Переоформление",callback_data="re-registration")
    jira_photo.row(photoReply,photoOne,textReply,photoAndText,photoDispute,re_registration)
    bot.send_message(message.chat.id, f"_", reply_markup=jira_photo)

def btn_process(bot,call):

    def plus():
        bot.send_message(chat_id=call.message.chat.id, text="+")
    def comment(text):
        bot.send_message(chat_id=call.message.chat.id, text=f"`{text}`",parse_mode="Markdown")
    
    if call.data =="jiraForOrder":
        ppc.copy(f'Передал информацию коллегам. Уже занимаемся решением вопроса, обязательно во всём разберёмся и вернёмся к вам с ответом. Предоставить ответ по заказу XXXXXXXX-XXXX должны будем в течение 3 суток. Пожалуйста, ожидайте обратной связи.'); plus()
    if call.data =="jiraForQuestion":
        ppc.copy(f'Передал информацию коллегам. Уже занимаемся решением вопроса, обязательно во всём разберёмся и вернёмся к вам с ответом. Предоставить ответ по вопросу должны будем в течение 3 суток. Пожалуйста, ожидайте обратной связи.'); plus()
    if call.data =="currentlyWorking":
        ppc.copy(f'Вижу, что мои коллеги пока что занимаются решением вопроса по заказу XXXXXXXX-XXXX. Сроки рассмотрения составляют 3 суток с момента начала обработки запроса. Простите, что заставляем ожидать. Когда решение по данному вопросу будет принято, мы вас обязательно об этом уведомим. Пожалуйста, ожидайте обратной связи.'); plus()
    if call.data =="jiraLong":
        ppc.copy(f'Вижу, что мои коллеги пока что занимаются решением вопроса заказу XXXXXXXX-XXXX. Простите, что до сих пор не вернулись с ответом. К сожалению, это потребовало больше времени, чем обычно. Когда решение по данному вопросу будет принято, мы вас обязательно об этом уведомим. Пожалуйста, ожидайте обратной связи.'); plus()
    if call.data =="certificateReq":
        ppc.copy(f'Передал информацию своим коллегам. Они уже занимаются вашим вопросом. Сертификат должны будут выдать в течение 7 суток. Пожалуйста, ожидайте обратной связи.'); plus()
    if call.data =="certificateLong":
        ppc.copy(f'Вижу, что мои коллеги пока что занимаются вопросом выдачи сертификата. Простите, что до сих пор не вернулись с ответом. К сожалению, это потребовало больше времени, чем обычно. Когда получим на руки документ от продавца, обязательно отправим его вам в этом же чате. Пожалуйста, ожидайте обратной связи.'); plus()

    if call.data =="photoReply":
        ppc.copy(f'Спасибо за фотографии. Прикрепили к заявке на возврат XXX. Ваш вопрос находится у коллег в работе. По результатам обязательно с вами свяжемся. Простите, что заставляем ждать. Стараемся как можно скорее решить вопрос.'); comment('Премодерация')
    if call.data =="photoOne":
        ppc.copy(f'Спасибо за фотографию. Прикрепили к заявке на возврат XXX. Ваш вопрос находится у коллег в работе. По результатам обязательно с вами свяжемся. Простите, что заставляем ждать. Стараемся как можно скорее решить вопрос.'); comment('Премодерация')
    if call.data =="textReply":
        ppc.copy(f'Спасибо за обратную связь. Прикрепили к заявке на возврат XXX. Ваш вопрос находится у коллег в работе. По результатам обязательно с вами свяжемся. Простите, что заставляем ждать. Стараемся как можно скорее решить вопрос.'); comment('Премодерация')
        bot.send_message(chat_id=call.message.chat.id, text="/start /fb `Премодерация`",parse_mode="Markdown")
    if call.data =="photoAndText":
        ppc.copy(f'Спасибо за фотографии и обратную связь. Прикрепили к заявке на возврат XXX. Ваш вопрос находится у коллег в работе. По результатам обязательно с вами свяжемся. Простите, что заставляем ждать. Стараемся как можно скорее решить вопрос.'); comment('Премодерация')
        bot.send_message(chat_id=call.message.chat.id, text="/start /fb `Премодерация`",parse_mode="Markdown")
    if call.data =="photoDispute":
        ppc.copy(f'Спасибо за фотографии. Прикрепили к заявке на возврат XXX. Ваш вопрос находится у коллег в работе. По результатам обязательно с вами свяжемся. Стараемся как можно скорее решить вопрос. Пожалуйста, ожидайте решения по спору.'); comment('Спор')
    if call.data =="re-registration":
        ppc.copy(f'Здравствуйте, ИМЯ. Благодарю за ожидание.\n\nСпасибо за фотографии. Прикрепили к заявке на возврат XXX. Вижу, что ваша заявка уже отклонена, потому что не получили от вас ответа в срок.\n\nВыдали вам кнопку на возврат, она появится в течение 24 часов, и будет доступна в течение 48 часов. Пожалуйста, оформите заявку на возврат повторно, чтобы мои коллеги смогли рассмотреть заявку на возврат.\n\nЕсли возникнут дополнительные вопросы, обращайтесь к нам в чат.'); plus()