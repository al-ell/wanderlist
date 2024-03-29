# Wanderlist -  Testing



Visit the deployed site: []()

- - -

## CONTENTS

* [AUTOMATED TESTING](#automated-testing)
  * [W3C Validator](#w3c-validator)
  * [JavaScript Validator](#javascript-validator)
  * [Python Validator](#python-validator)
  * [Lighthouse](#lighthouse)
  * [WAVE Testing](#wave-testing)
* [MANUAL TESTING](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
  * [Full Testing](#full-testing)
* [BUGS](#bugs)
  * [Solved Bugs](#solved-bugs)
  * [Known Bugs](#known-bugs)



- - -

## AUTOMATED TESTING

### W3C Validator

[W3C](https://validator.w3.org/) 


- - -

### JavaScript Validator



- - -

### Python Validator

[PEP8](http://pep8online.com/)

- - -

### Lighthouse


### Desktop Results

- - -

### WAVE Testing


- - -

## MANUAL TESTING

### Testing User Stories

| Goals | How are they achieved? | Image |
| :--- | :--- | :--- |
| `First Time Visitors` |
|  |  |  |
|`Returning Visitors`|
|  |  |  |
|`Admin User` |
|  |  |  |

- - -

### Full Testing


| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| ----- | --- | --- | --- | --- |
| `Navbar` |
| Click on home page nav link | index page loads | clicking on link   | taken to page | pass      |
| Click on trips page nav link | trips page loads | clicking on link        | taken to page | pass      |
| Click on journal page nav link  | journal page loads | clicking on link        | taken to page   | pass      |
| Click on profile page nav link   | profile page loads  | clicking on link        | taken to page    | pass      |
| Click on logout nav link  | User is logged out  | clicking on link        | taken to homepage and pages that can only be accessed when logged in shown | pass      |
| `Footer` |
| Click on twitter icon | twitter loads in new tab | clicking on link | twitter opens in new tab | pass |
| Click on youtube icon |youtube loads in new tab | clicking on link | youtube opens in new tab | pass |
| Click on facebook icon | facebook loads in new tab | clicking on link | facebook opens in new tab | pass |
| Click on instagram |instagram loads in new tab | clicking on link | instagram opens in new tab | pass |
| `Home Page` |
| Click on signup button | taken to signup page | clicking on button | taken to signup page | pass |
| Click on login button | taken to login page | clicking on button | taken to login page | pass |
| `Log in Page` |
| enter pre registered valid details into form | form submits | clicking on submit | taken to login page | pass |
| enter invalid valid details into form | user is informed data not valid, form won't submit | entering invalid details | HTML5 messages tell the user data is not valid | pass |
| enter an incorrect username or password into form | user is informed username or password is incorred via flash message, form won't submit | entering invalid details | user is informed username or password is incorred via flash message, form won't submit | pass |
| `Register Page` |
| enter invalid valid details into form | user is informed data not valid, form won't submit | entering invalid details | HTML5 messages tell the user data is not valid | pass |
| enter an existing username into form | user is informed username is taken via flash message, form won't submit | entering an exisiting username | user is informed username is taken via flash message, form won't submit | pass |
| enter a password that doesn't match criteria | user is informed of password criteria, form won't submit | entering invalid details | user is informed of password criteria, form won't submit | pass |
|   |   |   |   |  |
| `Trips Page` |
| Click on "add trip" button | taken to add trips page | clicking on button | taken to add trips page | pass |
| Click on "edit trip" button | taken to add trips page | clicking on button | taken to add trips page | pass |
| Click on "delete" button | delete modal pops up | clicking on delete button | delete modal pops up | pass |
| Click on journal entry name link | taken to edit journal entry page | clicking on button | taken to edit journal entry page | pass |
| `Add Trip Page`|
| enter invalid valid details into form | user is informed data not valid, form won't submit | entering invalid details | HTML5 messages tell the user data is not valid | pass |
| leave any details blank or only containt a space in the form | user is informed data is missing, form won't submit | attempting to enter the form with blank details | user is informed data is missing, form won't submit | pass |
| enter an existing trip name into form | user is informed trip name is taken via flash message, form won't submit | entering an exisiting existing trip | user is informed trip name is taken via flash message, form won't submit |  |
| `Edit Trip Page` |
| expect form to be pre-populated with correct data on page load | form is pre populated | clicking edit button on trips page | form is pre-populated | pass |
| enter invalid valid details into form | user is informed data not valid, form won't submit | entering invalid details | HTML5 messages tell the user data is not valid | pass |
| leave any details blank or only containt a space in the form | user is informed data is missing, form won't submit | attempting to enter the form with blank details | user is informed data is missing, form won't submit | pass |
| enter an existing trip name into form | user is informed trip name is taken via flash message, form won't submit | entering an exisiting existing trip | user is informed trip name is taken via flash message, form won't submit |  |
| `Journal Page` |
| Click on "add journal" button | taken to add journal page | clicking on button | taken to add journal page | pass |
| Click on "edit journal" button | taken to add journal page | clicking on button | taken to add journal page | pass |
| Click on "delete" button | delete modal pops up | clicking on delete button | delete modal pops up | pass |
| Click on trip name link | taken to trips page | clicking on button | taken to trips page |  |
| `Add Journal Page`|
| enter invalid valid details into form | user is informed data not valid, form won't submit | entering invalid details | HTML5 messages tell the user data is not valid | pass |
| leave any details blank or only containt a space in the form | user is informed data is missing, form won't submit | attempting to enter the form with blank details | user is informed data is missing, form won't submit | pass |
| choose a trip using the dropdown menu | user sees  and can selsect existing trips that the journal entry can be added to | selecting an existing trip from the menu | user sees  and can selsect existing trips that the journal entry can be added to | pass |
| user is unable to select a date in the future | future dates are inactive in the calendar pop up | attempting to select a date | future dates are inactive in the calendar pop up | |
| enter an existing journal entry name into form | user is informed journal name is taken via flash message, form won't submit | entering an exisiting existing journal entry name | user is informed journal entry name is taken via flash message, form won't submit |  |
| `Edit Journal Page`|
| expect form to be pre-populated with correct data on page load | form is pre populated | clicking edit button on trips page | form is pre-populated | pass |
| enter invalid valid details into form | user is informed data not valid, form won't submit | entering invalid details | HTML5 messages tell the user data is not valid | pass |
| leave any details blank or only containt a space in the form | user is informed data is missing, form won't submit | attempting to enter the form with blank details | user is informed data is missing, form won't submit | pass |
| choose a trip using the dropdown menu | user sees  and can selsect existing trips that the journal entry can be added to | selecting an existing trip from the menu | user sees  and can selsect existing trips that the journal entry can be added to | pass |
| user is unable to select a date in the future | future dates are inactive in the calendar pop up | attempting to select a date | future dates are inactive in the calendar pop up | |
| enter an existing journal entry name into form | user is informed journal name is taken via flash message, form won't submit | entering an exisiting existing journal entry name | user is informed journal entry name is taken via flash message, form won't submit |  |
| `Delete Modal` |
| click on the "cancel" button | taken back to trips or journal pages | clicking cancel | taken back to trips or journal pages | pass |
|click on the "delete" button | entry is deleted, taken back to trips or journal pages | clicking delete | entry is deleted, taken back to trips or journal pages | pass |
| `Profile Page` |
| Click on "add journal" button | taken to add journal page | clicking on button | taken to add journal page | pass |
| Click on "add trip" button | taken to add trip page | clicking on button | taken to add trip page | pass |
| `Error Page` |
|   |   |   |   |   |
| `Accessability`  |
| title or alt text for all non-text media | text appears/screenreader will read out                                            | hovering over media     | text appears/screenreader will read out | pass      |

 - - -

## BUGS

### Solved Bugs

| No | Bug | How I solved the issue |
| :--- | :--- | :--- |

- - -

### Known Bugs

| No | Bug | |
| :--- | :--- | :--- |
