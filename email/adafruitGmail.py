
import feedparser, time

DEBUG = True

USERNAME = "allhailglowcloud"     # just the part before the @ sign, add yours here
PASSWORD = "hackprinceton"     

NEWMAIL_OFFSET = 0        # my unread messages never goes to zero, yours might
MAIL_CHECK_FREQ = 60      # check mail every 60 seconds

while True:

        newmails = int(feedparser.parse("https://" + USERNAME + ":" + PASSWORD +"@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])

        if DEBUG:
                print "You have", newmails, "new emails!"

        if newmails > NEWMAIL_OFFSET:
        	print "NEWMAIL"
	else:
		print "no new mail"

        time.sleep(MAIL_CHECK_FREQ)

