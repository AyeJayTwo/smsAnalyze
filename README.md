smsAnalyze
==========

Project to do some rudimentary analysis on SMS data

Currently it only works on xml files that have been generated by the SMS Backup and Restore application for Android, by [Ritesh Sahu](http://android.riteshsahu.com/apps/sms-backup-restore)

A smarter way to develop this would have been to write something for Android that tapped directly into the SMS database, or at least utilize the XML datasheets provided by Ritesh on his website. Alas, I'm a n00b and I wanted some practice

Python Scripts
==========
`dbCreate.py`
------------
This is the main file. A few things to note:
<br>`Line 10` is where you can change the filename for the sms file in the same directory
<br>`Line 20` starts parsing each line (each text) for the appropriate information using the functions from the sms.py module
<br>`Lines 40-46` create an in-memory `SQLite3` database; once again - not most efficient, but meh

After the initial setup I utilize `matplotlib` and some SQL commands to create some rudimentary graphs. The comments in the code should explain what each graph represents pretty well

`sms.py`
------
This has the functions that do some of the basic parsing for each characteristic. Should be self-explanatory, I basically use the `.split()` function and the x
ml structure to get the info and some basic parsing.

`mapping.py`
------
This is a separate script which used the area codes from all the texts and created a map which shows where all your friends have come from. Currently it only supports area codes (So not super specific), and the central point (you) is hardcoded in.
The main challenges were learning howto use the `basemap` module, which is technically apart of `matplotlib`, but needs to be downloaded separately. I never realized how complicated cartography could be!
The other thing to potentially note is how I scale the colors of each line to indicate the frequencies. I took a count of the number of times that area code came in, turned it into a log scale, and then used that to adjust the HSV color values which later got translated into RGB colors. Lighter lines indicate heavier activity than the dark, dead lines.

`AreaCodePickler.py`
------
This is a short and sweet script which basically converts this JSON item from this random user on StackOverflow into a dictionary which is utilized in `mapping.py`.

`dictionary.py`
-------------
This is a separate script to run some quick analysis on word/phrase frequency. I give an option of changing the number of words/phrase on Line 17 with the window variable.
It outputs a .txt file which does a textal graph to show relative frequencies

I also include a graph through `matplotlib`.

Finally, you may notice there is a `common_Words()` function. Using the [top 100 words in the english language] (http://en.wikipedia.org/wiki/Most_common_words_in_English). Basically input a word and the range you want to check; so you can see if the word is in the top 100, top 50, top 10, or any number inside.
