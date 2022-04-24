# Safeguardauth Basic API Wrapper

Include `safeguard.py` in your directory, and import it

```
import safeguard as sg
```

We can then setup the safeguard class, before we do we'll need to get our Encrypted Password

Login to the site `https://safeguardauth.us/`, open inspect element; Goto the `Application Tab`; Click the `Session Storage` drop down.
You will see some json, the `'Password': 'xxxxxxxxxxxx'` is the password we need for below

```
account = sg.Safeguard(Username="Username", 
                    Password="Encrypted Password", # Password from above
                    ProgramID="xxxx-xxxx-xxxx-xxxx-xxxx", 
                    DownloadLink="https://downloadlink.com/", 
                    ProgramName="2500RequestSafeguardPlan")

```

Once you've entered your information you're ready to use the rest of the commands
A detailed example can be found in `main.py` - once released

```
account.GenerateTokens(level=1, days=30)
account.HWIDReset(username="Username)

account.UpdatePlan(option="expiration", username="Username", data=30) # Add 30 days to expiration
account.UpdatePlan(option="ban", username="Username") # Ban User
account.UpdatePlan(option="unban", username="Username") # Unban User
account.UpdatePlan(option="level", username="Username", data=1) # Set User to Level 1

users_response = account.TokenCreator(username="Username") 

log_response = account.FailLogs(username="Username") # Fetch the 5 Most Recent Fail Logs
```
