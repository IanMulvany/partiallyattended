---
title: Is caution justified when thinking about docker? 
url: 2018/05/16/Is_caution_justified_when_thinking_about_docker?_/
date: 2018-05-16T00:00:00Z
categories:
- software
- docker
- architecture
---

I’ve been fascinated by docker for the past few years, and there is clearly a “rush to dockerise” I’ve been Neville’s by how easy it is to get complex systems up and running locally, so perhaps it’s time to read with some caution some of the potential downsides. 

http://www.smashcompany.com/technology/docker-is-a-dangerous-gamble-which-we-will-regret Argues about those. 

He article highlights exactly why I like docker:

> Me: “I can write a bash script. Or “make”. Or any other kind of installer, of which there are dozens. We have all been doing this for many years.”  
> Them: “That’s insane. The bash script might break, and you’ll have to spend time debugging it, and it won’t necessarily work the same on your machine, compared to mine. With Docker, we write the build script and then its guaranteed to work the same everywhere, on your machine as well as mine.”  
> Like all sales pitches, this is seductive because it leads with the most attractive feature of Docker. As a development tool, Docker can seem less messy and more consistent than other approaches. It’s the second phase of Docker use, when people try to use it in production, where life becomes painful.  

but goes on to point out some of the risks of using docker in production. There is a lot in the post. If you are thinking about putting docker into production it’s well worth a read. 

A sentiment I can strongly get behind is 

> Solve your problems in the simplest way you can. If the switch away from Ruby/Python/Perl to a newer language and eco-system allows you to achieve massive scale with less technologies and less moving parts, then you absolutely have a professional obligation to do so.   

Also 

> We’ve been building websites for 25 years now, and we didn’t need Docker.  

Is a gem. 

My final thought on this post is that, as with so many things, it comes down to the people involved. No tool, docker or otherwise, is going to save you from the problems inherent in building software as a team, and if you can find a good path through those problems the technology you use to help you on your way is largely secondary. 



