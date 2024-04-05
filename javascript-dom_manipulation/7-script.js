const listToUpdate = document.querySelector("#list_movies");

fetch("https://swapi-api.hbtn.io/api/films/?format=json")
  .then((response) => response.json())
  .then((response) => {
    console.log(response.results);
    for (i = 0; i < response.results.length; i++) {
      const newElemLi = document.createElement("li");
      newElemLi.innerHTML = response.results[i].title;
      listToUpdate.append(newElemLi);
    }
  })
  .catch(() => console.error("Fetch problem"));
