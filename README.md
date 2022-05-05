# english-to-sql


## The language that I am parsing is English into SQL statements.

## Notes
Each english statement must specifiy which table you want to use and be in the form of a request, question, or action
Grammar starts out with three different options for types of SQL options: 
* Select statement: branches into other grammars to organize ordering of possible English, supports limiting rows, ordering, selecting columns, and conditions
* Returning how many rows are in the database (conditions are optional)
* Deleting a row/rows with a condition

Grammar is fairly flexible but could be more so, does not take in all orders of English keywords, order has to be last but I didn't fix that because allowing different orders became really tedious the more things I supported.

Grammar does not work well with two word names

## You can run my code with two different files.
python interactive_mode.py  
or 
python sample_programs.py

#### interactive_mode 
lets the user input English statements, converts it into a SQL statement and will execute that SQL statement using the Chinook sample database. Will print the displayed results.
sqlite3 is required for interacting with databse

#### sample_programs 
has several examples of english statements and converts them into SQL and compares them to what the expected result should be, however it does not execute the translated SQL statements within a database. Will print out error message if result isn't what is expected.

