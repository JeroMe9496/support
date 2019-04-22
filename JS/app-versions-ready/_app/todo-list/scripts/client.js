/* TODO LIST OBJECT
------------------------------------------------*/
var todoList = {

	todos: [],
	
	//ADD TODO
	addTodo: function (todoText) {
		this.todos.push({
			todoText: todoText,
			completed: false
		});
	},

	//CHANGE TODO
	changeTodo: function (position, todoText) {
		this.todos[position].todoText = todoText;
	},

	//DELETE TODO
	deleteTodo: function (position) {
		this.todos.splice(position, 1);
	},

	//TOGGLE COMPLETED TODOs
	toggleCompleted: function (position) {
		var todo = this.todos[position];
		todo.completed = !todo.completed;
	},

	toggleAll: function () {
		var totalTodos = this.todos.length;
		var completedTodos = 0;
		// Get the number of completed todos
		this.todos.forEach(function (todo) {
			if (todo.completed === true) {
				completedTodos++;
			}
		});
		this.todos.forEach(function (todo) {
			// If everything's true, make everything false.
			if (completedTodos === totalTodos) {
				todo.completed = false;
			// Otherwise, make everything true.
			} else {
				todo.completed = true;
			}
		});
	}

};


/* HANDLERS OBJECT
------------------------------------------------*/
var handlers = {

	addTodo: function () {
		var addTodoTextInput = document.getElementById('addTodoTextInput');
		todoList.addTodo(addTodoTextInput.value);
		addTodoTextInput.value = '';
		view.displayTodos();
	},

	changeTodo: function () {
		var changeTodoPositionInput = document.getElementById('changeTodoPositionInput');
		var changeTodoTextInput = document.getElementById('changeTodoTextInput');
		todoList.changeTodo(changeTodoPositionInput.valueAsNumber, changeTodoTextInput.value);
		changeTodoPositionInput.value = "";
		changeTodoTextInput.value = '';
		view.displayTodos();
	},

	deleteTodo: function (position) {
		todoList.deleteTodo(position);
		view.displayTodos();
	},

	toggleCompleted: function () {
		var toggleCompletedPositionInput = document.getElementById('toggleCompletedPositionInput');
		todoList.toggleCompleted(toggleCompletedPositionInput.valueAsNumber);
		toggleCompletedPositionInput = '';
		view.displayTodos();
	},

	toggleAll: function () {
		todoList.toggleAll();
		view.displayTodos();
	}

};


/* VIEW TODOs OBJECT
------------------------------------------------*/
var view = {

	//DISPLAY TODOs
	displayTodos: function () {

		var todoUl = document.querySelector('ul');
		todoUl.innerHTML = '';
		
		todoList.todos.forEach(function (todo, position) {
			var todoLi = document.createElement('li');
			var todoTextWithCompletion = '';

			if (todo.completed === true) {
				todoTextWithCompletion = '(x) ' + todo.todoText;
			} else {
				todoTextWithCompletion = '( ) ' + todo.todoText;
			}

			todoLi.id = position;
			todoLi.textContent = todoTextWithCompletion;
			todoLi.appendChild(this.createDeleteButton());
			todoUl.appendChild(todoLi);
		}, this);

	},


	createDeleteButton: function () {

		var deleteButton = document.createElement('button');
		deleteButton.textContent = 'Delete';
		deleteButton.className = 'deleteButton';

		return deleteButton;

	},



	setUpEventListeners: function () { //  Event Delegation Method

		var todosUl = document.querySelector('ul');

		todosUl.addEventListener('click', function (event) {
			// Get the element that was clicked on.
			var elementClicked = event.target;

			 // Check if elementClicked is a delete button.
			if (elementClicked.className === "deleteButton") {
				handlers.deleteTodo(parseInt(elementClicked.parentNode.id));
			}
		});

	}

};


view.setUpEventListeners();
