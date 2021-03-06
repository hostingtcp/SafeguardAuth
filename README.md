# Safeguardauth Basic API Wrapper

Safeguard.py can be imported into any directory
 && you'll have access to these safeguard functions
_______________________________________________________
Include `safeguard.py` in your directory, and import it
```
import safeguard as sg
```
We can then setup the safeguard class, before we do we'll need to get our Encrypted Password

Login to the site `https://safeguardauth.us/`, open inspect element; Goto the `Application Tab`; Click the `Session Storage` drop down.
You will see some json, the `'Password': 'xxxxxxxxxxxx'` is the password we need for below
```
account = sg.Safeguard(Username="Username", 
                    Password="Encrypted Password") # Password from above
```
                    
Once you've entered your information you're ready to use the rest of the commands
A detailed example can be found in `main.py`
```
account.GenerateTokens(level=1, days=30) # Generate Register Token
account.HWIDReset(username="Username") # Reset HWID

account.UpdatePlan(option="expiration", username="Username", data=30) # Add 30 days to expiration
account.UpdatePlan(option="ban", username="Username") # Ban User
account.UpdatePlan(option="unban", username="Username") # Unban User
account.UpdatePlan(option="level", username="Username", data=1) # Set User to Level 1

account.TokenCreator(username="Username") # Return users info & token creator

account.FailLogs(username="Username") # Fetch the 5 Most Recent Fail Logs

account.ProgramInformation() # Fetch Program Information - Text
account.ProgramInformation(dict=True) # Fetch Program Information - Dict

account.UpdateProgram(option="enable", data=True) # Enable/Disable program
account.UpdateProgram(option="checkhwid", data=True) # Enable/Disable HWID checks
account.UpdateProgram(option="autoupdate", data=True) # Enable/Disable autoupdate
account.UpdateProgram(option="autoupdateversion", data="2.0") # Update program version
account.UpdateProgram(option="autoupdateurl", data="https://downloadlink.com") # Update download link
```
