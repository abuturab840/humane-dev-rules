// Rule popups: Escape hides them until the pointer leaves the rule number or focus moves (WCAG 1.4.13).
document.addEventListener("keydown", function (e) {
  if (e.key === "Escape") document.body.classList.add("tips-off");
});
document.addEventListener("focusin", function () {
  document.body.classList.remove("tips-off");
});
document.addEventListener("mouseout", function (e) {
  var from = e.target.closest && e.target.closest(".ref");
  var to = e.relatedTarget && e.relatedTarget.closest && e.relatedTarget.closest(".ref");
  if (from && from !== to) document.body.classList.remove("tips-off");
});

// Copy buttons on templates and code blocks.
document.querySelectorAll("pre").forEach(function (pre) {
  var btn = document.createElement("button");
  btn.type = "button";
  btn.className = "copy";
  btn.textContent = "Copy";

  function done(label) {
    btn.textContent = label;
    setTimeout(function () { btn.textContent = "Copy"; }, 3000);
  }

  // If the clipboard is blocked, select the text so it can be copied by hand.
  function fallback() {
    var range = document.createRange();
    range.selectNodeContents(pre);
    var sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(range);
    var ok = false;
    try { ok = document.execCommand("copy"); } catch (e) { ok = false; }
    done(ok ? "Copied" : "Selected: press Ctrl+C or \u2318C");
  }

  btn.addEventListener("click", function () {
    var text = pre.innerText.replace(/\n$/, "");
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () { done("Copied"); }, fallback);
    } else {
      fallback();
    }
  });

  var wrap = document.createElement("div");
  wrap.className = "codewrap";
  pre.parentNode.insertBefore(wrap, pre);
  wrap.appendChild(btn);
  wrap.appendChild(pre);
});
