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
  // Directly capturing all attributes of interest, including a general approach for 'aria-*' and 'data-*'
  for (const attr of el.attributes) {
    // Check if the attribute is one of the specified ones or starts with 'aria-' or 'data-'
    if (
      ["id", "role", "href", "alt", "value", "placeholder", "title"].includes(
        attr.name
      ) ||
      attr.name.startsWith("aria-") ||
      attr.name.startsWith("data-")
    ) {
      attributes[attr.name] = attr.value;
    }
  }
  return Object.keys(attributes).length === 0 ? [] : attributes;
}

function getContentInfo(el) {
  const contentTags = [
    "tittle",
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
  // Replace newline characters with spaces, make it single line, and trim to 50 characters
  textContent = textContent.replace(/\s+/g, " ").substring(0, 50);

  return {
    isContentTag: isContentTag,
    textContent: textContent,
    hasTextContent: textContent.length > 0,
    originalLength,
  };
}
// Asynchronously analyze an element and apply a deterministic ID if it's semantic
async function analyzeElement(element) {
  if (!element.tagName) return null;

  const nonInteractiveTags = [
    "script",
    "noscript",
    "link",
    "style",
    "meta",
    "code",
  ];
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

  // Use getMeaningfulAttributes and getContentInfo to decide if the element is significant
  const meaningfulAttributes = getMeaningfulAttributes(element);
  console.log(meaningfulAttributes);
  const contentInfo = getContentInfo(element);
  const isSignificant =
    Object.keys(meaningfulAttributes).length > 0 || contentInfo.hasTextContent;

  if (isSignificant) {
    await applyDeterministicId(element);
  }

  // Building the info object with meaningful attributes and content info
  let info = {
    tag: element.tagName.toLowerCase(),
    ...contentInfo, // Include content info details
    attributes: meaningfulAttributes, // Include meaningful attributes
  };

  if (element.hasAttribute("did")) {
    // Capture the deterministic ID if it has been set
    info.did = element.getAttribute("did");
  }

  // Recursively analyze child elements
  const childNodes = Array.from(element.children);
  for (let child of childNodes) {
    const childInfo = await analyzeElement(child);
    if (childInfo) {
      if (!info.children) {
        info.children = [];
      }
      info.children.push(childInfo);
    }
  }

  return info;
}

function printElementInfoYAML(info, depth = 0) {
  let output = "";
  const indent = "  ".repeat(depth);

  // Process only elements with a deterministic ID
  if (info.did) {
    // Begin constructing the YAML representation for the element
    output += `${indent}- tag: ${info.tag}, did: ${info.did}\n`;

    // Append meaningful attributes if present
    if (info.attributes && Object.keys(info.attributes).length > 0) {
      Object.entries(info.attributes).forEach(([key, value]) => {
        output += `${indent}  ${key}: ${value}\n`;
      });
    }

    // Append text content if available
    if (info.textContent) {
      output += `${indent}  text: "${info.textContent}"\n`;
    }
  }

  // Recursively process child elements with an increased indentation
  if (info.children && info.children.length > 0) {
    info.children.forEach((child) => {
      output += printElementInfoYAML(child, depth + 1);
    });
  }

  return output;
}

//Initialize and observe the document for changes, applying IDs and analyzing asynchronously
(async () => {
  /*
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

  observer.observe(document.body, { childList: true, subtree: true });*/

  // Analyze the entire document initially and print YAML
  const analyzedDOM = await analyzeElement(document.documentElement);
  const outputYAML = printElementInfoYAML(analyzedDOM);
  console.log(outputYAML);
})();
