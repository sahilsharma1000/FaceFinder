#code stuck for some reason

from twython import Twython
#Get Twython from the folder or download form internet
import requests

APP_KEY = 'xZoZqimGHDtihqWByZ0rS1jZR'
APP_SECRET = 'Bz2pJD2M3rgJJPicNaHw8ZxATvMJs8dq9YqI0FBJhRUN9neQf9'
OAUTH_TOKEN = '3147247751-8GqOXDG41RrOj9h75Ie4Z4qnFknhJsvYxqit3oc'
OAUTH_TOKEN_SECRET = 'MU13fge95mTyXOA3hbQjBTuGgDPlYfOCMdcsyj2MqAP57'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
#for iteration through profiles by using ids
for x in range(666182,1000000):
  try:
    details = twitter.show_user(id=x)
    #Removing _normal form the image to retrieve the bigger images from there
    link= (details['profile_image_url'])
    if link.endswith('.jpeg'):
        link= link[:-12]
        link+= '.jpeg'
        print('profile picture link:')
        print(link)
    elif link.endswith('.jpg'):
        link= link[:-11]
        link+= '.jpeg'
        print('profile picture link:')
        print(link)
    elif link.endswith('.png'):
        link = link[:-11]
        link += '.jpeg'
        print('profile picture link:')
        print(link)
    #todo - Need to solve this looping problem to save the files in sequential folder
    f = open('0.jpg', 'wb')
    f.write(requests.get(link).content)
    f.close()
    print('friend count:',details['friends_count'])
    print('self description:',details['description'])
    print('location:',details['location'])
    print('follower count:',details['followers_count'])
    print('------------------------------------------------------------------')
    print('------------------------------------------------------------------')
    #print(details)-Prints all the other detauls you might be interested in
  except:
        pass
