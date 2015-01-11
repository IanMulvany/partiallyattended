---
layout: post
title: April digital strategy forum
categories:
- public sector
- product development
- agile
- open source
---

On the 1st of April I had the pleasure of being invited to a digital strategy forum event hosted by the Wellcome Trust. People involved in digital and online projects from across a number of not for profit organisations gathered to hear some short talks about using, and contributing to, open source, agile project development and responsive design.  



#  Open Source development.

## Open Sourcing Wellcome Library Player – Tom Crane, Digirati agency

The player can be embedded in other sites. They used lot's of OS technology. It's extensible. This is a general purpose container for exposing generally digitised objects.

The player takes JSON from a content store. The project was too complex to just put up on github, as it requires a content repository behind it to make it useful. After launching they were able to see which parts of the player were universal. On day one they didn't know which parts of the player were Wellcome specific, compared to the general components, so it might not have been possible to think of it as an open source project at the outset. They took a step back, reworked the player, created a core version, and refactored the Wellcome version to be built on top of the core version via extensions.

They realised that they also needed to have enough documentation to make this useful. Tom wrote the tutorial from the point of view of someone at home with a scanner, could that person use the documentation to create a stack that the player could use to display, that became the benchmark for the documentation.

They did a dry run of launching a timeline viewer. Within a few weeks they had someone using this piece of code. The [player is on github](https://github.com/wellcomelibrary/player).

They feel that questions on usage will depend on things like  

- is it maintained?  
- is there a community?  
- is it cool?  

Feels it's important that you have a bit of wow about the tool. A good example of a tool that doesn't do this is PUTTY. They spent a bit of time making their site a bit more exiting than that.


## Advantages of Drupal as an Open Source CMS (Mosaic example) – Alasdaire Cowie-Fraser, Drupal developer (ex Code Enigma)

This will be about Drupal. There is also some discussion around the MOSAIC content, and that the content is CC-BY. This has been working well for distribution of the content. (there is probably little that I can add on the topic of Drupal that I can add from this session that will be of interest of the eLife team).

Danil does make the point that one of the big benefits of Drupal is the existence of a community. They had a case a few weeks ago where they were able to get over an issue with the site by starting that conversation within Drupal.org.

Some questions from me?

- is there a future for content editable in Drupal?  
	- that will be coming in in Drupal 8, for Drupal 7 it might be quicker than that.

- what's the upgrade timeline for Drupal8?  
	- next 18 months stick on Drupal 7.
	- caching has been revolutionised in Drupal 7 in the last year

- how do you manage the maintenance of a system in code only  
	- they kept everything in code, the mosaic project is "zero touch".
	- all changes are introduced through code and CI systems.

- are there any comments on it's efficiency?  
	- it's heavy, you need to do some work to make it preformant, it's about the caching strategy.

- another question comes up about caching  
	- someone from the EBI mentions that when they make changes they take a time to propagate
	- caching strategy is mentioned, you need to have rolling expiration caching
	- caching is a really interesting conversation (I mention the Drupal Cambridge talk from Mick Diplock)
	- there seems to be an agreement that you want to take caching out of the hands of the CMS

- What about Dross in the Drupal Module, how does this team ensure that the modules that they plug in are safe over time?
	- Danil ensures this by having an internal team that is competent that is literate in the modules that are being brought into the site.
	- In terms of being safe, Drupal is self policing, there is a security team. (I guess you have to be careful to keep an eye on Drupal security updates).
	- It is something you have to think about when using a module, Al checks the following
		- usage of module
		- downloads
		- bug reports
		- check the opinion/reputation of certain developers

# Agile Projects and Responsive Design:

## Agile development and project management (Mosaic example) – Angie Vanhegan, Wellcome Trust Web Team

She has received lots of requests from other parts of the organisation to talk about agile. She is going to talk about some of the things that worked well, that surprised them, some of the areas that they are struggling with, and an example of how agile has helped in the design process.

## Where it went well.

1. build prototype in agile, but then built the full site in a non-agile way
2. stagger sprints (in a waterfall way)  
	they has some sprints that were focussed on front end, and some on back end.
4. additional bug fixing and UAT at the end  
	they devoted several weeks at the end to deal with bugs. UAT uncovered
	lot's of bugs. Do make sure you have that extra time.  
6. push for real content early, and leave time to enter it
	this helps discover some of the user needs, you can also uncover issues with the back end tools.  
8. training as doing  
	they did a week, with two day sprints, they did a full agile project within a week (this is a really interesting idea).
10. used a pilot agile project to kick things off
	they decided to do only one project, so that they were not over promising.

## Things they are still struggling with

1. getting the product owner more involved in the process  
	a. writing great stories and owning the backlog  
	b. managing stakeholders !!!  
	c. focus on epic stories (and not on details!!!)  
2. Done criteria  
3. release planning and backlog management could be improved, leaving some flexibility, she things they should be using better tools.  
4. Stakeholder feedback at demos  
	started as a congratulatory event, but when you get some critical feedback that can sit badly with the team.  
	person from Natural History museum says that for them they have to be very clear in preparing stakeholders for what they are going to see in the demo. They do not show work in progress. Someone else mentions that they have managed to train their stakeholders. There is also a discussion on who the Product Owner vs the stakeholders are.  
5. achieving more exclusivity for dev team  
6. managing the scrum board  

## self-timing
Their story on how to hand hold senior stakeholder through the design process was very interesting. They controlled the discussion space, and broke down the process into actionable steps. The actual process was very labor intensive, but worthwile.  

The key combination was to make the key stakeholders feel involved, but you control how they are invoked, and to what extent they can influence aspects of the process at given moments in time.  

# Responsive Design – Ben Sauer, Clearleft agency - ten things about responsive design  

## 10 things about responsive site

1. ROI  
2. there is no design (singular) it's not a photoshop flat any more. HTML was never about fixed designs. It's like we are going back to the fabric of the web  
3. development is design. you developers and your designers need to be sat as close to each other as possible
4. do small screen first, starting big, and getting smaller is really hard
	take all the things on a screen, put them on post-its, and stack em.
5. content, not devices, do not think of break points as device points, think about them in terms of the content.
6. know your patterns
	brad frost's [pattern lab](http://patternlab.io) is the best site for this.
7. architect in parallel - do not do this as a separate exercise
8. design in the browser/decide in the browser  
9. performance is design - provide kilobyte budgets  
10. the mobile trojan horse  

## ben on stakeholder management

What are they accountable for? They are accountable for business objectives. Their job is not tactical stuff, it is not design. Most cannot clearly describe what these are. Make them responsible for business strategy, not design.  

What is the criteria for success, not what it looks like, but does the site work for people.  

Reframing what they are responsible for is important, but difficult.  

Reframing uncertainty. There is uncertainty and risk.  

Don't do big show and tells, if you can. Do usability testing in the corridor.  

Don't show it all at once. Just black out bits of the design, and get them to focus on the bits that they need to understand.  


# Conclusion.

It was a great day. I often had a feeling that I had heard many of these points before, but reflecting back on my notes, it's great to know that the things that are hard for me in product development are those things that are hard for everyone, and that's it, that's the job, you just have to roll up your sleeves and get stuck in. The presenters were all excellent, and a big thank you to Danil and the Wellcome trust for hosting the event.
