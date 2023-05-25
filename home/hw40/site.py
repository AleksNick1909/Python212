# from flask import Flask, render_template, url_for, request, flash, session, redirect, g
# import os
# import sqlite3
# from FDataBase import FDataBase
#
# DATABASE = '/tmp/hw.db'
# DEBUG = True
# SECRET_KEY = 'a4aa26c7aeb356766843c5308ce00cf518c41c3b'
#
# app = Flask(__name__)
#
# app.config.from_object(__name__)
#
# app.config.update(dict(DATABASE=os.path.join(app.root_path, 'hw.db')))
#
#
# def connect_db():
#     con = sqlite3.connect(app.config['DATABASE'])
#     con.row_factory = sqlite3.Row
#     return con
#
#
# def create_db():
#     db = connect_db()
#     with app.open_resource('sq_db.sql', mode="r") as f:
#         db.cursor().executescript(f.read())
#     db.commit()
#     db.close()
#
#
# menu = [
#     {"name": "Главная", "url": "main"},
#     {"name": "Новости", "url": "news"},
#     {"name": "Инфо", "url": "info"},
# ]
#
#
# def get_db():
#     if not hasattr(g, 'link_db'):
#         g.link_db = connect_db()
#     return g.link_db
#
#
# @app.route("/")
# @app.route("/main")
# def main():
#     print(url_for('main'))
#     db = get_db()
#     dbase = FDataBase(db)
#     return render_template('main.html', title="Главная", menu=dbase.get_menu(), posts=dbase.get_posts_anonce())
#
#
# @app.route("/add_post", methods=["POST", "GET"])
# def add_post():
#     db = get_db()
#     dbase = FDataBase(db)
#
#     if request.method == 'POST':
#         if len(request.form['name']) > 4 and len(request.form['post']) > 10:
#             res = dbase.add_post(request.form['name'], request.form['post'], request.form['price'])
#             if not res:
#                 flash('Ошибка добавления курса', category='error')
#             else:
#                 flash('Курс добавлен успешно', category='success')
#         else:
#             flash('Ошибка добавления курса', category='error')
#     return render_template('add_post.html', title="Добавление курса", menu=dbase.get_menu())
#
#
# @app.route("/post/<int:id_post>")
# def show_post(id_post):
#     db = get_db()
#     dbase = FDataBase(db)
#     title, post, price = dbase.get_post(id_post)
#     return render_template('post.html', title=title, post=post, price=price, menu=dbase.get_menu())
#
#
# @app.route("/news")
# def news():
#     print(url_for('news'))
#     db = get_db()
#     dbase = FDataBase(db)
#     return render_template('news.html', title="Новости", menu=dbase.get_menu())
#
#
# @app.route("/info")
# def info():
#     print(url_for('info'))
#     db = get_db()
#     dbase = FDataBase(db)
#     return render_template('info.html', title="Инфо", menu=dbase.get_menu())
#
#
# @app.errorhandler(404)
# def page_not_found(error):
#     db = get_db()
#     dbase = FDataBase(db)
#     return render_template('page404.html', title="Страница не найдена", menu=dbase.get_menu())
#
#
# @app.teardown_appcontext
# def close_db(error):
#     if hasattr(g, 'link_db'):
#         g.link_db.close()
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
