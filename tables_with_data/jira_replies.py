import postgres_for_tables as psql

def create_table(cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS jira_replies (
        id SERIAL PRIMARY KEY, 
        name_en VARCHAR(255), 
        name_ru VARCHAR(255), 
        chat TEXT,
        closing_jira TEXT,
        category VARCHAR(255)
        );""")

def insert_data(cursor):
    cursor.execute("""INSERT INTO jira_replies (name_en,name_ru,chat,closing_jira,category) VALUES 
    ('cannotCancelPVZ','Не можем отменить ПВЗ','Ранее вы обращались по вопросу: отмена заказа XXX.\n\nОтвет специалиста: Здравствуйте, XXX. К сожалению, не обладаем возможностью отменить заказ. Вы можете отказаться от получения заказа в пункте выдачи. Если это неудобно, рекомендую дождаться, когда у посылки истечёт срок хранения и она будет отправлена обратно продавцу. Как и когда вернутся деньги подробно написали на странице: link','Клиент проинформирован','Просьба отменить товар/заказ'), 
    ('cannotCancelPostRF','Не можем отменить Почта РФ','Ранее вы обращались по вопросу: отмена заказа XXX.\n\nОтвет специалиста: Здравствуйте, XXX. К сожалению, не обладаем возможностью отменить заказ. Вы можете отказаться от получения заказа в отделении Почты России. Если это неудобно, рекомендую дождаться, когда у посылки истечёт срок хранения и она будет отправлена обратно продавцу. Как правило, это составляет 15 дней. Как и когда вернутся деньги подробно написали на странице: link','Клиент проинформирован','Просьба отменить товар/заказ'),
    ('jira31day','31 день на отмену','Ранее вы обращались по вопросу: отмена заказа XXX\n\nОтвет специалиста: Здравствуйте, XXX. Заявка на отмену заказа принята. Заказ собран и передается в доставку, чтобы мы смогли отменить заказ, нам необходимо подтверждение продавца.\n\nНапишите, пожалуйста, продавцу об отмене заказа. После его согласия поможем отменить заказ. Для этого в личном кабинете в заказе нажмите кнопку "Связаться с продавцом", они отвечают в течение 1-3 дней.\n\nЗаказ автоматически отменится, если не будет отгружен или задержится на 31 день. Если у вас появятся дополнительные вопросы - обязательно напишите нам в чат.','Клиент проинформирован','Просьба отменить товар/заказ'),
    ('orderBanLifted','Снят запрет заказа','Ранее вы обращались по вопросу:  сложности с оформлением заказов.\n\nОтвет специалиста: Здравствуйте, XXX. Проверили информацию по вашему случаю. Можете оформлять заказы, всё должно исправно работать.','Клиент проинформирован','Консультация по оформлению заказа'),
    ('noCertificate','Сертификата нет/ скрытие товара','Ранее вы обращались по вопросу: выдача сертификата для товара “XXX”\n\nОтвет специалиста: Здравствуйте, XXX. К сожалению, продавец не предоставил необходимый документ, который бы подтверждал, что товар безопасен для покупателей и изготовлен по стандартам качества. Поэтому было решено убрать его из продажи. В отношении нарушителя примем необходимые меры. Благодарим, что помогли нам выявить товар без сертификата.', 'Клиент проинформирован', 'Подделка / не оригинальный товар'), 
    ('certificateIssuance','Выдача сертификата','Ранее вы обращались по вопросу: получение документа, подтверждающего оригинальность товара “XXX”.\n\nОтвет специалиста: Здравствуйте, XXX. Высылаем документ, подтверждающий оригинальность товара. При желании можете с ним ознакомиться и убедиться в подлинности товара.', 'Клиенту был выдан документ','Сомнения в оригинальности товара'),
    ('answerIsDouble','Ответ в задании XXX: дубль','Ответ в задании XXX: дубль','',''),
    ('courierDelivered','Доставлен-не-получен: курьер доставил','Ранее вы обращались по вопросу: некорректный статус заказа XXX, товар "XXX"\n\nОтвет специалиста: Здравствуйте, XXX. Коллеги проверили информацию по вашему вопросу и сообщили, что заказ был доставлен.\n\nУточните, так ли это? Наш курьер привез вам заказ?', 'Клиенту задан уточняющий вопрос, в действительности ли он получил товар', 'Статус в ЛК «Получено», отправление не получено'),
    ('anotherWorkerResponse','НТО Ответил другой оператор','','До меня уже ответил другой оператор','')
    ;""")

def additional_data(cursor):
    pass
    # cursor.execute("""INSERT INTO feedback_shorts (name_en,name_ru,template) VALUES 
    # ('XXXX','XXXX','XXXX');""")

def show_me_all_data(cursor):
    cursor.execute("SELECT * FROM jira_replies;")
    dataStream = cursor.fetchall();
    for column in dataStream:
        print(f'{column[0]}\t{column[1]}\t{column[2]}\t{column[3]}\t{column[4]}')


def shange_column(paste, remove):
    cursor.execute("UPDATE jira_replies SET name_en = '{}' WHERE name_en = '{}';".format(paste, remove));

if __name__ == "__main__":
    conn, cursor = psql.obj.open_connection()
    # psql.obj.delete_table('feedback_shorts')
    create_table(cursor)
    insert_data(cursor)
    # psql.obj.delete_string('jira_replies',4)
    # psql.obj.add_string('jira_replies','name_en,name_ru,chat,closing_jira,category',"'anotherWorkerResponse','НТО Ответил другой оператор','','До меня уже ответил другой оператор',''")
    show_me_all_data(cursor)
    # psql.obj.print_column("feedback_shorts", "sellersResponse")
    psql.obj.close_connection(conn,cursor)