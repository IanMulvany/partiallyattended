---
categories:
- python
- time
- unix
date: 2011-10-13T00:00:00Z
title: Converting between dates and unix time in Python
url: /2011/10/13/managing-unix-time-in-python/
---

# Going from a date to a unix time:

{{< highlight python >}}
>>> from datetime import date
>>> from time import mktime
>>> start = date(2011, 9, 26)
>>> mktime(start.timetuple())
1316991600.0
{{< / highlight >}}

# Going from a unix time to a date:

{{< highlight python >}}
>>> from time import strftime
>>> from datetime import datetime
>>> datetime.fromtimestamp(int("1284101485")).strftime('%Y-%m-%d %H:%M:%S')
'2010-09-10 07:51:25'
{{< / highlight >}}


