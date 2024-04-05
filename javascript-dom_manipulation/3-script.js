const toggleHeader = document.querySelector("#toggle_header");
const redTitle = document.querySelector("header");

const changeClass = (elem) => {
  if (redTitle.classList.contains("green")) {
    redTitle.classList.remove("green");
    redTitle.classList.add("red");
  } else {
    redTitle.classList.remove("red");
    redTitle.classList.add("green");
  }
};

toggleHeader.addEventListener("click", changeClass);
