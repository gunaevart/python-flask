from flask import Flask, render_template, request, jsonify, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'hello'

@app.route('/')
def index():
    return render_template('index.html', title='Главная страница')


@app.route('/login', methods=['POST'])
def login():
    if request.method == "POST":
        user = request.form['user']
        if user == 'admin':
            session['Владимир'] = user
            return redirect(url_for('admin'))
    return render_template('login.html')


@app.route('/admin')
def admin():
    if 'Владимир' in session:
        user = session['Владимир']
        return render_template('admin.html', user=user)


@app.route('/test', methods=['GET'])
def test():
    lang = [{'name': 'java'}, {'name': 'python'}, {'name': 'PHP'}]
    return jsonify({'massenges': lang[0]})


@app.errorhandler(404)
def page_not_founf(e):
    return render_template('404.html')


if __name__ == "__main__":
    app.run(debug=True)
