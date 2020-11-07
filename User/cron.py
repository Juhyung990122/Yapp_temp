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

def monthly_stats():
    users = CustomUser.objects.all()
    startday = datetime.datetime.now() - relativedelta(months=1)
    endday = datetime.datetime.now()
    for user in users:
        feeds = Feed.objects.filter(uid=user.id ,date__range=[startday,endday])
        feeds_count = feeds.count()
        month = endday.month - user.registeredDate.month
        avg_count = round(feeds_count/month,2)
        user.monthly_stats = avg_count
        user.save()

def weekly_stats():
    print('log')
    users = CustomUser.objects.all()
    for user in users : 
        date = user.get_distance_for_level()
        print(date)
