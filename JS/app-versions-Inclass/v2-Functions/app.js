//MY TODO LIST - GLOBAL SCOPE
let todoList = [
  "Learn HTML5", 
  "Learn CSS", 
  "Learn JS", 
  "Learn PHP"
];


//DISPLAY TODOS
function displayTodos() {
  console.log(todoList);
  //let bob = 3; // LOCAL SCOPE - not available outside the function
}
displayTodos();


//ADD TODO
function addTodo(todoText) {
  todoList.push(todoText);
  displayTodos();
}
addTodo("Do that!");
// addTodo("Do this!");
// addTodo("Do NOT do that!");


//CHANGE TODO
function changeTodo(index, text) {
  todoList[index] = text;
  displayTodos(); 
}
changeTodo(0, "Some todo");
changeTodo(2, "Something like this");


//DELETE TODO
function deleteTodo(index) {
  todoList.splice(index, 1);
  displayTodos();
}
deleteTodo(1);
deleteTodo(3);






