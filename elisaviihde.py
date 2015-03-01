import getopt, sys, requests, json

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
  login = session.post("https://id.elisa.fi/sso/login",
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
  folderInfo = folders.json()
  
  # Read and print recording folders
  print "\nFound folders:"
  for folder in folderInfo["folders"][0]["folders"]:
    print str(folder["id"]) + ": " + folder["name"]

if __name__ == "__main__":
  main()

