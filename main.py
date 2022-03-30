from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
import os
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask('MyApp')
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def func1(title):
    return render_template('index.html', title=title)


@app.route('/training/<prof>')
def func2(prof):
    return render_template('prof.html', prof=prof)


@app.route('/list_prof/<list>')
def func3(list):
    l_prof = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог',
              'врач', 'инженер по терраформированию', 'климатолог',
              'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
              'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода',
              'киберинженер', 'штурман', 'пилот дронов']
    return render_template('list.html', ll=list, lp=l_prof)


@app.route('/answer', methods=['POST', 'GET'])
@app.route('/auto_answer', methods=['POST', 'GET'])
def func4():
    if request.method == 'GET':
        return render_template('form_answer.html')
    elif request.method == 'POST':
        try:
            _ = request.form['ready']
            answer_dict = {'surname': request.form['surname'],
                           'name': request.form['name'], 'education': request.form['education'],
                           'profession': request.form['profession'], 'sex': request.form['sex'],
                           'motivation': request.form['motivation'], 'ready': 'True'}
            return render_template('dict_answer.html', dict=answer_dict)
        except Exception as ev:
            answer_dict = {'surname': request.form['surname'],
                           'name': request.form['name'], 'education': request.form['education'],
                           'profession': request.form['profession'], 'sex': request.form['sex'],
                           'motivation': request.form['motivation'], 'ready': 'False'}
            return render_template('dict_answer.html', dict=answer_dict)


class LoginForm(FlaskForm):
    username = StringField('Id астронавта', validators=[DataRequired()])
    password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    username1 = StringField('Id капитана', validators=[DataRequired()])
    password1 = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route('/login', methods=['GET', 'POST'])
def func5():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/success')
def success():
    return 'Форма отправлена'


@app.route('/distribution')
def func6():
    astronauts = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Бин']
    return render_template('distribution.html', list=astronauts)


@app.route('/table/<male>/<int:age>')
def func7(male, age):
    return render_template('table.html', male=male, age=age)


photos = ['/static/img/s.jpg', '/static/img/t.jpg']


@app.route('/galery', methods=['POST', 'GET'])
def func8():
    global photos
    if request.method == 'GET':
        return render_template('galery.html', photos=photos)
    elif request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        if filename:
            file.save(f'static/img/{filename}')
            photos.append(f'static/img/{filename}')
        return render_template('galery.html', photos=photos)


app.run(port=8080, host='127.0.0.1', debug=True)
