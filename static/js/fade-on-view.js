const sponsorsBoxElements = document.querySelectorAll(".box");
const sponsorsIntroduction = document.querySelectorAll(
  ".sponsors-introduction"
);

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
});
