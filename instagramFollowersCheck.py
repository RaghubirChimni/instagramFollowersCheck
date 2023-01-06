import json, os

# reading json files
f = open('followers.json',)
followers_data = json.loads(f.read())
f.close()
    
f = open('following.json',)
following_data = json.loads(f.read())
f.close()

followers = []

# creates list of followers
for i in followers_data['relationships_followers']:
    followers.append(i['string_list_data'][0]['value'])

# file output path
output = 'notFollowingBack.txt'

# remove file if it exists
if os.path.isfile(output):
    os.remove(output)

emptyFile = True
f_write = open(output, 'a')

# checks if people you follow, follow you back
# writes to 'notFollowingBack.txt' if they do not follow you back
for i in following_data['relationships_following']:
    if i['string_list_data'][0]['value'] not in followers:
        if emptyFile == True:
            f_write.write(i['string_list_data'][0]['value'])
            emptyFile = False
        else:
            f_write.write('\n' + i['string_list_data'][0]['value'])

f_write.close()
