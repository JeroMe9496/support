//START OBJECT todos
let todos = {

  //MY TODO LIST - PROPERTY
  list : [
    "Learn HTML5", 
    "Learn CSS", 
    "Learn JS", 
    "Learn PHP"
  ],

  //DISPLAY TODOS - METHOD
  displayTodos: function() {
    console.log(this.list);
  },

  //ADD TODO
  addTodo: function(todoText) {
    this.list.push(todoText);
    this.displayTodos();
  },

  //CHANGE TODO
  changeTodo: function(index, text) {
    this.list[index] = text;
    this.displayTodos(); 
  },

  //DELETE TODO
  deleteTodo: function(index) {
    this.list.splice(index, 1);
    this.displayTodos();
  }

}; // END OBJECT todos


console.log( todos.list );
todos.addTodo("New todo");







