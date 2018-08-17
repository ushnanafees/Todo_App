from flask import Flask, render_template, jsonify , json, session, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///tododb.db'

database = SQLAlchemy(app)

class Todo_App(database.Model):
    id = database.Column(database.Integer , primary_key=True)
    title = database.Column(database.String(20))
    description = database.Column(database.String(100))
    done = database.Column(database.Boolean)

database.create_all() # creating tables

@app.route('/todo/api/v1.0/task/add' , methods=['POST'])
def add():
    add = request.get_json()
    add_task =Todo_App(title=add['title'],
                       description=add['description'],
                       done=True)
    database.session.add(add_task) # insert data query
    database.session.commit()
    return jsonify ({'prompt':'Added'})

@app.route('/todo/api/v1.0/task/view' , methods=['GET'])
def view_task():
    tasks = Todo_App.query.all() #use for view the data
    view=[]
    for task in tasks:
        task_list={}
        task_list['id']=task.id
        task_list['title']=task.title
        task_list['description']=task.description
        task_list['done'] = task.done
        view.append(task_list)
    return jsonify({'task':view})

@app.route('/todo/api/v1.0/task/delete/<int:id>', methods=['DELETE'])
def delete(id):
    tasks = Todo_App.query.filter_by(id=id).first() # first karwa rae id s
    if not tasks:
        return jsonify({'prompt': 'Empty'})
    else:
        database.session.delete(tasks) # delete query
        database.session.commit()
    return jsonify({'prompt':'Deleted'})

app.run(debug=True ,port=8000)