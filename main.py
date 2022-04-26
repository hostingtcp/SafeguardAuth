# (Version) v1.5
# (Author) Randle/tcpdev
# (Description) Safeguard Library Sample Use
# (PyV) 3.10.4

import safeguard as sg

''' Initiate the Safeguard Class '''
account = sg.Safeguard(Username="Username", 
                    Password="Encrypted Password") # Password from README.md

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

prog_response = account.ProgramInformation() # Fetch Program Information
# Program Name: Program Name
# Program ID: Program ID
# Program Version: Program Version
# Program Download: Program Download
# Program Expiration: Program Expiration

prog_response_1 = account.ProgramInformation(dict=True) # Fetch Program Information in DICT Format
# AutoUpdateEnable: bool
# AutoUpdateUrl: str
# AutoUpdateVersion: str
# CheckHID: bool
# ExpirationDate: str
# Id: int
# IsEnabled: bool
# Name: str
# ProgramKey: hex
# Randomize: bool

update_program_response = account.UpdateProgram(option="enable", data=True) # Enable/Disable program
update_program_response = account.UpdateProgram(option="checkhwid", data=True) # Enable/Disable HWID checks
update_program_response = account.UpdateProgram(option="autoupdate", data=True) # Enable/Disable autoupdate
update_program_response = account.UpdateProgram(option="autoupdateversion", data="2.0") # Update program version
update_program_response = account.UpdateProgram(option="autoupdateurl", data="https://downloadlink.com") # Update download linkte Program
