let searchForm = document.querySelector(".search-form");
let loginform = document.querySelector(".loginform");

document.querySelector("#search-btn").onclick = () => {
  searchForm.classList.add("active");
  loginform.classList.remove("active");
  navbar.classList.remove("active");
};

document.querySelector("#login-btn").onclick = () => {
  loginform.classList.toggle("active");
  searchForm.classList.remove("active");
  navbar.classList.remove("active");
};

let navbar = document.querySelector(".navbar");
document.querySelector("#menu-btn").onclick = () => {
  navbar.classList.toggle("active");
  searchForm.classList.remove("active");
  loginform.classList.remove("active");
};

window.onscroll = () => {
  searchForm.classList.remove("active");
  loginform.classList.remove("active");
  navbar.classList.remove("active");
};

var swiper = new Swiper(".product-slider", {
  loop:true,
  spaceBetween: 20,
  autoplay: {
    delay:7500,
    disableOnInteraction: false,
  },
  breakpoints: {
    0: {
      slidesPerView: 1,

    },
    768: {
      slidesPerView: 2,

    },
    1020: {
      slidesPerView: 3,

    },
  },
});

var swiper = new Swiper(".review-slider", {
  loop:true,
  spaceBetween: 20,
  autoplay: {
    delay:7500,
    disableOnInteraction: false,
  },
  breakpoints: {
    0: {
      slidesPerView: 1,

    },
    768: {
      slidesPerView: 2,

    },
    1020: {
      slidesPerView: 3,

    },
  },
});
