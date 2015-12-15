from flask.views import MethodView
from flask import request, render_template, redirect, url_for, abort

from models.restuarant import Rest
from models.country import CountryRating

class SearchAPI(MethodView):
    def get(self):
        keyword = request.args.get('keyword')
        if not keyword:
            return redirect(url_for('index'))

        kw = keyword.lower().split(',')

        temp = {}
        rests = Rest.get_rests_by_kw(kw[0].lstrip(), kw[len(kw)-1].lstrip(), None)
        all_rests = Rest.get_all_by_kw(kw[0].lstrip())

        for r in rests:
            temp[r.restid] = r
        for a in all_rests:
            if a.restid not in temp:
                rests.append(a)

        prices = sorted(rests, key=lambda rest: rest.price)
        lowest = prices[0].price
        highest = prices[len(prices)-1].price

        price_range = "[" + str(lowest) + "," + str(highest) + "]"

        for rest in rests:
            rest.country_rating = CountryRating.get_country_rating(rest.restid)

        return render_template('search_result.html', rests=rests, keyword=keyword, sort_by="rating",
                               price_range=price_range, lowest=lowest, highest=highest)

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
                temp = {}
                rests = Rest.get_rests_by_kw(kw[0].lstrip(), kw[len(kw)-1].lstrip(), country)
                all_rests = Rest.get_all_by_kw(kw[0].lstrip())
                for r in rests:
                    temp[r.restid] = r
                for a in all_rests:
                    if a.restid not in temp:
                        rests.append(a)
                print "range:", price_range[0]
                print "range:", price_range[1]
                for w in rests:
                    if w.price < int(price_range[0]) or w.price > int(price_range[1]):
                        rests.remove(w)
            else:
                if current_lat and current_long:
                    rests = Rest.get_rests_by_distance(kw[0].lstrip(), current_lat, current_long)
                else:
                    temp = {}
                    rests = Rest.get_rests_by_kw(kw[0].lstrip(), kw[len(kw)-1].lstrip(), None)
                    all_rests = Rest.get_all_by_kw(kw[0].lstrip())

                    for r in rests:
                        temp[r.restid] = r
                    for a in all_rests:
                        if a.restid not in temp:
                            rests.append(a)
                    for w in rests:
                        if w.price < int(price_range[0]) or w.price > int(price_range[1]):
                            rests.remove(w)

            for rest in rests:
                rest.country_rating = CountryRating.get_country_rating(rest.restid)

            return render_template('search_result.html', rests=rests, keyword=keyword,
                                   sort_by=sort_by, country=country,
                                   price_range='['+price_range[0]+','+ price_range[1]+']',
                                   lowest=int(price_range[0]),highest=int(price_range[1]))
        else:
            abort(404)