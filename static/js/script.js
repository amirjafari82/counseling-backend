'use strict'

// hamburger menu functionality

function menuOnClick() {
    document.getElementById("menu-bar").classList.toggle("change");
    document.getElementById("nav").classList.toggle("change");
    document.getElementById("menu-bg").classList.toggle("change-bg");
    document.getElementById("menu-bar").classList.toggle("burger-bg");
}

// Slider from Slick

$('.course-list-slider').slick({
    infinite:false,
    slidesToShow: 2,
    slidesToScroll: 1,
    rtl: true,
});