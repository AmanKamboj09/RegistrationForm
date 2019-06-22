from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/dellsoft'
db = SQLAlchemy(app)

class stud(db.Model):
    name = db.Column(db.String(50), nullable=False)
    contact = db.Column(db.Integer, primary_key=True)
    emailid = db.Column(db.String(50), nullable=False)
    college = db.Column(db.String(50), nullable=False)
    year = db.Column(db.String(10), nullable=False)
    startdate = db.Column(db.String(20), nullable=False)
    enddate = db.Column(db.String(20), nullable=False)
    course = db.Column(db.String(100), nullable=False)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/", methods = ['GET', 'POST'])
def reg():
    if(request.method=='POST'):
        '''Add entry to the database'''
        name = request.form.get('name')
        contact = request.form.get('contact')
        emailid = request.form.get('emailid')
        college = request.form.get('college')
        year = request.form.get('year')
        startdate = request.form.get('startdate')
        enddate = request.form.get('enddate')
        course = request.form.get('course')

        entry = stud(name=name, contact=contact, emailid=emailid, college=college,year=year, startdate=startdate, enddate=enddate, course=course )

        db.session.add(entry)
        db.session.commit()

    return render_template('index.html')


app.run(debug=True)

