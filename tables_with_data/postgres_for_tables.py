import psycopg2

class CursorAndConnect():

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

    def delete_table(self,argument):
        conn, cursor = self.open_connection()
        cursor.execute("DROP TABLE IF EXISTS {};".format(argument))
        print("+")
        self.close_connection(conn, cursor)

    def delete_string(self,table,number):
        conn, cursor = self.open_connection()
        cursor.execute("DELETE FROM {} WHERE id = '{}';".format(table,number))
        print("striing deleted"); self.close_connection(conn, cursor)
    
    def add_string(self,table,columns,values):
        conn, cursor = self.open_connection()
        cursor.execute("INSERT INTO {} ({}) VALUES ({});".format(table,columns,values))
        print("string added"); self.close_connection(conn, cursor)
                
                

    def print_column(self,table, subject):
        conn, cursor = self.open_connection()
        cursor.execute("SELECT template FROM {} WHERE name_en = '{}';".format(table,subject));
        result = cursor.fetchone()
        take = result[0]
        print(take) 
        self.close_connection(conn, cursor)

obj = CursorAndConnect()

if __name__ == "__main__":
    obj = CursorAndConnect()
    obj.test_func()