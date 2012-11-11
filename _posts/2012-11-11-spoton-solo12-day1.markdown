---
layout: post
title: SpotOn day 1. 
categories: 
- #solo12
- STM
- conference
- solo
- spoton
- London
- publishing
---

I'll keep a partial, live-idsh blog going during the day. I've been going to these things, I think, since about 2008. I really like these meetings. I'm going to probably keep these notes pretty lightweight. 

## sessions<a id="top">:</a>

- [Ben Goldacre](#ben)
- [Kamila ](#front)
- [Session on whether science journalism will be replaced](#replace)

now on to the sessions! 

## [Ben Goldacre][bg] - opening keynote, on data. <a id="ben">.</a> ([top](#top))

Ben is talking about the issues that arise when you place a lot of data in one place. Modern tools that allow large data sets to be indexable create a new thing, a thing that not many people understand. He makes the analogy between bringing many atoms of uranium together, this creates a qualatativley different thing. Dangerous, but powerful. Data has a similar property. (We often manage to ignore the potential power that the elves at google have). He mentions the new data store on health data.

For individual studies, we are learning ways to slightly distort the data to make it more useful. Bringing a lot of data together allows you to start looking for patterns. Sometimes you are only seeing faces in the cloud, but sometimes you do see real patterns. HRT is an interesting example where just observing leads you down very much the wrong path. You need to have randomised control trials. 

There is a great example of giving steroids to people with head injuries coming into A&E. There were no randomised trials, and people were unwilling to not give steroids, as there was a belief that it worked. When you are facing a person who is dying on the table it is very hard to take a step back and make the decision to not give the intervention _even if there was no evidence that the intervention worked_. When they finally did the trial they discovered that people who were given the steroids were more likely to die. 

(Although not as dramatic, by a long way this issue of trying randomised trials is something that is also hard in a business context, as large companies start to increase the cost of trying small iterations, one of the issues being the overhead that comes along with increased amounts of communication with a larger number of stakeholders). 

Ben mentions the problem also extends to government policy. Government tends to like to do pilot studies, and not controlled trialls. He was involved in the writing of a [white paper][pol] on the value of randomised trials in determining the effectiveness of policy. (an old [climbing partnerr][dh] of mine works on these issues, it's interesting to look at existing data to see where policy has a real effect). 

One of the threads of the talk is looking at data a low cost (how do you reduce the cost of iterating, and finding out whether what you are doing is working? - a common call in the startup scene, however it should be said that we often plough on regardless of the evidence, and just like doing what we like doing, it's really hard to pay attention to the data). 

How do you design trials that are cheap, that show you how to find those small improvements? 

At the moment we are already collecting a lot of data in health system. If you take the opportunity to put a little bit of structure at the beginning you can get a lot of valuable information downstream. They are doing a trial by looking at [statins][st]. 

The idea is to randomly assign a statin to people at the doctor, and track this at the point of assignment. (there is no current information on which statin is better, and they are effectively being assigned randomly, but with no tracking). By adding this small piece of structure at the beginning you end up with a nice randomised trial. 

If you could impose this structure at any point where there was uncertainty in efficacy of interventions, you could turn the whole of the NHS into a testing machine for finding those 1% improvements, that collectivity can have en enormous positive effect on our health.

Ben talks about the need to have tools that can find good content to read, over the crud, in the same way that we want to find good studies, over shit studies. (They are about to launch a project with the open data foundation that looks at waste that is happening at the point of prescription). 

He discusses [altmetrics][alm] - briefly. 

(Of course these issues of looking for good filters, and finding context at point of consumption, is an interesting topic, that is top of mind for a lot of us).

[bg]: http://www.badscience.net/
[pol]: http://www.cabinetoffice.gov.uk/resource-library/test-learn-adapt-developing-public-policy-randomised-controlled-trials
[dh]: http://sm.psc.isr.umich.edu/debra/
[st]: http://en.wikipedia.org/wiki/Statin 
[alm]: http://altmetrics.org/manifesto/



## [Kamila Markram][km] - publishing science in the internet age <a id="front">.</a> ([top](#top))

Kamila is one of the founders of [frontiers][front]. She starts by talking about some trends with science online. A trend is facebook, most scientists are now there, however both facebook and linkedin do not cater the direct needs of scientists. (I have some opinions about the value of online scientific networks and the difficulty of building these things). 

The [frontiers network][fn] immediately increased pageviews on articles and author profiles (+70% on some metrics). (this is pretty impressive). 

She mentions that google docs is being used to collaboratively creating papers. IMO getting the authoring tools fixed is one of the big areas of schlep/opportunity in the science communication space. 

(There are a very large number of services being mentioned in this talk, I have heard of most of them, but there seems to be too many for me to grok, and check on whether or not I know them). 

It also looks like frontiers is built on top of ASP, that is one stack that I have very little experience of. 

Kamila starts talking about publishing trends. There are some comments about open access. She is touching on the issue of bias in peer review. For sure, peer review is this weird process, and there is a lot of bias. ("~~Fixing~~"/Augmenting peer review, let's do that - actually, the issue is the social aspect, it's soylent green, it's totally made up by researchers themselves, it was put to me that the least important community is are the senior academics, as they are the ones that will die soonest).

What Frontiers have done with the peer review system is really nice. They have an open collaborative peer review system. In addition they track ALMs on published papers, and they do a review, looking for the most read papers, after a few months. Papers that get into this top list, get invited to be extended to review papers, and this has worked really well (though to be honest, on their journals pages it took me a few minutes to find the journals, I think this site is optimised for google to be the main landing route to the content). 

To see the reviewers you can navigate to the bottom of the paper, see [here][paper], for example. (the reviewers are exposed in a naked DOM element, this would be a really really great candidate for a microformat markup, the reviewers are not included in the article XML, so figuring out how to machine read this data is not totally transparent, but it is a great start.) 

They do link through to a [profile of the reviewer][profile]. I couldn't see a list of papers that this person had reviewed, but I understand that they have metrics which allow them to query in their backend to find out which reviewers end up accepting papers that get more reads, indicating that those reviewers are able to better identify better research. That would be really interesting information to make public. 

You can see an example of a [metrics][metric] page here. 

(IMO the key thing about the network that they have generated is that there is a very close connection between the published object and the persons involved with those published objects. I always wanted that for nature network, and had wished that we could have auto-created profile pages for nature authors, but with a journal like Nature you just have a very large challenge with legacy data.)

I've been looking for a landing page showing trending or top articles, but I can't find one at the moment. I'll post a link later if I find such a page. 


[km]: http://bluebrain.epfl.ch/page-68308-en.html
[front]: http://www.frontiersin.org/
[fn]: http://www.frontiersin.org/events/all_events
[sg]: http://en.wikipedia.org/wiki/Soylent_Green
[metric]: http://www.frontiersin.org/Journal/AbstractImpact.aspx?s=1270&name=Non-Coding_RNA&ART_DOI=10.3389/fgene.2012.00233&type=1
[paper]: http://www.frontiersin.org/Non-Coding_RNA/10.3389/fgene.2012.00233/full
[profile]: http://community.frontiersin.org/people/PengJin/14793


## Session on whether science journalism will be replaced<a id="replace">.</a> ([top](#top))

There is a lot of violent agreement in [this session][jnm]. Agreement is that new media won't replace science news media, but can compliment it.  

Some comments of moderate interest from this session:

- many members of the public still believe that news in unbiased
- having a science presence in the newsroom is a **good** thing
- mainstream news continues to attract larger audiences than new media on it's own.
- need a guarantee of independence 
- "Wellcome trust funded everything to do with lovely things"



I guess the reason that this is even a topic is that there is a feeling that science can be presented in terribly distorting ways in the media. 

[jnm]: http://www.nature.com/spoton/event/spoton-london-2012-will-multimedia-content-created-by-organisations-replace-traditional-science-journalism/
