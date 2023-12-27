'use strict'

// hamburger menu functionality

function menuOnClick() {
    document.getElementById("menu-bar").classList.toggle("change");
    document.getElementById("nav").classList.toggle("change");
    document.getElementById("menu-bg").classList.toggle("change-bg");
    document.getElementById("menu-bar").classList.toggle("burger-bg");
}

$(".alert").delay(5000).fadeOut('fast');

// swiper slider 

var swiper = new Swiper('.mySwiper', {
    slidesPerView: 2,
    spaceBetween: 10,
    grabCursor: true,
    rewind: true,
    navigation: {
        nextEl: '.swiper-button-next',
        pervEl: '.swiper-button-perv',
    },
    breakpoints: {
        270: {
            slidesPerView: 1,
        },
        599: {
            slidesPerView: 2,
            spaceBetween: 20,
        },
        992: {
            slidesPerView: 2,
            spaceBetween: 30,
        },
    }
})

const day = document.querySelectorAll("span.day");

if(day !== null) {
    day.forEach((dayitem) => {
    switch (dayitem.textContent) {
        case "Saturday":
            dayitem.textContent = "شنبه"
            break;

        case "Sunday":
            dayitem.textContent = "یکشنبه"
            break;

        case "Monday":
            dayitem.textContent = "دوشنبه"
            break;

        case "Tuesday":
            dayitem.textContent = "سه شنبه"
            break;

        case "Wednesday":
            dayitem.textContent = "چهارشنبه"
            break;

        case "Thursday":
            dayitem.textContent = "پنجشنبه"
            break;

        case "Friday":
            dayitem.textContent = "جمعه"
            break;

        default:
            break;
    }
}
)}

const month = document.querySelectorAll("span.month")

if(month !== null) {
    month.forEach((monthitem) => {
        switch (monthitem.textContent) {
            case "Farvardin":
                monthitem.textContent = "فروردین"
                break;
        
            case "Ordibehesht":
                monthitem.textContent = "اردیبهشت"
                break;
        
            case "Khordad":
                monthitem.textContent = "خرداد"
                break;
        
            case "Tir":
                monthitem.textContent = "تیر"
                break;
        
            case "Mordad":
                monthitem.textContent = "مرداد"
                break;
        
            case "Shahrivar":
                monthitem.textContent = "شهریور"
                break;
        
            case "Mehr":
                monthitem.textContent = "مهر"
                break;
        
            case "Aban":
                monthitem.textContent = "آبان"
                break;
        
            case "Azar":
                monthitem.textContent = "آذر"
                break;
        
            case "Dey":
                monthitem.textContent = "دی"
                break;
        
            case "Bahman":
                monthitem.textContent = "بهمن"
                break;
        
            case "Esfand":
                monthitem.textContent = "اسفند"
                break;
        
            default:
                break;
        }
    });   
}