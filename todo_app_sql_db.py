from flask import Flask, render_template, jsonify , json, session, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']='postgres://nwabmkhn:Ckfn-9UibDBRM1zM3Zji-WfQsSIyYSCc@pellefant.db.elephantsql.com:5432/nwabmkhn'

database = SQLAlchemy(app)

class Todo_App(database.Model):
    __tablename__ = 'todo'
    id = database.Column(database.Integer , primary_key=True)
    title = database.Column(database.String(20))
    description = database.Column(database.String(100))
    done = database.Column(database.Boolean)

database.create_all() # creating tables

@app.route('/todo/api/v1.0/task/add' , methods=['POST'])
def add():              # add function.
    added = request.get_json()
    add_task = Todo_App(title = added['title'],
                       description= added['description'],
                       done = True)
    database.session.add(add_task) # insert data query
    database.session.commit()
    return jsonify({'prompt':'Added'}) # return data in jsonify format

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
def delete(id):          # delete
    todo_tasks = Todo_App.query.filter_by(id=id).first()
    if not todo_tasks:
        return jsonify({'prompt': 'Empty'})
    else:
        database.session.delete(todo_tasks) # delete query
        database.session.commit()
    return jsonify({'prompt':'Deleted'})

@app.route('/todo/api/v1.0/task/update/<id>', methods=['PUT'])
def update(id):   #update function
    tasks = Todo_App.query.filter_by(id=id).first()
    if not tasks:
        return jsonify({'message': 'Empty Dictionary'})
    data = request.get_json()
    tasks.done = True
    tasks.title = data['title']
    tasks.description = data['description']

    task_list={}
    task_list['id']=tasks.id
    task_list['title']=tasks.title
    task_list['description']=tasks.description
    task_list['done'] = tasks.done
    database.session.commit()
    return jsonify(task_list)


app.run(debug=True ,port=8000)