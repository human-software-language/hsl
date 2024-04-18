function analyzeElement(element) {
  if (!element.tagName) return null;

  // Skip over elements that are not necessary for user interaction
  const nonInteractiveTags = ["script", "noscript", "link", "style", "code"];
  if (nonInteractiveTags.includes(element.tagName.toLowerCase())) {
    return null;
  }

  // Check if the element is visible
  const style = window.getComputedStyle(element);
  const isVisible =
    style.display !== "none" &&
    style.visibility !== "hidden" &&
    style.opacity !== "0" &&
    element.offsetWidth > 0 &&
    element.offsetHeight > 0;
  if (!isVisible) {
    return null;
  }

  // Ensure that className is a string before trying to manipulate it
  const classes =
    typeof element.className === "string" ? element.className : "";

  // Extract text from all child text nodes
  let textContent = "";
  element.childNodes.forEach((node) => {
    if (node.nodeType === Node.TEXT_NODE) {
      textContent += node.textContent.trim() + " ";
    }
  });

  const info = {
    tag: element.tagName.toLowerCase(),
    id: element.id ? `#${element.id}` : "",
    class: classes ? `.${classes.split(" ").join(".")}` : "",
    role: element.getAttribute("role") || "",
    ariaLabel: element.getAttribute("aria-label") || "",
    text: textContent.trim().substring(0, 50), // Limit text content to 50 characters
  };

  // Handling different element types
  if (
    info.tag === "input" ||
    info.tag === "select" ||
    info.tag === "textarea"
  ) {
    info.type = element.type;
    info.value = element.value;
    info.placeholder = element.placeholder || "";
  }

  if (info.tag === "a") {
    info.href = element.href;
  }

  if (info.tag === "img") {
    info.alt = element.alt;
  }

  // Recursively analyze child elements that are visible
  info.children = Array.from(element.children)
    .map(analyzeElement)
    .filter((child) => child); // Keep only non-null results from visible children

  return info;
}

function isElementSignificant(element) {
  // Checks if the element itself is significant
  let hasSignificantAttributes =
    element.id ||
    element.class ||
    element.role ||
    element.ariaLabel ||
    element.text ||
    element.href ||
    element.alt ||
    element.src ||
    element.value ||
    element.placeholder;
  let hasSignificantText = element.text.trim().length > 0;

  // Assume initially that if the element has significant attributes or text, it's significant
  if (hasSignificantAttributes || hasSignificantText) return true;

  // If the element has children, check if any child is significant recursively
  for (let child of element.children) {
    if (isElementSignificant(child)) return true; // If any child is significant, the element is considered significant
  }

  return false; // If no significant attributes, text, or significant children, the element is not significant
}

function isElementSemantic(el) {
  // Checks if an element is semantic based on specific attributes or content.
  let hasMeaningfulAttributes =
    el.id ||
    el.role ||
    el.ariaLabel ||
    el.value ||
    el.href ||
    el.alt ||
    el.src ||
    el.value ||
    el.placeholder;
  let isContentElement =
    el.text.trim().length > 0 ||
    ["a", "button", "input", "textarea", "img"].includes(el.tag);

  return hasMeaningfulAttributes || isContentElement;
}

function printElementInfoYAML(element, depth = 0) {
  let output = "";
  // Initial indentation based on the current depth.
  const indent = "  ".repeat(depth * 2);

  // Determine if the element is semantic.
  let isSemantic = isElementSemantic(element) || depth === 0; // The root element is always considered semantic.

  if (isSemantic) {
    // Construct the YAML representation for the current element.
    output += `${indent}- tag: ${element.tag}\n`;
    if (element.id) output += `${indent}  id: ${element.id}\n`;
    if (element.class)
      output += `${indent}  class: ${element.class
        .replace(/\s+/g, ".")
        .trim()}\n`;
    if (element.role) output += `${indent}  role: ${element.role}\n`;
    if (element.ariaLabel)
      output += `${indent}  aria-label: "${element.ariaLabel}"\n`;
    if (element.href) output += `${indent}  href: "${element.href}"\n`;
    if (element.alt) output += `${indent}  alt: "${element.alt}"\n`;
    if (element.type) output += `${indent}  type: ${element.type}\n`;
    if (element.value) output += `${indent}  value: "${element.value}"\n`;
    if (element.placeholder)
      output += `${indent}  placeholder: "${element.placeholder}"\n`;
    if (element.text.trim().length > 0)
      output += `${indent}  text: "${element.text.trim()}"\n`;
  }

  // Process child elements, increment depth only if the current element is included.
  element.children.forEach((child) => {
    // Only increment the depth if the current element is semantic.
    let childOutput = printElementInfoYAML(
      child,
      isSemantic ? depth + 1 : depth
    );
    if (childOutput) {
      output += childOutput;
    }
  });

  return output;
}

const rootElement = document.documentElement;
const analyzedDOM = analyzeElement(rootElement);
const outputYAML = printElementInfoYAML(analyzedDOM);
console.log(outputYAML);
