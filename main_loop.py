import settings
import util
import time
import sys
import traceback

if __name__ == "__main__":
    while True:
        # scrape time
        print "%s: Starting DOG Attack" % time.ctime()
        try:
            util.dog_attack()
        except KeyboardInterrupt:
            print "Exiting...."
            sys.exit(1)
        except Exception as exc:
            print "Error with the scraping: %s" % sys.exc_info()[0]
            traceback.print_exc()
        else:
            print "%s: Successfully finished scraping" % time.ctime()

        # Sleep time between attacks
        try:
            time.sleep(settings.SLEEP_INTERVAL)
        except KeyboardInterrupt:
            print "Exiting...."
            sys.exit(1)
        except Exception as exc:
            print "Error with the sleeping: %s" % sys.exc_info()[0]
            traceback.print_exc()
