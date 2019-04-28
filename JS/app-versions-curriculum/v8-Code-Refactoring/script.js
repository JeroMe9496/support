/** 
 * TODO LIST OBJECT
 * -------------------------------------------------
 * All methods related to list/array manipulation
*/
var todoList = {


	todos: [
		{
			todoText: "Item 1",
			completed: true
		},
		{
			todoText: "Item 2",
			completed: false
		},
		{
			todoText: "Item 3",
			completed: false
		}
	],


	displayTodos: function () {

		if (this.todos.length === 0) {
			console.log('Your todo list is empty!');
		}
		
		else {

			console.log('My Todos:');
			
			for (var i = 0; i < this.todos.length; i++) {
				if (this.todos[i].completed === true) {
					console.log('(x)', this.todos[i].todoText);
				}
				else {
					console.log('( )', this.todos[i].todoText);
				}
			}

		} //END else

	},


	addTodo: function (todoText) {
		this.todos.push({
			todoText: todoText,
			completed: false
		});

		this.displayTodos();
	},


	changeTodo: function (position, todoText) {
		this.todos[position].todoText = todoText;
		this.displayTodos();
	},


	deleteTodo: function (position) {
		this.todos.splice(position, 1);
		this.displayTodos();
	},


	toggleCompleted: function (position) {
		var todo = this.todos[position];
		todo.completed = !todo.completed;
		this.displayTodos();
	},


	toggleAll: function () {

		var totalTodos = this.todos.length;
		var completedTodos = 0;
		// Get the number of completed todos
		for (var i = 0; i < totalTodos; i++) {
			if (this.todos[i].completed === true) {
				completedTodos++;
			}
		}
		// If everything is true, make everything false.
		if (completedTodos === totalTodos) {
			for (var i = 0; i < totalTodos; i++) {
				this.todos[i].completed = false;
			}
			// Otherwise make everthing true.
		} else {
			for (var i = 0; i < totalTodos; i++) {
				this.todos[i].completed = true;
			}
		}

		this.displayTodos();

	}


};


/** 
 * HANDLERS OBJECT
 * -------------------------------------------------
 * Methods related to DOM elements
*/
var handlers = {


	//NOTE: 
	//Methods displayTodos() and toggleAll() are not mandatory 
	//as you can use them directly from todoList object
	//The are kept here for consistency...
	//Is more consistent using the same object (handlers) for all DOM actions
	

	displayTodos: function () {
		todoList.displayTodos();
	},


	toggleAll: function () {
		todoList.toggleAll();
	},


	addTodo: function () {
		var addTodoTextInput = document.getElementById('addTodoTextInput');
		todoList.addTodo(addTodoTextInput.value);
		addTodoTextInput.value = '';
	},


	changeTodo: function () {
		var changeTodoPositionInput = document.getElementById('changeTodoPositionInput');
		var changeTodoTextInput = document.getElementById('changeTodoTextInput');
		todoList.changeTodo(changeTodoPositionInput.valueAsNumber, changeTodoTextInput.value);
		changeTodoPositionInput.value = "";
		changeTodoTextInput.value = '';
	},


	deleteTodo: function () {
		var deleteTodoPositionInput = document.getElementById('deleteTodoPositionInput');
		todoList.deleteTodo(deleteTodoPositionInput.valueAsNumber);
		deleteTodoPositionInput = '';
	},


	toggleCompleted: function () {
		var toggleCompletedPositionInput = document.getElementById('toggleCompletedPositionInput');
		todoList.toggleCompleted(toggleCompletedPositionInput.valueAsNumber);
		toggleCompletedPositionInput = '';
	}


};





   