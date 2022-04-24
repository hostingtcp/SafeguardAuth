# (Version) v1.0
# (Author) Randle/tcpdev
# (Description) Entry Level SafeGuardAuth API Wrapper

import datetime
import uuid
from datetime import datetime, timedelta
from typing import List, Optional

import requests


class Safeguard:
    def __init__(self, Username, Password, ProgramID, DownloadLink, ProgramName) -> None:
        ''' Gather Required SafeGuard Data'''
        self.Username: str = Username # Regular SafeGuard Username
        self.Password: str = Password # This Your Encrypted Safeguard Password, Read README.md
        self.ProgramID: hex = uuid.UUID(ProgramID).hex # SafeGuards' ProgramID is GUID
        self.DownloadLink: str = DownloadLink # Link Returned With the Token
        self.ProgramName: str = ProgramName # SafeGuard Program Name
        
        self.s = requests.session()
        
        ''' Required SafeGuard Headers'''
        self.s.headers.update({
            'Accept': 'application/json; charset=utf-8',
            'User-Agent': 'SafeGuard Authentication',
            'Username': self.Username,
            'Password': self.Password
        })
        
    def GenerateToken(self, days: int, level: int) -> str:
        ''' Generate SafeGuard Token '''
        
        token_data: dict = {
            'ConsumedBy': "",
            'CreatedBy': "",
            'Days': int(days),
            'Id': 0,
            'ProgramId': self.ProgramID,
            'Token1': "",
            'UserLevel': int(level)
        }
        
        token_generate_req = self.s.put("https://safeguardauth.us/api/AddToken", data=token_data)
        if token_generate_req.status_code == 200:
            token_information = token_generate_req.json()
            
            return str(token_information['Token1'])
            #return f"Register Token: {token_information['Token1']}\nDownload Link: {self.DownloadLink}"
        else: return f"Unable to generate token, please check you've set your login information correctly."
            
    def HWIDReset(self, username: str) -> str:
        ''' Reset Users' HWID '''

        program_users_resp = self.s.get("https://safeguardauth.us/api//ProgramUsers")
        if program_users_resp.status_code == 200:
            users_info: dict = [user for user in program_users_resp.json() if user['UserName'].lower() == username.lower()][0]
            hwid_data: dict = {
                'HID': str(users_info['HID']),
                'Id': users_info['Id'],
                'ProgramId': self.ProgramID,
                'UserName': username
            }
            hwid_reset_req = self.s.post("https://safeguardauth.us/api/ClearHID", data=hwid_data)
            if hwid_reset_req.status_code == 200: return f"*{username}:* `HWID reset`"
            else: return "Unable to reset HWID, please check you've set your login information correctly."
            
    def DownloadLink(self) -> str:
        ''' Return the Download Link '''
        
        download_link_req = self.s.get("https://safeguardauth.us/api//AllPrograms") 
        if download_link_req.status_code == 200: 
            download_link: str = download_link_req.json()[0]['AutoUpdateUrl']
            return str(download_link)
        else: return "Unable to generate download link, please check you've set your login information correctly."
        
    
    def UpdatePlan(self, option: str, username: str, data: Optional[int] = None) -> str:
        ''' Update Users' Plans'''
        
        ''' Availabe arguments for 'option':
            - "expiration" - Update Expiration Date
            - "ban" - Ban User
            - "unban" - Unban User
            - "level" - Update User's Level
        '''
        try:
            option = option.lower()
            
            program_users_resp = self.s.get("https://safeguardauth.us/api//ProgramUsers")
            if program_users_resp.status_code == 200:
                user_info: dict = [user for user in program_users_resp.json() if user['UserName'].lower() == username.lower()][0]
                
                # Required Data for SafeGuard
                post_data: dict = {
                    'AID': user_info['AID'],
                    'AmountEarned': user_info['AmountEarned'],
                    'Banned': user_info['Banned'],
                    'Email': user_info['Email'],
                    'ExpirationDate': user_info['ExpirationDate'],
                    'FullName': user_info['FullName'],
                    'GeneratedAccounts': user_info['GeneratedAccounts'],
                    'HID': user_info['HID'],'Id': user_info['Id'],
                    'IsMobile': user_info['IsMobile'],
                    'Level': user_info['Level'],
                    'Notifications': user_info['Notifications'],
                    'Password': user_info['Password'],
                    'ProgramId': self.ProgramID,
                    'ProgramName': self.ProgramName, # Program Name Use Here
                    'PurchaseDate': user_info['PurchaseDate'],
                    'UserName': user_info['UserName']
                }
                
                return_msg: str = ""
                
                if option == "expiration":
                    OldExpiration = datetime.fromisoformat(user_info['ExpirationDate'].split('.')[0])

                    ''' Update Expiration Date According to Expiration '''
                    CurrentDate = datetime.now()
                    if OldExpiration < CurrentDate: NewExpiration = CurrentDate + timedelta(int(data))
                    else: NewExpiration = OldExpiration + timedelta(int(data))

                    post_data['ExpirationDate'] = NewExpiration.isoformat()
                    return_msg = f"*{username}:* `Expiration Date Updated - {post_data['ExpirationDate']}`"
                    
                elif option == "ban":
                    post_data['Banned'] = True
                    return_msg = f"*{username}:* `Banned`"
                    
                elif option == "unban":
                    post_data['Banned'] = False
                    return_msg = f"*{username}:* `Unbanned`"
                    
                elif option == "level":
                    post_data['Level'] = data
                    return_msg = f"*{username}:* `Level Updated - {data}`"
            
                ''' Update User's Information, Return Message Accordingly '''
                update_user_req = self.s.post("https://safeguardauth.us/api//ProgramUsers", data=post_data)
                return return_msg if update_user_req.status_code == 200 else "Unable to update user, please check you've set your login information correctly."
        
        except Exception as e: print(e) 
         
            
    def TokenCreator(self, username: str) -> str:
        ''' Return Token Creator/Token Information for a User '''
        
        program_tokens_resp = self.s.get("https://safeguardauth.us/api//AllTokens")
        if program_tokens_resp.status_code == 200:
            user_info: dict = [user for user in program_tokens_resp.json() if str(user['ConsumedBy']).lower() == username.lower()][0]
            if user_info: return f"*Token:* `{user_info['Token1']}`\n*Created By:* `{user_info['CreatedBy']}`\n*Days:* `{user_info['Days']}`\n*Level:* `{user_info['UserLevel']}`"
            else: return "Unable to find user"
        else: return "Unable to find user, please check you've set your login information correctly."
    
    def FailLogs(self, username: str) -> str:
        ''' Return Past 5 Entire in Fail Logs '''

        user_log_resp = self.s.get("https://safeguardauth.us/api//AllUserLogs")
        if user_log_resp.status_code == 200:
            return_list: List[str] = []
        
            ''' Look through all users, check contraints, then adds to return list '''
            for user in user_log_resp.json():
                if user['Username'].lower() == username.lower():                    
                    if len(return_list) < 5:
                        if len(user['ReasonPhrase']) > 1:
                            return_list.append(user['ReasonPhrase'])
                    else: break
            return_msg = '\n'.join(return_list)
            return f"Username: {username}\nFail Reasons:\n`{return_msg}`"
        else: return "Unable to find user, please check you've set your login information correctly."
