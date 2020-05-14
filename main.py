__author__  = 'Ricchi Tech <brg2289@gmail.com>'
__author_name__  = 'Bharathraj @Ricchi'
__version__ = 'v 0.1'

#import modules
import time
# pip install plyer
from plyer import notification 
if __name__ == '__main__':
    while True:
        notification.notify(
            title = "Please drink water",
            message = "Its time to drink some water please drink!!!!",
            app_icon = "icon.ico", #notification icon
            timeout=10
        )
        time.sleep(60*60) #define sleep time = 3600secs





