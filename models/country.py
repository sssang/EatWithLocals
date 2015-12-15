from models import mysql

class CountryRating(object):
    def __init__(self, restid=None, rating=None, country=None):
        self.restid = restid
        self.rating = rating
        self.country = country

    @classmethod
    def get_country_rating(cls, restid):
        connection = mysql.connect()
        cursor = connection.cursor()

        sql = "select * from CountryRating where restid=%s"
        cursor.execute(sql, (restid,))
        data = cursor.fetchall()

        cursor.close()
        connection.close()

        return [cls(t[0], t[1], t[2].title()) for t in data] if data else None