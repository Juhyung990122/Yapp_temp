from User import views
from User.models import MgmtUser,Feed
import datetime
from dateutil.relativedelta import relativedelta
from collections import Counter
def check_dormant():
    users =MgmtUser.objects.all()
    for user in users:
        if user.state == "N":
            if datetime.datetime.now() >= user.lastlogined + datetime.timedelta(days=3):
                user.state = "D"
                user.save()

def monthly_stats():
    users = MgmtUser.objects.all()
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
    week = ['월','화','수','목','금','토','일']
    startday = datetime.datetime.now() - datetime.timedelta(weeks=1)
    endday = datetime.datetime.now()
    all_users = list(MgmtUser.objects.all().values_list('id',flat=True))
    feeds = Feed.objects.filter(date__range=[startday,endday]).values_list('uid',flat=True).distinct()
    for i in feeds:
        user = MgmtUser.objects.get(id = int(i))
        best = Feed.objects.filter(date__range=[startday,endday],uid = int(i)).values_list('date')
        best = Counter(best).most_common(1)[0][0][0]
        all_users.remove(i)
        user.weekly_stats = week[best.weekday()]
        user.save()
    for j in all_users:
        user = MgmtUser.objects.get(id = int(j))
        user.weekly_stats = '-'
        user.save()
