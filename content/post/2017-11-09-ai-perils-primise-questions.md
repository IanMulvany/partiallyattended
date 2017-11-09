---
title: The robots are coming, the promise and perils of AI - questions
date: 2017-11-09T00:00:00Z
url: 2017/11/09/The_robots_are_coming,_the_promise_and_perils_of_AI_-_questions/
categories:
- AI
- publishing
- libraries
- charleston
- dystopia
- machine learning
- future
---


I'm at the Charleston conference, my first time, and we [had a panel discussion this morning talking about AI](https://2017charlestonconference.sched.com/event/CCxm/all-the-robots-are-coming-the-promise-and-the-peril-of-ai).

On the panel were:

Heather Staines
Director of Partnerships, Hypothes.is

Peter Brantley
Director of Online Strategy, UC Davis

Elizabeth Caley
Chief of Staff, Meta, Chan Zuckerberg Initiative

Ruth Pickering
Co-founder and Chief Strategy Officer, Yewno

and myself. It was a pleasure to be on a panel with these amazing people.

There was a lot of interest from the audience, and we didn't get anywhere close to talking through all of the questions that we had discussed as a panel ahead of the session, so I'm going to blog the questions that we had prepared. Importantly below are mostly **my answers** to those questions. The answers below don't necessarily represent the views of my fellow panellists, and in fact I'm pretty sure we hold divergent opinions on some of these questions, but that's OK, it's a complex topic. Some of the best answers below do actually belong to the other panelists, but google doc tells me that author was anonymous.

Before diving in to running over the questions I want to make a quick statement around one topic that came up a bit in the Q&A. We got to talking about how "AI" can solve problems, would "AI" have prevented the financial crisis were we to have had better insight into the market? and so on.

This framing of the conversation makes it sound like AI has agency in the solution of these kinds of problems, but that is not the case at all. It is us as individuals and together as a society that has agency. AI is a tool that we build, and the builders must be accountable for the usage of these kinds of tools. Many of the problems that we talked about in the session will neither be solved nor made worse by AI itself, but rather by the actions we collectively take as a society. In one of the examples discussed in the Q&A around whether AI would have prevented the financial meltdown of 2007 I believe that many people acted in ways that contributed to the magnitude of that crisis, in spite of knowing the risks involved, and no amount of better information would have changed their minds.

OK, on to the questions!

# What is AI and what is not?

AI is:  

* Just a set of simple computations - but lots of them   
* Entirely built by humans.  
* Old, current models were originally proposed around 40 years ago    
* Suddenly cheap to run  
* Is not “one algorithm” - different specific tools for different types of data   
* Surprisingly effective given a large training data set at:   
	* pattern matching   
	* Feature detection in images / audio   
	* Inference   
	* Prediction   

AI is not:

* Cognisant  
* Self aware   
* General  
* Dangerous (currently)   
* Going to take your job (possibly)  
* Good at providing explanations or explaining causation


# What is a narrow AI vs a general AI? _(answer is from the other panelists)_

>   
Narrow AI accomplishes one task, or is focused on a specific application, whereas a General AI can provide insights to a broader range of challenges by integrating across a larger array of sources. Narrow AI is language translation, autonomous driving, image recognition. A General AI might be an omnipresent personal assistant . . we are not there yet.  

# “How does machine learning fit into AI?” _(answer is from the other panelists)_

>  
Machine learning is a technical approach towards AI, a statistical process that utilises a body of data and tries to derive a rule or procedure that explains the data or can predict future data. This is, e.g., in contrast to older “expert systems” where humans tried to train or teach a proto-AI how to solve problems. Deep learning is a subfield of machine learning that uses “tiers” or layers, in which processing is handed from one tier to another for further derivation.

# Why is the availability of large amounts of data almost mandatory to design a successful AI?

* You need a large enough of a train g data set to be able to capture the features of the general case
	* Eg object recognition
* For supervised training getting a corpus of high quality labelled training data can be a challenge.
	* Eg recapcha
* For unsupervised learning the more data you have the higher the likely hod that you will be able to find “true” features of the data over “ghosts” of the process
	* E.g. using AI to extract new knowledge from scientific instruments.
	* Most clustering algorithms need enough data to be able to identify real clusters.
	* There may be something here about information bottleneck but I’m not sure.
* For simulation driven approaches you may want to run a lot of simulations and this leads to the generation of a lot of data as a by product.
	* E.g. teaching a machine how to play go, how to drive cars in video games.


# What are the problems of bias in AI? How might they affect publishers and users?

* Prediction and inference is based on the data we feed in. We can end up locking in existing bias is we don't look critically at the way we train our algorithms. E.g. if we feed in data about previous convictions data to predict future crime, and convictions happened in an unfair and biased way, then those biases will cary over into the model.
* If we try to predict future “impact” of scholarly work we may bias for individual, institution and previous publication record rather than looking at the content of the ideas. My favourite work on productivity on the sciences come from Dashun Wang, and he shows that the “super productive” period is not correlated with time in career, so unless you can identify that someone is in the middle of this kind of phase in their career looking at past impact is a poor predictor of future impact. [IC2S2 2017: Dashun Wang - YouTube](https://www.youtube.com/watch?v=goO3dWrtWc4)


# Should these tools be regulated, how might that happen?

* This is critical, and is sometimes referred to algorithmic accountability, but it is challenging.
* A clear way to do this is to make the people who make these systems accountable for their outcomes. There is a discussion around allowing AIs to be granted synthetic personhood ([Of, for, and by the people: the legal lacuna of synthetic persons | SpringerLink](https://link.springer.com/article/10.1007/s10506-017-9214-9)) This is a bad idea, we have to remember that these systems have been built by people and need to remain accountable.
* Another route is data privacy, and in the EU there is a new framework coming into place from next year called the General Data Protection Regulation (GDPR). I know that SAGE is doing a lot of work right now to make sure we are compliant, and more importantly that everyone in the company is aware of the implications of the act so that we don’t become accidentally non compliant.

# How has the widespread availability of software like Google’s TensorFlow helped to foster AI experimentation?

* Matato Koike used tensorflow to build a [machine vision system to help his mothers' cucumber farm auto classify cucumbers](https://cloud.google.com/blog/big-data/2016/08/how-a-japanese-cucumber-farmer-is-using-deep-learning-and-tensorflow).
* Jacques Mattheij built a [lego sorting machine](https://jacquesmattheij.com/sorting-two-metric-tons-of-lego).
* These all show that these tools are at the point where they can be used by the interested hobbyist.



# Is AI is most useful for production workflows or user needs?

* Yes
	* Adam Matthew have rolled it out to enable [hand writing recognition in digitised collections](http://www.amdigital.co.uk/m-editorial-blog/handwritten-text-recognition/).
	* IET are using machine learning to auto add ontology terms and indexing terms to articles that are indexed in Inspec (http://inspecdirect.theiet.org). This supports their taxonomists in their work.
	* Springer Nature are using some techniques to create the classification and information hierarchy for a new portal they are working on about nano technology.
	* Sage is not using it in production but is using it to help with business analysis.


# Could AI-enhanced writing tools help guide us toward writing better articles?

* Yes, but it’s very early days and it’s so so hard to get people to switch tools. I thought google wave would be able to do this, but it didn’t take off :(
* Two examples though:
	* Biomed Central BMC are using a system called StatReviewer for auto checking for things like CONSORT statements and reported p-values.
	* There is a small startup in london - [Penelope](https://www.penelope.ai), that provides early feedback to authors on their manuscript on a whole host of things in the article (https://www.penelope.ai/faq#checks-section). It’s being used by a few hundred academic a month at the moment.


# How can an AI help with determining what to publish?

* I think this is really hard at the moment, and I think it’s problematic.


# How might AI improve recommending services? For journals? For monographs?  

* It’s not clear to me that this approach can get you, for example, an order of magnitude lift on engagement with recommendations over other mechanisms for doing this. I’d prefer to see work continue around trying to extract semantics from the literature and auto-identify conflicting statements or statistically weak results. Chris Hartgerink recently used text mining over 160K papers to [review the way statistics are being reported across an entire discipline](http://www.mdpi.com/2306-5729/1/3/14). This kind of work can only be done through machine assisted methods, and I think will provide a lot more value than using AI to drive just paper recommendations.

# Would it be possible to draw in other external information about a user’s likes/patterns? (e.g. Google can figure out a reader was just in Vienna, maybe they would like to read a new historical murder mystery set in Austria Hungary that just came out?  

* So yes, but to get all of this data and integrate it you need to be convinced that this is going to give you the best return on this bet. Getting this kind of data is hard and a bit creepy.
*  I was an author on a white paper on this topic about 10 years ago, and we focussed on trying to understand how to [engineer serendipity](http://oro.open.ac.uk/21188/).  


# How could AIs help derive knowledge that might not be apparent to scholars in the data, by making inferences?  

*  See above about looking for systematic weakness in the full corpus.  
* At the moment getting consistent semantics out of research papers to be able to create networks of inference remains beyond what AI can do, but we should expect this to become possible.
	* Watson’s forays into the biomedical literature have [not planned out as expected](https://www.forbes.com/forbes/welcome/?toURL=https://www.forbes.com/sites/matthewherper/2017/02/19/md-anderson-benches-ibm-watson-in-setback-for-artificial-intelligence-in-medicine/&refURL=https://www.google.com/&referrer=https://www.google.com/)
	* [Victor Prankratius at MIT](http://www.victorpankratius.com) is one researcher working on machine generated discovery, but in his early forays into this field he found that working with the research literature to be too problematic as accessing full text is hard, text formats are inconsistent, and extracting meaning from papers is currently also very difficult. His group have made progress in generating new knowledge by looking at the raw data that comes out of scientific instruments, and in particular seismographs, so AI can do this kind of work today, but the real benefit will come when we can do this on the literature.
	* People in the semantic web community have proved that you can construct these inferential networks eg [Tim Clarke](http://www.massgeneral.org/neurology/researcher_profiles/clark_timothy.aspx) has done a lot of work on this but their work depended on manually tagging a lot of micro publications, and that doesn’t scale right now. (I need to catch up with Tim to see where they are at with this kind of work.)


# How might chatbots influence scholarly communication?  

* I have no opinion on this.

# Right now, it might seem that our interaction with AIs is occasional, episodic. How might AIs evolve to seem to be always with us, guiding our work?

* I’d want to be very careful about engaging with a system on that level. There is a great short story by Bruce Sterling that beautifully describes the [comedic dystopia](https://adactio.com/extras/manekineko/) that could result . When we talk about guiding our work we have to have a sense of what we value in life and the risk to be avoided is that we have attention sinks entering our lives that are maximising for a set of values that are not ours. That said, our connected selves has increased the burden of communication along with the volume of information that we interact with. I would want an AI that could reply to status request emails.

# Let’s end on a positive note: how can you be prepared for AI?  

At an individual level I’d recommend people take the time to learn some of the code that makes these things work.   
At an institutional level I would recommend that people review their data readiness and look for tasks that are time sinks that could be handed off to AIs, like cataloging, document conversion, copy editing. The answer below from someone else on the panel is fantastic:

>  
Riotously embed metadata, and insert data collection and harvesting breakpoints in services and platforms.
Ask others for data collected in transactions that involve you, if you can partner with them to improve services.
Think about organisational points of intersection or near-intersection and how AI might improve workflow or interactions with staff, contributors, or users.  
AI often ties together inputs and outputs by making inferences about outcomes: what are the things that you want to improve? For whom?


# How can we position ourselves so that AI benefits are not the sole territory of Google, FB, and other large technology players aggregating information?

* O’Reilly media got their entire catalog into a knowledge graph that sits in memory on their Webserver. If you have high quality data and metadata you don’t need to be at google scale to start to take advantage.
