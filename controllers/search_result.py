from flask.views import MethodView
from flask import request, render_template, redirect, url_for, abort

from models.restuarant import Rest

class SearchAPI(MethodView):
    def get(self):
        keyword = request.args.get('keyword')
        if not keyword:
            return redirect(url_for('index'))
            
        kw = keyword.lower().split(',')
        rests = Rest.get_rests_by_kw(kw[0])
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
            country = request.form.get('country')
            current_lat = request.form.get('current_lat')
            current_long = request.form.get('current_long')

            if not keyword:
                return redirect(url_for('index'))

            kw = keyword.lower().split(',')
            if sort_by == 'rating':
                if country:
                    rests = Rest.get_rests_by_rating(kw[0], country)
                else:
                    rests = Rest.get_rests_by_kw(kw[0])
            else:
                if current_lat and current_long:
                    rests = Rest.get_rests_by_distance(kw[0], current_lat, current_long)
                else:
                    rests = Rest.get_rests_by_kw(kw[0])

            return render_template('search_result.html', rests=rests, keyword=keyword, sort_by=sort_by,
                                   price_range=price_range[0]+','+price_range[1])
        else:
            abort(404)