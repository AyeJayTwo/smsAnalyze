smsAnalyze
==========

Project to do some rudimentary analysis on SMS data

Currently it only works on xml files that have been generated by the SMS Backup and Restore application for Android, by Ritesh Sahu (http://android.riteshsahu.com/apps/sms-backup-restore)

A smarter way to develop this would have been to write something for Android that tapped directly into the SMS database, or at least utilize the XML datasheets provided by Ritesh on his website. Alas, I'm a n00b and I wanted some practice

dbCreate.py
==========
This is the main file. A few things to note:
Line 10 is where you can change the filename for the sms file in the same directory
Line 20 starts parsing each line (each text) for the appropriate information using the functions from the sms.py module
Lines 40-46 create an in-memory SQLite3 database; once again - not most efficient, but meh (for now!)

After the initial setup I utilize matplotlib and some SQL commands to create some rudimentary graphs. The comments in the code should explain what each graph represents pretty well

sms.py
==========
This has the functions that do some of the basic parsing for each characteristic. Should be self-explanatory, I basically use the .split() function and the xml structure to get the info and some basic parsing.


dictionary.py
==========
This was a separate run to run some quick analysis on word/phrase frequency. I give an option of changing the number of words/phrase on Line 17 with the window variable.
It outputs a .txt file which does a textal graph to show relative frequencies

I also include a graph through matplotlib.

Finally, you may notice there is a common_Words() function. Using the top 100 words in the english language (http://en.wikipedia.org/wiki/Most_common_words_in_English). Basically input a word and the range you want to check; so you can see if the word is in the top 100, top 50, top 10, or any number inside.