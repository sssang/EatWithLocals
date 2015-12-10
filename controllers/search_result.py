from flask.views import MethodView
from flask import request, render_template, redirect, url_for, abort

from models.restuarant import Rest

class SearchAPI(MethodView):
    def get(self):
        keyword = request.args.get('keyword')
        rests = Rest.get_rests_by_kw(keyword)
        return render_template('search_result.html', rests=rests, keyword=keyword, sort_by="rating")

    def post(self):
        op = request.form.get('op')
        if op == 'search':
            keyword = request.form.get('keyword')
            return redirect(url_for('search_result') + '?keyword=' + keyword)
        elif op == 'update':
            price_range = request.form.get('p_range').split(',')
            sort_by = request.form.get('sort_by')
            keyword = request.form.get('keyword')

            if sort_by == 'rating':
                rests = Rest.get_rests_by_rating(keyword, int(price_range[0]), int(price_range[1]))
            else:
                rests = Rest.get_rests_by_distance(keyword, int(price_range[0]), int(price_range[1]))
            return render_template('search_result.html', rests=rests, keyword=keyword, sort_by=sort_by,
                                   price_range=price_range[0]+','+price_range[1])
        else:
            abort(404)