document.addEventListener("DOMContentLoaded", function () {
  const textUpdate = document.querySelector("#hello");

  let textToAdd = "";

  fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
    .then((response) => response.json())
    .then((response) => {
      textUpdate.innerHTML = response.hello;
    })
    .catch((err) => console.error(err));
});
