function analyzeElement(element) {
  if (!element.tagName) return null;

  // Skip over elements that are not necessary for user interaction
  const nonInteractiveTags = ["script", "noscript", "link", "style", , "code"];
  if (nonInteractiveTags.includes(element.tagName.toLowerCase())) {
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
    text: textContent.trim().substring(0, 50), // Text content (if applicable)
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

  // Exclude image sources but keep alt text for accessibility
  if (info.tag === "img") {
    info.alt = element.alt;
  }

  // Recursively analyze child elements
  info.children = Array.from(element.children)
    .map((child) => analyzeElement(child))
    .filter((child) => child);

  return info;
}

function printElementInfo(element, depth = 0, lastElement = true, output = "") {
  const pipe = "│   ";
  const branch = "├── ";
  const corner = "└── ";
  const space = "    ";

  let prefix = "";
  for (let i = 0; i < depth; i++) {
    prefix +=
      i === depth - 1
        ? lastElement
          ? corner
          : branch
        : element.parents[i]
        ? space
        : pipe;
  }

  if (
    element.text ||
    element.role ||
    element.ariaLabel ||
    element.href ||
    element.src ||
    element.value ||
    element.alt ||
    element.placeholder
  ) {
    let textContent = element.text.includes("\n")
      ? `\`${element.text}\``
      : `"${element.text}"`; // Handle multiline text

    output += `${prefix}${element.tag}${element.id}${element.class}`;

    if (element.role) output += ` (role: ${element.role})`;
    if (element.ariaLabel) output += ` (aria-label: ${element.ariaLabel})`;
    if (element.text) output += ` (text: ${textContent})`;
    if (element.href) output += ` (href: ${element.href})`;
    if (element.placeholder) output += ` (placeholder: ${element.placeholder})`;
    if (element.alt) output += ` (alt: ${element.alt})`;
    if (element.src) output += ` (src: ${element.src}, alt: ${element.alt})`;
    if (element.value) output += ` (value: ${element.value})`;

    output += "\n"; // Add a newline character after each element
  }

  // Recursively process child elements
  element.children.forEach((child, index) => {
    child.parents = (element.parents || []).concat(lastElement);
    output = printElementInfo(
      child,
      depth + 1,
      index === element.children.length - 1,
      output
    );
  });

  return output;
}

const rootElement = document.documentElement;
const analyzedDOM = analyzeElement(rootElement);
const output = printElementInfo(analyzedDOM);

console.log(output);
