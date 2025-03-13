// бургер
$('.button_menu').on('click', function () {
    $('.site-navigation').css({
        transform: 'translateX(0)'
    })
});

$('.cross_svg').on('click', function () {
    $('.site-navigation').css({
        transform: 'translateX(100%)'
    })
});

// карусель
$(".owl-carousel").owlCarousel({
    loop: true,
    dots: false,
    autoplay:true,
    autoplayTimeout: 1800,
    pagination: false,
    
    margin:20,
    responsiveClass:true,
    responsive:{
        // от 0 и больше
        0:{
            items:1,
        },
        // от 900 и больше
        900:{
            items:3,
        },
    }
});


// попап на обратный звонок
function togglePopup() {
    const overlay = document.getElementById('popupOverlay');
    overlay.classList.toggle('show');
}


// Email.send({
//     Host : "smtp.elasticemail.com",
//     Username : "Krasnodarrio@yandex.ru",
//     Password : "467E7304825B83F484A94B076D439BFCECBD",
//     To : 'Krasnodarrio@yandex.ru',
//     From : "mineburn22@gmail.com",
//     Subject : "This is the subject",
//     Body : "And this is the body"
// }).then(
//   message => alert(message)
// );
