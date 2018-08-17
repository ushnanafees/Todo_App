from flask import Flask, render_template, request, jsonify, url_for, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'todo_task'
app.config['MONGO_URI'] = 'mongodb://ushna:ushna25@ds123259.mlab.com:23259/todo_app'
mongo = PyMongo(app)

@app.route('/todo/api/v1.0/tasks',methods =['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/todo/api/v1.0/tasks/add', methods = ['POST'])
def add():
    todo_task = mongo.db.todo_task
    done = bool(request.form['title'] and request.form['description'])
    text = [{'title': request.form['title'],
               'description': request.form['description'], 'done' : done}]
    todo_task.insert(text)
    return redirect(url_for('find'))


@app.route('/todo/api/v1.0/tasks/find', methods =['GET'])
def find():
        emp_list = mongo.db.todo_task.find()
        #print(emp_list)
        return render_template('find.html', emp_list = emp_list)

@app.route('/todo/api/v1.0/tasks/<id>')
def delete(id):
    db = mongo.db.todo_task
    content = db.find_one({"_id" : ObjectId(id)})
    delete = db.remove(content)
    return 'done'


@app.errorhandler(404)
def not_found_error(e):
    return "URL not exist"
app.run(debug = True, port = 2000)
