from flask import Flask
from flask import render_template, redirect
from data.protection import LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def preparation(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def job(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<list>')
def job_list(list):
    return render_template("job_list.html", list_type=list)


@app.route('/answer')
@app.route('/auto_answer')
def form_answer():
    information = {"title": "Анкета",
                   "surname": "Watny",
                   "name": "Mark",
                   "education": "выше среднего",
                   "profession": "штурман марсохода",
                   "sex": "male",
                   "motivation": "Всегда мечтал застрять на Марсе!",
                   "ready": "True"}
    return render_template("auto_answer.html", dictionary=information, title=information["title"])


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('protection.html', title='Аварийный доступ', form=form)


@app.route('/distribution')
def distribution():
    people = ["Ридли Скотт", "Энди Уир", "Марк Уотни", "Венката Капур", "Тедди Сандерс", "Шон Бин"]
    return render_template('distribution.html', crew=people)


@app.route("/table/<sex>/<age>")
def table(sex, age):
    return render_template("table.html", sex=sex, age=int(age))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
