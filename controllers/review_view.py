from flask.views import MethodView
from flask import render_template, redirect, url_for, request

from models.restuarant import Rest

class ReviewAPI(MethodView):
    def get(self):
        restid = request.args.get('id')
        rests = Rest.get_rest_object(restid)

        return render_template('review.html', rests=rests)
        
    def post(self):
        pass