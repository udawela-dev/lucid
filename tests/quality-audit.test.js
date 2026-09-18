// =============================================
// quality-audit.test.js — plain Node tests for the
// audit fixes: no-JS fallback, reduced motion,
// focus-visible styles, and smooth scrolling.
//
// Run with:  node build-lab/tests/quality-audit.test.js
// Exit code 0 = all green. Anything else = red.
// =============================================

const fs = require("fs");
const path = require("path");

const buildLab = path.join(__dirname, "..");
const html = fs.readFileSync(path.join(buildLab, "index.html"), "utf8");
const css = fs.readFileSync(path.join(buildLab, "style.css"), "utf8");

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

console.log("\n--- Critical: no-JS hero fallback ---");
check("noscript block exists", html.includes("<noscript>"));
check(
  "noscript forces hero visible (opacity 1)",
  /<noscript>[^]*?opacity\s*:\s*1[^]*?<\/noscript>/.test(html)
);

console.log("\n--- Important: reduced motion ---");
check(
  "prefers-reduced-motion media query exists",
  css.includes("prefers-reduced-motion")
);
check(
  "reduced-motion disables hero animation",
  /prefers-reduced-motion[\s\S]*?\.hero-reveal[\s\S]*?(animation|none)/.test(css)
);
check(
  "reduced-motion sets scroll-behavior auto",
  /prefers-reduced-motion[\s\S]*?scroll-behavior\s*:\s*auto/.test(css)
);

console.log("\n--- Important: keyboard focus-visible ---");
const focusVisibleMatch = css.match(/:focus-visible\s*\{[^}]*\}/);
check(":focus-visible rule exists", focusVisibleMatch !== null);
if (focusVisibleMatch) {
  check(
    ":focus-visible styled with tokens (var(--color-...) or token ring)",
    /var\(--color-/.test(focusVisibleMatch[0])
  );
}

console.log("\n--- Nice-to-have: smooth scrolling ---");
check(
  "scroll-behavior: smooth on html",
  /html\s*\{[^}]*scroll-behavior\s*:\s*smooth/.test(css)
);

console.log("\n=== Results: " + passed + " passed, " + failures + " failed ===");
process.exit(failures > 0 ? 1 : 0);