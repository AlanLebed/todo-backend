from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
CORS(app)

class TodoModel(db.Model):
	id = db.Column(db.String(36), primary_key=True)
	text = db.Column(db.String(240), nullable=False)
	done = db.Column(db.Boolean, nullable=False)
	important = db.Column(db.Boolean, nullable=False)
	deadline  = db.Column(db.DateTime(timezone=True), nullable=True)
	
	def __repr__(self):
		return f"Todo(id = {self.id})"

with app.app_context():
    db.create_all()

todo_put_args = reqparse.RequestParser()
todo_put_args.add_argument("id", type=str, help="Id is required", required=True)
todo_put_args.add_argument("text", type=str, help="Text is required", required=True)
todo_put_args.add_argument("done", type=bool, help="Done Flag required", required=True)
todo_put_args.add_argument("important", type=bool, help="Important Flag required", required=True)
todo_put_args.add_argument("deadline", type=str, help="Deadline required", required=True)

todo_update_args = reqparse.RequestParser()
todo_update_args.add_argument("id", type=str, help="Id is required", required=True)
todo_update_args.add_argument("text", type=str, help="Text is required")
todo_update_args.add_argument("option", type=str, help="Update option required")

todo_delete_args = reqparse.RequestParser()
todo_delete_args.add_argument("id", type=str, help="Id is required", required=True)

resource_fields = {
	'id': fields.String,
	'text': fields.String,
	'done': fields.Boolean,
	'important': fields.Boolean,
	'deadline': fields.DateTime
}

class Todo(Resource):
	@marshal_with(resource_fields)
	def get(self):
		return TodoModel.query.all()
	

	@marshal_with(resource_fields)
	def post(self):
		args = todo_put_args.parse_args()
		format = "%d/%m/%Y"
		todo = TodoModel(id=args['id'], text=args['text'], done=args['done'], important=args['important'], deadline=datetime.strptime(args['deadline'], format))
		
		db.session.add(todo)
		db.session.commit()

		return todo, 201

	@marshal_with(resource_fields)
	def patch(self):
		args = todo_update_args.parse_args()
		result = TodoModel.query.filter_by(id=args['id']).first()
		if not result:
			abort(404, message="Id doesn't exist, cannot update")

		if args['text']:
			result.text = args['text']
		if args['option'] == "done":
			result.done = not result.done
		if args['option'] == "important":
			result.important = not result.important

		db.session.commit()

		return result

	@marshal_with(resource_fields)
	def delete(self):
		args = todo_delete_args.parse_args()
		result = TodoModel.query.filter_by(id=args['id']).first()
		if not result:
			abort(404, message="Could not find that id")
		
		db.session.delete(result)
		db.session.commit()
		
		return '', 204
	
	
		
api.add_resource(Todo, "/todo")

if __name__ == "__main__":
	app.run(host='localhost', port=5000, debug=False)