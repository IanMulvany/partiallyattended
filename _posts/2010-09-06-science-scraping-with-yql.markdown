---
layout: post
title: science scraping with YQL
categories:
- yql
- science
- scripting
- hacking
- cool
- solo10
---

Last Saturday at Science Online London I gave a quick tutorial on [YQL][yql], and how it might be used to mash up scientific data sets.  Below I list some of the sample queries that I was playing with.  Before you get started with the [console][console] have a look through the documentation.  I got a lot of milage out of the part about [filters][filter] and [joins][join].  The blog post by Paul Hogan on [using YQL for library maships][libs] was also very helpful.

[yql]: http://developer.yahoo.com/yql/
[console]: http://developer.yahoo.com/yql/console/
[filter]: http://developer.yahoo.com/yql/guide/filters.html 
[join]: http://developer.yahoo.com/yql/guide/joins.html 
[libs]: http://www.paulhagon.com/blog/2009/12/09/yql-mashups-for-libraries/

In my presentation I was originally looking at extracing data from a [report on soy bean rust spread][soy].

[soy]: http://sbr.ipmpipe.org/cgi-bin/sbr/county_info.cgi?date=2010-07-13&pest=soybean_rust&host=All%20Legumes/Kudzu 

Here are a few sample queries to get you started

1:
{% highlight sql %}
select * from html where 
url="http://sbr.ipmpipe.org/cgi-bin/sbr/county_info.cgi?date=2010-07-13&pest=soybean_rust&host=All%20Legumes/Kudzu"
{% endhighlight %}
This query just pulls all of the HML from the page. [Open in console][q1].

[q1]: http://developer.yahoo.com/yql/console/#h=select%20*%20from%20html%20where%20url%3D%22http%3A//sbr.ipmpipe.org/cgi-bin/sbr/county_info.cgi%3Fdate%3D2010-07-13%26pest%3Dsoybean_rust%26host%3DAll%2520Legumes/Kudzu%22%0

----

2:
{% highlight sql %}
select * from html where 
url="http://sbr.ipmpipe.org/cgi-bin/sbr/county_info.cgi?date=2010-07-13&pest=soybean_rust&host=All%20Legumes/Kudzu" 
and xpath='//table'
{% endhighlight %}
This query extracts only the table element from the page. [Open in console][q2].

[q2]: http://developer.yahoo.com/yql/console/#h=select%20*%20from%20html%20where%0Aurl%3D%22http%3A//sbr.ipmpipe.org/cgi-bin/sbr/county_info.cgi%3Fdate%3D2010-07-13%26pest%3Dsoybean_rust%26host%3DAll%2520Legumes/Kudzu%22%0Aand%20xpath%3D%27//table%27%0A

----

3:
{% highlight sql %}
select * from html where 
url="http://sbr.ipmpipe.org/cgi-bin/sbr/county_info.cgi?date=2010-07-13&pest=soybean_rust&host=All%20Legumes/Kudzu" 
and xpath='//table/tr/td[2]'
{% endhighlight %}
This query pulls the second item from each row of the table. [Open in console][q3].

[q3]: http://developer.yahoo.com/yql/console/#h=select%20*%20from%20html%20where%0Aurl%3D%22http%3A//sbr.ipmpipe.org/cgi-bin/sbr/county_info.cgi%3Fdate%3D2010-07-13%26pest%3Dsoybean_rust%26host%3DAll%2520Legumes/Kudzu%22%20and%20xpath%3D%27//table/tr/td%5B2%5D%27

----

4:
{% highlight sql %}
select * from html where 
url="http://www.mulvany.net/files/ipmsemanticpipe.html" 
and xpath='//table/tr/td[@id="status" and p="Confirmed"]/..'
{% endhighlight %}
For this query I copied the table onto my own server and added some basic proto-semantic markup to the column descriptors.  I could then call out specific columns from the table. [Open in console][q4].

[q4]: http://developer.yahoo.com/yql/console/#h=select%20*%20from%20html%20where%0Aurl%3D%22http%3A//www.mulvany.net/files/ipmsemanticpipe.html%22%0Aand%20xpath%3D%27//table/tr/td%5B@id%3D%22status%22%20and%20p%3D%22Confirmed%22%5D/..%27 

----

5:
{% highlight sql %}
select * from csv WHERE 
url="http://www.mulvany.net/files/ipmpipe.csv" 
and columns='date,place,status'
and status='Confirmed'
{% endhighlight %}
With this query I converted the table into a csv file.  This demonstrates YQL's ability to query against csv files.  [Open in console][q5].

[q5]: http://developer.yahoo.com/yql/console/#h=select%20*%20from%20csv%20WHERE%0Aurl%3D%22http%3A//www.mulvany.net/files/ipmpipe.csv%22%0Aand%20columns%3D%27date%2Cplace%2Cstatus%27%0Aand%20status%3D%27Confirmed%27
