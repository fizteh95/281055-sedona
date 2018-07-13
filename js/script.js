var link = document.querySelector(".interst__form__div");

var popup = document.querySelector(".interst__form");

link.addEventListener("click", function(evt) {
    evt.preventDefault();
    popup.classList.toggle("homepage-booking-form-hide");

});