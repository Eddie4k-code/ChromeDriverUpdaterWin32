<h1>Description</h1>
Deletes old chrome driver and replaces it with a specified version ofchromedriver in a specified location! Only meant for window 32 version of chromedriver.


<h1>How to use</h1>
Head to config -> config.ini and change the following settings:
<ul>
<li><h3>downloadPath</h3> - This is where the chromedriver_win32.zip file will be downloaded to</li>
<li><h3>zipFileName</h3> - Name of the zip file which by default is "chromedriver_win32.zip"</li>
<li><h3>extractToPath</h3> - This is the path of where the chromedriver.exe in the chromedriver_win32.zip file will be extracted to (the script will also check this location for an existing chromedriver.exe and will delete it if it exists)</li>
<li><h3>neededVersion</h3> - The version of chromedriver you want to download, must be exactly how it looks on the chromedriver site for example "110.0.5481.77"</li>
</ul>


<h1>Run in terminal "py main.py" and enjoy your driver being changed!! :)</h1>
