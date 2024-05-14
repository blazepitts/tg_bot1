import postgres_for_tables as psql


def create_table(cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS feedback_counter (
        id SERIAL PRIMARY KEY, 
        btn_name_en VARCHAR(255), 
        btn_name_rus VARCHAR(255), 
        number_pressed INT);""")

def insert_data(cursor):
    cursor.execute("""INSERT INTO feedback_counter (btn_name_en,btn_name_rus,number_pressed) VALUES 
    ('persnlOpnion','Субъективное мнение',0),
    ('badTaste','Вкус',0),
    ('badSmell','Запах',0),
    ('jira31day','Жира: 31 день',0),
    ('pkgDamaged','Упаковка повреждена',0),
    ('noPkg','Без упаковки',0),
    ('noPkgAndDamaged','Заводская упаковка повреждена + не упаковано',0),
    ('checkedInf','Проверили',0),
    ('figureItOut','Хотим разобратьсяся',0),
    ('lateRet3d','Просрочено 3 дня',0),
    ('lateRet7d','Просрочено 7 дней',0),
    ('lateRet30d','Просрочено 30 дней',0),
    ('lateRet24h','Просрочено 24 часа',0),
    ('fbMoneyBackMKKnoBalance','Вернул МКК НЕ на балансе',0),
    ('fbMoneyBackMKKtoBalance','Вернул МКК НА балансе',0),
    ('fbMoneyBackBank','Вернули карта банка',0),
    ('fbMoneyBackComp','Вернули Ozon карта',0),
    ('fbMoneyBackSBP','Вернули СБП',0),
    ('notWork','Не работает',0),
    ('malfunctioning','Неисправно работает',0),
    ('badView','Неподобающий вид',0),
    ('doesntFit','Просто не подошёл',0),
    ('openedItem','Товар вскрыт',0),
    ('spilledGoods','Товар пролит',0),
    ('notWholeSet','Некомплект',0),
    ('notMatchDescription','Неточности описания',0),
    ('damagedGood','Повреждённый товар',0),
    ('brokenGood','Сломанный товар',0),
    ('wrongSize','Не тот размер',0),
    ('wrongColour','Не тот цвет',0),
    ('wrongItem','Не тот товар',0),
    ('lowQuality','Некачественный товар',0),
    ('retAllowed','Заявка одобрена',0),
    ('noNeedToThrow','Выбрасывать не обязятельно',0),
    ('canWriteChat','Можете написать нам',0),
    ('sellerRespNoVlation','НТО ответ селлера',0),
    ('answerBeforeMe','НТО ответил другой оператор',0),
    ('clientIsInformed','Клиент проинформирован',0),
    ('doubleJira','Жира дубль',0),
    ('noReturnFb','Без возврата',0),
    ('goodFeedback','Положительный отзыв',0),
    ('deleteSeller','Селлер делится контактами',0),
    ('sellerAccuses','Селлер виноватит Ozon',0),
    ('noQuestionNoAngry','Нет вопроса и недовольства',0),
    ('companyPoints','Баллы Ozon возвр.',0)
    """)

def additional_data(cursor):
    pass
    # cursor.execute("""INSERT INTO feedback_counter (btn_name_en,btn_name_rus,number_pressed) VALUES 
    # ('XXXX','XXXX','XXXX');""")

def show_me_data(cursor):
    cursor.execute("""SELECT * FROM feedback_counter;""") 
    result = cursor.fetchall() 
    for row in result:
        print(f'{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}')


if __name__ == "__main__":
    conn, cursor = psql.obj.open_connection()
    # create_table(cursor)
    # insert_data(cursor)
    # additional_data(cursor)
    show_me_data(cursor)
    psql.obj.close_connection(conn,cursor)