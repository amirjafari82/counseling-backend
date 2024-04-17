'use strict'

// hamburger menu functionality

function menuOnClick() {
    document.getElementById("menu-bar").classList.toggle("change");
    document.getElementById("nav").classList.toggle("change");
    document.getElementById("menu-bg").classList.toggle("change-bg");
    document.getElementById("menu-bar").classList.toggle("burger-bg");
}

// swiper slider

const mySwiper = document.querySelector(".mySwiper");

if (mySwiper) {
    var swiper = new Swiper('.mySwiper', {
        slidesPerView: 2,
        autoplay: {
            delay: 2500,
        },
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
}



// Slider functionality

const slides = document.querySelectorAll('.slide');
const btnLeft = document.querySelector('.slider__btn--left');
const btnRight = document.querySelector('.slider__btn--right');

let curSlide = 0;
const maxSlide = slides.length;

slides.forEach((s, i) => s.style.transform = `translateX(${100 * i})`)  

const goToSlide = function(slide) {
    slides.forEach((s, i) => s.style.transform = `translateX(${50 * (i - slide)}%)`);
};
goToSlide(0);


// next slide

const nextSlide = function () {
    if(curSlide === maxSlide - 1) {
        curSlide = 0;
    } else {
        curSlide++;
    }
+
    goToSlide(curSlide);
}

const prevSlide = function () {
    if(curSlide === 0) {
        curSlide = maxSlide - 1;
    } else {
        curSlide--;
    }
    goToSlide(curSlide)
}

setInterval (nextSlide, 5000);

if (btnRight || btnLeft) {
    btnRight.addEventListener('click', nextSlide);
    btnLeft.addEventListener('click', prevSlide);
}


// Remember me functionality

const rmCheck = document.getElementById("rememberMe");
const numberInput = document.getElementById("phoneNumber");
const rememberMeLabel = document.getElementById("rememberMeLabel");

if(rmCheck) {
    if (localStorage.checkbox && localStorage.checkbox !== "") {
        rmCheck.setAttribute("checked", "checked");
        numberInput.value = localStorage.username;
      } else {
        rmCheck.removeAttribute("checked");
        numberInput.value = "";
    }
    
    function lsRememberMe() {
        if (rmCheck.checked && numberInput.value !== "") {
          localStorage.username = numberInput.value;
          localStorage.checkbox = rmCheck.value;
        } else {
          localStorage.username = "";
          localStorage.checkbox = "";
        }
    }
}

// visible password functionality 

const togglePassword = document.querySelector("#togglePassword");
const password = document.querySelector("#password");

if (togglePassword) {
    togglePassword.addEventListener("click", function () {
        // toggle the type attribute 
        const type = password.getAttribute("type") === "password" ? "text" : "password";
        password.setAttribute("type", type);
    
        // toggle the icon
        this.classList.toggle("bi-eye");
        password.focus()
    })
}

const csrf = document.getElementsByName('csrfmiddlewaretoken')

$(".alert").delay(5000).fadeOut('fast');

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

const comment_scores = document.querySelectorAll(".feedback label input")
const form = document.querySelector("#course-comment-form")

if (comment_scores) {
    let val = null
    comment_scores.forEach((score) => {
        score.addEventListener("click", function() {
            val = score.value
        })
    })
    form.addEventListener('submit', e => {
        const body = form.children[1].value
        $.ajax({
            type: 'POST',
            url: window.location.pathname,
            data: {
                'csrfmiddlewaretoken': csrf[0].value,
                'val': val,
                'body': body,
            },success : function(data) {
                if(data['status'] == 'ok') {
                    window.location.reload()
                }
            }
        })
    })
}