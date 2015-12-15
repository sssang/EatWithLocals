from models import mysql

class Menu(object):
    def __init__(self, menuid=None, restid=None, revid=None):
        self.menuid = menuid
        self.restid = restid
        self.revid = revid

    @classmethod
    def insert_menu(cls, restid, revid):
        connection = mysql.connect()
        cursor = connection.cursor()

        sql = "insert into Menu(restid, revid) values (%s, %s)"
        cursor.execute(sql, (restid, revid))
        connection.commit()

        cursor.execute("select menuid from Menu order by menuid desc")
        menuid = cursor.fetchall()
        menuid = menuid[0][0]

        cursor.close()
        connection.close()
        return menuid