from models import mysql

class Rest(object):
    def __init__(self, restid=None, restname=None, picurl=None, resttag=None, rating=None,
                 address=None, place=None, created=None, updated=None):
        self.restid=restid
        self.restname=restname
        self.picurl=picurl
        self.resttag=resttag
        self.rating=rating
        self.address=address
        self.place=place
        self.created=created
        self.updated=updated

    @classmethod
    def get_rests_by_kw(cls, keyword):
        connection = mysql.connect()
        cursor = connection.cursor()

        sql = "select * from Rest where place=%s"
        cursor.execute(sql, (keyword,))
        data = cursor.fetchall()

        cursor.close()
        connection.close()
        return [cls(*t) for t in data] if data else []

    @classmethod
    def update_rating(cls, rating, restid):
        connection = mysql.connect()
        cursor = connection.cursor()

        sql = "update Rest set rating=%s where restid=%s"
        cursor.execute(sql, (rating, restid))
        connection.commit()

        cursor.close()
        connection.close()