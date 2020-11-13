import os
import datetime
import time
from first import lup

TEST_URL = "https://forms.office.com/Pages/ResponsePage.aspx?id=cnEq1_jViUiahddCR1FZKiO7YT_hx85Csl2xmNoFL7pUMDE1VEFKREk4RVJTU1VSMTI0OVFWNzYwVy4u"
URL = "https://forms.office.com/Pages/ResponsePage.aspx?id=cnEq1_jViUiahddCR1FZKi_YUnieBUBCi4vce5KjIHVUMkoxVUdBMVo2VUJTNFlSU1dFNEtNWUwxNS4u"
EMAIL = "h1810101@nushigh.edu.sg"
PASSWORD = "wetre2UJ"

senttoday = False
hour = 60*60*2

while True:
	now = datetime.datetime.now()
	today6am = now.replace(hour=6, minute=0, second=0, microsecond=0)
	today9am = now.replace(hour=9, minute=0, second=0, microsecond=0)
	if now>today6am and now<today9am:
		lup(URL,EMAIL,PASSWORD)
		print("time now is  "+str(now)+". logging temperature...")	
	time.sleep(hour)
