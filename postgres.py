import psycopg2


class postgres():

    def test_func(self):        
        print("hello from postgres")

    def open_connection(self):
        conn = psycopg2.connect(
            database='camad',
            user = 'postgres',
            password='21684',
            host='localhost',
            port='5432'
        )
        cursor = conn.cursor()
        print('psql connection established')
        return conn, cursor

    def close_connection(self,conn,cursor):
        conn.commit() # save changes
        cursor.close()
        conn.close()
        
    def how_namy_times_pressed(self, lang):
        conn, cursor = self.open_connection()
        cursor.execute("""SELECT * FROM feedback_counter""") 
        res = cursor.fetchall() 
        allRows,rows,spaces,idSpaces = "",""," "," "
        num1 = 0
        while num1 < 45:
            if num1 == 40:
                    tmp = res[40:]
            else:
                num2 = num1 + 5
                tmp = res[num1:num2]
            for row in tmp:
                spaces *= 30 - len(row[2])
                idSpaces *= 4 - len(str(row[0]))
                if lang == 'en':
                    rows += str(row[0]) + idSpaces + str(row[3]) + "  " + str(row[1]) +"\n"
                if lang == 'ru':
                    rows += str(row[0]) + idSpaces + str(row[3]) + "  " + str(row[2]) +"\n"
                spaces, idSpaces = " ", " "
            allRows += rows + "\n"
            rows=""
            num1+=5

        self.close_connection(conn, cursor)
        return allRows

    def take_feedback_main(self,subject,text_type):
        # text_type 1, 2, comm, cat
        conn, cursor = self.open_connection()
        self.update_counter_button(subject)
        if text_type == "template1":
            cursor.execute("SELECT template_1 FROM feedback_main WHERE name_en = '{}';".format(subject))
        elif text_type == "template2":
            cursor.execute("SELECT template_2 FROM feedback_main WHERE name_en = '{}';".format(subject))
        elif text_type == "comm":
            cursor.execute("SELECT comment FROM feedback_main WHERE name_en = '{}';".format(subject))
        elif text_type == "cat":
            cursor.execute("SELECT category FROM feedback_main WHERE name_en = '{}';".format(subject))
        for item in cursor.fetchall():
            take = item[0]
        self.close_connection(conn, cursor)
        return take


    def take_feedback_short(self,subject, closing):
        conn, cursor = self.open_connection()
        self.update_counter_button(subject)
        cursor.execute("SELECT template FROM feedback_shorts WHERE name_en = '{}';".format(subject))
        for item in cursor.fetchall():
            take = item[0]
        if closing == 1:
            cursor.execute("SELECT nto FROM feedback_shorts WHERE name_en = '{}';".format(subject))
            for item in cursor.fetchall():
                closing = item[0]
            self.close_connection(conn, cursor)
            return take, closing
        else: 
            self.close_connection(conn, cursor)
            return take
        
# ЖИРЫ
    def take_jira_full(self,subject):
        conn, cursor = self.open_connection()
        def switcher(column):
            cursor.execute("SELECT {} FROM jira_replies WHERE name_en = '{}';".format(column,subject))
            for item in cursor.fetchall(): return item[0]
        chat = switcher('chat')
        closing_jira = switcher('closing_jira')
        category = switcher('category')
        self.close_connection(conn, cursor)
        return chat,closing_jira,category

    def take_jira_chat_only(self,subject):
        conn, cursor = self.open_connection()
        cursor.execute("SELECT chat FROM jira_replies WHERE name_en = '{}';".format(subject))
        for item in cursor.fetchall(): chat = item[0]
        self.close_connection(conn, cursor); return chat

    def take_no_need_response(self,subject):
        conn, cursor = self.open_connection()
        cursor.execute("SELECT closing_jira FROM jira_replies WHERE name_en = '{}';".format(subject))
        for item in cursor.fetchall(): template = item[0]
        self.close_connection(conn, cursor); return template

        

    # ОБНОВЛЕНИЕ СЧЁТЧИКА
    def update_counter_button(self,subject):
        conn, cursor = self.open_connection()
        cursor.execute("UPDATE feedback_counter SET number_pressed = number_pressed + 1 WHERE btn_name_en = '{}';".format(subject))
        print("counter updated: {}".format(subject))

    # ДОБАВЛЕНИЕ КОЛОНКИ В ТАБЛИЦУ
    def table_add_column(self):
        conn, cursor = self.open_connection()
        cursor.execute("ALTER TABLE feedback_main ADD category VARCHAR(255);")
        cursor.execute("ALTER TABLE feedback_main ADD comment VARCHAR(255);")
        self.close_connection(conn, cursor)

    # ПЕРЕИМЕНОВАНИЕ КОЛОНКИ В ТАБЛИЦЕ
    def rename_column(self):
        conn, cursor = self.open_connection()
        cursor.execute("ALTER TABLE feedback_main RENAME COLUMN template_text TO template_1;")
        # cursor.execute("ALTER TABLE feedback_main RENAME COLUMN template_2 TO template_2;")
        self.close_connection(conn, cursor)

    # ДОБАВЛЕНИЕ ДАННЫХ, ТОЛЬКО ВСЯ СТРОКА. ЕСЛИ НЕ ВСЯ, СМОТРИ update_data
    def isert_data(self):
        conn, cursor = self.open_connection()
        cursor.execute("""  INSERT INTO feedback_main 
                            (template_name_en, template_name_ru, template_1, template_2, category, comment) VALUES 
                            ('Вопросы по товарам','Субъективное мнение');""")
        self.close_connection(conn, cursor)

    # ОБНОВЛЕНИЕ ДАННЫХ, ЕСЛИ СТРОКА СУЩЕСТВУЕТ, ДАЖЕ НЕ ВСЯ
    def update_data(self):
        conn, cursor = self.open_connection()
        # cursor.execute("UPDATE feedback_main SET category = 'Вопросы по товарам' WHERE template_name_en = 'persnlOpnion';")
        cursor.execute("UPDATE feedback SET number_pressed = '0' WHERE btn_name_en = 'persnlOpnion';")
        self.close_connection(conn, cursor)

    # СТЕРЕТЬ ВСЮ СТРОКУ
    def delete_string(self,argument):
        conn, cursor = self.open_connection()
        cursor.execute("DELETE FROM feedback_main WHERE id='{}';".format(argument))
        print("+")
        self.close_connection(conn, cursor)

    def delete_table(self,argument):
        conn, cursor = self.open_connection()
        cursor.execute("DROP TABLE IF EXISTS {};".format(argument))
        print("+")
        self.close_connection(conn, cursor)
                
    def print_column(self,table, subject):
        conn, cursor = self.open_connection()
        cursor.execute("SELECT template FROM {} WHERE name_en = '{}';".format(table,subject));
        result = cursor.fetchone()
        take = result[0]
        print(take[0]) 
        self.close_connection(conn, cursor)

    
obj = postgres()

if __name__ == "__main__":
    obj = postgres()
    obj.delete_table('name')
    # obj.select_template('persnlOpnion',text_type=1)
    # obj.update_data()
    # obj.delete_string(4) # paste here your string id you want to delete


