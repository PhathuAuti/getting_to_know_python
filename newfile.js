function promptUser() {
  var num = prompt("Please enter number of squares...");
  if (num != null) {
    document.getElementById("demo").innerHTML =
    "You want " + num + " number of squares...";
  }
}
