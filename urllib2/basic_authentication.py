#handling basic authentication using urllib2
import urllib2

#create a password manager
#password manager handles the mapping of url's and realms to passwords and usernames
#use HTTPPasswordMgrWithDefaultRealm when you don't care what the realm is. Otherwise use HTTPPasswordMgr
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

#set username and password
username = 'hansika'
password = 'hansika'


# Add the username and password.
# If we knew the realm, we could use it instead of None.
top_level_url = "http://example.com/foo/"
password_mgr.add_password(None, top_level_url, username, password)

handler = urllib2.HTTPBasicAuthHandler(password_mgr)

# create "opener" (OpenerDirector instance)
opener = urllib2.build_opener(handler)

# use the opener to fetch a URL which is deeper than the top level url
opener.open('http://example.com/foo/nextfoo/')

# Install the opener.
# Now all calls to urllib2.urlopen use this custom opener.
urllib2.install_opener(opener)
