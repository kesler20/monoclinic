const sponsorsBoxElements = document.querySelectorAll(".box");
const sponsorsIntroduction = document.querySelectorAll(
  ".sponsors-introduction"
);
const productElements = document.querySelectorAll(".product");
const productFunctionalityElements = document.querySelectorAll(
  ".product-functionality"
);
const contactMeElements = document.querySelectorAll(".contact-me");
const teamCardsElements = document.querySelectorAll(".team");
const teamIntroduction = document.querySelectorAll(".team-introduction");

const fadeIn = (element, fadeInPace) => {
  let rect = element.getBoundingClientRect();
  element.classList.toggle(fadeInPace, window.scrollY >= rect.top);
};

window.addEventListener("scroll", () => {
  Array.from(sponsorsBoxElements).forEach((box, index) => {
    if (index === 0) {
      fadeIn(box, "fade-in-fast");
    } else if (index === 1) {
      fadeIn(box, "fade-in-normal");
    } else {
      fadeIn(box, "fade-in-slow");
    }
  });

  Array.from(sponsorsIntroduction).forEach((text) => {
    fadeIn(text, "fade-in-normal");
  });

  Array.from(productElements).forEach((box) => {
    fadeIn(box, "fade-in-slow");
  });

  Array.from(productFunctionalityElements).forEach((box) => {
    fadeIn(box, "fade-in-slow");
  });

  Array.from(contactMeElements).forEach((box) => {
    fadeIn(box, "fade-in-slow");
  });

  Array.from(teamCardsElements).forEach((box) => {
    fadeIn(box, "fade-in-slow");
  });

  Array.from(teamIntroduction).forEach((box) => {
    fadeIn(box, "fade-in-slow");
  });
});
