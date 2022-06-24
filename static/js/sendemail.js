let loader = document.querySelector("#loader");
let contact_img = document.querySelector("#contact-img");

function show_hide() {
    setTimeout(() => {
        loader.style.display = "inline";
        contact_img.style.display = "none";
    }, 2500);
    setTimeout(() => {
            loader.style.display = "none";
            contact_img.style.display = "inline";
        }, 8500);
}


window.onload = function() {
    document.getElementById('contact-form').addEventListener('submit', function(event) {
        event.preventDefault();
        show_hide();
        // these IDs from the previous steps
        emailjs.sendForm('vintage-cars', 'vintage-cars-temp', this)
            .then(function() {
                console.log('SUCCESS!');
                let contactform = document.getElementById('contact-form');
                contactform.reset();
            }, function(error) {
                console.log('FAILED...', error);
            });
    });
}