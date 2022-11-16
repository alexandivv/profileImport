# main file

import time
from library import Dolphin, GoLogin
from config import DOLPHIN_EMAIL, DOLPHIN_PASSWORD, GOLOGIN_TOKEN

dolphin = Dolphin(DOLPHIN_EMAIL, DOLPHIN_PASSWORD)
dolphinProfiles = dolphin.getProfiles()

for profile in dolphinProfiles:
    dolphinProfileDataDict = dolphin.getProfileInfo(profile['id'])
    print(dolphinProfileDataDict['name'])
    gologin = GoLogin(GOLOGIN_TOKEN)
    response = gologin.createProfile(dolphinProfileDataDict)
    

    if response.status_code == 201:
        print('Profile', dolphinProfileDataDict['name'], 'successfully created')
    else:
        print('Profile', dolphinProfileDataDict['name'], 'Error!')

    time.sleep(6)

print('Migration process completed')
print(response)
