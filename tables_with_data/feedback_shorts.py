import postgres_for_tables as psql


def create_table(cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS feedback_shorts (
        id SERIAL PRIMARY KEY, 
        name_en VARCHAR(255), 
        name_ru VARCHAR(255), 
        template TEXT,
        nto TEXT
        );""")


def insert_data(cursor):
    cursor.execute("""INSERT INTO feedback_shorts (name_en,name_ru,template,nto) VALUES 
    ('sellersResponse','НТО ответ селлера','Селлер предоставил ответ клиенту, не нарушая правил публикации',''),
    ('sellerSentReturn','НТО селлер направил на возврат','Селлер направил клиента на возврат, не нарушая правил публикации',''),
    ('answeredBeforeMe','НТО ответил другой оператор','До меня уже предоставил консультацию другой оператор',''),
    ('goodFeedback','НТО положительный отзыв','Положительный отзыв',''),
    ('noFeedback','НТО нет отзыва на сайте','Отзыв отсутствует на сайте Ozon',''),
    ('clientIsInformed','Клиент проинформирован','Клиент проинформирован',''),
    ('doubleJira','Жира дубль','Ответ в CTASK-XXX: дубль',''),
    ('noQuestionNoAngry','Нет вопроса и недовольства','Отзыв клиента не содержит вопроса и не выражает недовольство',''),
    ('sharesContacts','Селлер делится контактами','Причина: селлер предлагает решить вопрос не на Ozon\n\nЧто изменить/удалить: Удалить ответ селлера','Создано задание на удаление ответа селлера, т.к. селлер предлагает решить вопрос не на Ozon'),
    ('sellerAccusesDelivery','Селлер виноватит службу доставки','Причина: Причина: селлер виноватит службу доставки\n\nЧто изменить/удалить: Удалить ответ селлера','Создано задание на удаление ответа селлера, т.к. селлер виноватит службу доставки'),
    ('sellerAccuses','Селлер виноватит Ozon','Причина: Причина: селлер виноватит Ozon\n\nЧто изменить/удалить: Удалить ответ селлера','Создано задание на удаление ответа селлера, т.к. селлер виноватит Ozon')
    ;""")

def additional_data(cursor):
    pass
    # cursor.execute("""INSERT INTO feedback_shorts (name_en,name_ru,template) VALUES 
    # ('XXXX','XXXX','XXXX');""")

def show_me_all_data(cursor):
    cursor.execute("SELECT * FROM feedback_shorts;")
    dataStream = cursor.fetchall();
    for column in dataStream:
        print(f'{column[0]}\t{column[1]}\t{column[2]}')


def shange_column(paste, remove):
    cursor.execute("UPDATE feedback_shorts SET name_en = '{}' WHERE name_en = '{}';".format(paste, remove));


if __name__ == "__main__":
    conn, cursor = psql.obj.open_connection()
    # psql.obj.delete_table('feedback_shorts')
    create_table(cursor)
    insert_data(cursor)
    show_me_all_data(cursor)
    # psql.obj.print_column("feedback_shorts", "sellersResponse")
    psql.obj.close_connection(conn,cursor)