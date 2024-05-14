import telebot
import pyperclip as ppc
from telebot import types as tps
api_token = "api_token"
bot = telebot.TeleBot(api_token, parse_mode=None)

def show_expected(bot,message):
    exp = tps.InlineKeyboardMarkup()
    expDatePVZ = tps.InlineKeyboardButton("Ожидаемая: ПВЗ/ПОСТАМАТ",callback_data="expDatePVZ")
    expDateCourier = tps.InlineKeyboardButton("Ожидаемая: курьер",callback_data="expDateCourier")
    expPVZInterval = tps.InlineKeyboardButton("Ожидаемая: ПВЗ С ИНТЕРВАЛОМ",callback_data="expPVZInterval")
    exactTimePVZ = tps.InlineKeyboardButton("Точное время для ПВЗ",callback_data="exactTimePVZ")
    exp.row(expDatePVZ,expDateCourier,expPVZInterval,exactTimePVZ)
    violatedPVZ = tps.InlineKeyboardButton("Нарушены сроки: ПВЗ",callback_data="violatedPVZ")
    violatedPVZinterval = tps.InlineKeyboardButton("Нарушены сроки: ПВЗ интервал",callback_data="violatedPVZinterval")
    violatedCourier = tps.InlineKeyboardButton("Нарушены сроки: курьер",callback_data="violatedCourier")
    exp.row(violatedPVZ,violatedPVZinterval,violatedCourier)
    bot.send_message(message.chat.id, "_", reply_markup=exp)

def btn_process(bot,call):
    def plus():
        bot.send_message(chat_id=call.message.chat.id, text="+")

    if call.data =="exactTimePVZ":
        ppc.copy(f'К сожалению, срок доставки в пункт выдачи указывается только в днях, не в часах. Если бы могли сказать точнее, мы бы обязательно сообщили.\n\nОжидаемая дата доставки ХХ МЕСЯЦА. Как только заказ будет готов для получения, сразу вышлем вам Push уведомление на телефон. Если будут какие-то изменения в доставке, мы обязательно вас уведомим.'); plus()
    if call.data =="expDatePVZ":
        ppc.copy(f'Ожидаемая дата доставки ХХ МЕСЯЦА. Как только заказ будет готов для получения, сразу вышлем вам Push уведомление на телефон. Если будут какие-то изменения в доставке, мы обязательно вас уведомим.'); plus()
    if call.data =="expDateCourier":
        ppc.copy(f'Ожидаемая дата доставки ХХ МЕСЯЦА с ХХ:ХХ до ХХ:ХХ. Курьер должен будет с вами связаться за 30-60 минут до прибытия для уточнения деталей встречи. Если будут какие-то изменения в доставке, мы обязательно вас уведомим.'); plus()
    if call.data =="expPVZInterval":
        ppc.copy(f'Ожидаемая дата доставки с ХХ МЕСЯЦА ХХ:ХХ до ХХ МЕСЯЦА ХХ:ХХ. Как только заказ будет готов для получения, сразу вышлем вам Push уведомление на телефон. Если будут какие-то изменения в доставке, мы обязательно вас уведомим.'); plus()
    if call.data =="violatedPVZ":
        ppc.copy(f'Извините, что перенесли доставку на другой день. Иногда служба доставки сталкивается со сложностями, которые задерживают транспортировку товара.\n\nЗаказ должны привезти к актуальной ожидаемой дате, ХХ МЕСЯЦА. Пожалуйста, ожидайте ваш заказ. Как только он будет готов для получения, сразу вышлем вам Push уведомление на телефон.'); plus()
    if call.data =="violatedPVZinterval":
        ppc.copy(f'Извините, что перенесли доставку на другой день. Иногда служба доставки сталкивается со сложностями, которые задерживают транспортировку товара.\n\nЗаказ должны привезти к актуальной ожидаемой дате, с ХХ МЕСЯЦА ХХ:ХХ до ХХ МЕСЯЦА ХХ:ХХ. Как только он будет готов для получения, сразу вышлем вам Push уведомление на телефон.'); plus()
    if call.data =="violatedCourier":
        ppc.copy(f'Извините, что перенесли доставку на другой день. Иногда служба доставки сталкивается со сложностями, которые задерживают транспортировку товара.\n\nКурьер должен привезти заказ к актуальной ожидаемой дате, ХХ МЕСЯЦА с ХХ:ХХ до ХХ:ХХ. Он свяжется с вами за 30-60 минут до прибытия для уточнения деталей встречи. Если будут какие-то изменения в доставке, мы обязательно вас уведомим.')
        bot.answer_callback_query(call.id, text=f"Copied: нарушены сроки курьер"); plus()
            