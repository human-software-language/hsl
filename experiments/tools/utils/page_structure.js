// Helper function to generate a deterministic path for an element
function getPathTo(element) {
  if (!element || element === document.body) {
    return element ? element.tagName : "";
  }
  if (element.id) {
    return 'id("' + element.id + '")';
  }

  var ix = 0;
  var siblings = element.parentNode ? element.parentNode.childNodes : [];
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

function getMeaningfulAttributes(el) {
  let attributes = {};
  for (const attr of el.attributes) {
    // Check if the attribute is one of the specified ones or starts with 'aria-' or 'data-'
    // Removed "href"
    if (
      [
        "id",
        "role",
        "alt",
        "value",
        "placeholder",
        "title",
        "type",
        "for",
      ].includes(attr.name) ||
      attr.name.startsWith("aria-") ||
      attr.name.startsWith("data-")
    ) {
      attributes[attr.name] = attr.value;
    }
  }
  return Object.keys(attributes).length === 0 ? [] : attributes;
}

function isImportantEl(el) {
  const importantTags = [
    "a",
    "form",
    "button",
    "input",
    "textarea",
    "main",
    "table",
    "video",
    "audio",
    "section",
    "article",
    "aside",
    "header",
    "footer",
    "details",
    "summary",
    "iframe",
    "embed",
    "object",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
  ];

  return importantTags.includes(el.tagName.toLowerCase());
}

function getContentInfo(el) {
  const contentTags = [
    "title",
    "body",
    "a",
    "form",
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
    "div",
    "aside",
    "main",
    "figure",
    "figcaption",
    "iframe",
    "embed",
    "object",
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
    "blockquote",
  ];

  // Check if the element's tag is in the list of content tags
  const isContentTag = contentTags.includes(el.tagName.toLowerCase());

  // Gather and trim text content of the element, make it single line and limit to 50 characters
  let textContent = Array.from(el.childNodes)
    .reduce((acc, node) => {
      if (node.nodeType === Node.TEXT_NODE) {
        acc += node.textContent.trim() + " ";
      }
      return acc;
    }, "")
    .trim();

  const originalLength = textContent.length;
  // Replace newline characters with spaces, make it single line, and trim to 45 characters
  textContent = textContent.replace(/\s+/g, " ").substring(0, 45);

  return {
    isContentTag: isContentTag,
    textContent:
      originalLength !== textContent.length ? textContent + "..." : textContent,
    hasTextContent: textContent.length > 0,
    originalLength,
  };
}

// Asynchronously analyze an element and its children, applying a deterministic ID if deemed necessary
async function analyzeElement(element) {
  if (!element.tagName) return null; // Skip non-element nodes

  const isVisibleOrRelevant = (() => {
    const nonInteractiveTags = [
      "script",
      "noscript",
      "link",
      "style",
      "meta",
      "code",
    ];
    if (nonInteractiveTags.includes(element.tagName.toLowerCase())) {
      return false; // Considered not relevant for analysis
    }

    const style = window.getComputedStyle(element);
    return (
      style.display !== "none" &&
      style.visibility !== "hidden" &&
      style.opacity !== "0" &&
      element.offsetWidth > 0 &&
      element.offsetHeight > 0
    );
  })();

  let info = {
    tag: element.tagName.toLowerCase(),
    attributes: getMeaningfulAttributes(element),
  };

  // Apply deterministic ID and analyze content if element is visible or relevant
  if (isVisibleOrRelevant) {
    const contentInfo = getContentInfo(element);
    const isImportant = isImportantEl(element) || element.tagName.includes("-"); // Assume custom elements are important
    if (
      Object.keys(info.attributes).length > 0 ||
      contentInfo.hasTextContent ||
      isImportant
    ) {
      await applyDeterministicId(element);
      // Include content info and deterministic ID if applicable
      info = { ...info, ...contentInfo, did: element.getAttribute("did") };
    }
  }

  // Recursively analyze all child elements without filtering
  const childNodes = Array.from(element.children);
  info.children = await Promise.all(
    childNodes.map((child) => analyzeElement(child))
  ).then((results) => results.filter((childInfo) => childInfo !== null));

  return info;
}

function printElementInfoYAML(info, depth = 0) {
  let output = "";

  // Check if the current element has a 'did', process only if true
  if (info.did) {
    const indent = "  ".repeat(depth);
    let elementLine = `- ${info.tag}[did="${info.did}"]`;

    // Process attributes if any
    if (info.attributes) {
      const attributes = Object.entries(info.attributes)
        .map(([key, value]) => `${key}: ${value}`)
        .join(", ");
      elementLine += ` ${attributes}`;
    }

    // Add text content if available
    if (info.textContent) {
      elementLine += `text: "${info.textContent}"`;
    }

    // Append the processed line to the output
    output += `${indent}${elementLine}\n`;

    // Increment depth for child elements
    depth++;
  }

  // Process child elements recursively
  if (info.children && info.children.length > 0) {
    info.children.forEach((child) => {
      output += printElementInfoYAML(child, depth);
    });
  }

  return output;
}

//Initialize and observe the document for changes, applying IDs and analyzing asynchronously
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

  // TODO: Understand repetitive blocks and shorten the output

  // Analyze the entire document initially and print YAML
  const analyzedDOM = await analyzeElement(document.documentElement);
  const outputYAML = printElementInfoYAML(analyzedDOM);
  console.log(outputYAML);
  return outputYAML;
})();
