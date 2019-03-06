# JRScheduleScraper
A python script that allows a JoyRun Admin to see how many shifts each team member has in a given week. The script Authenticates through FB login.
Works best if 2 factor authentication is turned off (otherwise each run will require more action from user).

# Login.py
Your facebook credentials go here.

# scraper.py
This should function without too many changes. The <b>ONE</b> change needed is this.<br>In <code> cProgField.send_keys("ilsu Spring 19 team")</code> enter the search term needed to bring 
your campuses name to the top of the recommended list.

# Stripper.py
This strips "R - " from the beginning of each cell and cuts anything after the user's name. This ensures that users who have exited do not get credit for shifts that they don't run

# Dependencies 
You can use<br>
<code>pip install selenium</code><br>
to get selenium but you will need to download chromedriver.exe and direct this line to where you're storing it<br>
<code>driver_path = '/Users/luke_/chromedriver.exe'</code>
