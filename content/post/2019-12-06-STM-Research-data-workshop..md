---
title: STM Research data workshop. 
url: 2019/12/06/STM_Research_data_workshop._/
date: 2019-12-06T00:00:00Z
categories:
- data
- research
- das
- data-citation
- impact
- stm
---

The start of December is always a busy time for news in the STM / Product space. There is the annual STM meeting in London, and AWS re-invent also kicks off this week. As a result, within just a few days, I find that I have more things to write about than I can ever possibly have time to get through before the end of the year, we must plough on, and plough on we will. 

This post is about a half day workshop that I attended on Monday on the topic of research data sharing, and the role that publishers can play in this. The STM society is going to have a focus on research data in 2020. They say:

> As part of STM’s mission to support Open Science and Research Reproducibility, STM will commence an action-driven initiative over the next year to promote the transparency, availability, linking, and proper citation of research data in scholarly communication.   

This is being led by Joris van Rossum. 

The workshop mainly involved updates on what has, or hasn't worked for different stakeholders around promoting research data sharing. 

If I were to summarise very briefly, then here are my main takeaways: 

* Implement a data policy for your journals. 
* Try to mandate data availability statements. 
* Further to that, try to mandate data availability statements that require links, where the data is available, rather than statements about “data being available upon request”, which usually means that the data is not available upon request. 
* There remains skepticism in many fields about data sharing (engineering and chemistry), but hey, better get in now, before your funders demand this, and you have to scrabble.
* That said, growth in publications with links to data is strong (21% year on year growth to a current annual rate of about 60K publications annually).  
* Growth in papers with a data availability statement is positively exploding.  
* If you deposit good metadata about links to data repositories, CrossRef will auto-filter these for you, to make it easy to see these connections, using the event data infrastructure (good to see that having a real use-case!). 
* If you were so inclined, and wanted to create your own data linking hub, then use the scholix standard. 
* Most publishers consider themselves to be at the start of this journey (that means we should have no embarrassment about just getting started, as everyone can only look better from here on out!). 

It was clear that there are lots of great pieces of current infrastructure that support data to object linking. It’s almost as if having shared infrastructure and standards that can be flexible enough to support emerging scholarly norms, and the needs of researchers, funders and publishers is a good thing, and that it might be a royal pain in the ass to re-write core pieces of this infrastructure to support edge cases, or a small number of stakeholder (just a thought). 
It was also clear from the engagement in the room that many people are taking this seriously. This is great to see, after nearly a decade of observing conversations about this kind of thing, this kind of thing is now becoming a real thing. 

A personal highlight for me was seeing the utility of the JATS extensions to marking up citations as data citations. I participated in the group that led to that change. We imagined back then that publishers would flock to this standard. OK, so that didn’t happen then, but c’mon, it’s starting to happen now! 

Big shout-outs go to Taylor & Francis, Elsevier, Wiley and SpingerNature who are all doing great work to support this kind of linking. 

I was most impressed by the work that Taylor & Francis have done to support the adoption of data citation and data linking. They have done a lot of work to make this easier for all stakeholders, and what they have done really represents a great shopping list for anyone thinking about what it might take to implement really well. They:

* have a 5-tier data policy 
* run workshops for authors (SpringerNature do this too, as I am sure do others). 
* check papers that have data to ensure they cite the data 
* give guidance on what repository authors should use 
* provide guiding information on how to create data availability statements  
* a catch-all email inbox to handle queries about data 
* updates to their publishing platform and submissions platforms 
* typesetters with specific instructions on how to handle data 
* implementing open science badges 
* creating author guides in different languages, especially in Chinese.

The two big issues in my mind are the following: 

* there are lots of patterns for data policies. Do you follow TOP guidelines, do you have two, three, four, five, six or more levels? We have all been finding our way. If you are getting started, just follow the [TOP Guidelines](https://cos.io/top/)! 
* metadata infrastructure is still creaky (I mean, it's always going to be, but this means that there is a real cost to implementing this stuff). If we could get vendors to agree and share on good practice about how to identify links to data sets, and how to tag them appropriately, then this could become a turn-key ask by publishers, and that would accelerate adoption. 

Overall I think things are really moving in the right direction. It was a great workshop, and I’d like to thank Joris and Eefke Smit for running it! 

### Some related and interesting links. 

[FAIRsharing](https://fairsharing.org) were at the meeting. They curate and host a registry of data repositories and data policies, and make it possible for you to determine which repositories match which policies. This is a fantastic resource. 

Chris Graf from Wiley mentioned this preprint [The open data challenge: An analysis of 124,000 data availability statements, and an ironic lesson about data management plans - Authorea](https://www.authorea.com/users/260319/articles/399874-the-open-data-challenge-an-analysis-of-124-000-data-availability-statements-and-an-ironic-lesson-about-data-management-plans?commit=ad98ddb9a1e072174f34e0c5ae88de32c8431409). They saw a huge uptick in papers with a DAS in 2019, after requiring it in more of their journals. Now about 120K papers have such a statement, but with large growth.

Many researchers are now writing data management plans, and there are tools out there to support this (e.g. [DMPonline](https://dmponline.dcc.ac.uk) and [DMP tool CDL - Google Search](https://www.google.com/search?client=safari&rls=en&q=DMP+tool+CDL&ie=UTF-8&oe=UTF-8)). It would be great if these tools could also provide template DAS’s for authors! 

If you are interested in machine learning models that can connect data to papers, the rich context project from the Coleridge initiative is running a competition to build such models. We didn’t discuss this approach in the workshop, but it might be worth looking at in a followup workshop. You can read about the last iteration of the comp here: [The Coleridge Initiative](https://coleridgeinitiative.org/richcontextcompetition) and the next iteration will be announced soon. 


