const task3Element = document.getElementById("task-3");

function sayHello() {
  alert("Hello my Friend");
}

function reseiveName(name) {
  alert(`Hello ${name}`);
}

function combine(fistName, middleName, lastName) {
  const combineText = `Hello ${fistName} ${middleName} ${lastName}`;
  return combineText;
}

reseiveName("Ghazaly");

task3Element.addEventListener("click", sayHello);

alert(combine("med", "Ghazaly", "Abk"));
