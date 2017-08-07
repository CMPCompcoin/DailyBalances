# Ending Daily Balances


## Prerequisites:
Please make sure you have installed Python version 2.7.12, and also have pip installed.

## Using The Script:
Once setting up the system is finished, using the script is easy.

### Preparing the JSON file:

You will need to convert the html table to a JSON file. You can find a converter online. 

This is the one used for development:
http://convertjson.com/html-table-to-json.htm

Make sure the following boxed are checked:
   * Always use first row of table as JSON property names 
   * Consider value of NULL in Text to be null in JSON
   * Change < br > tags to \n in JSON
   * Remove HTML tags in JSON
   

You can copy and paste the raw binary of the .html file into the html input of the site listed above. 

When converting, you **MUST** choose 'To Keyed JSON'. It will generate the hashed JSON needed. 

You can choose the table you want, by slecting **Which Table**, typically it's the 5th table. But it could change.

Download the .json file and save it to the *src/docs/json/* directory.

###Running the script
Go to the top of the daily_ending_balances.py file in the *src/* directory and change the name of the file present, 
with your newly downloaded .json file.

## Results
Your results will be in *src/docs/csv/* directory, labeled converted_csv_#.csv. Where '#' will be some randomly generated number.
