/* TODO LIST OBJECT
======================================================*/
//#region
var todoList = {


	/* TODO ARRAY (of objects)
	----------------------------------------------*/
	todos: [],


	/* ADD SAMPLE TODOs (ONLY IF EMPTY !)
	----------------------------------------------*/
	addSampleData: function() {

		//IF LIST IS EMPTY
		if(this.todos.length === 0) {

			this.todos = [
				{
					"todoText": 'First',
					"completed": false
				},
				{
					"todoText": 'Second',
					"completed": false
				},
				{
					"todoText": 'Third',
					"completed": false
				},
				{
					"todoText": 'Forth',
					"completed": false
				}
			];

			view.displayTodos();

		}

		//IF LIST IS NOT EMPTY
		else {
			console.log("Cannot add data, Todo List is not empty it contains " + this.todos.length + " elements");
		}

	},


	/* ADD TODO
	----------------------------------------------*/
	addTodo: function(todoText) {
		this.todos.push({
			todoText: todoText,
			completed: false
		});
	},


	/* CHANGE TODO
	----------------------------------------------*/
	changeTodo: function(position, todoText) {
		this.todos[position].todoText = todoText;
	},


	/* DELETE TODO
	----------------------------------------------*/
	deleteTodo: function(position) {
		this.todos.splice(position, 1);
	},


	/* TOGGLE (ITEM) COMPLETED STATUS
	----------------------------------------------*/
	toggleCompleted: function(position) {
		console.log(position);
		var todo = this.todos[position];
		todo.completed = !todo.completed;
	},


	/* TOGGLE ALL TODOs COMPLETED STATUS
	----------------------------------------------*/
	toggleAll: function() {

		var totalTodos = this.todos.length;
		var completedTodos = 0;
		
		// Get the number of completed todos
		this.todos.forEach(function (todo) {
			if (todo.completed === true) {
				completedTodos++;
			}
		});

		//LOOP into todos
		this.todos.forEach(function (todo) {

			// If everything's true, make everything false.
			if (completedTodos === totalTodos) {
				todo.completed = false;
			}

			// Otherwise, make everything true.
			else {
				todo.completed = true;
			}

		});

	}


};
//#endregion



/* HANDLERS
======================================================*/
//#region
var handlers = {


	/* ADD TODO
	----------------------------------------------*/
	addTodo: function(inputElem) {

		//debugger;
		todoList.addTodo(inputElem.value);
		inputElem.value = '';

		view.displayTodos();

	},


	/* CHANGE TODO
	----------------------------------------------*/
	changeTodo: function(position, value) {

		todoList.changeTodo(position, value);
		view.displayTodos();

	},


	/* DELETE TODO
	----------------------------------------------*/
	deleteTodo: function(position) {

		todoList.deleteTodo(position);
		view.displayTodos();

	},


	/* TOGGLE (ITEM) COMPLETED STATUS
	----------------------------------------------*/
	toggleCompleted: function(position) {

		todoList.toggleCompleted(position);
		view.displayTodos();

	},


	/* TOGGLE ALL TODOs COMPLETED STATUS
	----------------------------------------------*/
	toggleAll: function() {

		todoList.toggleAll();
		view.displayTodos();

	}


};
//#endregion



/* HANDLERS VARIANTE (manual input)
======================================================*/
//#region
var handlersVariante = {


	/* ADD TODO
	----------------------------------------------*/
	addTodo: function() {

		var addTodoTextInput = document.getElementById('addTodoTextInput');
		todoList.addTodo(addTodoTextInput.value);
		addTodoTextInput.value = '';

		view.displayTodos();

	},

	
	/* CHANGE TODO
	----------------------------------------------*/
	changeTodo: function() {

		var changeTodoPositionInput = document.getElementById('changeTodoPositionInput');
		var changeTodoTextInput = document.getElementById('changeTodoTextInput');
		todoList.changeTodo(changeTodoPositionInput.valueAsNumber, changeTodoTextInput.value);
		changeTodoPositionInput.value = "";
		changeTodoTextInput.value = '';

		view.displayTodos();

	},


	/* DELETE TODO
	----------------------------------------------*/
	deleteTodo: function(position) {

		var deleteTodoPositionInput = document.getElementById('deleteTodoPositionInput');
		todoList.deleteTodo(deleteTodoPositionInput.valueAsNumber);
		deleteTodoPositionInput.value = '';

		view.displayTodos();

	},


	/* TOGGLE (ITEM) COMPLETED STATUS
	----------------------------------------------*/
	toggleCompleted: function() {

		var toggleCompletedPositionInput = document.getElementById('toggleCompletedPositionInput');
		todoList.toggleCompleted(toggleCompletedPositionInput.valueAsNumber);
		toggleCompletedPositionInput = '';

		view.displayTodos();

	},


	/* TOGGLE ALL TODOs COMPLETED STATUS
	----------------------------------------------*/
	toggleAll: function() {

		todoList.toggleAll();
		view.displayTodos();

	}


};
//#endregion



/* VIEW TODOs
======================================================*/
//#region
var view = {


	/* DISPLAY TODOs
	----------------------------------------------*/
	displayTodos: function () {

		
		var todoUl = document.querySelector('.todo-list');
		todoUl.innerHTML = '';
		//console.log('todos: ', todoList.todos);

		//var listTodos = (storage.checkStorage === true) ? storage.getData() : todoList.todos; //not there yet
		var listTodos = todoList.todos;
		
		//LOOP into todos
		for(var i = 0; i < listTodos.length; i++) {


			var todo = listTodos[i];

			//CREATE LI (FOR EACH TODOs ITEM)
			var ulLi = document.createElement('li');
			ulLi.setAttribute('id', 'item-' + i);
			ulLi.setAttribute('data-id', i);


			/* CREATE LI CONTENT
			---------------------------------------*/
			//DIV container
			var liDiv = document.createElement("div");
			liDiv.setAttribute('class', 'view');
			
			//INPUT - hidden, will show on DblClick
			var divInput = document.createElement("input");
			divInput.setAttribute('class', 'toggle');
			divInput.setAttribute('type', 'checkbox');

			//LABEL
			var divLabel = document.createElement("label");
			divLabel.className = "item-label";
			divLabel.textContent = todo.todoText;

			//BUTTON delete/destroy
			var divButton = document.createElement("button");
			divButton.setAttribute('data-id', i);
			divButton.setAttribute('class', 'destroy');


			/* CHECK IF COMPLETED
			---------------------------------------*/
			if(todo.completed === true) {
				ulLi.setAttribute('class', 'completed');
				divInput.setAttribute('checked', '');
			}
			else {
				ulLi.removeAttribute('class');
				divInput.removeAttribute('checked');
			}


			/* APPEND ELEMENTS
			---------------------------------------*/
			todoUl.appendChild(ulLi);
			ulLi.appendChild(liDiv);
			liDiv.appendChild(divInput);
			liDiv.appendChild(divLabel);
			liDiv.appendChild(divButton);
			
			


			/* TODOs FILTERS
			----------------------------------------*/
			var countCompleted = document.querySelector(".todo-count strong");
			var uncompleted = 0;
			
			for(let i = 0; i < todoList.todos.length; i++) {
				let todo = todoList.todos[i];
				if(todo.completed === false) {
					uncompleted++;
				}
			}
			countCompleted.textContent = uncompleted;

			filters.checkStatus();


		} //End Loop


	}, //END displayTodos


	/* EVENT LISTENERS
	----------------------------------------------*/
	setUpEventListeners: function () { //  Event Delegation Method


		/* LIST EVENTS
		***************************************/
		const todosUl = document.querySelector('.todo-list');


		//CLICK EVENT
		todosUl.addEventListener('click', function(e) {

			//debugger;
			
			//GET CLICKED ELEMENT
			const clickedElem = e.target; //console.log('dataId from Event:', dataId);
			
			//GET DATA ID FROM PARENT LI
			const dataId = parseInt(clickedElem.closest("li").dataset.id); //console.log('Event dataId:', dataId);


			//IF CLIECKED ELEMENT IS DELETE BUTTON
			if(clickedElem.className === "destroy") {
				handlers.deleteTodo(dataId);
			}

			//IF CLIECKED ELEMENT IS TOGGLE INPUT
			if(clickedElem.className === "toggle") {
				handlers.toggleCompleted(dataId);
			}

		});


		//DBLCLICK EVENT
		todosUl.addEventListener('dblclick', function(e) {


			//REMOVE ALL EDIT INPUTS (if any)
			var editElement = document.querySelector('input.edit'); //console.log(editElement);

			if(editElement !== null) {
				editElement.parentNode.classList.remove("editing");
				editElement.remove();
			}

			//GET CLICKED ELEMENT
			const clickedElem = e.target; //console.log("dbclick on: ", clickedElem);
			
			// IF CLICKED ELEMENT IS A LABEL
			if(clickedElem.className === "item-label") {	

				var closestLi = clickedElem.closest('li'); //variante: clickedElem.parentNode
				var labelText = clickedElem.textContent; //console.log(labelText);
				var dataId = parseInt(closestLi.dataset.id); //console.log(dataId);

				closestLi.classList.add('editing');
				

				//Create an Input to edit label...
				var inputEdit = document.createElement('input');
				inputEdit.className = 'edit'; //setAttribute() variante

				closestLi.appendChild(inputEdit);
				inputEdit.focus();
				inputEdit.value = labelText;


				//ON Input Keypress ENTER
				inputEdit.addEventListener('keypress', function(e) {
					
					var key = e.which || e.keyCode;

					if(key === 13) { // 13 is enter

						handlers.changeTodo(dataId, inputEdit.value);
						
						closestLi.classList.remove("editing");
						inputEdit.remove();

						view.displayTodos(); //refresh the view of the list
					}

				}); //End inputEdit KEYPRESS


			} //End IF clickedElem

		});



		/* TOP INPUT (new-todo) EVENTS
		***************************************/
		const newTodo = document.querySelector('.new-todo');

		//KEYPRESS EVENT
		newTodo.addEventListener('keypress', function(e) {

			var key = e.which || e.keyCode;
			
			if(key === 13) { // 13 is enter

				const clickedElem = e.target; //console.log(clickedElem);
				handlers.addTodo(clickedElem);
			}

		});



		/* UTILITIES EVENTS
		***************************************/
		const todosUtilities = document.querySelector('.utilities');

		//CLICK EVENT
		todosUtilities.addEventListener('click', function(e) {
			// Get the element that was clicked on.
			const clickedElem = e.target;

			// Check if clickedElem is SAVE.
			if (clickedElem.id === "save-list") {
				storage.saveData();
			}
		});


	} //END setUpEventListeners


};
//#endregion



/* TODOs FILTERS
======================================================*/
//#region
var filters = {


	checkStatus: function() {

		var listIsEmpty = todoList.todos.length === 0;
		var sampleDataLink = document.getElementById("sample-data");
		var saveToStorageLink = document.getElementById("save-list");

		//IF EMPTY LIST, REMOVE CLASS HIDE ON SAVE AND ADD SAMPLE
		if(listIsEmpty) {
			sampleDataLink.classList.remove("hide");
		}
		else {
			sampleDataLink.classList.add("hide");
		}

		if(!listIsEmpty) {
			saveToStorageLink.classList.remove("hide");
		}

	},


	showAll: function() {

	},


	showActive: function() {
		
	},


	showCompleted: function() {
		
	}


};
//#endregion



/* TODOs LOCAL STORAGE
======================================================*/
//#region
var storage = {


	//CHECK STORAGE - Once per refresh
	checkStorage: true,


	// STORAGE ITEM NAME
	keyName: 'todosData',


	//GET STORAGE
	getData: function() {
		
		//debugger;
		const data = localStorage.getItem(this.keyName);
		
		if(data !== null && data !== undefined) {
			
			var storageData = JSON.parse(data);
			todoList.todos = storageData;

			return todoList.todos;
		}
		else {
			this.saveData();
			const data = localStorage.getItem(this.keyName);

			return JSON.parse(data);
		}

	},


	//SET STORAGE
	saveData: function() {
		localStorage.setItem(this.keyName, JSON.stringify(todoList.todos));
	},


	//REMOVE STORAGE
	removeData: function() {
		localStorage.removeItem(this.keyName);
	},

}
//#endregion



//CALL TODOs
view.setUpEventListeners();
view.displayTodos();
filters.checkStatus();
