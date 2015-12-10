from models import mysql

class Rest(object):
    def __init__(self, restid=None, restname=None, picurl=None, resttag=None,description=None, rating=None,
                 address=None, city=None,state=None,country=None, created=None, lastupdated=None):
        self.restid=restid
        self.restname=restname
        self.picurl=picurl
        self.resttag=resttag
        self.description=description
        self.rating=rating
        self.address=address
        self.city=city
        self.state=state
        self.country=country
        self.created=created
        self.lastupdated=lastupdated

    @classmethod
    def get_rests_by_kw(cls, keyword):
        connection = mysql.connect()
        cursor = connection.cursor()

        sql = "select * from Rest where city=%s"
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

    @classmethod
    def get_rest_object(cls, restid):
        connection = mysql.connect()
        cursor = connection.cursor()

        sql = "select * from Rest where restid=%s"
        cursor.execute(sql,(restid,))
        data = cursor.fetchall()

        cursor.close()
        connection.close()
        return [cls(*t) for t in data] if data else []
