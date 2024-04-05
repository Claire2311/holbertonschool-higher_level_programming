const divToUpdate = document.querySelector("#character");

fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
  .then((response) => response.json())
  .then((response) => {
    const newName = response.name;
    divToUpdate.innerHTML = newName;
  })
  .catch(() => console.error("Fetch problem"));
