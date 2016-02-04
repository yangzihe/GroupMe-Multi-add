import csv
import json
import requests

# Name of your roster csv file
roster = "bangzi.csv"

# Number of lines before the first member of your roster
LINES_TO_SKIP = 6

# Your access token. See README for details on how to obtain
ACCESS_TOKEN = "0a602c90ad460133280f2d28fad7266d"

# Group Id. See README for details on how to obtain
GROUP_ID = "19572990"

# Only update this if Groupme releases a new API
GROUPME_API_URL = "https://api.groupme.com/v3"


def formatNumbers(number):
    import re
    rep = {"(": "", ")": "", " ": ""}
    rep = dict((re.escape(k), v) for k, v in rep.iteritems())
    pattern = re.compile("|".join(rep.keys()))
    formattedNum = pattern.sub(lambda m: rep[re.escape(m.group(0))], number)
    return formattedNum


def csvToJson():
    with open(roster, 'rb') as csvfile:
        members = csv.reader(csvfile)
        for _ in xrange(LINES_TO_SKIP):
            members.next()
        members_data = []
        for member in members:
            if member[0] == "":
                break
            number = formatNumbers(member[1])
            new_groupme_member = {"nickname": member[0], "phone_number": number}
            members_data.append(new_groupme_member)
        wrapper = {"members": members_data}
        json_members = json.dumps(wrapper)
        return json_members


def add_members():
    json_members = csvToJson()
    requests.post(GROUPME_API_URL + "/groups/" + GROUP_ID + "/members/add" + "?token=" + ACCESS_TOKEN, data=json_members)


def main():
    add_members()

if __name__ == "__main__":
    main()
