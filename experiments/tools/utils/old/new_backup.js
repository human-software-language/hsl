// Helper function to generate a deterministic path for an element
function getPathTo(element) {
  if (element.id) {
    return 'id("' + element.id + '")';
  }
  if (element === document.body) {
    return element.tagName;
  }
  var ix = 0;
  var siblings = element.parentNode.childNodes;
  for (var i = 0; i < siblings.length; i++) {
    var sibling = siblings[i];
    if (sibling === element) {
      return (
        getPathTo(element.parentNode) +
        "/" +
        element.tagName +
        "[" +
        (ix + 1) +
        "]"
      );
    }
    if (sibling.nodeType === 1 && sibling.tagName === element.tagName) {
      ix++;
    }
  }
}

// Function to apply a deterministic ID based on the element's path
async function applyDeterministicId(element) {
  const path = getPathTo(element);
  const encoder = new TextEncoder();
  const data = encoder.encode(path);
  const hashBuffer = await crypto.subtle.digest("SHA-256", data);
  const hashArray = Array.from(new Uint8Array(hashBuffer)); // Convert buffer to byte array
  const hashHex = hashArray
    .map((b) => b.toString(36).padStart(2, "0"))
    .join("");
  const uniqueId = hashHex.substring(0, 4); // Take first 4 characters for simplicity
  element.setAttribute("did", uniqueId);
}

function isElementSemantic(el) {
  // Ensure el is a DOM element capable of having attributes
  if (!el || typeof el.hasAttribute !== "function") {
    console.error(
      "Attempted to check semantic significance of a non-element:",
      el
    );
    return false;
  }

  // Check for semantic significance through attributes
  let hasMeaningfulAttributes = [
    "id",
    "role",
    "aria-label",
    "href",
    "alt",
    "src",
    "value",
    "placeholder",
  ].some((attr) => el.hasAttribute(attr));
  let isContentElement =
    el.textContent.trim().length > 0 ||
    ["a", "button", "input", "textarea", "img"].includes(
      el.tagName.toLowerCase()
    );

  return hasMeaningfulAttributes || isContentElement;
}

function isElementSemantic(el) {
  // Ensure el is a DOM element capable of having attributes
  if (!el || typeof el.hasAttribute !== "function") {
    console.error(
      "Attempted to check semantic significance of a non-element:",
      el
    );
    return false;
  }
  // Enhanced to check for additional meaningful attributes and more tags
  const meaningfulAttributes = [
    "id",
    "role",
    "aria-*",
    "href",
    "alt",
    "src",
    "value",
    "placeholder",
    "title",
    "data-*",
  ].some((attr) => el.hasAttribute(attr));
  const contentTags = [
    "a",
    "button",
    "input",
    "textarea",
    "img",
    "label",
    "select",
    "section",
    "article",
    "header",
    "footer",
    "nav",
    "aside",
    "main",
    "figure",
    "figcaption",
    "table",
    "th",
    "td",
    "video",
    "audio",
    "ul",
    "ol",
    "li",
    "p",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
  ];
  const isContentElement =
    contentTags.includes(el.tagName.toLowerCase()) ||
    el.textContent.trim().length > 0;

  return meaningfulAttributes || isContentElement;
}

// Asynchronously analyze an element and apply a deterministic ID if it's semantic
async function analyzeElement(element) {
  if (!element.tagName) return null;

  const nonInteractiveTags = ["script", "noscript", "link", "style", "code"];
  if (nonInteractiveTags.includes(element.tagName.toLowerCase())) {
    return null;
  }

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

  let textContent = "";
  element.childNodes.forEach((node) => {
    if (node.nodeType === Node.TEXT_NODE) {
      textContent += node.textContent.trim() + " ";
    }
  });

  if (
    isElementSemantic({
      tag: element.tagName.toLowerCase(),
      text: textContent,
    })
  ) {
    await applyDeterministicId(element);
  }

  const info = {
    tag: element.tagName.toLowerCase(),
    did: element.getAttribute("did"), // Now capturing the deterministic ID
    text: textContent.trim().substring(0, 50),
    children: [],
  };

  // Additional details based on element type
  if (["input", "select", "textarea"].includes(info.tag)) {
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

  const childNodes = Array.from(element.children);
  for (let child of childNodes) {
    const childInfo = await analyzeElement(child);
    if (childInfo) {
      info.children.push(childInfo);
    }
  }

  return info;
}

function printElementInfoYAML(element, depth = 0) {
  let output = "";
  const indent = "  ".repeat(depth);

  // Basic element representation
  output += `${indent}- tag: ${element.tag}\n`;

  // Append deterministic ID if available
  if (element.did) {
    output += `${indent}  did: ${element.did}\n`;
  }

  // Append other semantically meaningful attributes
  const attributes = [
    "role",
    "aria-label",
    "href",
    "alt",
    "src",
    "type",
    "value",
    "placeholder",
  ];
  attributes.forEach((attr) => {
    if (element[attr]) {
      output += `${indent}  ${attr}: ${element[attr]}\n`;
    }
  });

  // Include text content if present, limited to first 50 characters for brevity
  if (element.text) {
    output += `${indent}  text: "${element.text.substring(0, 50)}"\n`;
  }

  // Recursively process and print children
  if (element.children && element.children.length > 0) {
    output += `${indent}  children:\n`;
    element.children.forEach((child) => {
      output += printElementInfoYAML(child, depth + 2);
    });
  }

  return output;
}

// Initialize and observe the document for changes, applying IDs and analyzing asynchronously
(async () => {
  const observer = new MutationObserver(async (mutations) => {
    for (let mutation of mutations) {
      for (let node of mutation.addedNodes) {
        if (node.nodeType === 1) {
          // ELEMENT_NODE
          await analyzeElement(node);
        }
      }
    }
  });

  observer.observe(document.body, { childList: true, subtree: true });

  // Analyze the entire document initially and print YAML
  const analyzedDOM = await analyzeElement(document.documentElement);
  const outputYAML = printElementInfoYAML(analyzedDOM);
  console.log(outputYAML);
})();
