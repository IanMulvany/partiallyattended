---
layout: post
title: How to create threads between publications and clinical trial registraion numbers
categories: 
- publishing
- crossref
- threaded publications
- eLife
---

Yesterday I attended an interesting meeting to discuss how to improve the connection between clinical trial registration ids and publications. My raw notes from the meeting follow. This is being discussed as publication threads, but the idea discussed here stands apart from the kind of publication threads that the endcode project worked on. 

# attendees
## ATTENDEES - organisations:
eLife
f1000
PLOS
BMC
Springer
lancet
BMJ
crossref 

## attendees - people
Geoffrey Bilder, CrossRef, Director of Strategic Initiatives Rachael Lammey, CrossRef, Product Manager CrossMark Daniel Shanahan, BioMed Central, Associate Publisher Tim Stevenson, BioMed Central, Product Manager
Deborah Kahn, BioMed Central, EVP Publishing Caroline Black, BioMed Central, Senior Publisher Katherine Barton, BMJ, Operations Manager Josie Breen, BMJ, Head of Editorial Production Isaac Jones, BMJ, Production Manager
Ian Mulvany, eLife, Head of Technology
Iain Hrynaszkiewicz, F1000, Outreach Director
Karen Rowlett, F1000Research, Managing Editor
Helene Faure, ISRCTN Database Manager
Hannah Jones, The Lancet, Managing Editor
Dan Lewsley, The Lancet, Head of Production
Joseph Brown, PLoS, Senior Editorial Manager
Volker Boeing, Springer, Director, Process and Content Management Mirjam Kessler, Springer, Bibliographic Metadata Manager

## Background and status
- this is a followup for the idea that was originally [blogged by iainh in 2011](http://blogs.biomedcentral.com/bmcblog/2011/01/14/towards-threaded-publications-helping-to-set-the-scientific-record-straight/). 
- the initiative stalled in 2013
- about 30k trials are registered per year
- for trials that are registered, there is nothing to link all of this together 
- currently we have 1 way links from the trial to the publications

The vision is for every publication to forward and backward link to every other publication, but this is not practical. This is where crossmark comes in. The idea would be to implement a hub and spoke model, and get everyone to wire things together in crossmark. (My take from the technical side was that the trial registration id will be the parent in all of the relationships, but this needs a bit more fleshing out).

## Crossmark notes
- lots of uptake. 
- over 1M assertions so far. 
### Fundref
- the key thing here is that it's a typed namespace that sits under the crossmark metadata container. They call this a "program" within crossmark. 
### Threaded publications proposal
- they would like to mock the fundref approach for publication threads, and this meeting is to promote this idea, and to move towards an agreement for the namespace. 
- Geoff does the "can you identify" the blacked out paper. 
### Threaded publications model
- mentions that delays were related to missing infrastructure and competing with priorities
- feels that they have launched another project that can act as a good model for threaded publications
- this model is fundref 
#### Fundref
- was done quickly
	- they tried to do the simplest thing that could possibly work
	- they put together a quick governance group from funders and publishers
	- knew that they didn't want to overcomplicate things 
- they did a couple of things
	- they standardised on a vocabulary released under CC0
	- have an update mechanism
	- provided an example widget for filling out the info
		- main thing was this is an example for implementation purposes [labs.corssref.org/fundref/widget](labs.corssref.org/fundref/widget)
	- the data collected is also released under a CC0 licence 
##### Proposal
- create a working group
- create a registry of registries
	- assign registry ids to the registries that we are interested in interoperating with
	- registration template for URLs to get to the registration (might need a resolution service?)
- how do we collect it? would like to put up a similar widget to the fundref one, and get this implemented in the submission systems 
- this all then gets passed into crossref in the same way that fundref information gets in. 
- then using the crossref API you can answer the following question
	- "show me all the articles that refer to the same clinical trial numbers mentioned in this document"
	- could be extended to also include the following query 
	- AND "the publisher of that article is in a list of trusted participants"
	- BOOM! done, thank you! 
##### Issues
- how do you find out if something has been updated?
	- the "do you know what this is" game does not work with how we signify that there is an update to an article 

## open discussion
- the proposal is to only include the trial ID
- original proposal from ian H proposed in addition
	- article type
	- publication date
	- some other attributes ...
### Issues
- no article ontology
- systematic reviews could explode the threads
- many papers may not cite the trial 
- how do you identify the trial ID in the content?
	- some publishers have collected this from some point in time, however not all publishers will have this data retroactively. 
	- BMC tags this in their XML, and example can be seen here: 
- how journals publish the id and name is not at all standardised 
	- checking that the trial id is valid 
	- that the registration is valid
		- Geoff mentions that they had exactly the same issues at the start of fundref
		- mentions that we might be able to identify the "shape of an id"
		- issue is raised that journals might just screw this up
		- AIP did a survey and ran fundref to see how often people got things wrong 
		
## Discussions 
- there is no standard article type ontology across publishers
	- Geoff mentions that his take is that the thing we are trying to capture is the relationship between the article and the protocol. 
- the issue of systematic reviews is that they are important, can we afford not to include them
	- perhaps get the author to fill in the widget, ask them to be thoughtful in terms of which trials they link to. 
- data is mentioned as being important
- tracking provenance of claims is mentioned as an issue
	- how do we allow other people to make assertions about DOIs after the fact, this leads to issues of provenance, and is related to trust
- if we only go forward from this date, it will be years before we have any useful data, if we can go backwards as well as forwards (make assertions on existing entities), it would help	
	- publishers could try and get their authors to go back and post-annotate their own publications - perhaps via ORCID
- funders should be involved
	- wellcome should be involved
- Geoff mentions that more requirements on the initiative will increase the chances the initiative would fail
	- Iain H mentions that there is probably an editorial issue of what our tolerance to the data quality is. Are editors happy with the quality of the result? 
		- is that an important enough of an issue to stop a pilot?
		- thinks that a pilot is a great way to have that conversation, if people know we are tracking this data, then people will start playing attention to the data more quickly
		- might help sort out the predatory publishers 
			- mentioned that that might not be the case, we should worry about this, but on the other hand, the more contribuions you get from researchers, the easier it is to self regulate 
			- will get sock puppet problems, but these problems are there anyway, this initative won't be a cause of that issue
			- clearly there are people out there who are trying to game the system, best thing you can do is provide as much evidence as you can
	- would there be a role for an admin and curation role
		- these are the kinds of things that fundref are discussing
		- in any of these cases you need to know who is making the assertion 
		- at the moment in the crossref system everything is being asserted by the publisher 
- interesting question, how is this better than just scraping pubmed?
	- would capture more articles that are connected to clinical ids, where at the moment those connections are not tagged
- Geoff mentions that there are many situations where the best answer is to force people to cite this information, but his instinct is that they don't want to overload that section, there won't be a way to enforce consistency. (we all know that won't work :P)
- do we include article type? 
- do we need any other metadata? can anyone think of any other kind of metadata 
- how do we identify the trial id in the content? 
- how feasible is this for production/operations to manage?
	- really needs to happen at submission, and automate everything downstream from there
- is there any additional cost on top of crossref?
	- NO (at this point)
		- if however the steering group complicated the spec, the cost might need to be recouped, basically easier is cheaper 
- trials can be registered in many different places, often because trials can happen in different countries, each requiring registration
	- could the system under discussion be used to connect one trial to another trial
	- how do you then traverse this graph
	- could this be done in a self-policing kind of a way?
	- how do you distinguish between multiple ids for the same trial and trials related to a clinical review
		- the parent is always the clinical trial, under one trial a clinical review will only be listed once
		- if you want to traverse to publications that are tied a trial via another name for that trial, under the parent trial you would want to have the other trial listed as a child, and you could then traverse to the children of that node.
- Do we need to worry about article types now?
	- Geoff says that we should come up with a proposed name for the relationships and if the debate goes on too long, then pass on and not worry about it.

### round table wrap up 
- good idea 
- registration of trials is a worry 
- could become self policing
- doubts we could get back data
	- everything needs critical mass
- prospect and licensing information is mentioned
	- Geoff mentions that this is all confused a bit
- great project, need to talk to editors
- if you have a field in your submissions system then you want to make this as a condition of acceptance
- can we say that back-files are optional?
	- yes, we have to say that this is optional
	- we would also say that back-files are not out of bounds
- from the perspective of a registrar, there is a benefit
	- more often than not a trial, when quoted, it's correct
	- the key issue is that not all papers about trials quote the trial
	- registers can find related papers via keyword search 
- thinks its worth doing from the point of the enduser
	- what's the data policy? who owns the data? what's the licence of the data?, crossref make no claims on the data, there are batch delivery methods, and there are charges for this delivery, with opt outs. 
- another element of this is that sometimes papers are recommended in F1000, and they will check if they include trial IDs there
- what next? is this system, or a version of this, a model for any funded piece of research that creates multiple outputs?
	- it has to be something that links them there has to be a starting point
- f1000 research also thinks it's a great idea, they have a posters type that might also be something that could be included. Is slightly worried about letting authors put the info in. Would be great to have a check to see if the registration is a valid registration. 
	- anything we can do to help them not put in typos is a good idea, enforcing honesty is a much harder issue
- voice of the researcher would be nice to have in the room
- BMC thinks its a strong idea, they think it's overdue, it's based on clinical trial registration, and we are not doing anything with this data at present. We are not currently exposing benefits of getting links between trials and publications. We need to possibly start simple, be aware that we might encounter some issues, but we need to move forward. 

## Actions 
	- propose a namespace for relationships to be modelled  
	- create an interest group now, that could potentially move towards being a crossref working group
		- get a funder involved  
		- get someone from the registry community  
		- get a chair who is not from crossref @done 
			- chair will come from BMC @done 
		- have a product manager who helps coordinate the meeting  
		- we can call the meeting today - meeting 0  
		- arrange the next meeting   












