from models import mysql

class Review(object):
    def __init__(self, revid=None, rating=None, country=None,content=None, created=None, lastupdated=None):
        self.revid = revid
        self.rating = rating
        self.content = content
        self.created = created,
        self.lastupdated = lastupdated
        self.country=country

    @classmethod
    def get_rest_reviews(cls, restid):
        connection = mysql.connect()
        cursor = connection.cursor()

        sql = "select Review.revid, Review.rating,Review.country, Review.content, Review.created, Review.lastupdated from Review inner join ReviewContain on Review.revid=ReviewContain.revid where ReviewContain.restid=%s order by Review.lastupdated desc"
        cursor.execute(sql, (restid,))
        data = cursor.fetchall()

        cursor.close()
        connection.close()
        return [cls(t[0], t[1], t[2].title(), t[3], t[4], t[5]) for t in data] if data else []

    @classmethod
    def insert(cls, restid, rating, content, country):
        country = country.lower()
        connection = mysql.connect()
        cursor = connection.cursor()

        sql = "insert into Review(rating, content, country) values (%s, %s, %s)"
        cursor.execute(sql, (rating, content, country))
        connection.commit()

        cursor.execute("select revid from Review order by revid desc")
        revid = cursor.fetchall()
        revid = revid[0][0]

        cursor.execute("select sequencenum from ReviewContain where restid=%s order by sequencenum desc"%restid)
        sn = cursor.fetchall()
        sn = sn[0][0]+1 if sn else 1

        sql = "insert into ReviewContain(restid, revid, sequencenum) values (%s, %s, %s)"
        cursor.execute(sql, (restid, revid, sn))
        connection.commit()

        sql = "select rating from CountryRating where restid=%s and country=%s"
        cursor.execute(sql, (restid, country))
        data = cursor.fetchall()
        if not data:
            rating_new = rating
            sql = "insert into CountryRating(rating, restid, country) values (%s, %s, %s)"
        else:
            rating_new = (float(data[0][0]) + float(rating))*0.5
            sql = "update CountryRating set rating=%s where restid=%s and country=%s"

        cursor.execute(sql, (rating_new, restid, country))
        connection.commit()

        cursor.close()
        connection.close()
        return revid

