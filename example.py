import getopt, sys, elisaviihde

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
  
  # Init elisa session
  try:
    elisa = elisaviihde.elisaviihde(verbose)
  except Exception as exp:
    print "ERROR: Could not create elisa session"
    sys.exit(1)
  
  # Login
  try:
    elisa.login(username, password)
  except Exception as exp:
    print "ERROR: Login failed, check username and password"
    sys.exit(1)
  
  # Read and print recording folders
  folders = elisa.getfolders()
  
  print "\nFound folders:"
  for folder in folders:
    print str(folder["id"]) + ": " + folder["name"]
  
  # Read and print recording folders
  folderid = folders[0]["id"]
  recordings = elisa.getrecordings(folderid)
  
  print "\nFound recordings from folder " + str(folderid) + ":"
  for recording in recordings:
    print str(recording["programId"]) + ": " + recording["name"] + " (" + recording["startTimeFormatted"] + ")"
  
  # Get recording stream uri from first recording
  streamuri = elisa.getstreamuri(recordings[0]["programId"])
  print "\nFound stream uri from recording " + str(recordings[0]["programId"]) + ":"
  print streamuri
  
  # Close session
  elisa.close()

if __name__ == "__main__":
  main()

