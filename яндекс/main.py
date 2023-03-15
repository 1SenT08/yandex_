from flask import Flask, url_for
from random import choice

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Миссия Колонизация Марса</h1>"

@app.route('/index')
def countdown():
    return '<h1>И на Марсе будут яблони цвести!</h1>'


@app.route('/promotion')
def promation():
    countdown_list = ['<h1>Человечество вырастает из детства.</h1>', '<h1>Человечеству мала одна планета.</h1>',
                      '<h1>Мы сделаем обитаемыми безжизненные пока планеты.</h1>', '<h1>И начнем с Марса!</h1>',
                      '<h1>Присоединяйся!</h1>']
    return '</br>'.join(countdown_list)


@app.route('/image_mars')
def im():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/Без названия (3).jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                    <p>Вот она какая, красная планета.</p>
                  </body>
                </html>'''


@app.route('/promotion_image')
def imf():
    lst_sents = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
                 "Мы сделаем обитаемые безжизненые пока планеты.", "И начнем с Марса!", "Присоединяйся!"]
    lst_alert = ['alert-primary', 'alert-success', 'alert-danger', 'alert-warning']

    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/Без названия (3).jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert {choice(lst_alert)}" role="alert">
                      {lst_sents[0]}
                    </div>
                    <div class="alert {choice(lst_alert)}" role="alert">
                      {lst_sents[1]}
                    </div>
                    <div class="alert {choice(lst_alert)}" role="alert">
                      {lst_sents[2]}
                    </div>
                    <div class="alert {choice(lst_alert)}" role="alert">
                      {lst_sents[3]}
                    </div>
                    <div class="alert {choice(lst_alert)}" role="alert">
                      {lst_sents[4]}
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
