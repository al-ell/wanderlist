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
        format: "dd mm, yyyy",
        i18n: {done: "Choose"}
    });

    // form select initialization
    let selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);
});