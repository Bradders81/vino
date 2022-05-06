# Vino

  
The live site is [here](https://bradders81-vino.herokuapp.com/).

A website for wine lovers

See current position of the side below
____

## Description

This site is created for people who like to cook and discover new wines.  Users can visit the site to buy wines for online delivery.  Returning users can create an account to keep a history of the orders, delivery details and also leave revies for other uses.

## Purpose

Along with being convenient place to buy wine.  User will be able to consider the reviews of other users and leave their own reviews so that might may a more informed decicion before making a purchase.
____

## User Stories

### User

*"I want a website that I can navigate easily.”
“I want to be able to have my own profile.”
“I want to be able to search for the wines I want results”
"I want to be able to look for wines by color (red, white, rose)
“I want to be able to leave a review and read reviews of other users”
"I want to be able to amend my profile information"
“I want to be able to use the site on mobile devices”*

### Owner
*"I want to be be able to add and update products"
"I want to be able to take payment online"
"I want to be able to receive online orders*

____

## UX

### **Strategy**

#### Owner

- provide a site that users learn to navigate intuitively.
- build up a database of users.
- generate repeat visitors.


#### User

- To be able to create their own account.
- To find wines that they would like to try and leave a review.

### **Scope**

The site will have the following:

 - Allow users to create and delete their account.
 - Functionally for the user to be able to update and also delete their personal information.
 - A place for users to be able to see and search for all wines available from the site.
 - A landing page with with a call to action button to encourage users to look through the wines
 - The front-end will be written in HTML and CSS JavaScript and will use Bootstrap's grid system and for some of the templates (such as for forms and the navbar). 

The back-end will be written in Python, just the Django framework and Jinja templates.
dd
 #### Scheme

TBC


### **Structure**

The site is to be intuitive and simple to use.  

 - This will be a multi-page site.
 - Navigation bar at the top right.
 - Logged user will have access to the full site
 - Logged out/non-registered user will not have access to the proflie page or be able 
 - 
### **Skeleton**

 **Navigation**
The navigation bar will be fixed to the top of the screen.  On the left will be the sites name/logo, which if clicked will link back to the home page.  The navigation links will be on the right and collapse into a burger menu on smaller screens such as mobile phones.  The search bar will be in the navbar to save space.


**Home Page** (visible to all users)
The user will be greeted by a hero background  image, upon which will be a call to action button and text.  The image will only cover 80% to 90% of the view hight so that top of the section below.


**Sign Up**
Simple sign up form.  The form will capture the user's username, password and email.  

Having a registered email address will also help the site owner identify the user in the database, should the user make contact via email.

When entering a password the user will be asked to re-enter their chosen password to help eliminate typographical errors in the password that could prevent the user from accessing their site.
 
A link will also be provided to direct the user to the login page if they already have an account

** Login Page**
Simple login form.  Only username and password will be required to login.  Link provided to take the user to the Sign Up page if they do not have an account.


## Testing

Test doc will go here

____

## Deployment


### Heroku
Heroku is used to host the application.  Heroku will need to know what dependencies/applications are needed to run the app.  These should be stored in the requirement.txt file.  

Using pip3 use the following command: pip3 freeze --local > requirements.txt
A Procfile  is also needed so Heroku knows how to run the app.  which an be created with the following command: echo web: python *{name of .py file}* > Procfile.

Then:

1.Go to [Heroku.com](https://www.heroku.com/) and create an account/login.
1. Click create new app, provide a name for your app and select the region near your location.
1. Click create app.
1. There are various methods to deploy the application and you should refer to the Heroku documentation [here](https://devcenter.heroku.com/categories/reference#deployment) if you want further information on all the methods.  I used automatic deployment from GitHub.  To deploy the site in this way click on the deployment tab and then click on the 'GitHub Connect to GitHub' button.  You may then be asked to log in to GitHub at this point.
1. Search for your repository in the 'Search for a repository to connect to' section.
1.  click 'Connect' when you have found your repository.
1. Next click on the 'Settings' tab near the top of the page and go to 'reveal Config Vars'.
1. You will then need to input the config variables that you will have stored .
1. Next click the 'Deploy' at top near the top of the page and click 'Enable Automatic Deployment'
10.Next click 'Deploy Branch', If there is more than one branch make sure you select the branch you want to deploy. 
1. App will then be built by Heroku and a link to the deployed site will be provided.




### Cloning The Site

1. From within the repository click on 'Code' button with the download icon.
2. A small menu will appear to give you various options.  One option is to copy the URL provided in this menu.
3. Within the Integrated Development Environment (IDE) that you are using, change the directory to the ULR you have just copied.
4. For more options and details as to how to clone the site click [here](https://docs.github.com/en/free-pro-team@latest/github/using-git/which-remote-url-should-i-use) You may need to be logged into GitHub to view this page.

____

## Credits

### Images

Image credits will go here



## General Credits

**Bootstrap** has been used to create the grid system.  It has also been used to create the navbar, forms and  cards.  However all have been customised by me

**Google Fonts:**  Fonts for this project are from Google Fonts.  The import at the top of the CSS file was copied from Google Fonts.

**Icons:** The icons used in the site are from Font Awesome

**Code Institue** The logic in building this app has come from my learning in the Code Institute Full Stack Developer Course and influenced from the mini work though project: Task List

## Acknowledgements

Thanks go to:

* My mentor, Brian Macharia for his continued  advice and feedback.

* The Code Institute Slack Community who are always on hand to answer queries.

* The Code Institute Tutors for their assistance with any queries.


