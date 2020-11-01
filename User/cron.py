from User import views
from User.models import MgmtUser
import datetime

def check_dormant():
    users =MgmtUser.objects.all()
    for user in users:
        if user.state == "N":
            if datetime.datetime.now() >= user.lastlogined + datetime.timedelta(days=3):
                user.state = "D"
                user.save()