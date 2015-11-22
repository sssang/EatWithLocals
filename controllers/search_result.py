from flask.views import MethodView
from flask import request, render_template, redirect, url_for, abort

from models.restuarant import Rest

class SearchAPI(MethodView):
    def get(self):
        keyword = request.args.get('keyword')
        rests = Rest.get_rests_by_kw(keyword)
        return render_template('search_result.html', rests=rests, keyword=keyword)

    def post(self):
        op = request.form.get('op')
        if op == 'search':
            keyword = request.form.get('keyword')
            return redirect(url_for('search_result') + '?keyword=' + keyword)
        elif op == 'sort':
            sort_by = request.form.get('sort_by')
            keyword = request.form.get('keyword')
            if sort_by == 'rating':
                rests = Rest.get_rests_by_rating(keyword)
            else:
                rests = Rest.get_rests_by_distance(keyword)
            return render_template('search_result.html', rests=rests, keyword=keyword)
        elif op == 'price':
            #need to finish
            keyword = request.form.get('keyword')
            return redirect(url_for('search_result') + '?keyword=' + keyword)
        else:
            abort(404)