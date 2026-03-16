// Keep this minimal to avoid CSP issues later.
// Example: add a class to the body once loaded (useful for CSS transitions).
document.addEventListener("DOMContentLoaded", () => {
  document.body.classList.add("slc-loaded");
  // Replace "SecurityLawCase" in main content with branded spans (Security green, LawCase blue)
  applyBrandInContent();
});

function applyBrandInContent() {
  const brand = "SecurityLawCase";
  const replacement = document.createElement("span");
  replacement.innerHTML = '<span class="brand-security">Security</span><span class="brand-lawcase">LawCase</span>';
  const walk = (node) => {
    if (node.nodeType === Node.TEXT_NODE && node.textContent.includes(brand)) {
      const fragment = document.createDocumentFragment();
      const parts = node.textContent.split(brand);
      for (let i = 0; i < parts.length; i++) {
        if (i > 0) fragment.appendChild(replacement.cloneNode(true));
        if (parts[i]) fragment.appendChild(document.createTextNode(parts[i]));
      }
      node.parentNode.replaceChild(fragment, node);
      return;
    }
    if (node.nodeType === Node.ELEMENT_NODE) {
      const tag = node.tagName.toLowerCase();
      if (tag === "script" || tag === "style" || tag === "code" || tag === "pre") return;
    }
    Array.from(node.childNodes).forEach(walk);
  };
  const content = document.querySelector(".md-content__inner, .md-typeset");
  if (content) walk(content);
}

