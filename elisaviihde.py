import getopt, sys, requests, json, re

def main():
  # Parse command line args
  if len(sys.argv[1:]) < 2:
    print "ERROR: Usage:", sys.argv[0], "[-u username] [-p password]" 
    sys.exit(2)
  try:
    opts, args = getopt.getopt(sys.argv[1:], "u:p:v", ["username", "password"])
  except getopt.GetoptError as err:
    print "ERROR:", str(err)
    sys.exit(2) 
  
  # Init args
  username = ""
  password = ""
  baseUrl = "https://beta.elisaviihde.fi"
  ssoBaseUrl = "https://id.elisa.fi"
  verbose = False
  
  # Read arg data
  for o, a in opts:
    if o == "-v":
      verbose = True
    elif o in ("-u", "--username"):
      username = a
    elif o in ("-p", "--password"):
      password = a
    else:
      assert False, "unhandled option"
  
  # Init session to store cookies
  if verbose: print "Initializing session..."
  session = requests.Session()
  session.headers.update({"Referer": "https://beta.elisaviihde.fi/"})
  
  if verbose: print "Making initial request to", baseUrl, "..."
  session.get(baseUrl + "/")
  
  # Get sso auth token
  if verbose: print "Getting single-sign-on token..."
  token = session.post(baseUrl + "/api/sso/authcode",
                       data={"username": username},
                       headers={"Content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                                "X-Requested-With": "XMLHttpRequest"})
  try:
    authCode = token.json()["code"]
  except ValueError as err:
    print "ERROR: Could not fetch auth token from beta.elisaviihde.fi, check your username and password."
    sys.exit(1) 
  
  # Login with token
  if verbose: print "Logging in with single-sign-on token..."
  login = session.post(ssoBaseUrl + "/sso/login",
                       data=json.dumps({"accountId": username,
                                        "password": password,
                                        "authCode": authCode,
                                        "suppressErrors": True}),
                       headers={"Content-type": "application/json; charset=UTF-8",
                                "Origin": "https://beta.elisaviihde.fi"})
  
  # Login with username and password
  if verbose: print "Logging in with username and password..."
  user = session.post(baseUrl + "/api/user",
                      data={"username": username,
                            "password": password},
                      headers={"Content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                               "X-Requested-With": "XMLHttpRequest"})
  try:
    userInfo = user.json()
  except ValueError as err:
    print "ERROR: Could not fetch user data from beta.elisaviihde.fi, check your username and password."
    sys.exit(1) 
  
  # Get recording folders
  folders = session.get(baseUrl + "/tallenteet/api/folders",
                        headers={"X-Requested-With": "XMLHttpRequest"})
  folderInfo = folders.json()["folders"][0]["folders"]
  
  # Read and print recording folders
  print "\nFound folders:"
  for folder in folderInfo:
    print str(folder["id"]) + ": " + folder["name"]
  
  # Get recordings from first folder
  recordings = session.get(baseUrl + "/tallenteet/api/recordings/" + str(folderInfo[0]["id"]) + "?page=0&sortBy=startTime&sortOrder=desc&watchedStatus=all",
                           headers={"X-Requested-With": "XMLHttpRequest"})
  recordingInfo = recordings.json()
  
  # Read and print recording folders
  print "\nFound recordings from folder " + str(folderInfo[0]["id"]) + ":"
  for recording in recordingInfo:
    print str(recording["programId"]) + ": " + recording["name"] + " (" + recording["startTimeFormatted"] + ")"
  
  # Parse recording stream uri from first recording
  recUri = session.get(baseUrl + "/tallenteet/katso/" + str(recordingInfo[0]["programId"]))
  uri = recUri.text
  
  print "\nFound stream uri from recording " + str(recordingInfo[0]["programId"]) + ":"
  for line in uri.split("\n"):
    if "new Player" in line:
      uri = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)[0]
      print uri
  
  # Close session
  session.close()

if __name__ == "__main__":
  main()

