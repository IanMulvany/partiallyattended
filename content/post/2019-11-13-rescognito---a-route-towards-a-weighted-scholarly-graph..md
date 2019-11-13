---
title: rescognito - a route towards a weighted scholarly graph.
url: 2019/11/13/rescognito_-_a_route_towards_a_weighted_scholarly_graph./
date: 2019-11-13T00:00:00Z
categories:
- graph
- pid
- orcid
- startups
- credit
---

I sat down with Richard Wynne. Richard has a long career in the publishing space, having been one of the senior team at Aries for a long time. 

Over the last year Richard has founded [Rescognito](https://rescognito.com). Rescognito is a service to allow institutions or individuals to award credits (or `rescogs` ) to anyone for anything within the scholarly ecosystem. You can reward article contributions, reviews, presentations, knowledge, providing open data. The schema is extendible, so if you have a particular use-case in mind it could be accommodated.  The key thing is that all of the awarding is pinned on top of the persistent identifier graphs. Everyone involved has to have an ORCID. You can see my own page here: [Rescognito - Ian Mulvany](https://rescognito.com/0000-0002-6754-1421#). 

Initially the underlying model is that the service will sell a bag of credits to institutions, and when an institution awards someone for something their credits will have a different value to those awarded by individuals. This provides a way to see “trusted” claims along with “normal” claims, while at the same time providing an instant monetisation framework for the service. 

I was initially skeptical because what is going on here is that for this service to work everyone has to invest in beliveing that these tokens have real value, and until everyone does, they don’t. 

However, there are a number of other ways to look at what Richard is building here, and it's been interesting to stay in touch with him over the last few months and observe the ongoing evolution of the service. 

For example one way to look at this is that by combining different kinds of recognition, and being able to weight contributions, one can start to build out a directed graph of recognition and contribution. Instead of having to get over the cold start one could take a network of interactions that was of interest to a stakeholder (grants awarded, or data deposited) and using the weighted graph one could start to use something like the Page rank algorithm to find key loci in the network. For a paper or individual you could also start to provide insight into weighted contributions by contribution type. If we truly wanted to support a diverse research ecosystem something like this could be a valuable tool for funders to determine whether their values are being realised in practice. You can get a sense of this from the following view: [Rescognito](https://rescognito.com/doiVisualization.php?doi=10.12688/f1000research.19585.1) 

Another thing that is interesting here is that everything is built on top of the PID graph. This means that there is an opportunity for rescognito to offer the infrastructure to run services that are wired together with persistent identifiers, where it might be challenging to create that infrastructure on a per service level in a distributed way. The key thing is that if the claims that you want to provide services for can be described as relationships between persistent identifiers, then rescognito could make those claims operable through a PID-driven API without a huge amount of extra work on top of what has already been built. For example let’s imagine that open review was a demand of certain funders, and different funders had different requirements for what they mean by open review, then if rescognito could name these differences, then it could offer these things as services to publishers, building once, and meaning that each publisher would not have to build out each different use case themselves. 

Richard himself says:

> Rescognito is a great way for journal publishers to rapidly and efficiently collect data throughout the research/publication lifecycle **without** modifying workflow or adding to back-office administration.   

You can learn more from this webinar: [Structured Recognition via Rescognito & ORCID - YouTube](https://www.youtube.com/watch?v=6RGf2g8DmDY). 

Overall I’ve been impressed by what Richard has succeeded in building out in a short time. 