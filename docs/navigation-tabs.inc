<script>
document.addEventListener("DOMContentLoaded", () => {
  const toc = document.getElementById("TOC");
  const collectionLink = toc?.querySelector('a[data-scroll-target="#collections"]');
  const collectionItem = collectionLink?.closest("li");
  const groups = collectionItem?.querySelector("ul");
  if (!toc || !groups) {
    return;
  }

  const hierarchy = toc.querySelector(":scope > ul");
  const title = toc.querySelector(":scope > h2");
  const tabs = document.createElement("div");
  tabs.className = "nav nav-tabs vocabulary-navigation-tabs";
  tabs.setAttribute("role", "tablist");
  tabs.setAttribute("aria-label", "Vocabulary navigation");

  for (const [label, list] of [["Hierarchy", hierarchy], ["Groups", groups]]) {
    const id = `vocabulary-${label.toLowerCase()}`;
    const active = label === "Hierarchy";
    const tab = document.createElement("button");
    tab.id = `${id}-tab`;
    tab.className = `nav-link${active ? " active" : ""}`;
    tab.type = "button";
    tab.textContent = label;
    tab.setAttribute("role", "tab");
    tab.setAttribute("aria-controls", id);
    tab.setAttribute("aria-selected", String(active));
    tab.tabIndex = active ? 0 : -1;
    tab.addEventListener("click", () => {
      for (const button of tabs.children) {
        const selected = button === tab;
        button.classList.toggle("active", selected);
        button.setAttribute("aria-selected", String(selected));
        button.tabIndex = selected ? 0 : -1;
        document.getElementById(button.getAttribute("aria-controls")).hidden = !selected;
      }
    });
    tab.addEventListener("keydown", (event) => {
      if (event.key === "ArrowLeft" || event.key === "ArrowRight") {
        event.preventDefault();
        const other = Array.from(tabs.children).find((button) => button !== tab);
        other.click();
        other.focus();
      }
    });
    tabs.append(tab);
    const panel = document.createElement("div");
    panel.id = id;
    panel.setAttribute("role", "tabpanel");
    panel.setAttribute("aria-labelledby", tab.id);
    panel.hidden = !active;
    panel.append(list);
    toc.append(panel);
  }
  collectionItem.remove();
  if (title) {
    title.replaceWith(tabs);
  } else {
    toc.prepend(tabs);
  }
});
</script>
