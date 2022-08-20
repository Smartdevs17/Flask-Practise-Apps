from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:testpassword@localhost:5432/todoDB'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Todo(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer,primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean,nullable=False,default=False)
    list_id = db.Column(db.Integer, db.ForeignKey("todolists.id"), nullable=False)
    
    def __repr__(self):
        return f'<Todo id={self.id} name={self.name} >'
 
class TodoList(db.Model):
    __tablename__ = "todolists"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    todos = db.relationship("Todo", backref='list', lazy=True)
    
# db.create_all()
@app.route("/")
def index():
    return "Welcome to my todo app"
