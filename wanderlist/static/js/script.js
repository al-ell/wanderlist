// Materlialize JS: 
document.addEventListener('DOMContentLoaded', function() {
    // Mobile side menu
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // initialize dropdown
    let dropdown_trigger = document.querySelectorAll('.dropdown-trigger');
    M.Dropdown.init(dropdown_trigger);
});