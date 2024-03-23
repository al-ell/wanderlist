# WanderList




Link to deployed site: []()

![GitHub last commit]()


## CONTENTS

* [User Experience](#user-experience)
  * [Project Goals](#project-goals)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)
  * [Database Schema & User Journey](#database-schema--user-journey)
    * [User Journey](#user-journey)
    * [First Draft Database Schema](#first-draft-database-schema)
    * [Final Database Schema](#final-database-schema)

* [Features](#features)
  * [Elements Found on Each Page](#elements-found-on-each-page)
  * [Future Implementations](#future-implementations)
  * [Accessibility](#accessibility)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Databases Used](#databases-used)
  * [Frameworks Used](#frameworks-used)
  * [Libraries & Packages Used](#libraries--packages-used)
  * [Programs Used](#programs-used)
    * [API](api)
    * [Error Handling](#error-handling)
    * [Defensive Programming](#defensive-programming)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)

* [Testing](#testing)
  
* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

- - -

## User Experience

### Project Goals



### User Stories

#### __Target Audience__

The target audience of the website are people who are planning to travel to other countries. The website will have inspiration from others as well as practical information about different countries. 


#### __First Time Visitor Goals__

As a first time visitor to the website I want to:

* Create an account
* Search for information about different cournties
* Create and save a list, or multiple lists, of destinations they want to travel to
* Read other user's travel journal entries
* Create their own journal entries


#### __Returning Visitor Goals__

As a first time visitor to the website I want to:

* Login to the account created
* Update a country from "want to go" to "travelled to" after a trip
* Record information about their trip in a travel journal
* Edit and delete journal entries


#### __Admin User__

As an admin user I want to be able to:

* Remove offensive content (pending update)

- - -

## Design

### Colour Scheme

I have chosen colours that are vibrant for the website. 
![colour pallete](/documentation/design/colorPalette1.png)

### Typography

Google Fonts was used to import the chosen fonts for use in the site.

#### Fredricka The Great
![Logo font](/documentation/design/fredrickaTheGreat.png)

#### Caveat Brush
![Header font](/documentation/design/caveatBrush.png)

#### Quattrocento
![Body font](/documentation/design/quattrocento.png)


### Imagery

Imagery for the website was created using [Microsoft Bing Copilot (AI)](https://www.bing.com/images/create?FORM=GENILP) 

### Wireframes

Wireframes were created for mobile, tablet and desktop using Balsamiq.

#### __Register Page__

![Register Page]()

#### __Login Page__

![Login Page]()

#### __Logged In Home/Profile Page__

![Home Page](/documentation/wireframes/profile.png)

#### __Journal Feed Page__

![Journal Feed Page](/documentation/wireframes/read.png)

#### __Country Search Page__

![Country Search Page](/documentation/wireframes/find.png)

#### __Add Journal Entry Page__

![Add Journal Entry Page](/documentation/wireframes/document.png)

#### __My Trips Page__

![My Trips Page](/documentation/wireframes/myTrips.png)

### __Itinerary/ Trip Page__

![Itinerary/ Trip Page](/documentation/wireframes/Itinerary1.png)


#### __Error Page__

to design

### Database Schema & User Journey

#### __User Journey__

![User Flow Chart](/documentation/design/websiteFlowChart.png)


#### __ Database Plan__

| Key | Name | Type |
| --- | --- | --- |
| `Journal` |
|  | Trip Name(unique) | TextInput|
| ForeignKey | Author | User model |
|  | Trip Rating |  | 
|  | Where | Select from API data |
|  | When | DateTime | 
|  | How | TextInput |
| ForeignKey | Add to Itinerary | User Model |
| `Itineraries` | 
|  | Name(unique) |  |
| ForeignKey | Author | User model |
|  | Country Name | Selected from API |  


- - -

## Features


### Elements found on each page

* Favicon - created at [favicon.io](https://favicon.io/favicon-generator/). I decided to keep it as a simple W from the website's logo.

* Navbar. - The Navbar is displayed on all pages from the base.html template. Links to all pages are featured, the links vary depending on the user being logged in.

  __User logged in Navbar__


  __User not logged in Navbar__



- - -

### Home Page

![Home Page]()

### Login Page

![Log in Page]()

### Register Page

![Register Page]()

### Profile Page

![Profile Page]()


### Edit collection? Page

![Edit  Page]()


### Add Review Page

![Add Review Page]()

### Edit Review Page

![Edit Review Page]()


### Error Page

![Error Page]()

- - -

### Future Implementations


### Accessibility




- - -

## Technologies Used

### Languages Used

HTML, CSS, Javascript, Python

### Databases Used

[MongoDB](https://www.mongodb.com/) 

[PostgreSQL](https://www.postgresql.org/) 


### Frameworks Used

[Flask](https://pypi.org/project/Flask/) - A micro framework.

[Materialize](https://materializecss.com/)

### Libraries & Packages Used

[PyMongo](https://pypi.org/project/pymongo/) - Python Driver for MongoDB.

[SQLAlchemy](https://pypi.org/project/SQLAlchemy/) - Database abstraction library, used to interact with PostgreSQL.

[Flask Login](https://flask-login.readthedocs.io/en/latest/)


### Programs Used

[Pip](https://pypi.org/project/pip/) - Tool for installing python packages.

[Jinja](https://jinja.palletsprojects.com/en/3.1.x/) - Templating engine.

[Balsamiq](https://balsamiq.com/) - Used to create wireframes.

[Figma](https://www.figma.com/) - To make flow charts.

[Git](https://git-scm.com/) - For version control.

[Github](https://github.com/) - To save and store the files for the website.

[Google Fonts](https://fonts.google.com/) - To import the fonts used on the website.

[Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - To troubleshoot and test features, solve issues with responsiveness and styling.

[Tiny PNG](https://tinypng.com/) To compress images for use in the readme.

[Birme](https://www.birme.net/) To resize images and convert to webP format for the site.

[Favicon.io](https://favicon.io/) To create the favicon.

[Am I Responsive?](http://ami.responsivedesign.is/) To show the website image on a range of devices.


### API

I have chosen to use the [Rest Countries API](https://restcountries.com/) provide useful information to website users.

#### __How to Access API__


### Error Handling


### Defensive Programming



## Deployment & Local Development


### Deployment


### Local Development


#### How to Fork


#### How to Clone


## Testing

Please see [TESTING.md](TESTING.md) for all testing performed
- - -

## Credits


### Code Used

- How to link an API to Flask
Uses the cat facts api, but I was able to apply this to rest countries api with ease
(Youtube video)[https://www.youtube.com/watch?v=F_SBxcV335k]


- Flask Blueprints
To update the routing as the project is larger
[Intro to Flask Blueprints](https://www.youtube.com/watch?v=pjVhrIJFUEs)

- Flask Authentication
To initiate user login with Flask libraries
[Learn Flask Login](https://www.youtube.com/watch?v=71EU8gnZqZQ)

### Content


### Media


### Acknowledgments

