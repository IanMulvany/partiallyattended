---
layout: post
title: STM innovations seminar, London, 2013
categories: 
- data
- STM
- publishing
- lens
---

Today I'm at the STM innovations seminar. The twitter tag for today is [#ukinno](https://twitter.com/search?q=%23ukinno&src=typd). The program is [online](http://www.stm-assoc.org/events/innovations-seminar-2013/).

I'm going to take a light approach to blogging today, I'll probably hang out mostly on Twitter. 


## 9.35 The Research Data Revolution, Sayeed Choudhury, Associate Dean for Research Data Management,
Johns Hopkins University 
> Data has become a major topic of interest from all sectors of society with headlines such as “Data is the new oil” to assertions from McKinsey that data is the fourth factor of production. Within higher education, new forms of data intensive scholarship have already begun to transform research and learning. The “Research Data Revolution” will examine the implications of these developments for libraries and publishers especially as they relate to new forms of competition.

Sayeed is talking about data in general, he is associated with [http://dataconservancy.org](http://dataconservancy.org).

Some key points from his talk.

- data is the new Oil
- data has to be made open and actionable by machines
- from the libraries perspective, data are a new form of collections 
- treat manuscripts like a dataset, even humanists are starting to see new possabilites and new methods, creating a completely new experience online. 
- as librarians, think about the realtionship you can have with your communities, if they start to manage and curate the data, this leads to an opportunity for creating new relationships built around those special collections. 

Nice take on `Big Data`. If a community is overwhelme by it's data, then the data becomes big. For the Astronomers today the SDSS is no longer big - 150TB, as the astronomers now have tools to deal with this data. New proposed experiments are creating data that will overwhelm the field, lead to a situation in which most of the data will have to be thrown away on first run. 

He makes the point of needing to know the provenonce of data, how data moves from one fromat to another. I'm a big fan now of making this available in code, via automated tool chains such as [chef](http://www.opscode.com/chef/) and [vagrant](http://www.vagrantup.com). 

If data collections become open, no one is going to care about how much data you have, in contrast to the services that you provide. Some services may be hard to run across the network, but generally libraries and publishers might differentiate themselves via the servcies they offer, rather than as acting as gatekeepers to the content. We need to get serious about machine based services to the content. There will be some things that only humans can do. 

Mentions a seminal report on the dynamics of infrastrucure developement. (you can find a copy online here [http://deepblue.lib.umich.edu/bitstream/handle/2027.42/49353/UnderstandingInfrastructure2007.pdf?sequence=3][http://deepblue.lib.umich.edu/bitstream/handle/2027.42/49353/UnderstandingInfrastructure2007.pdf?sequence=3] - open access FTW!). The conclusion from the reoprt is that we will need new forms of infrastrucutre. Que story about stupid machines and reccomendation engines going wrong, but the machine corrected itself quickly. 

Google and Amazon have figured out that at scale even dumb machines can do well. That is why scale is important. It's a means, but not an end. At Hopkins they have one large astronomy dataset, but there are many other astronomy data sets out there. They have to think of services across all of those data sets, not just on one data set. The scale will allow machines to appear to be clever, and this is where the role of the expert will remain important. 

The discussion moves on to curation of data, and who is doing a good job. He mentions [http://schema.org](http://schema.org), mentions that top 5 places that do data management are Apple, Facebook, Twitter, Google and Amazon. Big question, are these pople doing the creation of these knowledge graphs with a view to preservation. The answer is proabaly not. The informaiton graphs that are coming out of the librarian community - OAE-ORE - are richer, smaller, are not incompatable with Schema.org, but at the moment they have no skin the the game, they have to offer something. (I didn't really get the point here).  
	
>
Publising is about content and not format

Question time, but I'm probably not going to capture the Q&A session. 


## 11.00 Morning plenary: ePublishing evolutions
Moderated by: Dave Martinsen, ACS
 
## Watson and the Journey to Cognitive Computing Frank Stein, IBM 



> Today, many of our science, technical, and medical professionals can not keep up with the growing amount of new information being produced in the world.   The complication is that although we have ever faster computers, they haven’t been designed to process and understand this information which is mostly in human-consumable formats. This means we’re not getting the full value out of our scientific, medical, and technical endeavors.  This talk will provide a brief overview of Watson as a cognitive computing exemplar, and of Cognitive Computing more generally. We will discuss some of the implications of this new technology, providing a basis to envision changes that will start impacting our world and to understand some of the benefits and challenges that cognitive computers will bring to the scientists and professionals in the fields that you support.
 
He is making the Watson algorithm seem comprehensible. I'm sure there is a lot of work behind this system. I like that the Watson system uses inference, and they use probablistic reasoning. 

They have over 100 algorithms to do the matching between input and the underlying knowledge corpus. 

Semaintic technlogy was helpful, but not the be all, and end all, they used a whole bunch of other techniques in order to win at Jeapordy. 

How do they start appying the Watson technology to the needs of their customers? They have a new divsion of the company to just figure out how to commmercialise the tech. They started with appliations in Medicine, have moved to finance, and they are looking at networks of industries now that this could be applied in. 

(Of course a great question is how could we imagine brining this technology into the publishing domain). 

They are moving forward with productising Watson, however they have a problem. For them the next phase they are looking at cognitive computing. The Watson brain used about 85 - 100KW of power. If they are going to get bigger more sophisticated systems, they would need to spend more power.

There are a bunch of techologies that need to be enabled, but they boil down to doming more networked computing on smaller faster less power hungry chips, with better learning algorithms sitting on top of this. 

They want natural language interactions to these systems, and they want to move away from the von Neumann architectures, these future architectures will break down the barrieres between memory and computaton, on the chip. They are prototyping chips - such as the SyNAPSE chip. Does not use a clock, it's all event based on the chip. This needs an entirely new stack of programming tools, from compliers - all the way up. More information on these chips [here](http://www.research.ibm.com/cognitive-computing/neurosynaptic-chips.shtml#fbid=OH8oQM4QCP0). The goal for SyNAPSE is to

>IBM’s long-term goal is to build a neurosynaptic chip system with ten billion neurons and hundred trillion synapses, all while consuming only one kilowatt of power and occupying less than two liters of volume.

Basically, they want to build a brain on a chip - good luck to them!

 
## Source Data and other article enrichments Thomas Lemberger, EMBO Journals

>
The aim of the EMBO SourceData project is to build tools that will allow journals to integrate data and structured biological metadata in published papers and to develop data-oriented methods to search the literature. 
 
I've reported on what Thomas talks about elsewhere before. I'll really focus my notes here on any specific, interesting and new thoughts that come up in the course of this talk. 

Makes the good point that the majority of journals in the life science are data journals as they all have data in them. Small scale data, but data nonetheless. 

They look for Actionable data, this does not have to be the underlying raw data. An example is the graph derviced from high throughput screening. The underlying data is several TB in size. They allow the community to decide what the most actionable, and processed version of the data are, that should be presented with the paper. 

For tagging the metadtaa in their papers they have three levels of metadata:

- level 1 - lists of chemcial and biological components  
- level 2- representation of the causality of the experiment, e.g. "measurement of Y as a function of A using method C".
- level 3 - machine readable representation with standard identifiers 

They are generating tools to help with this curation. 'Data copy editors'. This is very interesting, and it would be great to understand their toolchain. Hopefully I'll get a chance to see it more closely at the workshop that we are organising next week on data and literature integration. 

Now using Filemaker to demo how a structured query based on tagged entities could do for simplifying discovery. I suspect that the next speaker will have something to say about this topic too. 


## Actionable Data - the Wolfram Approach Matthew Day, Wolfram Research  
 >
Wolfram Research has created several actionable data technologies, particularly WolframAlpha.com and the Computable Document Format. The new focus is on enhancements that will greatly extend our ability to make all sorts data files readily actionable with minimal work from data producers or curators.

(In terms of the context of Matt's talk, it might be interesting to point to the recent blog post by Stephen Wolfram on [the promise of the Wolfram ecosystem](http://blog.stephenwolfram.com/2013/11/something-very-big-is-coming-our-most-important-technology-project-yet/)).

They want to be able to create an engine that can provide answers, where those answers don't exist yet, so an engine like google can't currently help. 

Not taking so many notes, getting a little nervous about my impending flash presentation. 


## 14 00 Special Introduction on Science 2.0 and current developments in the EU, Prof Jean-Claude Burgelman, EU Commission, DG Research and Innovation, Head of Unit

Bottom line, most stakeholders support open science. Different aspects of open science, and science2.0, are moving at different paces. The directorate is producing a green paper on the topic. This will focus on what actions, or not, the EC will take. 




## 14 15 Afternoon Keynote: e-Science and we-Science: Making citizen science work Moderated by: Dave Smith (IET)  ## Lessons from the Zooniverse : Science with (nearly) a million collaborators Chris Lintott, Researcher, Oxford Astrophysics and Principal Investigator, Zooniverse  

>
The Zooniverse is the world’s most successful platform for citizen science - the involvement of non-professionals in the scientific enterprise. Zooniverse founder Chris Lintott will cover the highlights of six years of collaboration, including mysterious galaxy-sized gas clouds, unusual planets and a journey across the Serengeti, and explain the lessons for researchers and publishers alike in bringing science to such a large audience.

This is an amazing talk. I'm not even going to try to take notes, I'm enjoying the talk waaaaay too much. 

There is an interesting issue raised at the end of the talk. Zooniverse still cares about scientific publications, but they see little interaction between the community who do the contribution, and the research publications. There is a strong desire from Chris to do something about this, but what to do is not yet aswered. 


15 00 Afternoon Plenary: e-Science, e-Research, e-Publishing
 
## e-Research and the demise of the scholarly article. David De Roure, Director of e-Research Centre, Oxford

Dave is going to focus on the intersection between large numbers of people and large computaional capacity. (A great example is that facebook is genering 100s of terabytes of data per year). 

A nice story on how Dave came up with the 8 things that will have led to the demise of the paper. 

"A pdf exploded today when a scientist tried to paste in the twitter firehose" 




## 16 00 Afternoon Plenary: e-Science, e-Research, e-Publishing Moderated by: Howard Ratner, CHORUS   ## Text and Data Mining, discovering new patterns Nicko Goncharoff, Digital Science

Very interesting. SureChem is going into the public domain. Will find out more during the course of this talk. Bottom line, EMBL is taking over. 

(This is obviously the first entity that Digital Science is divesting. It's important that Digital Science do this if their model is to succeed in the long term, it's intersting to see this starting to happen. It will be interesting to see if this trend continues).

  
## Wearable Computers: Future Fix-All or Fashion Faux Pas? Heather Ruland Staines, SIPX    
> 
From Google Glass to the Samsung Gear, technology blogs and expos are all over wearable computing. Whether as extensions to our phones or as sensors to monitor our health or purchasing behavior, wearables are coming. Learn about how wearable computers are being tested in education and teaching contexts, what the latest initiatives are, and hear from a Glass Explorer about the potential and the perils of a computer on your face.

She is wearing a google glass. I really like the idea of diminished reality, in which a google glass like device could block out aspects of reality that you don't want to interact with - like advertising (pverty and misery perhaps?).

(Getting one of these things into a contact lens would really really annoy my wife, so I applaud the rest of humanities march towards the cyborg singularity, and I shall be watching quietly from the sidelines.)

Final word on ethics of using the google glass

>
If you are going to be a jerk, you're going to be a jerk. 

