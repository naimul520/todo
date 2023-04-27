from app import app,db
from Schema import todo_schema as sh
from flask import render_template,request,redirect
@app.route('/', methods=["GET","POST"])
def index():
    if request.method=="POST":
       todo = sh.Todo(title=request.form['title'],desc = request.form['desc'])
       db.session.add(todo)
       db.session.commit()
       return redirect("/")
       
    todo = sh.Todo.query.all()
    return render_template("index.html",todo = todo)

@app.route('/delete/<int:id>')
def delete(id):
    todo = sh.Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

@app.route('/edit/<id>',methods=["GET","POST"])
def update(id):
    if request.method=="POST":
        todo = sh.Todo.query.filter_by(id=id).first()
        todo.title = request.form['title']
        todo.desc = request.form['desc']
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
    todo = sh.Todo.query.filter_by(id=id).first()
    return render_template("update.html",todo = todo)

