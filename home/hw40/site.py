from flask import Flask, render_template, url_for

app = Flask(__name__)

menu = [
    {"name": "Главная", "url": "main"},
    {"name": "Новости", "url": "news"},
    {"name": "Инфо", "url": "info"},
]


@app.route("/")
@app.route("/main")
def main():
    print(url_for('main'))
    return render_template('main.html', title="Главная", menu=menu)


@app.route("/news")
def news():
    print(url_for('news'))
    return render_template('news.html', title="Новости", menu=menu)


@app.route("/info")
def info():
    print(url_for('info'))
    return render_template('info.html', title="Инфо", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)

