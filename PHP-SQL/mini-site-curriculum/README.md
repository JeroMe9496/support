# PHP CRUSHCOURSE
HOW TO CONVERT A STATIC SITE INTO A DYNAMIC ONE IN 7 STEPS<br>


## v1-Static
- Understanding the file structure
- Study the HTML tags
- Understanding WHAT are we doing and WHY a static site is problematic

## v2-PHP
- We should create an html file for each content 
- We should have an "index.php" file
- We need to have placeholders for the dynamic content
- Understand the purpose and the syntax of PHP
	
## v3-Dynamic-Thinking
- We have to display errors
- We have to change the href of menu links to use URI vars
- We have to GET the URI vars
- We have to target the correct html file depending on URI var
- We have to get the content of the html file and display it
	
## v4-Data-Storage
- We should have a storage file to store the site data
- We should get the content of the storage file
- We should convert the json content into a PHP array
- We should use site data to replace static PLACEHOLDERS

## v5-Dynamic-Menu
- We need to create the menu dynamically from site pages and store it
- We have to replace the "static" menu with the PHP generated menu

## v6-Separation-of-Concerns - REFACTORING !
- We should have a "functions.php" file to store our logic
- We should have a site_data() function
- We should have a menu_html() function
- We should have a title() function
- We should have a content() function
- We should have a debug() function
- We should include the functions.php file into index.php
- We should replace index.php PHP code with functions

## v7-Seo-Friendly-URL
- We shoud have a .htaccess file with Apache "mod_rewrite" code
- We should change the site pages keys with SEO keys
- We should store the pages SEO keys into an array
- We have to change the menu hrefs with SEO keys
- We shold have a router() function who decompose the URI and grabs the current page