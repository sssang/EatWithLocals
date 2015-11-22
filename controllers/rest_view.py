from flask import render_template, redirect, request, url_for
from flask.views import MethodView

from models.pic import Pic
from models.review import Review

class RestAPI(MethodView):
    def get(self):
        restname = request.args.get('restname')
        pics = Pic.get_rest_pics(restname)
        reviews = Review.get_rest_reviews(restname)
        return render_template('rest_index.html', pics=pics, reviews=reviews)

    def post(self):
        op = request.form.get('op')
        if op == 'search':
            keyword = request.form.get('keyword')
            return redirect(url_for('search_result') + '?keyword=' + keyword)