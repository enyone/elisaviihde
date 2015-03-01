# Elisa Viihde API Python implementation
# License: GPLv3
# Author: Juho Tykkala

import requests, json, re

class elisaviihde:
  # Init args
  verbose = False
  baseUrl = "https://beta.elisaviihde.fi"
  ssoBaseUrl = "https://id.elisa.fi"
  session = None
  authCode = None
  userInfo = None
  
  def __init__(self, verbose=False):
    # Init session to store cookies
    self.verbose = verbose
    self.session = requests.Session()
    self.session.headers.update({"Referer": "https://beta.elisaviihde.fi/"})
    
    # Make initial request to get session cookie
    if self.verbose: print "Initing session..."
    self.session.get(self.baseUrl + "/")
  
  def login(self, username, password):
    # Get sso auth token
    if self.verbose: print "Getting single-sign-on token..."
    token = self.session.post(self.baseUrl + "/api/sso/authcode",
                              data={"username": username},
                              headers={"Content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                                       "X-Requested-With": "XMLHttpRequest"})
    try:
      self.authCode = token.json()["code"]
    except ValueError as err:
      raise Exception("Could not fetch sso token", err)
    
    # Login with token
    if self.verbose: print "Logging in with single-sign-on token..."
    login = self.session.post(self.ssoBaseUrl + "/sso/login",
                              data=json.dumps({"accountId": username,
                                               "password": password,
                                               "authCode": self.authCode,
                                               "suppressErrors": True}),
                              headers={"Content-type": "application/json; charset=UTF-8",
                                       "Origin": "https://beta.elisaviihde.fi"})
    
    # Login with username and password
    if self.verbose: print "Logging in with username and password..."
    user = self.session.post(self.baseUrl + "/api/user",
                             data={"username": username,
                                   "password": password},
                             headers={"Content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                                      "X-Requested-With": "XMLHttpRequest"})
    try:
      self.userInfo = user.json()
    except ValueError as err:
      raise Exception("Could not fetch user information", err)
  
  def close(self):
    self.session.close()
  
  def gettoken(self):
    return self.authCode
  
  def getuser(self):
    return self.userInfo
  
  def getfolders(self):
    # Get recording folders
    if self.verbose: print "Getting folder info..."
    folders = self.session.get(self.baseUrl + "/tallenteet/api/folders",
                               headers={"X-Requested-With": "XMLHttpRequest"})
    return folders.json()["folders"][0]["folders"]
    
  def getrecordings(self, folderid=0):
    # Get recordings from first folder
    if self.verbose: print "Getting recording info..."
    recordings = self.session.get(self.baseUrl + "/tallenteet/api/recordings/" + str(folderid) + "?page=0&sortBy=startTime&sortOrder=desc&watchedStatus=all",
                                  headers={"X-Requested-With": "XMLHttpRequest"})
    return recordings.json()
  
  def getstreamuri(self, programid):
    # Parse recording stream uri from first recording
    if self.verbose: print "Getting stream uri info..."
    uridata = self.session.get(self.baseUrl + "/tallenteet/katso/" + str(programid))
    
    for line in uridata.text.split("\n"):
      if "new Player" in line:
        return re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)[0]

