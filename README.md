--Matt Tu
--CS50 Final Project
--EZ Chem Tables
--README.md

EZ Chem Tables is a web app allowing students taking Organic Chemistry Lab at Yale to quickly create formatted Chemical Tables for their 
prelabs. I created it in hopes of speeding up the time it took for students to create these tables, since correctly formatting these tables
takes up a considerable amount of time.

The web app can be accessed at the following URL: https://ezchem.herokuapp.com. Also, the web app can be tested by entering "flask run" in 
the "ezchem" directory, assuming the environment has flask installed. The GitHub repository can be found at 
https://github.com/2matttu/ezchem2.

The first step is to enter the number of chemicals in the table. This number must be positive and is capped at 99 to prevent the
website from crashing due to too many form rows.

Once the user clicks submit, a form appears with the number of rows (chemicals) that the user has specified. The user then enters all the
properties of each chemical, including its name, formula, molecular weight, melting and boiling points, density, etc. The user can also
add or delete rows if they want to add or delete chemicals from their table.

When the user is done inputting all the the information, they will click "submit", which renders the formatted table with all the
information. If some fields are blank when the user clicks submit, the app will confirm whether or not they still want to proceed with
rendering the table. 

When the table appears, the user can then copy the entire table by simply clicking on the table. The user then can paste the table into
Microsoft Word, which will retain the formatting. All the user has to do is add chemical structures and citations if needed.

At this point, the user can either select to Go Back to the form page where they could make changes or start over completely, which will 
return them to the page prompting them for the number of rows.
