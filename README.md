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
    * [Database Plan](#database-plan)

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
* Login to the accoutn created
* Make a list of trips they are planning
* Document their own journal entries about their trips
* Read other user's travel journal entries


#### __Returning Visitor Goals__

As a returning time visitor to the website I want to:

* Login to the account created
* Make a list of trips they are planning
* Record information about their trip in a travel journal
* Edit and delete journal entries and trips
* Read other user's travel journal entries

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


#### __Database Plan__

| Key | Name | Type |
| --- | --- | --- |
| `Journal` |
|  | Trip Name(unique) | TextInput|
|  | Description | TextInput |
|  | Where | TextInput |
|  | When | DateTime |
|  | How | TextInput |
|  | Author | User model |
| ForeignKey | Add to Itinerary | User Model |
| `Itineraries` |
|  | Name(unique) | TextInput |
|  | Author | User model |
|  | Country/Area Name | TextInput |
| `User` |
|  | Username(unique) | TextInput |
|  | Name | TextInput | 
|  | Password | TextInput |


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

### Trips Page
![Trips Page]()

### Add Trip Page

![Add Trip Page]()

###  Edit Trips Page
![Edit Trips Page]()

### Journal Page
![Journal Page]()

### Document Page
![Document Page]()

###  Edit Document Page
![Edit Document Page]()

### Error Page

![Error Page]()

- - -

### Future Implementations

- Link the Country option to an RestCountries API to ensure correct use of country option.
- Use the api to provide useful information about different travel destinations
- Allow users to follow friends.


### Accessibility




- - -

## Technologies Used

### Languages Used

HTML, CSS, Javascript, Python

- - -

### Databases Used

[PostgreSQL](https://www.postgresql.org/) 

- - -

### Frameworks Used

[Flask](https://pypi.org/project/Flask/) - A micro framework.

[Materialize](https://materializecss.com/)

- - -

### Libraries & Packages Used

[SQLAlchemy](https://pypi.org/project/SQLAlchemy/) - Database abstraction library, used to interact with PostgreSQL.

[Flask Login](https://flask-login.readthedocs.io/en/latest/)

- - -

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

[Any webP](https://www.anywebp.com/) To resize images and convert to webP format for the site.

[Favicon.io](https://favicon.io/) To create the favicon.

[Am I Responsive?](http://ami.responsivedesign.is/) To show the website image on a range of devices.


### Error Handling


### Defensive Programming


## Deployment & Local Development

### Local Development

#### How to Fork

1. On GitHub.com, navigate to the octocat/Spoon-Knife repository
2. In the top-right corner of the page, click **Fork**
3. Under "Owner," select the dropdown menu and click an owner for the forked repository
4. By default, forks are named the same as their upstream repositories. Optionally, to further distinguish your fork, in the "Repository name" field, type a name
5. Optionally, in the "Description" field, type a description of your fork
6. Optionally, select **Copy the DEFAULT branch only**
7. Click **Create fork**

#### How to Clone

1. On GitHub.com, navigate to the main page of the repository 2. Above the list of files, click **<> Code** 3. Copy the URL for the repository
   _To clone the repository using HTTPS, under "HTTPS", click **clipboard icon**
   _ To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click SSH, then click **clipboard icon** \* To clone a repository using GitHub CLI, click GitHub CLI, then click **copy icon** 4. Open Terminal, change the current working directory to the location where you want the cloned directory 5. Type 'git clone', and then paste the URL copied earlier 6. Press **Enter** to create your local clone

### Deployment

#### ElephantSQL

The database is held on the ElephantSQL Server. To set up:

Create ElephantSQL Account:
* Navigate to ElephantSQL.com and click “Log in”
* Select “Sign in with GitHub”
* Authorise ElephantSQL with your selected GitHub account
* In the Create new team form:
  * Add a team name (your own name is fine)
  * Read and agree to the Terms of Service
  * Select Yes for GDPR
  * Provide your email address
  * Click “Create Team”

Create Database:
* Click “Create New Instance”
* Set up your plan
  * Give your plan a Name (this is commonly the name of the project)
  * Select the Tiny Turtle (Free) plan
  * You can leave the Tags field blank
* Select “Select Region” (Sekect a data center near you)
* Then click “Review", check your details are correct and then click “Create instance”
* Return to the ElephantSQL dashboard and click on the database instance name for this project
* In the URL section, clicking the copy icon will copy the database URL to your clipboard
* Leave this tab open, we will come back here later

In IDE Space:
* Before we can build our application on Heroku, we need to create a few files that Heroku will need to run our application:
  * A requirements.txt file which contains a list of the Python dependencies that our project needs in order to run successfully.
  * A Procfile which contains the start command to run the project

* Generate the requirements.txt file with the following command in the terminal. After you run this command a new file called requirements.txt should appear in your root directory
<code>pip3 freeze --local > requirements.txt</code>

* The Procfile tells Heroku which files run the app and how to run it. To create the Procfile run the following command in the terminal:
  <code>echo web: python app.py > Procfile</code>
  NOTE: The Procfile uses a capital P and doesn't have a file extension on the end.

* If the Procfile has been created correctly it will have the Heroku logo next to it. It is also important to check the Procfile contents, as sometimes on creation a blank line will be added at the end of the file. This can sometimes cause problems when deploying to Heroku, so if the file contains a blank line at the end, delete this and save the file. Make sure to save both these files and then add, commit and push them to GitHub.

* Open your __init__.py file:
  Add an if statement before the line setting the SLQALCHEMY_DATABASE_URI and, in the else, set the value to reference a new variable, DATABASE_URL.

<code>
  if os.environ.get("DEVELOPMENT") == "True":
     app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
  else:
     app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
</code>

* To ensure that SQLAlchemy can also read our external database, its URL needs to start with “postgresql://”, but we should not change this in the environment variable. Instead, we’ll make an addition to our else statement from the previous step to adjust our DATABASE_URL in case it starts with "postgres://:". Underneath the last line add:

<code>
  if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
  app.config["SQLALCHEMY_DATABASE_URI"] = uri
</code>

* Save all your files and then add, commit and push your changes to GitHub

Connect database to hosting platform:
* Login (or sign up) to Heroku.com.
* Use Salesforce Authenticator code to access account.
* Click the new button and then click create new app.
* Choose a unique name for your app, select the region closest to you and click “Create app”
* Go to the Settings tab of your new app
* Click Reveal Config Vars
* Return to your ElephantSQL tab and copy your database URL
* Back on Heroku, add a Config Var called DATABASE_URL and paste your ElephantSQL 
  database URL in as the value. Make sure you click “Add”
* Add each of your other environment variables except DEVELOPMENT and DB_URL from the env.py file as a Config Var. 
  The result should look something like this:

| KEY | VALUE |
| :--- | :--- |
| DATABASE_URL | url from ElephantSQL |
|IP | 0.0.0.0 |
| PORT | 5000 |
| SECRET_KEY | your_secret_key |
|DEBUG | True |

*Debug must be set to "False" straight after deployment (used to ensure no issues during deployment)

---

## Testing

Please see [TESTING.md](TESTING.md) for all testing performed

- - -

## Credits

### Code Used

- Flask Blueprints
To update the routing as the project is larger
[Intro to Flask Blueprints](https://www.youtube.com/watch?v=pjVhrIJFUEs)

- Flask Authentication
To initiate user login with Flask libraries
[Learn Flask Login](https://www.youtube.com/watch?v=71EU8gnZqZQ)

- - -

### Content

- Homepage image created using [Bing AI Image genetator](https://www.bing.com/images/create?FORM=GENILP)

- - -
