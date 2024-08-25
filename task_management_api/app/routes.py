from flask import request, jsonify
from flask_jwt_extended import create_access_token
from .models import User, Task
from . import db
import jwt
import datetime


def register_routes(app):
    @app.route('/test', methods=['GET', 'POST'])
    def test():
        return jsonify({'message': 'Test endpoint is working'}), 200

    @app.route('/api/register', methods=['POST'])
    def register():
        # Ensure the request's content type is application/json
        if request.content_type != 'application/json':
            return jsonify({'message': 'Content-Type must be application/json'}), 415

        data = request.get_json()

        # Validate that JSON data was provided
        if data is None:
            return jsonify({'message': 'Invalid JSON'}), 400

        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'message': 'Username and password are required'}), 400

        if User.query.filter_by(username=username).first():
            return jsonify({'message': 'User already exists'}), 400

        new_user = User(username=username)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully'}), 201

    @app.route('/api/login', methods=['POST'])
    def login():
        data = request.get_json()

        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username=username).first()

        if user is None or not user.check_password(password):
            return jsonify({'message': 'Invalid username or password'}), 401

        # Create JWT token
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, app.config['JWT_SECRET_KEY'], algorithm='HS256')

        return jsonify({'access_token': token}), 200

    @app.route('/api/tasks', methods=['POST'])
    def create_task():
        data = request.get_json()

        title = data.get('title')
        description = data.get('description')
        status = data.get('status')
        priority = data.get('priority')
        due_date = data.get('due_date')
        user_id = data.get('user_id')  # Make sure user_id is included in the request

        new_task = Task(
            title=title,
            description=description,
            status=status,
            priority=priority,
            due_date=due_date,
            user_id=user_id
        )

        db.session.add(new_task)
        db.session.commit()

        return jsonify({'message': 'Task created successfully'}), 201

    @app.route('/api/tasks', methods=['GET'])
    def get_tasks():
        tasks = Task.query.all()
        return jsonify([task.to_dict() for task in tasks]), 200

    @app.route('/api/tasks/<int:task_id>', methods=['PUT'])
    def update_task(task_id):
        data = request.get_json()

        task = Task.query.get(task_id)
        if not task:
            return jsonify({'message': 'Task not found'}), 404

        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.status = data.get('status', task.status)
        task.priority = data.get('priority', task.priority)
        task.due_date = data.get('due_date', task.due_date)

        db.session.commit()

        return jsonify({'message': 'Task updated successfully'}), 200

    @app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
    def delete_task(task_id):
        task = Task.query.get(task_id)
        if not task:
            return jsonify({'message': 'Task not found'}), 404

        db.session.delete(task)
        db.session.commit()

        return jsonify({'message': 'Task deleted successfully'}), 200


