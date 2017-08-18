---
categories:
- conference
- JISC
- report]
date: 2010-07-14T00:00:00Z
title: Notes from JISC activity streams workshop
url: /2010/07/14/raw-notes-jiscad/
---

## Dave Jennings giving the opening talk, http://www.slideshare.net/davidjennings

abundance of content without structure is not to be feared, example comes from music.
uses a Medneley slide to talk about the lastfm -- Medneley bridge.
talks about the amazon collaborative filter
mentions how this can lead to a dystopia, Googlezon, the big brother of recommender system.
talks about the future of pervasive recommender systems, and brain matching to content matching. 
john cage - my favourite music the music I haven't heard yet.

search
browsing
monitoring
wait for interesting things to pass by you
 
there is a social aspect, you see the tracks that others have left
there is a bandwagon effect (the network clustering effect)
black sheep element - people like to be individuals

Another dystopia, tower of babylon, how do you organise this?
 (take a leaf out of the anarchists book)

flickr does this with the use of interestingness 
	(I like his description of this as a first part in a dialog)

Jenning's law "people make most of their discoveries elsewhere" 
	(serendipitous, algorithmic recommendation, word of mouth)

Feyerabend - the conquest of abundance

In what way are the organisation represented in this room different from more commercial organisations? 

The academic operation is not framed around a totally production oriented model, and this is one big way in which these are different.


## Dave Pattern University of Huddresfield, 
These guys are using usage data. 

a path though the history of information in supermarkets:

history of user data in retail
- stamps with prices
- barcode 
- stock control
- then there were loyalty cards for data mining across transaction history
	- customer profiling
	(will libraries ever do this kind of customer profiling, at the moment they don't)

what they do at huddersfield
- 22k students
- 2k staff
- 300k books
- 3M borrowing records

not much had been done with this data, they stared playing around with this data
- people who borrowed this borrowed that
- initially they didn't know if this would be useful
	a librarian dissed this as something that amazon does to sell books, not the kind of thing that a libarary should do.
- logged in giving users a history of what they borrowed recently
- show lending paths, which books got borrowed with books 
	(that's brilliant,)

they were also able to create new book lists for the entire library (lists of new books coming in to the library)

they profiled the borrowing of students from a course, based on dewey numbers. as new books with those dewey numbers com in to the library, these get pushed to that class (also genius)

on the front page of library catalog, they pushed in the most popular keywords onto the front page as a tag cloud. this seeded a spike at the start of the year on those keywords for new searches

they can also push related keywords along with keyword search
	[[ this came up in the meeting on our new universal search bar ]] 

they have clickstream data, but they don't know what to do with this yet.

they know what they most popular keywords are that lead to a specific book, but they don't know what to do with this data yet.

# measuring the impact

from 2005 their range of unique titles that are being borrowed go up from 65k to 80k in 2009, trend continues to rise, this comes from the layer of serendipity 

it's not clear how much of this increase comes from these new tools, but certainly it's not driving to a homologous self similar borrowing behaviour

also average number of books per student is going up
	[[ how was that number calculated, as a student average, or based on per student numbers ]]

more book-loans correlate with better grades <- this is very interesting. 


# sharing data

giving the data to students in a BA design course, and creating interesting visualisations 
 
at the end of 2008 they released book circulation recommendation data. 
it's important to attach a licence with the data, they are using an opendata licence, public domain,

within a couple of days someone created a semantic representation of the data. 

"the coolest thing to do with your data will be thought of by someone else" - Rufus Pollock. 


# summary

# QA

Q what kind of conversations have you had with your academics
A the attitude was less why should we, and more why shouldn't we, academic feedback has been positive

Q from paul walk, data needs to be managed because raw low quality data is not useful

Q Richard Geddis, OUP, Counter, and something else
	would it be less easy to do recommendation for journal articles than for books, 
	talking about

	[[ how many books with dewey codes are represented in our catalog? ]]



## There's something going on, title of the first debate

# ken chad
point is "how can libs make better us of the data that they have, great rich bibliographic data".

it's not an 'it', the data is valuable, is libs don't use this, then perhaps someone else will (facebook). 


# paul millar
have been concentrating on measuring activity in the systems that libs have, but perhaps been missing the context. as we get a point where we can do something interesting with activity data, perhaps we won't need it as we will have other ways of getting recommendations.
	
with social networks people are becoming the entry points into ... ? what? 
how do we accommodate social networks into libs approach going forward

business intelligence needs context to be useful. 
context is not easily derived from a single system
there needs to be ways of adding context from different systems
	[[ perhaps one should mention the work being done by Ciro's group?? ]]

user should have control, the ability to add value to a system
he mentions that there are risks involved, anonymity can be reverse engineered
	(reminds me of paper on network anonymity)

who should own the attention data?	
	[[ mention pubsubhubbub ]]
	an open licence
	a trusted party
	the government
	google?

is afraid that we will go through a centralised service, like facebook, initially 


# richard nurse
approach it from a business intel point of view, rather that the user data. 

is it in the best interest of the institution?

essential message is that institutions need to be more pro-active.

four key reasons for why institutions should get involved

- diversity of users
- direction though data, navigation through that data
- degree of control 
- duty of service, because of public investment 

there are risks, privacy, legal etc, but these also depend on institutional policy

need selectivity on which users institutions address

if institutions don't build an understanding on this information, then others may step in and create services in their stead (could end up working in partnership, but at least institutions need to have a seat at that table.)

Q&A session for this debate:

Joy Patten from MIMAS
	do institutions have the level of data that huddersfield have
		some have and some don't (TILES project)
	then at what point do you need to look at a national strategy
	what do we know of the goldmine of data?
	(that seems like a silly point)

	A: informed by the maturity of systems
		(I would say that it has to related to the prevalence and openness of identifiers)
	Paul Millar opposed the idea of aggregating this kind of data.
	is afraid of having the data cornered by commercial institutions
	this leads to him wanting to see the data centralised and control

	[[ send notes to David Kay ]]



## debate 2, love data, hate silos

open university case study

most students are not on campus, they are not registered with the LMS

Richard Nurse leads a discussion about the kind of systems that students use, leads a discussion about what kind of information students might interact with, listed on whiteboard 
	[[ take a photo of this ]]

	there are a huge number of sources for data
		e.g. 
		reading lists
		borrowing systems
		site access
		access control systems
		VLE data
	
		uk borders agency have a requirement to know what points of contact people  on student visas have with the institute? (need 10 per year)

	an interesting question is how accessible is this data
		people have a day job, and getting the data out requires time

	someone asks "why are libraries collecting this data?"
	if it is used for business intel for institutions
	  
	Q: do these data exist in a way that can be pulled together?
		- yes, but there is a ?? on showing that one can be trusted with this data
		Manchester Metropolitan have created uniview (a students record driven data set, they are now starting to mash that up with VLE click data, and that is giving interesting information on success, 
		e.g. don't fiddle with the VLE area
		if staff put too much information into a VLE there is a negative impact on student performance

		context is everything for interpreting this data

there is a lot of evidence that students prefer to interact with others and teachers through 3rd spaces, social networking spaces, such as facebook.

students like groups, but they don't want the institutional activity to appear directly on their spaces on facebook

interesting questions:
	would any of these people consider opening up some more of this data as "open data"
	(somewhat of a stunned silence)

interesting point, will government enthusiasm for open data affect universities 
	- teaching quality information should be made available, for instance

OU have started thinking about mining this, using SFX for instance
one of the big problems is getting access to that data, the structures that manage things like the VLE are not directly involved in doing this investigation, so you need to get high enough up on their agenda.

one could go an look at user generated content, book reviews from amazon, for instance.

have started to use google apps, are thinking about building custom apps for their users

my comment - identifiers are key

other comment - data warehouses are hugely valuable.
	comment: these are mainly being built at the moment for institutions to make institutional decisions

	not currently being thought of as being used to drive student services, but one could get that in via the back door.



## debate 4, appropriate or inappropriate use, legal issues

- privacy is not the issue, control is

some opening remarks, 

the landscape of the data is not simple, all of these cases will apply, open/closed legal/illegal appropriate/inappropriate 

often some of this is related to catalog entries, who creates the catalog entry.

all of the data under discussion is currently under the control of institutions.

there are clear legal provisions
	17 yo students are children
		adds requirements to what you can do with data

	privacy
	
	access

comment, legal requirements can change. 
mentions the downstream dilemma, 

naomi klein -- works on IP, and has looked at IP and bibliographic information. 

mentioned that the information commissioner has issued a guidance that you should treat any such information as personal information

jisc legal mentioned some guidelines

- need to keep personal data secure
- there is a danger of triangulation 

question what are we risking by not doing something with this data?
	
a: we risk missing opportunities to cross reference data, and to create new connections.

conversation reverts to legal FUD discussions

one risk in not doing anything is getting labelled that ones institution is not innovating, and hence not providing value for money.



##  feedback from two evening debates

questions about evidence and whether we should "just do it"

Elib was the 1000 flowers bloom approach

there is a fear here that funding is going to be reduced, so not doing this is going to be a road to ruin,

doing these things is going to be a need to do thing, in order to enhance the learning experience.

- increase student satisfaction
- increase student progression

this means service delivery, and learning enabling need to focus on tools (?) that can drive satisfaction and progression.


## afternoon session

interm report on mosaic

they are looking to build a version built on lucene, hadoop and linked data.

mark@headtech.com


## mark toole (director of stirling information services), richard korn OU, naomi klein legal


# Mark Toole
some benefits 
	is a fascinating area
	could see some things that could be made

some costs
	biggest cost is priority, working on this stops him working on other things. 
	how do the benefits from this contribute more than resources put into other efforts, buying more books, for instance.

	in the end, there is not enough quantifiable evidence, we need more real case studies.

	comment: challenge the idea that there is not enough evidence. 
		there is a large body of existing data, e.g. known algorithms, amazon, understanding of privacy issues. it might be outside of the sector at the moment, perhaps we need within sector examples [[ our expert finder could be a good example within this context ]]

# richard korn, open university

	nice quotes from wall-mart, google, and ms, data should be used to change the services that produce the data, not simply seen as a by-product of the data.

	mentions SFX, are thinking of playing around with an api to improve this.

	nice example from search results. 

	Telstar is using SFX to link to resources

	linked data for OU content, Lucero

	slideshare.net/richardnurse


# naomi klein, getting business intelligence from user activity data, legal challenges

areas of law that touch on this

- DP act 1998
- human rights act
- right of privacy
- database rights
- contract law


with minors there are further issues

there may be IP rights associated with a 'mere fact' if it is collated in a DB, or if it has been enhanced through a process, e.g. recommended 

- built a tool hosted by jisc legal that gives info on IP rights on bibliographic data

the data may be provided under contract from a 3rd party, you may be bound by those contractual obligations.

Data Pretension act in a nutshell:
	if the individual can be identified it is classed as personal data
	
	there are a a few debates about this issue
	
	if it is personal data, you need consent

	JISC legal is publishing a report on consent management

	institutions may have a get out clause, regarding requirement to provide services (was that right?)

	look at web2rights toolkit

mentions cultural fear in the face of data protection issues, very good point, one should not be frozen into inaction, with the appropriate information it is possible to navigate these issues.

when might activity data be personal data?

	- cloud computing and personal data
		if the information is processed externally, and can be tracked back to an individual

	- use of social networking

	- google and usage data, e.g. search data.
		triangulation

	- library activity data

recommendation
	- any info that provides an indication of a users' online activity should be treated as peronal data, even if individual can\t be identified

	role of passing on user data to 3rd bpodies

the role of the institution:
	
bottom line
	need to ensure that you have consent before processing personal data

	anonymous data still needs to be checked against risk of triangulation.


## evening session making recommendations for JISC activity on a national level,

we need to give some concrete suggestions on a national level:

davep produced data, and the world didn't end 
data model from jisc mosaic project
there is potential for legal advice

is next step then is to encourage the creation of more services??
clarify what we have

thinking nationally, what is the case?

can we give more compelling business cases,
mosaic project ran into trouble with senior stakeholder buy-in

again the connection between item usage and performance indicators is hi-lighted as being hugely important. 

the performance data is contained in something like a VLE, 

HESA data provides something in the public record, though it may be in a somewhat convoluted form.

many systems are not even collecting data at the moment, they sort of need to collect the data if they want to use it at some point.


## recommendations

# national infrastructure

- find a way to test the hypothesis that extending the data towards a national level could provide value

- get institutions to start tracking this data, for if they don't they can't use the data in the future, should they wish to


# learning & research recommendations

- cookbooks for VLES, how do you get activity data out of these vendor systems

- who are the stakeholders that need to be won over? involve them, they may have some experience to lend to the issue

- researchers are a problem, they go about community building in a totally different way, they may be looking to things like Medneley to get information about research communities, rather than something like the VLE


# library and local collections

- concern of duplication of effort, need and a desire to share knowledge, so for example methods for getting data out of systems can be shared

- need some case studies that could support the anecdotal stories

- concern that we don't know what data we are going to share, address this with a survey to see what's been done, and what can be done in library systems. 

- who is the authority on this, if it's not dave, who is it?

- something about this and books, and numbers of books, missed that bit.

- discussions around reading lists, and how useful students find these to be, some lecturers have IP around their reading lists, making this difficult to share.

specific recommendations:

- need to profile student behaviour in terms of e-resources, not just books

- need strong evidence that library services are integral to learning, and not just an addon.

- open source systems

- if we share our data others will find the interesting things within the data. 


# end comments

this community needs to be accountable, usage stats and services built around that can be one way to do that 


