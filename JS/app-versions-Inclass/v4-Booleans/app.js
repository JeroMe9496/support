//START OBJECT todos
let todos = {

  //MY TODO LIST - PROPERTY
  list : [

    {
      text: "Learn HTML5",
      completed: false
    },
    {
      text: "Learn CSS",
      completed: false
    },
    {
      text: "Learn JS",
      completed: false
    },
    {
      text: "Learn PHP",
      completed: false
    }

  ],

  //DISPLAY TODOS - METHOD
  displayTodos: function() {
    console.log(this.list);
  },

  //ADD TODO
  addTodo: function(todoText) {

    let newTodo = {
      text: todoText,
      completed: false
    }

    this.list.push(newTodo);
    this.displayTodos();
  },

  //CHANGE TODO
  changeTodo: function(index, newText) {
    this.list[index].text = newText;
    this.displayTodos();
  },

  //DELETE TODO
  deleteTodo: function(index) {
    this.list.splice(index, 1);
    this.displayTodos();
  },

  //TOGGLE COMPLETED
  toggleTodo: function(index) {
  
    let currentStatus = this.list[index].completed; //true or false
    this.list[index].completed = ! currentStatus;
    this.displayTodos();

  }


}; // END OBJECT todos

// todos.displayTodos();
// todos.addTodo("New todo");
// todos.addTodo("Another todo");

// //todos.changeTodo(4, "Bob is great!");
// console.log( todos.list[4] );
// todos.list[4].text = "Something else";
// console.log( todos.list[4] );

console.log(todos);
console.log(todos.list);
console.log(todos.list[1]);

todos.list[2].completed = true;
console.log(todos.list[2]);





