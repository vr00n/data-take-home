# Data Take Home Exercises

Thank you for taking the time to attempt these exercises. We're sincerely thankful for your time in attempting these. 
We estimate depending on your skill level these exercises to take between 30 minutes to 2 hours. If you find yourself
taking more than 2 hours, you may be over-engineering the solution, consider taking an easier option.

## Instructions

Please create a fork of this repository. Create a folder named `solution` and place your responses here. When ready please notify
your coordinator to take a look.

### Structure

[edgar](edgar) - company listing site. To start the web application review the readme in the foler
[files](files) - csv files

## Questions

### Web Scrape

Write a script to scrape a sample site and output its data in JSON.

edgar is a company listings site containing ten pages of company links. Each link endpoint holds company-specific data such 
as name, description and address. The sole requirement of this part of the test is to produce JSON of all of the company 
listings data for the site.

Please attach a "edgar.json" file of the parsed company listings data along with your solution code in the `solution/edgar` folder.
Please include a `requirements.txt` file if necessary

#### Recommended libraries: 

[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) contains a robust HTML parser.

Python's [json](https://docs.python.org/2/library/json.html) module is convenient for [JSON](http://json.org) format. 
