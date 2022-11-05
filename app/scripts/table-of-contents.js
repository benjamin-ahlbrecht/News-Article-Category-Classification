function tableOfContents() {
    const headings = document.querySelectorAll(["h2", "h3"]);
    var tableOfContents = document.getElementById("table-of-contents");

    for (let i=0; i<headings.length; i++) {
        let heading = headings.item(i);
        let headingName = heading.nodeName;
        let headingText = heading.id;

        let listItem = document.createElement("li");
        let linkItem = document.createElement("a");
        let node = document.createTextNode(headingText);

        linkItem.appendChild(node);
        linkItem.href = "#" + headingText;
        linkItem.className = "better-nav"
        listItem.appendChild(linkItem);

        switch(headingName) {
            case "H2":
                tableOfContents.appendChild(listItem);
                break;
            case "H3":
                let orderedList = document.createElement("ol");
                orderedList.id = "table-of-contents";
                orderedList.appendChild(listItem);
                tableOfContents.appendChild(orderedList);
                break;
        }
    }
}


window.addEventListener("load", tableOfContents);

