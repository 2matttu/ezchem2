-- Matt Tu
-- CS50 Final Project: EZ Chem Tables
-- DESIGN.md

I decided to implement my EZ Chem Tables project as web app to make it easily accessible to chemistry students who wanted to use my tool.
I figured that the typical Organic Chemistry student would not be invested enough to want to download a separate program for this tool, but
would be completely fine if it was just a website that they could access on Chrome or Safari. Using flask was a no-brainer since the last
few psets were all in flask.

The next set of challenges and decisions was how exactly I could create a table using html/css/javascript that could be copied and pasted
into MS Word and would show up correctly formatted in Word as well. Initially, I found that even though my table looked correctly formatted,
with all the right fonts and spacings, the table would not show up correctly in Word. Sometimes, the pasted text was not even in table
format, and when it was, the fonts and font sizes were different. Eventually, I found out that Javascript had to be used to explicitly
specify the font and font-size of the text in the table. For font-sizes, I discovered that for a 16px font-size translated into a 12pt
font-size in Word after some trial and error. I also determined the ideal widths of each table column using trial and error as well.

To allow my program to receive the inputs (chemical information) from the user, I decided to use forms and the GET/POST requests similar
to the survey and finance psets. The index.html of my app is just a simple form asking how many chemicals the user will include in their Chemical
Table. My app then passes this info via the POST request to the next page, form.html which is the main form where the user inputs the
properties for each chemical.

This POST request is where my code gets interesting. In application.py, I set a variable n equal to the number of chemicals the user submitted
through the form. Then I created a list of length n from of a set of numbers from 0 to n-1 cast as strings. For example, if the user wants
3 chemicals, the list will be ['0','1','2']. That list is then passed to form.html via render_template for Jinja to use. Jinja then iterates
across that list, and for each iteration, creates form entries across the same row corresponding to the same molecule. For each row/chemical,
the names of the form entries will have a number at the end added via the list, which represents each chemicals unique id. For instances, the
first chemical's corresponding form names are name0, formula0, mw0, etc, while the second chemical's form names will all have 1 at the
end, and so on. See the comments in application.py and form.html for a better sense of how it works. Essentially this allows the form.html page
to be dynamic and change based on how many chemicals the user wants.

To transfer the information inputted into the form into the table, I ultimately decided that I would input the data into a list of lists
in application.py, with lists in the parent list corresponding to different chemicals/rows, and the elements in those child lists corresponding
to the properties of those chemicals. I used a for loop inside a forever loop for this, and a conditional checking if name<x> existed at the
end of each inside loop. For instance, if application.py sees that request.form.get(name9) is "None", that means there is no 10th row/chemical,
meaning that all the information has been saved in the list and application.py can safety render table.html and pass on that list. Again,
looking at the source code will give a better sense of how it works.

In table.html, Jinja is used one last time to take in that list of lists and "convert" it into a table. As discussed earlier, the Javascript
and CSS correctly formats the table, making it show up correctly in MS Word when a user copies and pastes it. There are also Javascript
functions which helps with special symbols; for the chemical formulas, a function converts numbers into subscripts by adding <sub> tags
between each number. Additionally, for densities, a function converts regular C's (ie 1.00 g/mL at 20C) into the degrees celcius symbol.

After the basic functionality above was implemented, I then implemented minor features that improved the user experience. In form.html,
I added the ability to add or remove rows, in case a user under/overestimated the number of chemicals in their Chem Table. For removing a row,
I used Javascript to remove the last instance of the <tr> tag, and for adding a row, I had Javascript figure out the "id" of the new row
based on the number of <tr> tags, and then add a row with all form entries having that id number at the end of their name. Additionally, I
added a feature where clicking on any part of the table would automatically select and copy the table, in case some tables (very long ones)
are time-consuming to select and copy all at once.

Finally, I decided to use Heroku to ultimately deploy my flask app to the web mainly due to how it worked nicely with GitHub and because
CS50's Hackathon had a seminar on Heroku.

During my project, I was thinking about implementing SQL or some other external database instead of the unconventional python code. While
that may have been the better move for the long run, especially if I wanted to implement more features like user-saved chemicals/tables,
in the short run it helped me get my web app functional sooner. For instance, Heroku has certain guidelines and restrictions when it comes
to SQL, which would have hindered my ability to get my app online if I did switch to SQL in the beginning. However, now that my app works,
I can try experimenting with implementing an SQL version of my app if need be.