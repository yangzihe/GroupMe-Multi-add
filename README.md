# GroupMe-Multi-add

A small Python script I wrote in order to bulk add a list of members from a .csv file to a GroupMe group, because I didn't want to do it manually.

## Installation

In your terminal, run `git clone https://github.com/yangzihe/GroupMe-Multi-add.git` in the directory you would like to keep this script in.

## Usage

To use this script, you need 2 pieces of information from GroupMe.

1. Group ID. To get this, login to [GroupMe](https://app.groupme.com/) and select the group you want to add members to. Then click the arrow right next to the name of your group, and select settings. Copy your Group ID and replace the current `GROUP_ID` constant (located at the top of the python file) with what you copied.

2. Access Token. To get an access token, go [here](https://dev.groupme.com/applications/new) and fill out the form. You can put whatever you want for the fields, it doesn't really matter, as long as the format matches. Once you check the box and click save, your access token should appear at the bottom of the page as an alphanumeric string. Copy it and replace the current `ACCESS_TOKEN` constant.

Once you've gotten the information and editted the corresponding values in the python file, download your roster as a .csv file, and save it in the same directory that the python file is in. Replace the current value of `ROSTER` with the name of your .csv file. Then, count how many rows there are before the first member. Replace the current value of `LINES_TO_SKIP` with that number.

Finally, in your terminal, cd to the directory containing your .csv file and python script. Then type `python groupme_multi_add.py` and press Enter, and you're done! Congratulations, you've just added your entire roster to your GroupMe group.


## API Reference

[GroupMe API](https://dev.groupme.com/docs/v3)
