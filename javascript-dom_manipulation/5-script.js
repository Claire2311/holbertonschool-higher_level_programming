const updateHeader = document.querySelector("#update_header");
const headerToUpdate = document.querySelector("header");

updateHeader.addEventListener("click", function () {
  headerToUpdate.innerHTML = "New Header !!!";
});
