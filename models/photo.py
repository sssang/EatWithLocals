from models import mysql

class Photo(object):
    def __init__(self, picid=None, url=None, created=None):
        self.picid = picid
        self.url = url
        self.created = created

    @classmethod
    def get_rest_pics(cls, restid):
        connection = mysql.connect()
        cursor = connection.cursor()

        sql = "select Photo.picid, Photo.url, Photo.created from Photo inner join PhotoContain on Photo.picid=PhotoContain.picid where PhotoContain.restid=%s order by PhotoContain.sequencenum asc"
        cursor.execute(sql, (restid,))
        data = cursor.fetchall()

        cursor.close()
        connection.close()

        return [cls(*t) for t in data] if data else []