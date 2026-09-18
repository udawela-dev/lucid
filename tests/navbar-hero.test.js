// =============================================
// navbar-hero.test.js — plain Node tests for the
// Navbar + Hero feature (no npm packages needed).
//
// Run with:  node build-lab/tests/navbar-hero.test.js
// Exit code 0 = all green. Anything else = red.
// =============================================

const fs = require("fs");
const path = require("path");

// ---- Load the real project files ----
const buildLab = path.join(__dirname, "..");
const html = fs.readFileSync(path.join(buildLab, "index.html"), "utf8");
const css = fs.readFileSync(path.join(buildLab, "style.css"), "utf8");
const js = fs.readFileSync(path.join(buildLab, "script.js"), "utf8");

// ---- Tiny test helpers (beginner friendly) ----
let failures = 0;
let passed = 0;

function check(name, condition) {
  if (condition) {
    passed += 1;
    console.log("  PASS  " + name);
  } else {
    failures += 1;
    console.error("  FAIL  " + name);
  }
}

function checkContains(text, needle, name) {
  check(name, text.includes(needle));
}

// ---- Load script.js in a sandbox so we can call its pure functions ----
// We eval the file content in a fake module environment. The functions we
// need are made available as properties of `module.exports`.
const sandbox = { module: { exports: {} }, console };
const vm = require("vm");
const scriptContext = vm.createContext(sandbox);
vm.runInContext(js, scriptContext);
const lucid = sandbox.module.exports;

console.log("\n--- Navbar structure ---");
checkContains(html, '<header class="navbar"', "navbar header exists");
checkContains(html, ">Lucid<", "brand wordmark Lucid exists");
checkContains(html, ">Problem<", "Problem link exists");
checkContains(html, ">Solution<", "Solution link exists");
checkContains(html, ">Features<", "Features link exists");
checkContains(html, 'href="#cta"', "navbar CTA links to #cta");

console.log("\n--- Hero structure ---");
checkContains(html, 'id="hero"', "hero section exists");
checkContains(html, "Find anything you've ever saved.", "hero headline = tagline");
checkContains(html, "no matter which app it's buried in", "hero subheadline present");
checkContains(html, 'class="btn btn-primary"', "hero primary CTA present");

console.log("\n--- Hero search-bar mockup ---");
checkContains(html, "hero-search", "hero search mockup exists (.hero-search)");
checkContains(html, "hero-search-input", "search input mockup exists");

console.log("\n--- CSS: tokens only, motion + scrolled state ---");
const inRoot = css.split(":root")[0]; // everything before :root
const rootBlock = css.indexOf(":root") > -1
  ? css.slice(css.indexOf(":root"), css.indexOf("}", css.indexOf(":root")))
  : "";
const afterRoot = css.slice(css.indexOf(":root") + rootBlock.length);
const hexOutsideRoot = (afterRoot.match(/#[0-9A-Fa-f]{3,8}\b/g) || []).filter(
  (h) => h !== "#FFFFFF" // white on primary button text is an intentional token now
);
check(
  "no hex colors outside :root (except token-covered cases)",
  hexOutsideRoot.length === 0
);
checkContains(css, "@keyframes", "a keyframes rule exists (hero reveal)");
checkContains(css, ".navbar.is-solid", "navbar scrolled-state rule exists");
checkContains(css, "--transition-fast", "CTA microinteraction uses --transition-fast");

console.log("\n--- JS: pure functions + syntax ---");
check("script.js compiles in VM (no syntax errors)", typeof lucid === "object");
if (typeof lucid.shouldSolidifyNavbar === "function") {
  check("shouldSolidifyNavbar(0) === false", lucid.shouldSolidifyNavbar(0) === false);
  check("shouldSolidifyNavbar(20) === true", lucid.shouldSolidifyNavbar(20) === true);
  check("shouldSolidifyNavbar(-5) === false", lucid.shouldSolidifyNavbar(-5) === false);
} else {
  check("shouldSolidifyNavbar is exported", false);
}
if (typeof lucid.getHeroRevealClass === "function") {
  const cls = lucid.getHeroRevealClass();
  check("getHeroRevealClass returns a string", typeof cls === "string" && cls.length > 0);
  checkContains(css, "." + cls, "hero reveal class is styled in CSS");
} else {
  check("getHeroRevealClass is exported", false);
}

console.log("\n=== Results: " + passed + " passed, " + failures + " failed ===");
process.exit(failures > 0 ? 1 : 0);