from flask.views import MethodView
from flask import render_template, request, redirect, url_for

class IndexAPI(MethodView):
    def get(self):
        return render_template('index.html')

    def post(self):
        op = request.form.get('op')
        if op == 'search':
            keyword = request.form.get('keyword')
            return redirect(url_for('search_result') + '?keyword=' + keyword)