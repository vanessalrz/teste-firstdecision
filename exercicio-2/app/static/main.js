document.addEventListener('DOMContentLoaded', () => {
    const taskForm = document.getElementById('task-form');
    const taskInput = document.getElementById('task-input');
    const tasksList = document.getElementById('tasks');

    taskForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const task = taskInput.value;
        const response = await fetch('/tasks', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ task }),
        });
        const data = await response.json();
        addTaskToList(data.task);
        taskInput.value = '';
    });

    tasksList.addEventListener('click', async (e) => {
        if (e.target.tagName === 'BUTTON') {
            const taskId = e.target.dataset.id;
            const response = await fetch(`/tasks/${taskId}`, {
                method: 'DELETE',
            });
            if (response.ok) {
                e.target.parentElement.remove();
            }
        }
    });

    async function fetchTasks() {
        const response = await fetch('/tasks');
        const tasks = await response.json();
        tasks.forEach(addTaskToList);
    }

    function addTaskToList(task, id) {
        const li = document.createElement('li');
        li.textContent = task;
        const button = document.createElement('button');
        button.textContent = 'Delete';
        button.dataset.id = id;
        li.appendChild(button);
        tasksList.appendChild(li);
    }

    fetchTasks();
});
