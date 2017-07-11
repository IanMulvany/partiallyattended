---
layout: post
title: IC2s2 - Tuesday Morning 
categories:
- ic2s2
- computational social science 
- conference 
---

# IC2s2 - Tuesday Morning 

---
# Open Remarks, President of GESIS
* main note is his call for the potential creation of a new disciple, computational social science 

---
# opening session, chaired by Duncan Watts 

### Ciro Cattuto - ISI foundation, director of the data science lab

* is behind sociopattersn.org 
* have many deployments over the last 10 years 
* they make the data open at sociopatterns.org/datasets 
* really cool work on interaction patterns in schools and hospitals
	* can see the gender separation as age going on, 
* also really interesting network study on depression, gender and social network position 
* I like the dimensional reduction techniques on looking at time resolved graphs. One of the keys here is the use of visualisation 
* also nice example of using AI / Machine learning to clean up the dataset 
* interesting point about how sensor cost is coming down, but phone cost is not, sensors will soon be disposable, next phase is to make sensors that are self-sufficient for collection of data over weeks 

I remover seeing one of the first roll-outs if this kind of work about nine years ago, so great to see the work that has evolved from that, and the tensor analysis on time sliced networks to extract structure is really exciting. 

---
### Agnes Horvat - hidden signals of collective intelligence in crowdfunding 

* “wisdom of the crowd” has been confirmed 
* is looking at the framework of crowdfunding site 
	* is interested in who gets finding and who pays back 
	* also looking at outcomes

A really interesting aspect of this talk is that traditional social measures (such as credit-worthiness) can merge really nicely with the data that is coming at scale from the online crowdfunding platforms. Agnes is also going to followup with some survey methods to find out more qualitative data about the people who are using this work. 

---
## Morning session - User Demographics and Privacy 

We have six rapid fire presentations in this session. I was talking to someone earlier today who has access to a large volume of phone record data. He was describing to me the steps they take to ensure user privacy, and also how they get consent. What was interesting to me in that conversation was how very much the norms and decisions being made around this topic are being done on a case-by-case basis. 

I’m constantly thinking now about questions like:

> Is the lack of a global framework for some of these questions an issue? 

> The researchers I meet with seem trustworthy, how are they socialising the expected behaviours of how to deal with this kind of data, and does that affect their behaviours? 

> Are EU-like regulations going to lead us to an envorinemat where we are unable to help patients as much as we might (thinking of DeepMind and some calls I’ve heard about trying to understand how to affect social change to better health outcomes in developing nations)  

> Are there moral positions that are self-evident around our idol of data privacy in a world where that privacy almost certainly does not exist as we think that it does? 

Many many questions, let’s see what the speakers in this session have to say? 

---

### Yang-chih Fu et. al.  — Inducing Egocentric Networks with Privacy Settings: 

This talk is looking at how privacy settings within social networks tend to impose structures on the data that you can get from those networks that might not actually exist in the ground truth of social interactions. I guess that this is quite a nice example of how the latent structure of the online system imposes structure in the data, I’m not sure how often we think about this kind of thing. 

They compare surveys with Facebook data (another example of “the survey’s not dead yet” theme that I am starting to see at this conference). 

---

### Kalimeri at al - What do our digital records reveal about us? 

* They are inferring the moral construct or people from a wide range of online data. 
* They have recruited 7500 people in the US, and these people agreed to provide access to a number of data sources, along with providing a lot of demographic data as well as the moral foundations questionnaire. 
* The data was collected over one month. 
* Medium in scale, but demographically representative 

So, what do they find? At a very high level you can identify Binders and Individualists based on the kind of sites that they visit. To be fair, the sites that are being shown are not intuitively surprising (Fox News — Binders, Google — Individualists), but it is clear that they have fairly fine grained data on behaviours. 

---
### Bennati et al - New Techniques for privacy preserving record linkage at large-scale social science data sets 

---
### Schnell at al - New Techniques for privacy preserving record linkage at large-scale social science data sets 

* EU regulation recommended encrypting identifiers used for linking 
* GDPR will also prevent linkage through cleartext data 

A key point of this talk is that using encryption kills your ability to have any tolerance for errors in your data. The protocol being presented here is to use a two party protocol. This has been done with patient data in the past. 

One suggestion is to use encrypted statistical linkage keys. You pull a random set of a substring from a larger string. This is somewhat error tolerant, but you loose data. It’s messy. 

This group is working on a tool built on top of bloom filters. 

They create a bi-vector representation of the original source. You can then get to n-gram similarity between two strings. This kind of encryption does persevere similarity, so is open to attack. A method of vector folding is presented as a way to throw away some of the signal to Harden against attack. They use 1-time and 2-time folding in their experiment. 

Their metrics come out pretty well using this technique. 

So, you can encrypt the data, while being error tolerant, but the folding leads to a high level of false-positives. 

So, the idea has potential, but the talk leaves the end point a bit unproven, but It is very encouraging. 

The key think on the bloom filter is that the bloom filter needs to be hashed, and that hashing has to be shared by the two parties, so this techniques is very useful for private sharing between two agreeing parties, but not useful for making encrypted data public for re-use. Still, this is an advance. 

Here is a bit about (Bloom Filters)[[Bloom filter - Wikipedia](https://en.wikipedia.org/wiki/Bloom_filter)]

---
### Bennati et al - Incentivised data sharing via group-level privacy-preservation 

So, how do you convince people to give up their data so that you can create better services? 

Sensors provide data to an aggregator. Those sensors can apply functions to the outbound messages. If the sensors increase privacy, the quality of their data goes down. 

They are looking at a bottom-up approach based on network topology. 

There are nodes of aggregators that roll up to a main aggregator. Each local aggregator is collecting from a collection of sensors. 

They ran simulations to look at how different parameters of the graph led to different characteristics of privacy. 

They found a way to saturate privacy while not giving up on accuracy, but they have not yet checked whether people would actually adopt this kind of system to give up more of their data. This seems to me to be really one of the critical points of work like this. 

---

### Dennis Feehan and Curtis Cobb - How many people have access to the internet? (The title is longer, check out the program!)

Ok, so standing on the other side of “surveys are not dead yet” meme, there is a big graph showing that response rates to survey data are declining rapidly. 

So the idea is to ask people in an inexpensive way how other people behave as a way of getting to scale, e.g. ask people on Facebook how many of their friends use the internet. 

They actually collected information on Facebook! They took a random sample of people on Facebook. 

There are lots of design decisions going on to make sure that respondents don’t get hit by survey fatigue. There are lots of other things going on here to help check for consistency in the reports too. 

They got about 1500 people in each of six different countries. 

Aside from he headline title of this talk, looking at the methodology of doing this kind or reporting on Facebook is fascinating. 

They find that just under 50% of people are online in India, and in the US and UK the numbers head towards the high 80% rates. 

---
### Kashyap et al Ultrasound technology and missing women in India 

They are looking for sex ratio at birth distortions. People do not want to openly talk about sex-preferential abortions. 
There are a lot of data issues, it’s hard to capture the footprints of the data. 

They want to think about how Google might be a source of information leading to the decision path towards sex selective abortions. They looked at searches for access to ultrasound. 

They tried to train data on the sex ratio\s they have, correlated with search for Ultrasound to predict sex-ratio stats in the future. 

This is a really interesting talk, showing how these kinds of techniques can lead to real insight into a deep societal problem. 




