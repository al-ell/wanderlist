// Materlialize JS: 
document.addEventListener('DOMContentLoaded', function() {
    // Mobile side menu
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // initialize dropdown
    let dropdown_trigger = document.querySelectorAll('.dropdown-trigger');
    M.Dropdown.init(dropdown_trigger);

    // initialize datepicker
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
        format: "dd mmm, yyyy",
        i18n: {done: "Choose"}
    });

    // form select initialization
    let selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);

    // initialize collapsible 
    let collapsibles = document.querySelectorAll('.collapsible');
    M.Collapsible.init(collapsibles);

    // initialize modal
    let modal = document.querySelectorAll('.modal');
    M.Modal.init(modal);



    // When the user scrolls the page, execute myFunction
    window.onscroll = function() {stickyHeader()};

    // Get the header
    let header = document.getElementById("base-header");

    // Get the offset position of the navbar
    let sticky = header.offsetTop;

    // Add the sticky class to the header when you reach its scroll position. Remove "sticky" when you leave the scroll position
    function stickyHeader() {
        if (window > sticky) {
            header.classList.add("sticky");
        } else {
            header.classList.remove("sticky");
        }
    }

});