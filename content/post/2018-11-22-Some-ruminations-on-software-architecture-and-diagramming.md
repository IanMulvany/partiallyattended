---
title: Some ruminations on software architecture and diagramming
url: 2018/11/22/Some_ruminations_on_software_architecture_and_diagramming/
date: 2018-11-22T00:00:00Z
categories:
- diagramming
- architecture
- systems
---

So Pat Kua recently tweeted:

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">UML failed so here we have AML (Arbitrary Modeling Language) <a href="https://t.co/BnbgC8ZHTD">https://t.co/BnbgC8ZHTD</a></p>&mdash; Pat Kua (@patkua) <a href="https://twitter.com/patkua/status/1061021362716852225?ref_src=twsrc%5Etfw">November 9, 2018<_a><_blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

and this got me thinking about the worries I've had about not doing "diagramming" right, but the above tweet led me to read a ton of really interesting posts on software architecting. 

Bottom line is, as with so many things, pick the artefact that fits the purpose and the audience. 

UML - the unified modelling language (https://en.wikipedia.org/wiki/Unified_Modeling_Language) is the de-facto standard for creating entity-relationship diagrams. The following thread talks about why it looks like this approach has "failed"https://dzone.com/articles/uml-failed-so-here-we-have-aml. The question under consideration is whether UML has met the needs of creating great software. 

This post for me nails it: http://memeagora.blogspot.com/2008/12/irrational-artifact-attachment.html 

> If you create a beautiful UML diagram using some tool like Visio that takes 2 hours, you have an irrational attachment to that artifact that's roughly proportional to the amount of time invested. That means that you'll be more attached to a 4 hour diagram than a 2 hour one. By "irrational attachment", I mean that it's harder to listen to reason as to why it's wrong because you know how much time it took to create it (and therefore the required effort to update it).  

What this is saying is that you need to not get too tied to an artefact when what you are doing is changing underneath you, as it will prevent you from adapting you thinking towards the best solution. 

One of my good friends who is an architect for transport for London had a great take on this. For communicating plans, and working through the design phase keeping diagrams really low fidelity is important, and this is the level of abstraction that architects should probably live in, but a problem arises when developers think that the architects should be doing detailed diagramming, and vice versa. The  [C4 model](https://c4model.com) sounds like a great way to navigate these kinds of discussions, at what level of abstraction are we dealing with? Who are the stakeholders that are involved? What is being communicated? How is this artefact going to reduce uncertainty and increase the likelihood for success?  

If you do want to create diagrams though then do try to make your diagrams easy to read: [Communicate with more Appealing Diagrams | Sparks](https://blog.zone24x7.com/communicate-with-more-appealing-diagrams/)

Tools that I have found to be useful for creating “diagrams” of the high level design of system that I try to show to people are:

* Keynote  
* Paper by 53 on iOS 
* Omnigraffle with AWS service stencils 

Recently (within the last week), I’ve found a nice tool for crating network relationships — [Arrow Tool](http://www.apcjones.com/arrows/#). 

Finally, (this episode)[[Episode 228: Software Architecture Sketches with Simon Brown  : Software Engineering Radio](http://www.se-radio.net/2015/06/episode-228-software-architecture-sketches-with-simon-brown/)] of software engineering radio sounds like it has a good take on this topic (but I’ve not had the time to fully listen to it yet). It talks about the c4 model for describing software architecture [The C4 model for software architecture](https://c4model.com). 
