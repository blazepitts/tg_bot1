import telebot, postgres
import pyperclip as ppc
from telebot import types as tps

api_token = "5504305892:AAEEDAuidnKOG1refLzWJ9aQvsIV7YW5iRg"
bot = telebot.TeleBot(api_token, parse_mode=None)

class Temp:
    def __init__(self):
        self.moneyBack = False

    def getMoneyBack(self):
        return self.moneyBack

feedback_obj = Temp();

def show_feedback(bot,message):
    
    fback_main = tps.InlineKeyboardMarkup()
    persnlOpnion = tps.InlineKeyboardButton("Субъективное мнение",callback_data="persnlOpnion")
    badTaste = tps.InlineKeyboardButton("Вкус",callback_data="badTaste")
    badSmell = tps.InlineKeyboardButton("Запах",callback_data="badSmell")
    noCompanyPkg = tps.InlineKeyboardButton("Без упаковки",callback_data="noCompanyPkg")
    pkgDamaged = tps.InlineKeyboardButton("Поврежд упак.",callback_data="pkgDamaged")
    factoryPkgDamaged = tps.InlineKeyboardButton("Завод.уп. поврежд",callback_data="factoryPkgDamaged")
    fback_main.row(persnlOpnion,badTaste,badSmell,pkgDamaged,noCompanyPkg,factoryPkgDamaged)

    lateRet3d = tps.InlineKeyboardButton("Прср-3д",callback_data="lateRet3d")
    lateRet24h = tps.InlineKeyboardButton("Прср-24ч",callback_data="lateRet24h")
    figureItOut = tps.InlineKeyboardButton("Хотим утч",callback_data="figureItOut")
    checkedInf = tps.InlineKeyboardButton("Прове рили",callback_data="checkedInf")
    lateRet7d = tps.InlineKeyboardButton("Прср-7д",callback_data="lateRet7d")
    lateRet30d = tps.InlineKeyboardButton("Прср-30д",callback_data="lateRet30d")
    empty4 = tps.InlineKeyboardButton("пустой 2",callback_data="empty4")
    fback_main.row(lateRet3d,lateRet24h,figureItOut,checkedInf,lateRet7d,lateRet30d,empty4)
    
    notWork = tps.InlineKeyboardButton("Не работает",callback_data="notWork")
    malfunctioning = tps.InlineKeyboardButton("Неисправ но робит",callback_data="malfunctioning")
    expiredDateWithPhoto = tps.InlineKeyboardButton("Срок годн +фото",callback_data="expirationDateAndPhoto")
    fakeGoodJira = tps.InlineKeyboardButton("Подделк Jira",callback_data="fakeGoodJira")
    whyfakeGood = tps.InlineKeyboardButton("Почему подделк",callback_data="whyfakeGood")
    fakeGoodrfbs = tps.InlineKeyboardButton("Подделк rfbs снг/Globl",callback_data="fakeGoodrfbs")
    fback_main.row(notWork,malfunctioning,expiredDateWithPhoto,fakeGoodJira,whyfakeGood,fakeGoodrfbs)

    wrongColour = tps.InlineKeyboardButton("Не тот цвет",callback_data="wrongColour")
    wrongSize = tps.InlineKeyboardButton("Не тот размер",callback_data="wrongSize")
    spilledGoods = tps.InlineKeyboardButton("Пролит",callback_data="spilledGoods")
    badView = tps.InlineKeyboardButton("Неподо -бающий",callback_data="badView")
    doesntFit = tps.InlineKeyboardButton("Не подошёл",callback_data="doesntFit")
    empty1 = tps.InlineKeyboardButton("пустой 1",callback_data="empty1")
    empty2 = tps.InlineKeyboardButton("пустой 2",callback_data="empty2")
    fback_main.row(wrongColour,wrongSize,spilledGoods,badView,doesntFit,empty1,empty2)

    notWholeSet = tps.InlineKeyboardButton("Неком плект",callback_data="notWholeSet")
    damagedGood = tps.InlineKeyboardButton("Повреж дённый",callback_data="damagedGood")
    wrongItem = tps.InlineKeyboardButton("Не тот товар",callback_data="wrongItem")
    openedItem = tps.InlineKeyboardButton("Вскрыт",callback_data="openedItem")
    secondHand = tps.InlineKeyboardButton("Б/У",callback_data="secondHand")
    empty3 = tps.InlineKeyboardButton("пустой 3",callback_data="empty3")
    fback_main.row(notWholeSet,damagedGood,wrongItem,openedItem,secondHand,empty3)

    fbMoneyBack = tps.InlineKeyboardButton("Вернули дс/ в пути",callback_data="fbMoneyBack")
    notMatchDescription = tps.InlineKeyboardButton("Неточ. описания",callback_data="notMatchDescription")
    lowQuality = tps.InlineKeyboardButton("Некачес твенный",callback_data="lowQuality")
    returnAllowed = tps.InlineKeyboardButton("Заявка одобрена",callback_data="returnAllowed")
    requestProcessing = tps.InlineKeyboardButton("Заявка рассм-тся",callback_data="requestProcessing")
    canWriteChat = tps.InlineKeyboardButton("Можете написать",callback_data="canWriteChat")
    feedbackShorts = tps.InlineKeyboardButton("Шорты",callback_data="feedbackShorts")
    fback_main.row(fbMoneyBack,notMatchDescription,lowQuality,returnAllowed,requestProcessing,canWriteChat,feedbackShorts)
    bot.send_message(message.chat.id, text=f'_',reply_markup=fback_main)


def btn_process(bot,call):
    
    def show_feedback_shorts():
        short = tps.InlineKeyboardMarkup()
        sellersResponse = tps.InlineKeyboardButton("нто ответ селлера",callback_data="sellersResponse")
        sellerSentReturn = tps.InlineKeyboardButton("нто сллр направил вернуть",callback_data="sellerSentReturn")
        answeredBeforeMe = tps.InlineKeyboardButton("нто др. оператор",callback_data="answeredBeforeMe")
        goodFeedback = tps.InlineKeyboardButton("нто положит отзыв",callback_data="goodFeedback")
        noFeedback = tps.InlineKeyboardButton("нто отзыв отсутствует",callback_data="noFeedback")
        noQuestionNoAngry = tps.InlineKeyboardButton("Нет вопроса и недо вольства",callback_data="noQuestionNoAngry")
        short.row(sellersResponse,sellerSentReturn,answeredBeforeMe,goodFeedback,noFeedback,noQuestionNoAngry)

        clientIsInformed = tps.InlineKeyboardButton("Кл проин формирован",callback_data="clientIsInformed")
        doubleJira = tps.InlineKeyboardButton("Жира дубль",callback_data="doubleJira")
        sellerAccuses = tps.InlineKeyboardButton("Селлер виноватит Ozon",callback_data="sellerAccuses")
        sharesContacts = tps.InlineKeyboardButton("Селлер делится контактами",callback_data="sharesContacts")
        sellerAccusesDelivery = tps.InlineKeyboardButton("Селлер виноватит доставку",callback_data="sellerAccusesDelivery")
        short.row(clientIsInformed,doubleJira,sharesContacts,sellerAccuses,sellerAccusesDelivery)
        bot.send_message(chat_id=call.message.chat.id, text=f'_',reply_markup=short)
    
    def plus():
        bot.send_message(chat_id=call.message.chat.id, text=f'`+`', parse_mode="Markdown")

    def short_response(subject):
        take = postgres.obj.take_feedback_short(subject); ppc.copy(f'{take}'); plus()

    def text1_and_cat(subject):
        template1 = postgres.obj.take_feedback_main(subject,text_type='template1')
        cat = postgres.obj.take_feedback_main(subject,text_type='cat'); ppc.copy(f'{template1}')
        bot.send_message(chat_id=call.message.chat.id, text=f'`{cat}`', parse_mode="Markdown")

    def text1_only(subject):
        template = postgres.obj.take_feedback_main(subject,text_type='template1'); ppc.copy(f'{template}'); plus()
        
    def both_texts_and_cat(subject):
        template1 = postgres.obj.take_feedback_main(subject,text_type='template1'); ppc.copy(f'{template1}')
        template2 = postgres.obj.take_feedback_main(subject,text_type='template2')
        cat = postgres.obj.take_feedback_main(subject,text_type='cat')
        if subject == 'figureItOut':
            bot.send_message(chat_id=call.message.chat.id, text=f'`{cat}`\n\n{template2}', parse_mode="Markdown")
        elif subject == 'fakeGoodJira':
            bot.send_message(chat_id=call.message.chat.id, text=f'`{cat}`\n\nШаблон для отзыва уже скопирован\n\nЧат: `{template2}`', parse_mode="Markdown")
            bot.send_message(chat_id=call.message.chat.id, text=f'`{template1}`', parse_mode="Markdown")
        else:
            bot.send_message(chat_id=call.message.chat.id, text=f'`{cat}`\n\nШаблон для отзыва уже скопирован\n\nЧат: `{template2}`', parse_mode="Markdown")

    def short_response(subject):
        take = postgres.obj.take_feedback_short(subject, closing=0); ppc.copy(f'{take}'); plus()

    def short_and_closing(subject):
        take, closing = postgres.obj.take_feedback_short(subject, closing=1); ppc.copy(f'{take}')
        bot.send_message(chat_id=call.message.chat.id, text=f'`{closing}`', parse_mode="Markdown")

    def reason(subject):
        reason = postgres.obj.take_feedback_main(subject,text_type='template1')
        if subject == 'doesntFit': reason,space = '',''
        else:reason,space = reason,' '

        if feedback_obj.getMoneyBack() == True:
            ppc.copy(f'Здравствуйте, XXX. Благодарим за обратную связь.\n\n{reason}{space}Видим, вы вернули покупку. Как и когда вернутся деньги, подробно написали на странице: link\n\nНадеемся, что будущие покупки принесут лишь положительные эмоции.'); plus(); feedback_obj.moneyBack = False
        else:
            if subject == 'notMatchDescription':
                template = postgres.obj.take_feedback_main(subject,text_type='template2'); ppc.copy(f'{template}')
                cat = postgres.obj.take_feedback_main(subject,text_type='cat')
                bot.send_message(chat_id=call.message.chat.id, text=f'`{cat}`', parse_mode="Markdown")
            else:
                comm = postgres.obj.take_feedback_main(subject,text_type='comm')
                cat = postgres.obj.take_feedback_main(subject,text_type='cat')
                ppc.copy(f'Здравствуйте, XXX. Благодарим за обратную связь.\n\n{reason}{space}Можете оформить заявку на возврат. Для этого нажмите "Вернуть товары" в заказе и следуйте дальнейшим шагам. Подробнее о возврате товара рассказываем тут: link\n\nКак и когда вернутся деньги, подробно написали на странице: link\nЕсли возникнут трудности при возврате, напишите нам в чат.')
                if subject == 'doesntFit':plus()
                elif subject == 'badView':plus()
                else: bot.send_message(chat_id=call.message.chat.id, text=f'`{cat}`\n\n`{comm}`', parse_mode="Markdown")

        


    def moneyBack():
        feedback_obj.moneyBack = True
        bot.send_message(chat_id=call.message.chat.id, text=f'Выбери причину возврата', parse_mode="Markdown")

    switcher = {
        'sellersResponse':lambda:short_response('sellersResponse'),
        'sellerSentReturn':lambda:short_response('sellerSentReturn'),
        'answeredBeforeMe':lambda:short_response('answeredBeforeMe'),
        'goodFeedback':lambda:short_response('goodFeedback'),
        'noFeedback':lambda:short_response('noFeedback'),
        'clientIsInformed':lambda:short_response('clientIsInformed'),
        'doubleJira':lambda:short_response('doubleJira'),
        'sharesContacts':lambda:short_and_closing('sharesContacts'),
        'sellerAccuses':lambda:short_and_closing('sellerAccuses'),
        'sellerAccusesDelivery':lambda:short_and_closing('sellerAccusesDelivery'),
        'noQuestionNoAngry':lambda:short_response('noQuestionNoAngry'),
        'feedbackShorts':lambda:show_feedback_shorts(),
        'persnlOpnion':lambda:text1_and_cat('persnlOpnion'),
        'badTaste':lambda:text1_and_cat('badTaste'),
        'badSmell':lambda:text1_and_cat('badSmell'),
        'noCompanyPkg':lambda:text1_and_cat('noCompanyPkg'),
        'pkgDamaged':lambda:text1_and_cat('pkgDamaged'),
        'factoryPkgDamaged':lambda:text1_and_cat('factoryPkgDamaged'),
        'lateRet3d':lambda:text1_only('lateRet3d'),
        'lateRet24h':lambda:text1_only('lateRet24h'),
        'figureItOut':lambda:both_texts_and_cat('figureItOut'),
        'checkedInf':lambda:text1_and_cat('checkedInf'),
        'lateRet7d':lambda:text1_only('lateRet7d'),
        'lateRet30d':lambda:text1_only('lateRet30d'),
        'notWork':lambda:reason('notWork'),
        'malfunctioning':lambda:reason('malfunctioning'),
        'expiredDateWithPhoto':lambda:text1_only('expiredDateWithPhoto'),
        'fakeGoodJira':lambda:both_texts_and_cat('fakeGoodJira'),
        'whyfakeGood':lambda:both_texts_and_cat('whyfakeGood'),
        'fakeGoodrfbs':lambda:both_texts_and_cat('fakeGoodrfbs'),
        'wrongColour':lambda:reason('wrongColour'),
        'wrongSize':lambda:reason('wrongSize'),
        'spilledGoods':lambda:reason('spilledGoods'),
        'badView':lambda:reason('badView'),
        'doesntFit':lambda:reason('doesntFit'),
        'notWholeSet':lambda:reason('notWholeSet'),
        'damagedGood':lambda:reason('damagedGood'),
        'wrongItem':lambda:reason('wrongItem'),
        'openedItem':lambda:reason('openedItem'),
        'secondHand':lambda:reason('secondHand'),
        'fbMoneyBack':lambda:moneyBack(),
        'notMatchDescription':lambda:reason('notMatchDescription'), 
        'lowQuality':lambda:reason('lowQuality'),
        'returnAllowed':lambda:text1_and_cat('returnAllowed'),
        'requestProcessing':lambda:text1_and_cat('requestProcessing'),
        'canWriteChat':lambda:text1_only('canWriteChat')
        }

    switcher[call.data]()

