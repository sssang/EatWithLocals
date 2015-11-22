from flask import Flask, render_template

from controllers.index_view import IndexAPI
from controllers.search_result import SearchAPI
from controllers.rest_view import RestAPI

from models import mysql

app = Flask(__name__, template_folder='views')

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'ewl'

mysql.init_app(app)

app.add_url_rule('/', view_func=IndexAPI.as_view('index'))
app.add_url_rule('/search', view_func=SearchAPI.as_view('search_result'))
app.add_url_rule('/restuarant', view_func=RestAPI.as_view('rest_index'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)

