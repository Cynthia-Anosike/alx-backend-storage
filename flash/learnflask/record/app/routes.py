from app import app
from flask import render_template, request, flash
from app.models import db


@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/index', methods = ['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        if not request.form['first_name'] or not request.form['last_name'] or not request.form['department'] or not request.form['email'] or not request.form['email'] or not request.form['Addr'] or not request.form['pin']:
            flash("Please input valid value for all fields", "error")
        else:
            student = students(request.form['first_name'], request.form['last_name'], request.form['department'], request.form['email'], request.form['email'], request.form['Addr'], request.form['pin'])
            db.session.add(student)
            db.session.commit()
            flash("Record was successfully added")
            return redirect(url_for('home.html'))
    
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
