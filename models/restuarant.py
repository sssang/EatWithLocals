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
    def get_all_by_kw(cls, keyword):
        connection = mysql.connect()
        cursor = connection.cursor()

        sql = "select * from Rest where Rest.city='{0}' or Rest.state='{0}' or Rest.country='{0}' order by rating desc".format(keyword)
        cursor.execute(sql)
        data = cursor.fetchall()

        cursor.close()
        connection.close()

        return [cls(*t) for t in data] if data else []

    @classmethod
    def get_rests_by_kw(cls, keyword, kw_country, country):
        connection = mysql.connect()
        cursor = connection.cursor()

        print keyword
        print kw_country
        print country

        if not country:
            country = kw_country

        sql = "select * from CountryRating where country=%s"
        cursor.execute(sql, (country,))
        data = cursor.fetchall()

        if not data:
            sql = "select * from Rest where Rest.city='{0}' or Rest.state='{0}' or Rest.country='{0}' order by rating desc".format(keyword)
        else:
            sql = "select * from Rest inner join CountryRating on Rest.restid=CountryRating.restid where (Rest.city='{0}' or Rest.state='{0}' or Rest.country='{0}') and CountryRating.country='{1}' order by CountryRating.rating desc".format(keyword, country)

        cursor.execute(sql)
        data = cursor.fetchall()

        cursor.close()
        connection.close()
        return [cls(*t[:12]) for t in data] if data else []

    @classmethod
    def get_rests_by_distance(cls, keyword, latitude, longitude):
        connection = mysql.connect()
        cursor = connection.cursor()

        print keyword
        print latitude
        print longitude

        sql = "select Rest.restid, Rest.restname, Rest.picurl, Rest.resttag, Rest.description, Rest.rating, Rest.address, Rest.city, Rest.state, Rest.country, Rest.created, Rest.lastupdated, 3956 * ACOS(COS(RADIANS({1})) * COS(RADIANS(RestGeo.latitude)) * COS(RADIANS({2}) - RADIANS(RestGeo.longitude)) + SIN(RADIANS({1})) * SIN(RADIANS(RestGeo.latitude))) AS distance from Rest inner join RestGeo on Rest.restid=RestGeo.restid where Rest.city='{0}' or Rest.state='{0}' or Rest.country='{0}' order by distance asc".format(keyword, latitude, longitude)
        cursor.execute(sql)
        data = cursor.fetchall()

        cursor.close()
        connection.close()
        return [cls(*t[:12]) for t in data] if data else []


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
