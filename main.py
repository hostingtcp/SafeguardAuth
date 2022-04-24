# (Version) v1.0
# (Author) Randle/pydev3/tcpdev
# (Description) Safeguard Library Sample Use

import safeguard as sg

''' Initiate the Safeguard Class '''
account = sg.Safeguard(Username="Username", 
                    Password="Encrypted Password",
                    ProgramID="xxxx-xxxx-xxxx-xxxx-xxxx", 
                    DownloadLink="https://downloadlink.com/", 
                    ProgramName="Program Name")

''' Generate a Level 1, 30 day token '''
token_response = account.GenerateToken(level=1, days=30)
# xxxx-xxxx-xxxx-xxxx-xxxx - Returns token

''' Reset Users' HWID '''
hwid_response = account.HWIDReset(username="Username") 
# Username: HWID reset

''' Update Plans '''
expiration_response = account.UpdatePlan(option="expiration", username="Username", data=30) # Add 30 days to expiration
ban_response = account.UpdatePlan(option="ban", username="Username") # Ban User
unban_response = account.UpdatePlan(option="unban", username="Username") # Unban User
level_response = account.UpdatePlan(option="level", username="Username", data=1) # Set User to Level 1

''' Fetch User Info '''
users_response = account.TokenCreator(username="Username")
# Token: xxxx-xxxx-xxxx-xxxx-xxxx
# Created By: Usernamex
# Days: 30
# Level: 1

log_response = account.FailLogs(username="Username") # Fetch the 5 Most Recent Fail Logs
# Username: Username
# Fail Reasons:
#  - Reason 1
#  - Reason 2
#  - Reason 3
#  - Reason 4
#  - Reason 5