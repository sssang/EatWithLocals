from flask import render_template, redirect, request, url_for
from flask.views import MethodView

from models.photo import Photo
from models.review import Review
from models.restuarant import Rest
from models.course import Course

class RestAPI(MethodView):
    def get(self):
        restid = request.args.get('id')
        rests = Rest.get_rest_object(restid)
        pics = Photo.get_rest_pics(restid)
        reviews = Review.get_rest_reviews(restid)

        for review in reviews:
            review.menu = Course.get_courses(review.revid)

        return render_template('rest_index.html', pics=pics, reviews=reviews, rests=rests)

    def post(self):
        op = request.form.get('op')
        if op == 'search':
            keyword = request.form.get('keyword')
            return redirect(url_for('search_result') + '?keyword=' + keyword)