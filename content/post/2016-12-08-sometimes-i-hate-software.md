---
categories:
- Jekyll
- software
- blogging
- friction
- ruby
date: 2016-12-08T00:00:00Z
title: Something broke in a Jekyll upgrade (a.k.a, sometimes I hate software)
url: /2016/12/08/sometimes-i-hate-software/
---

This is a short story about software, some of the things I hate about it, my lack of knowledge of ruby, and a desire to own my own words.

For various reasons I'm working on a brand new machine, I decided that I want to start posting to my [own blog](http://partiallyattended.com) again (as well as cross posting to Medium, because fuck it, why not). 

That involved dusting down my Jekyll site and seeing if I could get it to work again. 

It's been a while, mind, so the very first thing that I did was go and pull my blog content down from Github and fire up Jekyll. 

Jekyll has moved on since I last used it, and I discovered that the mechanism that I was using to create an index page of my tags no longer works. [The following line](https://github.com/IanMulvany/partiallyattended/blob/gh-pages/Rakefile#L13) in the rake-file that I was using is deprecated, and throws an error. 

```ruby
	site.read_posts('')
```

I thought, it's one line, how hard can it be to fix? Of course, the dirty little secret is that I don't know ruby, I'd just been using Jekyll in the past as a fast way to generate blog content from markdown. I spent several hours this afternoon trying to tack down a short comprehensible workaround, and have come to the conclusion that I won't make progress without actually learning enough ruby to become proficient at writing ruby plugins, and my life is too short to do that. 

Writing my markdown in Byword gives me almost instant access to publish to Medium via the publish button, but I want to control my own domain, and I want a git archive of my blog posts too, so what do I do? 

I really liked the way that tagging used to work on my site, but have decided that the value add to getting it working again is too low, given the time that it might take me to work around the issue. I thought briefly about moving to a python static site generation tool, but that would involve so much work that it would defeat the purpose of doing what I want to do, which is to blog fairly efficiently. 

In the end I decided to change my tagging strategy, and create some static tag templates. [This post from Mike Apted](https://www.mikeapted.com/jekyll/2015/12/30/category-and-tag-archives-in-jekyll-no-plugins/) was easy to follow along and get working. 

This comes to the nub of my problem with software. I want it to serve me, and mostly to get out of my way, but by knowing just enough to have a little bit of control of my environment I often get seduced by the desire to have perfect control. I just need to step back a little, and ask, it what I want to do here worth the potential time and effort that it might take me to complete, in contrast to finding a solution that is good enough and meets most of my needs. 



