const hamburger = document.querySelector(".hamburger");
const navLinksDropdownMenu = document.querySelector(".nav-links-dropdown-menu");
const navbarLinks = document.querySelectorAll(".nav-links a");

hamburger.addEventListener("click", () => {
  hamburger.classList.toggle("open");
  navbarLinks.forEach((link) => {
    navLinksDropdownMenu.appendChild(link);
  });
});

