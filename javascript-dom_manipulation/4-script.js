const addItem = document.querySelector("#add_item");
const listToAdd = document.querySelector("ul");

addItem.addEventListener("click", function () {
  const newElemLi = document.createElement("li");
  newElemLi.innerHTML = "Item";
  listToAdd.append(newElemLi);
});
