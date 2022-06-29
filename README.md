# Vintage Cars
***
 
## Table of Contents:
* [What does it do and what does it need to fulfill?](#what-does-it-do-and-what-does-it-need-to-fulfill)
* [Functionality of Project](#functionality-of-project)
* [User Experience](#user-experience)
   * [User Stories](#user-stories)
   * [Design](#design)
       * [1. Font](#1-font)
       * [2. Color Scheme](#2-color-scheme)
       * [3. Logo](#3-logo)
       * [4. Wireframing](#5-wireframing)
* [Technology Used](#technology-used)
* [Database](#database)
* [Features](#features)
   * [Future Features](#future-features)
* [Testing](#testing)
   * [Defensive Design](#defensive-design)
* [Deployment](#deployment)
* [Credits](#credits)
   * [Special Thanks & Acknowledgements](#special-thanks--acknowledgements)
 
***
 
## Welcome to Vintage Cars!

![Responsive](static/images/screenshots/screenshot-amiresponsive.png)
 
***
 
## What does it do and what does it need to fulfill?

Ever since automotives were invented, they were evolving very fast and even more environmentally friendly. But there are old cars that, though time already passes, are still as good as the modern ones. It’s good to point out that the world is accumulating a lot of garbage and, instead of scrapping the old unused cars, it should be integrated into circulation again but lessen their emission of contaminant gas.

With this project, I want to showcase the simplicity but elegant style of these cars and to be able to reuse these cars for different purposes and to promote them back into circulation with the help of modern technology. It's also a good opportunity for owners to gain cash by sharing their properties to avid fans of classic and vintage cars.

This project is to show how easy and fast a single framework can build a real-life website with complete functionality and libraries to choose from. Django is an open-source web framework that provides an easy and efficient way to create websites with minimum hassles. It comes with resources that are required by developers, specially those who are just starting their journey in Software Development.

<br>

### Favicon
I opted to use an image of a very well known classic car as the favicon of my project.

![Vintage car favicon](static/images/favicon.ico)

<br>

### Functionality of Project

There are different functionalities that are implemented in this project. One of them is to be able to register, to log in the registered username and to log out.

Any users, general users and registered users can view and read any post created. Those posts are created only by registered users. It can also be updated or deleted only by the author.

The Events section is integrated to the web page where anyone can browse to different upcoming events. Only admin staff can create, update and delete these posts. The rest of users can only read the content.
A contact page is available for anyone who wants to rent a car or has any enquiry regarding a car, a post or the webpage.

 
[Back to top](#table-of-contents)
 
## User Experience:
 
### User Stories:
_Generic (Guest/Public) User:_
* As a Generic User, I want to browse through different types of classic cars.
* As a Generic User, I want to be able to filter out the cars that are available for rent.
* As a Generic User, I want to see reviews of some users in the comment section.
* As a Generic User, I want to be able to read about any upcoming event in the future.
* As a Generic User, I want to be able to rent my favorite car.
* As a Generic User, I want to contact the website for any enquiries.
 
<br>

_Registers (Logged in) User:_
* As a Registered User, I want to be able to enjoy a ride with my favorite classic cars by renting one anytime.
* As a Registered User, I want to enjoy the car without worrying about the car expenses and maintenance.
* As a Registered User, I want to be a part of a community of avid fans of classic and vintage cars.
* As a Registered User, I want to post, edit and delete a classic car.
* As a Registered User, I want to filter my posts so that I can manage them all, more especially those posts pending to be published.
* As a Registered User, I want to be able to view any upcoming event and be able to be part of it.

<br>

_Administrator:_
* As an Administrator, I want to promote a very friendly community who wants to help and share with other users.
* As an Administrator, I want to notify the whole community about upcoming events regarding classic cars anywhere.

<br>

_Developer:_
* As a Developer, I want to to be able to make a fully functioning webpage.
* As a Developer, I want to use and apply the different languages I learned.
* As a Developer, I want to upgrade my knowledge to gain more skills.

<br>

### Design
 
#### 1. Font
Google fonts were used in this project. For the heading, `PLAYFAIR DISPLAY` was used to give it a vintage but elegant vibe. For the navbar font and some other area, `SPECIAL ELITE` was used to apply a look of an old typewriter style. For the rest of the website `SPACE MONO` was used.

<br>

#### 2. Color Scheme

Black is mainly used throughout the project. It provides elegance and simplicity. I used other colors to add more life and appeal to the page.

The main page background belongs to Shecodes gradient color palette for students/alumni to use in their projects. I did some modifications of the colors follow the chosen color scheme.

The background gradient color code is `linear-gradient(179.2deg, rgb(34, 34, 34) 0%, rgb(15, 18, 22) 29.7%, rgb(37, 47, 53) 63.4%, rgba(49, 65, 75, 0.8) 100.1%)`

The rest of the colors I used are as follows:

![Color Scheme](static/images/retro-colors.png)

* Red color: `#CD6C4A`

* Light brown color: `#b1987f`

* Brown: `#6F5643`

* White: `#f3f3f3`

* Orange: `#D2A24C`

* Yellow: `#ECE6C2`

* Green: `#73BDA8`

<br>

#### 3. Logo

The logo was created in a free application that allows users to create logos. I chose the LOGO MAKER app because it has extensive designs, especially vintage designs. And it’s also free of charge and it can be created with a transparent background.

The logo has three parts. Across in the middle is the name of the project: VINTAGE CARS. An image of a classic car enclosed by a circle was provided by the app which gives an obvious meaning to the page. And the laurel underneath signifies honor and distinction.
 
![Page Logo](static/images/screenshots/sshot-logo-dark.png)

<br>
 
#### 4. Wireframing
 
The wireframes were created for each individual page on three different screen sizes and two different mobile devices.
<br>

#### The home page
![Home](static/images/wireframes/homepage.png)

Here are the rest of the wireframes:

<details>

<summary>Cars page</summary>

![Cars page](static/images/wireframes/cars-page.png)

</details>

<details>

<summary>Events page</summary>

![Events](static/images/wireframes/events-page.png)

</details>

<details>

<summary>Log in and Sign up page</summary>

![Log in and sign up](static/images/wireframes/log-in.png)

</details>

<details>

<summary>Profile page in browser view</summary>

![Profile page browser](static/images/wireframes/profile-lg.png)

</details>

<details>
<summary>Profile page in medium and small devices</summary>

![Profile page in medium and small devices](static/images/wireframes/profile-md-sm.png)

</details>

<details>

<summary>Contact Us</summary>

![Contact Us page]()

</details>
 
[Back to Top](#table-of-contents)
 
## Technology Used
 
#### Languages, Frameworks, Editors & Version Control:
 
* add notes here on techstack...
 
#### Tools Used:
 
* add notes here on tools used to assist in developing the project...
 
## Database
 
#### Database Schema:
 
Detail the db schema here (if applicable)....images, thoughts behind fks etc
 
## Features
 
The project boasts several key features:
* Create: ...
 
[Back to Top](#table-of-contents)
 
#### Future Features:
 
* Detail future implementations here...
 
## Testing
 
Testing was ...
 
#### Found Bugs and Fixes:
 
During manual testing...
 
[Back to Top](#table-of-contents)
 
#### Defensive Design
 
Defensive design for this application was...
 
## Deployment
 
Detail deployment here...
 
[Back to Top](#table-of-contents)
 
## Credits
 
* background fix= https://css-tricks.com/perfect-full-page-background-image/
 
[Back to Top](#table-of-contents)
 
#### Special Thanks & Acknowledgements:
 
* Team 11 🤜
 
###### <i>Disclaimer: This project was created for educational use only as part of Code Institute's __________</i>
 
[Back to Top](#table-of-contents)