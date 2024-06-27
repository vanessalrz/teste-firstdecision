from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)

class Todo(db.Model):
    """
    Modelo de tarefa (Todo).

    Args:
        id (int): ID da tarefa.
        todo (str): Descrição da tarefa.
    """
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        """
        Representação da tarefa.

        Retorna:
            str: Representação da tarefa.
        """
        return f'<Todo {self.todo}>'

    def serialize(self):
        """
        Serializa a tarefa em um dicionário.

        Retorna:
            dict: Dicionário com os dados da tarefa.
        """
        return {
            'id': self.id,
            'todo': self.todo
        }


with app.app_context(): # garante que as tabelas sejam criadas no banco de dados quando o aplicativo Flask é executado.
    db.create_all()

@app.route('/api/todo', methods=['GET']) # obtem todas as tarefas
def get_todos():
    """
    Obtém todas as tarefas.

    Retorna:
        flask.Response: Resposta JSON com a lista de tarefas.
    """
    todos = Todo.query.all()
    json_list = [todo.serialize() for todo in todos]
    return jsonify(json_list)

@app.route('/api/todo/<int:todo_id>', methods=['GET']) # obtem uma tarefa pelo ID
def get_todo(todo_id):
    """
    Obtém uma tarefa pelo ID.

    Args:
        todo_id (int): ID da tarefa.

    Retorna:
        flask.Response: Resposta JSON com os dados da tarefa.
    """
    todo = Todo.query.get_or_404(todo_id)
    return jsonify({"id": todo.id, "todo": todo.todo})

@app.route('/api/todo', methods=['POST']) # cria uma nova tarefa
def add_todo():
    """
    Cria uma nova tarefa.

    Retorna:
        flask.Response: Resposta JSON com os dados da nova tarefa.
    """
    todo = request.json.get('todo')
    new_todo = Todo(todo=todo)
    db.session.add(new_todo)
    db.session.commit()
    return jsonify(new_todo.serialize()), 201

@app.route('/api/todo/<int:todo_id>', methods=['DELETE']) # deleta uma tarefa
def delete_todo(todo_id):
    """
    Deleta uma tarefa específica.

    Args:
        todo_id (int): ID da tarefa.

    Retorna:
        flask.Response: Resposta JSON com a tarefa deletada.
    """
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify(todo.serialize())

# executa o aplicativo
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
