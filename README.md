# Vino

  
The live site is [here](https://bradders81-vino.herokuapp.com/).

A website for wine lovers

See current position of the side below
____

## Description

This site is created for people who like to cook and discover new wines.  Users can visit the site to buy wines for online delivery.  Returning users can create an account to keep a history of the orders, delivery details and also leave review for other uses.

## Purpose

Along with being convenient place to buy wine.  User will be able to consider the reviews of other users and leave their own reviews so that might may a more informed decision before making a purchase.
____

## User Stories

### User

“I want to be able to have my own profile.”
“I want to be able to search for the wines I want”
"I want to be able to look for wines by color (red, white, rose)
“I want to be able to leave a review and read reviews of other users”
"I want to be able to amend my profile information"
"I want to be able to create an account"

### Owner
*"I want to be be able to add and update and delete products"
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
 - Logged out/non-registered user will not have access to the proflie page, add reviews or keep a list of their order history.
 - 
### **Skeleton**

 **Navigation**
The navigation bar will be fixed to the top of the screen.  On the left will be the sites name/logo, which if clicked will link back to the home page.  The navigation links will be on the right and collapse into a burger menu on smaller screens such as mobile phones.  The search bar will be in the navbar.  There will also be buttons to allow the dispay products by type of wine (red, white, rose)


**Home Page** (visible to all users)
The user will be greeted by a hero background  image, upon which will be a call to action button and text.  

**Products Page** 

This will list all the producs available and will dispaly the seach results and filter buttons from the navbar (red, white, rose)

**Profile Page** 

This will display the users address details down the left and order history on the right, which will stack on moble devices.
The useer will also have buttons to update their delviery details and delete their account.  Superusers will not have the abiltiy to delete their account.  This is to make sure that their is alwasy access to the site admin features, such as adding and deleting products.

**Review Page** 
This will display the users reviews and review history and will have the same layout as the profile page.  The form on the left will allow users to add a review of the products. To the right of the form, will be the users review history.  The form on the right and the reveiw history on the left will stack on mobile devices

**Review Detail Page** 

When a reveiw from the history is clikced on in the Review Page, this will dispaly the details of that particular review.
The user will also have the option to edit the review.

**Basket Page** 
The baskset page will detail the items in the basket, showing wine, type, quantity and price per bottole.  The user will have the option to update the quantity and their will be buttons to go the checkout page or go back to the prodcuts page to keep shopping.

**Checkout Page**

The checkout page will have a form for the user to provide their delivery details.  If signed, this will be populated from their profile, apart from the email, which they will have to add, to make sure the site owner has a current email on file, should the site owner need to contact them about the order.

The site will use Stipe for the payment faciltiy and their will be a f

**Checkout Success Page and Order History Page**
This will page will be the same layout for both the checkout success page and order histroy page, but the django message at the top will indicate to the user that they are looking at a past order.  The page will display the order number, costs, delivery information and the date the order was made.


## Testing

Test doc will go here

____

## Deployment
### Heroku
Heroku is used to host the application.  Heroku will need to know what dependencies/applications are needed to run the app.  These should be stored in the requirement.txt file.  

Using pip3 use the following command: pip3 freeze --local > requirements.txt
A Procfile will also be needed

Then:

1.Go to [Heroku.com](https://www.heroku.com/) and create an account/login.
1. Click create new app, provide a name for your app and select the region near your location.
1. Click create app.
1. There are various methods to deploy the application and you should refer to the Heroku documentation [here](https://devcenter.heroku.com/categories/reference#deployment) if you want further information on all the methods.  I prefer to use automatic deployment from GitHub.  To deploy the site in this way click on the deployment tab and then click on the 'GitHub Connect to GitHub' button.  You may then be asked to log in to GitHub at this point.
1. Search for your repository in the 'Search for a repository to connect to' section.
1.  click 'Connect' when you have found your repository.
1. Next click on the 'Settings' tab near the top of the page and go to 'reveal Config Vars'.
1. You will then need to input the config variables that you will have stored .
1. Next click the 'Deploy' at top near the top of the page and click 'Enable Automatic Deployment'
1. Next click 'Deploy Branch', If there is more than one branch make sure you select the branch you want to deploy. 
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

**Bootstrap** has been used to create the grid system.  It has also been used to create the navbar, forms and  cards.  However all have been customised by me.

**Google Fonts:**  Fonts for this project are from Google Fonts.  The import at the top of the CSS file was copied from Google Fonts.

**Icons:** The icons used in the site are from Font Awesome.

**Code Institue** The logic in building this app has comes from my learning in the Code Institute Full Stack Developer Course and is signifiantly influenced from the work though project: Butique Ado.

## Acknowledgements

Thanks go to:

* My mentor, Brian Macharia for his continued advice and feedback.

* The Code Institute Slack Community who are always on hand to answer queries.

* The Code Institute Tutors for their assistance with any queries.


