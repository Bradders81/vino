# Testing    

### User Stories
USER:
1. "I want to be abel to have my own profile"  - PASS
1. "I want to be abel to search for the wines I want" - PASS
1. "I want to be able to look for wines by color (red, white, rose)" - PASS
1. "I want to be able to leave a review and read reviews of other users" - PASS
1. "I want to be able to amend my profile information" - PASS
1. "I want to be able to see my order history from my account" - PASS
-----
OWNER: 
1. "I want to be be able to add and update and delete products" - PASS
1. "I want to be able to take payment online" - PASS
1. "I want to be able to receive online orders* - PASS
-----
FORM WORKING
- Allauth Forms work and manage the creation of the client account and varification - PASS
- User Profile Form works?  PASS
- Create User Reveiew Form Works - PASS
- Checkout Form Works? - PASS

- REVIEW FORM WORKS, including update  - PASS
-----
LINKS
Buttons on side work = PASS

--------

PYTHON CODE PASSED PEP8 CHECKER?
Code passes through PEP8 Check, apart from line 2 in Checkout View and a line in wehbhook.py.  I did not amend these lines so not to break the code.
------

STRIPE PAYMENTS WORK - PASS

----
Is the site responseive?
Yes the site can be viewed on screen sizse makes use of Bootstrap Grid
-----

BUGS
Developement was significantlay hampered due to a crupption between the development and the deployment database.  This resulted in having to make a new profiles app, which is why the one in the project is called profile1.  This did eat up a lot of my time.  The response the issue the databases had to be reset.  The products did have descriptions in the descriptoin filed, but I have not had time to put them back in.  These can be added for testing and it work.

The flashing button on the home screen does not seem to work on Apple Iphone and I assume it will be the same on a Ipad but I do not have one to test on.  From reasearch this seems to stem from using the interival to control the flashing.  Had I had more time I would have found a why to resolve this.  It does work however on PC and android.
