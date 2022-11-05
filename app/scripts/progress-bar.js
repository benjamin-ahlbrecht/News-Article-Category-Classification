function progressBar() {
    const pBar = document.getElementById("header-progress-inner");
    let width = window.scrollY / window.scrollMaxY * 100;
    pBar.style.width = width.toString() + "%";
}


window.addEventListener("scroll", progressBar);
window.addEventListener("resize", progressBar);
window.addEventListener("load", progressBar);

