from models import mysql

class Review(object):
    def __init__(self, revid=None, rating=None, content=None, created=None, lastupdated=None):
        self.revid = revid
        self.rating = rating
        self.content = content
        self.created = created,
        self.lastupdated = lastupdated

    @classmethod
    def get_rest_reviews(cls, restid):
        connection = mysql.connect()
        cursor = connection.cursor()

        sql = "select Review.revid, Review.rating, Review.content, Review.created, Review.lastupdated from Review inner join ReviewContain on Review.revid=ReviewContain.revid where ReviewContain.restid=%s order by Review.lastupdated desc"
        cursor.execute(sql, (restid,))
        data = cursor.fetchall()

        cursor.close()
        connection.close()
        return [cls(*t) for t in data] if data else []