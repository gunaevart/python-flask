from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from file import File

app = Flask(__name__)
app.secret_key = 'hello'


@app.route('/')
def index():
    db = File.Db()
    if 'Владимир' in session:
        user = session['Владимир']
    else:
        user = True
    return render_template('index.html', db=db, title='Главная страница', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user = request.form['user']
        if user == 'admin':
            session['Владимир'] = 'Владимир'
            return redirect(url_for('admin'))
    return render_template('login.html')


@app.route('/admin')
def admin():
    if 'Владимир' in session:
        user = session['Владимир']
        return render_template('admin.html', user=user)


@app.route('/test/<int:id>')
def test(id):
    db = File.Db()
    for item in db:
        if id == item['id']:
            return render_template('user.html', login=item['login'])
        else:
            return f'<h1>с id  {id} пользователь не найтен</h1>'

@app.route('/delete')
def delete_visits():
    session.pop('Владимир', None)  # удаление данных о посещениях
    return 'Visits deleted'



@app.errorhandler(404)
def page_not_founf(e):
    return render_template('404.html')


if __name__ == "__main__":
    app.run(debug=True)
