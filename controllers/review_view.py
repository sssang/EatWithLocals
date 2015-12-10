from flask.views import MethodView
from flask import render_template, redirect, url_for, request

from models.restuarant import Rest
from models.review import Review

class ReviewAPI(MethodView):
    def get(self):
        restid = request.args.get('id')
        rests = Rest.get_rest_object(restid)

        return render_template('review.html', rests=rests)

    def post(self):
        op = request.form.get('op')
        if op == 'search':
            keyword = request.form.get('keyword')
            return redirect(url_for('search_result')+'?keyword='+keyword)
        elif op == 'review':
            restid = request.form.get('restid')
            rating = request.form.get('rating')
            content = request.form.get('review_content')
            country = request.form.get('country')

            Review.insert(restid, rating, content, country)
            return redirect(url_for('rest_index')+'?id='+restid)