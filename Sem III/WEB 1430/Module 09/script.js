//iniitalize the app
function InitializeTodoApp() {
    const appContainer = document.getElementById('app-container');

    
    const h1 = document.createElement('h1');
    h1.textContent = 'TODO Application';
    appContainer.appendChild(h1);

    //creating input group div
    const inputGroup = document.createElement('div');
    inputGroup.className = 'input-group';

    //creating inout field for user id
    const input = document.createElement('input');
    input.type = 'number';
    input.placeholder = 'Enter User ID (e.g., 1)';
    input.min = '1'; // Ensure positive integers
    inputGroup.appendChild(input);

    const button = document.createElement('button');
    button.textContent = 'Get Todo List';
    inputGroup.appendChild(button);

    appContainer.appendChild(inputGroup);

    //creating div for error 
    const errorDiv = document.createElement('div');
    errorDiv.id = 'error-message';
    appContainer.appendChild(errorDiv);

    //creating list for todo
    const todoList = document.createElement('ul');
    todoList.id = 'todo-list';
    appContainer.appendChild(todoList);

    button.addEventListener('click', () => {
        const userId = input.value.trim();
        if (!validateInput(userId)) return;
        fetchTodos(parseInt(userId));
    });
}

//function to check user input
function validateInput(userId) {
    const errorDiv = document.getElementById('error-message');
    if (!userId) {
        errorDiv.textContent = 'Please enter a User ID.';
        return false;
    }
    if (isNaN(userId) || userId <= 0) {
        errorDiv.textContent = 'User ID must be a positive integer.';
        return false;
    }
    errorDiv.textContent = ''; 
    return true;
}

//function to get todos from API
async function fetchTodos(userId) {
    const storedUserId = localStorage.getItem('lastUserId');
    const storedTodos = localStorage.getItem('lastTodos');

    
    if (storedUserId && parseInt(storedUserId) === userId && storedTodos) {
        displayTodos(JSON.parse(storedTodos));
        return;
    }

    
    try {
        const response = await fetch(`https://jsonplaceholder.typicode.com/users/${userId}/todos`);
        if (!response.ok) throw new Error('API request failed');
        const todos = await response.json();
        if (todos.length === 0) throw new Error('No todos found for this user.');

        
        localStorage.setItem('lastUserId', userId);
        localStorage.setItem('lastTodos', JSON.stringify(todos));

        displayTodos(todos);
    } catch (error) {
        document.getElementById('error-message').textContent = error.message;
        document.getElementById('todo-list').innerHTML = ''; 
    }
}

//function to display todos
function displayTodos(todos) {
    const todoList = document.getElementById('todo-list');
    todoList.innerHTML = ''; 
    todos.forEach(todo => {
        const li = document.createElement('li');
        li.className = `todo-item ${todo.completed ? 'completed' : 'not-completed'}`;
        li.innerHTML = `
            <span>${todo.title}</span>
            <span>${todo.completed ? 'Completed' : 'Not Completed'}</span>
        `;
        todoList.appendChild(li);
    });
}

InitializeTodoApp();
