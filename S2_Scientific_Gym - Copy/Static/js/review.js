// var swiper = new Swiper(".mySwiperReview", {
//     effect: "coverflow",
//     grabCursor: true,
//     centeredSlides: true,
//     slidesPerView: "auto",
//     coverflowEffect: {
//         rotate: 50,
//         stretch: 0,
//         depth: 100,
//         modifier: 1,
//         slideShadows: true,
//     },
//     pagination: {
//         el: ".swiper-pagination",
//     },
// });




//  Initialize Swiper
var swiper = new Swiper(".reviewSwiper", {

    autoplay: {
        delay: 2000,
        disableOnInteraction: false,
    },
    // Optional parameters
    loop: false,

    // If we need pagination
    slidesPerView: 3,
    spaceBetween: 30,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },


    breakpoints: {
        300: {
            slidesPerView: 1,
            spaceBetween: 10,
        },
        380: {
            slidesPerView: 1,
            spaceBetween: 10,
        },
        480: {
            slidesPerView: 1,
            spaceBetween: 10,
        },

        640: {
            slidesPerView: 1,
            spaceBetween: 10,
        },
        768: {
            slidesPerView: 2,
            spaceBetween: 20,
        },
        1024: {
            slidesPerView: 2,
            spaceBetween: 20,
        },
        1124: {
            slidesPerView: 3,
            spaceBetween: 30,
        },
    },





});