import telebot
import pyperclip as ppc
from telebot import types as tps
api_token = "5504305892:AAEEDAuidnKOG1refLzWJ9aQvsIV7YW5iRg"
bot = telebot.TeleBot(api_token, parse_mode=None)

def show_shorts_and_clar(bot,message):
    shrt = tps.InlineKeyboardMarkup(row_width=1)
    whatSituation = tps.InlineKeyboardButton("Ситуация/подробнее?", callback_data="whatSituation")
    itemNumber = tps.InlineKeyboardButton("Номер?", callback_data="itemNumber")
    noDeliveryMethod = tps.InlineKeyboardButton("Не предлагается способ доставки?", callback_data="noDeliveryMethod")
    pickupPointClosed = tps.InlineKeyboardButton("ПВЗ закрыт", callback_data="pickupPointClosed")
    cant_take_order_pvz = tps.InlineKeyboardButton("не выдают заказ", callback_data="cant_take_order_pvz")
    adressOnly = tps.InlineKeyboardButton("Какой адрес?", callback_data="adressOnly")
    linkOrCode = tps.InlineKeyboardButton("Ссылку/код товара?", callback_data="linkOrCode")
    shrt.row(whatSituation, itemNumber, noDeliveryMethod, pickupPointClosed,cant_take_order_pvz, adressOnly, linkOrCode)

    transferToBank = tps.InlineKeyboardButton("Перевод в банк",callback_data="transferToBank")
    postPay = tps.InlineKeyboardButton("Пост оплата",callback_data="postPay")
    bankDocs = tps.InlineKeyboardButton("Выписка",callback_data="bankDocs")
    dynamicCost = tps.InlineKeyboardButton("Динамич цены",callback_data="dynamicCost")
    workerBriefing = tps.InlineKeyboardButton("Инструк таж сотр",callback_data="workerBriefing")
    cookie = tps.InlineKeyboardButton("Куки и др.",callback_data="cookie")
    hotLine = tps.InlineKeyboardButton("Горячая линия",callback_data="hotLine")
    shrt.row(transferToBank, postPay, bankDocs, dynamicCost, workerBriefing, cookie, hotLine)

    cancelRequest = tps.InlineKeyboardButton("Отм обращ-е",callback_data="cancelRequest")
    textShell = tps.InlineKeyboardButton("Обол очка",callback_data="textShell")
    ifQuestions = tps.InlineKeyboardButton("Закры вашка",callback_data="ifQuestions")
    greetingStr = tps.InlineKeyboardButton("Откры вашка",callback_data="greetingStr")
    waitingForClient = tps.InlineKeyboardButton("Ждем ответа клиента",callback_data="waitingForClient")
    waitingNoTheme = tps.InlineKeyboardButton("Ждем на уточ нении",callback_data="waitingNoTheme")
    noWaitingForAnswer = tps.InlineKeyboardButton("Не дожд ался ответа",callback_data="noWaitingForAnswer")
    shrt.row(cancelRequest, textShell, ifQuestions, greetingStr, waitingForClient, waitingNoTheme, noWaitingForAnswer)
    bot.send_message(message.chat.id, f"_", reply_markup=shrt)

def btn_process(bot,call):

    def plus():
        bot.send_message(chat_id=call.message.chat.id, text="+")
    def comment(text):
        bot.send_message(chat_id=call.message.chat.id, text=f"`{text}`",parse_mode="Markdown")
    def reply_closing(text):
        ppc.copy('{}'.format(text)); plus()

    if call.data =="canWatchBS":
        ppc.copy('Вы можете отследить все операции по покупкам и возвратам в личном кабинете, во вкладке "Баланс средств".'); plus()
    if call.data == "fourNineHours":
            ppc.copy('Статус изменится в следующие 49 часов с момента отмены заказа.'); plus()
    if call.data =="ifRelevant":
        ppc.copy('Если товар будет ещё актуален - можете переоформить заказ. Для этого зайдите в нужный и нажмите "Повторить заказ".'); plus()
    if call.data == "dynamicCost":
        ppc.copy('У нас динамичное ценообразование, поэтому стоимость может меняться, как в большую, так и в меньшую сторону со временем.'); plus()
    if call.data == "cancelRequest":
        ppc.copy('Здравствуйте, ИМЯ. Спасибо за обращение. Хорошего вам дня. Если возникнут дополнительные вопросы, обращайтесь к нам в чат.'); comment('Клиенту не потребовалась помощь'); comment('Бот уже решил вопрос клиента')

    if call.data == "whatSituation":
        ppc.copy("Здравствуйте, XXX. Благодарю за ожидание.\n\nЧтобы корректно вас проконсультировать, не могли бы вы поподробнее рассказать ситуацию? Так я смогу помочь вам быстрее."); plus()
    if call.data == "itemNumber":
        ppc.copy("Здравствуйте, XXX. Благодарю за ожидание.\n\nЧтобы корректно вас проконсультировать, уточните, пожалуйста, номер вашего заказа."); plus()
    if call.data == "noDeliveryMethod":
        ppc.copy("Здравствуйте, XXX. Благодарю за ожидание.\n\nУточните, пожалуйста, у вас не предлагается только предпочитаемый способ доставки или вообще не предлагается никакой?") 
        bot.send_message(chat_id=call.message.chat.id, text=f'ВОПРОС СКОПИРОВАН\n\nВТОРОЙ ШАБЛОН: `Некоторые товары доставляются не везде или не всеми способами, потому что зоны доставки для них ограничены. Мы работаем над тем, чтобы исправить эту ситуацию.\n\nВ качестве альтернативы можете подобрать аналогичный товар с помощью фильтров поиска на нашем сайте. Также рекомендую воспользоваться разделом "Похожие товары". Для этого перейдите на страницу товара и выберите позицию с доступной доставкой.`',parse_mode="Markdown")

    if call.data == "workerBriefing":
        ppc.copy('Извините, что курьер не доставил товар надлежащим образом и не позвонил перед доставкой. Уже передал информацию коллегам. Обязательно во всём разберёмся. С курьером/сотрудником проведут дополнительный инструктаж.'); comment('Некорректное поведение / внешний вид')


    if call.data == "textShell":
        ppc.copy('Здравствуйте, ИМЯ. Благодарю за ожидание.\n\n\n\nЕсли возникнут дополнительные вопросы, обращайтесь к нам в чат.'); plus()
    if call.data == "pickupPointClosed":
        ppc.copy("Здравствуйте, XXX. Благодарю за ожидание.\n\nЧтобы корректно вас проконсультировать, уточните, пожалуйста:\n1. Адрес вашего визита\n2. Дата и время посещения\n3. Как долго ожидали, если ожидали\n4. Была ли табличка на двери информирующая, почему пункт выдачи закрыт"); 
        bot.send_message(chat_id=call.message.chat.id, text=f"Первое обращение за 30 дней: `'Благодарю за уточнение. Простите, что пункт выдачи был закрыт. Связаться с сотрудниками не удалось. Пожалуйста, попробуйте подойти в пункт выдачи на следующий день. Для удобства продлили срок хранения посылки до XXX.\n\nЕсли ситуация останется прежней или возникнут дополнительные вопросы, обращайтесь к нам в чат.'`",parse_mode="Markdown")
    if call.data == "adressOnly":
        ppc.copy("Здравствуйте, XXX. Благодарю за ожидание.\n\nУточните, пожалуйста, по какому адресу обращались?"); plus()
    if call.data == "linkOrCode":
        ppc.copy("Здравствуйте, XXX. Благодарю за ожидание.\n\nЧтобы корректно вас проконсультировать, пришлите, пожалуйста, ссылку на товар или код товара."); plus()


    if call.data =="ifQuestions": ppc.copy('Если возникнут дополнительные вопросы, обращайтесь к нам в чат.'); plus()
    if call.data =="greetingStr": ppc.copy('Здравствуйте, XXX. Благодарю за ожидание.'); plus()
    if call.data =="waitingForClient": ppc.copy('Ждём ответа клиента'); plus()
    if call.data =="waitingNoTheme": ppc.copy('Ждём ответа клиента. Тема обращения на уточнении'); plus()
    if call.data =="noWaitingForAnswer": ppc.copy('К сожалению, не дождался вашего ответа. Как только у вас появится свободное время – напишите в этот чат.'); plus()


# ДРУГОЕ
    if call.data =="transferToBank":
        ppc.copy(f'Здравствуйте, ИМЯ. Благодарю за ожидание. \n\nПо вопросам продуктов *** Банка рекомендую написать в чат в личном кабинете банка: link\n\nМои коллеги обязательно вам помогут. Если будут вопросы по другим продуктам и услугам ***, напишите нам.'); plus()
    if call.data =="postPay":
        ppc.copy(f'Здравствуйте, ИМЯ. Благодарю за ожидание.\n\nОплата после получения доступна для следующих товаров: одежда, обувь, аксессуары, ювелирные изделия со значком "Оплата после примерки".\n\nЭта функция доступна только при доставке в некоторые пункты выдачи. То есть не каждый пункт выдачи будет доступен с таким вариантом оплаты. При заказе нескольких товаров оплата после получения должна быть доступна для каждого товара.\n\nОплата заказа с баланса средств не доступна. Можно оплатить банковской картой или картой  ***. Максимальная сумма заказа не должна превышать 100 тыс. руб.\n\nКак проверить доступность оплаты после: выберите пункт выдачи и перейдите к оформлению покупки. В качестве альтернативы можно найти аналогичный товар. Подробнее про способы оплаты рассказываем здесь: link\n\nЕсли возникнут дополнительные вопросы, обращайтесь к нам в чат.');  plus()

    if call.data =="bankDocs":
        ppc.copy(f'Здравствуйте, ИМЯ. Благодарю за ожидание.\n\nПришлите, пожалуйста, выписку из банка за период: с даты списания по текущий день. Выписку можно запросить в мобильном приложении вашего банка или в самом отделении банка. Обращаю внимание на то, что это должен быть именно документ, а не снимок экрана. Образец выписки можно посмотреть здесь: link\n\nЕсли возникнут дополнительные вопросы, обращайтесь к нам в чат.'); comment('Ждём клиента с выпиской')

    if call.data =="cookie":
        ppc.copy(f'Здравствуйте, ИМЯ. Благодарю за ожидание.\n\nВозможно, вам поможет одно из следующих решении:\n— выйдите и снова зайдите в свой аккаунт\n— повторите попытку с сайта\n— очистите кэш и cookies на устройстве\n— повторите попытку с другого устройства\n— повторите попытку через несколько часов\n— удалите приложение и повторно установите его\n\nЕсли эти варианты решения никак не помогут, пожалуйста, сообщите нам об этом.'); plus()
    

    if call.data =="hotLine":
        ppc.copy(f'Здравствуйте, ИМЯ. Благодарю за ожидание.\n\nК сожалению, у нас нет горячей линии. Всё взаимодействие происходит в чате. Вы можете задать свой вопрос и мы оперативно и подробно на него ответим. Так вам не придётся ожидать ответа оператора на линии десятки минут. Когда мы ответим вам в чате, вам просто придет уведомление.\n\nЕсли возникнут дополнительные вопросы, обращайтесь к нам в чат.'); plus()

    if call.data =="cant_take_order_pvz":
        ppc.copy(f'Здравствуйте, XXX. Благодарю за ожидание.\n\nЧтобы корректно вас проконсультировать, уточните, пожалуйста:\n1. Адрес вашего визита\n2. Дата и время посещенияn\3. Что вам сообщил сотрудник пункта выдачи'); plus()