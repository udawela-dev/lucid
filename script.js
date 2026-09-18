// =============================================
// script.js — Lucid interactions & animations
//
// Structure:
//   1) Pure functions (no DOM, easy to test in Node)
//   2) initLucid(): wires them to the page
//
// Motion budget (from MISSION.md / TECH.md):
//   1 hero effect (headline load-in) +
//   1 scroll effect (navbar solid on scroll) +
//   1 microinteraction (CTA hover, pure CSS)
//   + Progressive enhancement: scroll reveals (IntersectionObserver)
// =============================================

// The hero reveal class name — used by JS to trigger
// the load-in animation and by CSS to style it.
const HERO_REVEAL_CLASS = "is-revealed";

function getHeroRevealClass() {
  return HERO_REVEAL_CLASS;
}

// The navbar becomes "solid" once the page is scrolled
// past a small distance. Pure function, returns a boolean.
function shouldSolidifyNavbar(scrollY) {
  return scrollY > 8;
}

// --- Mobile menu toggle (DOM-dependent, not exported) ---
function initMobileMenu() {
  var toggle = document.querySelector(".navbar-toggle");
  var menu = document.getElementById("mobile-menu");
  var overlay = document.getElementById("mobile-menu-overlay");
  if (!toggle || !menu || !overlay) return;

  function closeMenu() {
    toggle.setAttribute("aria-expanded", "false");
    menu.classList.remove("is-open");
    overlay.classList.remove("is-visible");
    menu.hidden = true;
    overlay.hidden = true;
    document.body.style.overflow = "";
  }

  function openMenu() {
    toggle.setAttribute("aria-expanded", "true");
    menu.hidden = false;
    overlay.hidden = false;
    // force reflow for transition
    requestAnimationFrame(function() {
      menu.classList.add("is-open");
      overlay.classList.add("is-visible");
    });
    document.body.style.overflow = "hidden";
  }

  toggle.addEventListener("click", function() {
    var isOpen = toggle.getAttribute("aria-expanded") === "true";
    if (isOpen) closeMenu(); else openMenu();
  });

  overlay.addEventListener("click", closeMenu);

  // Close on link click
  menu.querySelectorAll("a").forEach(function(link) {
    link.addEventListener("click", closeMenu);
  });

  // Close on Escape
  document.addEventListener("keydown", function(e) {
    if (e.key === "Escape" && menu.classList.contains("is-open")) closeMenu();
  });
}

// --- Scroll reveal (IntersectionObserver) ---
function initScrollReveal() {
  // Respect reduced motion
  var prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (prefersReduced) {
    document.querySelectorAll(".reveal").forEach(function(el) {
      el.classList.add("is-visible");
    });
    return;
  }

  var observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      }
    });
  }, {
    root: null,
    rootMargin: "0px 0px -10% 0px",
    threshold: 0.1
  });

  document.querySelectorAll(".reveal").forEach(function(el) {
    observer.observe(el);
  });
}

// ---- initLucid: connects pure functions to the page ----
function initLucid() {
  var navbar = document.getElementById("navbar");
  var heroReveal = document.querySelector(".hero-reveal");

  // 1) Hero load-in effect — play the animation once, on load.
  if (heroReveal) {
    heroReveal.classList.add(getHeroRevealClass());
  }

  // 2) Navbar solid-on-scroll effect.
  function updateNavbar() {
    if (navbar) {
      if (shouldSolidifyNavbar(window.scrollY)) {
        navbar.classList.add("is-solid");
      } else {
        navbar.classList.remove("is-solid");
      }
    }
  }

  updateNavbar(); // set the correct state on first paint
  window.addEventListener("scroll", updateNavbar, { passive: true });

  // 3) Mobile menu
  initMobileMenu();

  // 4) Scroll reveal animations
  initScrollReveal();
}

// Make the pure functions available to tests (Node), and
// start the page only when running in a real browser.
if (typeof module !== "undefined" && module.exports) {
  module.exports = {
    shouldSolidifyNavbar: shouldSolidifyNavbar,
    getHeroRevealClass: getHeroRevealClass
  };
}

if (typeof window !== "undefined" && window.document) {
  window.addEventListener("DOMContentLoaded", initLucid);
}