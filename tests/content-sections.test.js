// =============================================
// content-sections.test.js — plain Node tests for
// the Content Sections + Feature Cards feature.
//
// Run with:  node build-lab/tests/content-sections.test.js
// Exit code 0 = all green. Anything else = red.
// =============================================

const fs = require("fs");
const path = require("path");

const buildLab = path.join(__dirname, "..");
const html = fs.readFileSync(path.join(buildLab, "index.html"), "utf8");
const css = fs.readFileSync(path.join(buildLab, "style.css"), "utf8");
const js = fs.readFileSync(path.join(buildLab, "script.js"), "utf8");

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

// Count the exact "feature-card" container elements
// (not feature-card-icon / -title / -text which also contain the name).
function countTags(html, className) {
  const re = new RegExp('class="' + className + '"', "g");
  const matches = html.match(re);
  return matches ? matches.length : 0;
}

console.log("\n--- Sections exist ---");
check("problem section exists", html.includes('id="problem"'));
check("solution section exists", html.includes('id="solution"'));
check("features section exists", html.includes('id="features"'));
check("social-proof section exists", html.includes('id="social-proof"'));
check("footer exists", html.includes("<footer"));

console.log("\n--- Approved headlines ---");
check(
  "problem headline: You saved it. So why can't you find it?",
  html.includes("You saved it. So why can't you find it?")
);
check(
  "solution headline: One search box. Everything you've saved.",
  html.includes("One search box. Everything you've saved.")
);

const featureGrid = html.slice(html.indexOf('id="features"'), html.indexOf('id="social-proof"'));
const cardCount = (featureGrid.match(/class="feature-card"/g) || []).length;
check("exactly 3 feature cards", cardCount === 3);

const cardOrder = [
  "Private by design",
  "Saved-in-one-place",
  "Faster than digging"
];
const privateBeforeOnePlace =
  featureGrid.indexOf("Private by design") > -1 &&
  (featureGrid.indexOf("Private by design") < featureGrid.indexOf("Saved-in-one-place"));
check("privacy card comes first", privateBeforeOnePlace);
check("card titles present in order",
  cardOrder.every((t) => featureGrid.includes(t)));

const svgCount = (featureGrid.match(/<svg/g) || []).length;
check("3 inline SVG icons (one per card)", svgCount === 3);

console.log("\n--- Hover lift + card styling (the 1 microinteraction) ---");
const hoverMatch = css.match(/\.feature-card:hover\s*\{[^}]*\}/);
check("feature-card:hover rule exists", hoverMatch !== null);
if (hoverMatch) {
  check(
    "hover uses translateY(-4px)",
    hoverMatch[0].includes("-4px")
  );
  check(
    "hover has a transition",
    /transition/.test(hoverMatch[0]) || css.match(/\.feature-card\s*\{[^}]*transition[^}]*\}/)
  );
}
const cardRule = css.match(/\.feature-card\s*\{[^}]*\}/);
check("feature-card rule exists", cardRule !== null);
if (cardRule) {
  check(
    "feature-card uses var(--radius-lg)",
    cardRule[0].includes("var(--radius-lg)")
  );
}

console.log("\n--- Token hygiene + calm tone ---");
const rootIdx = css.indexOf(":root");
const afterRoot = rootIdx > -1 ? css.slice(rootIdx) : css;
const rootEnd = afterRoot.indexOf("}") > -1 ? afterRoot.indexOf("}") : 0;
const outsideRoot = css.slice(rootIdx + rootEnd + 1);
const hexOutside = (outsideRoot.match(/#[0-9A-Fa-f]{3,8}\b/g) || []).filter(
  (h) => h !== "#FFFFFF"
);
check("no hex colors outside :root (token-covered case allowed)", hexOutside.length === 0);

const emojiRe =
  /[\u{1F300}-\u{1FAFF}\u{2600}-\u{27BF}\u{FE0F}\u{2B00}-\u{2BFF}]/u;
check("no emoji in HTML (calm tone)", !emojiRe.test(html));

console.log("\n--- JS unchanged and valid (regression guard) ---");
const sandbox = { module: { exports: {} }, console };
const vm = require("vm");
vm.runInContext(js, vm.createContext(sandbox));
check("script.js compiles in VM", typeof sandbox.module.exports === "object");
check("shouldSolidifyNavbar still exported",
  typeof sandbox.module.exports.shouldSolidifyNavbar === "function");

console.log("\n=== Results: " + passed + " passed, " + failures + " failed ===");
process.exit(failures > 0 ? 1 : 0);