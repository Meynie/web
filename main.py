from flask import Flask, render_template, request, url_for, flash, session, redirect, abort, g

from DB import create_db, DBHelper

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fsdfsdf'


menu = [{"name": "Главная", "url": "/"},
        {"name": "Профиль", "url": "profile"},
        {"name": "О сайте", "url": "about"},
        {"name": "Обратная связь", "url": "contact"},
        {"name": "Регистрация", "url": "login"},
        {"name": "Выход", "url": "exit"}]


@app.route('/')
def main_page():
    db = create_db()
    dbase = DBHelper(db)
    return render_template('main_page.html', the_title='Welcome to main page!', menu = menu)


# @app.route('/about')
# def about():
#     return 'Тут будет информация о сайте'


@app.route('/counter', methods=['POST'])
def counter():
    # if request.method == 'POST':
    return render_template('counter.html', the_title='Давай посчитаем')


@app.route('/contact', methods=['POST', 'GET'])
def contact():

    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено', category='success')
        else:
            flash('Ошибка отправки', category='error')

    return render_template('contact.html', title='Обратная связь', menu=menu)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'admin' and request.form['psw'] == '123':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('login.html', title='Авторизация', menu=menu)


@app.route('/profile/<username>')
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return render_template('profile.html', username=username, menu=menu)


@app.route('/profile/exit')
@app.route('/exit')
def ex_session():
    if 'userLogged' in session:
        session.pop('userLogged')
        return 'Вы вышли'
    else:
        return render_template('main_page.html', menu=menu)
    # session.pop('userLogged')
    # return render_template('main_page.html', menu=menu)


@app.errorhandler(404)
def pageNotFount(error):
    return render_template('page404.html', title="Страница не найдена", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
