// Materlialize JQuery: 
$(document).ready(function(){
    // Mobile side menu
    $(".sidenav").sidenav({edge: "right"});

    // initialize dropdown
    $('.dropdown-trigger').dropdown();

    // initialize datepicker
    $(".datepicker").datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 15,
        maxDate: "1",
        showClearBtn: true,
        i18n: {
            done: "Choose"
        }
    });

    // form select initialization
    $('select').formSelect();

    // initialize collapsible 
    $('.collapsible').collapsible();

    // initialize modal
    $('.modal').modal();

});