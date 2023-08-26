  var dateInputs = document.querySelectorAll(".dateInput");
  var currentDate = new Date().toISOString().slice(0, 16);
  dateInputs.forEach(function(input) {
    input.setAttribute("min", currentDate);
  });