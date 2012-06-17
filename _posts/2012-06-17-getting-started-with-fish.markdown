---
layout: post
title: Super quick start guide to fluidinfo
categories:
- fluidinfo
- python
- readwriteweb
---


This is a quick and dirty guide to getting started with fish, the command line tool for [fulidinfo][fi]. I did it by setting up a [virtualenv][ve], as I find it a lot easier to manage python dependancies that way.

[fi]: http://www.fluidinfo.com
[ve]: http://pypi.python.org/pypi/virtualenv



Setup a virtualenv:

{% highlight python %}
% mkvirtual env fi
{% endhighlight %}



Open the virtual env session:

{% highlight python %}
% workon fi
{% endhighlight %}



Install httplib2:

{% highlight python %}
% pip install httplib2
{% endhighlight %}



Install readline:

{% highlight python %}
% pip install readline
{% endhighlight %}



Get fish, you can either get it from github and install from source, last time I checked that was:

{% highlight python %}
% git clone https://github.com/njr0/fish"  
{% endhighlight %}

*or* you can just go ahead and:

{% highlight python %}
% pip install fish
{% endhighlight %}



Create a credentials file:

{% highlight python %}
% touch ~/.fluidinfocredentials
{% endhighlight %}

Put your credentials in ~/.fluidinfocredentials as a simple two liner, username, then password.
If you signed in to fluidinfo with your twitter handle then you will need to create a password for your account, you can do this by going to the "Set password" option under your username in the web interface.



Start fish:

{% highlight python %}
% fish
This is fish version 4.34.
Synchronizing . . . Nothing to sync from Fluidinfo

synchronized.
> 
{% endhighlight %}

For further information on using fish have a look at the [documentation][doc]

[doc]: http://fluiddb.fluidinfo.com/about/fish/fish/index.html
