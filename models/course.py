from models import mysql

class Course(object):
    def __init__(self, course_name=None, course_content=None):
        self.course_name = course_name
        self.course_content = course_content

    @classmethod
    def insert_course(cls, menuid, course_name, course_content):
        connection = mysql.connect()
        cursor = connection.cursor()

        sql = "insert into Course(menuid, course_name, course_content) values(%s, %s, %s)"
        cursor.execute(sql, (menuid, course_name, course_content))
        connection.commit()

        cursor.close()
        connection.close()

    @classmethod
    def get_courses(cls, revid):
        connection = mysql.connect()
        cursor = connection.cursor()

        sql = "select Course.course_name, Course.course_content from Course inner join Menu where Menu.menuid=Course.menuid and Menu.revid=%s"
        cursor.execute(sql, (revid,))
        data = cursor.fetchall()

        cursor.close()
        connection.close()
        return [cls(*t) for t in data] if data else None