---
title: RAVE publishing technology conference 2018 
url: 2018/10/24/RAVE_publishing_technology_conference_2018_/
date: 2018-10-24T00:00:00Z
categories:
- drafttoblog
- publishing
- rave
- technology
- innovations
- blockchain
---


I took some notes on some of the sessions at the conference yesterday. 

### Dave Smith - object oriented publishing.

Dave makes a good case here about how we should think about the future of scholarly publishing — in terms of objects that can be reformed based on the needs and competencies of the readers. He points out that while we do have in place good ontologies and domain models, our entire view of publishing and our publishing infrastructures, remain laggy and are a barrier to moving in this direction. 

He mentions the usual examples of initiatives that point towards the future, protocols.io, project Jupyter, code ocean, Figshare, overleaf, stencilla, the CoKo foundation model and I think some others. 

For me one of the core issues with this vision is that these interesting initiatives are essentially island efforts with few routes of connection between them. 

Finally David mentions the very critical point that we might be moving into an environment where the core elements of a scholarly publishing infrastructure may be owned by a few key players. Would this be good or bad overall for the entire ecosystem? The answer to this question is sort of left hanging, however he also makes the great point that funders seem not to be looking at this aspect of the ecosystem and that there is a need for financing the experimentation needed to work towards this more object oriented future. 



### Louise Russell - blockchain - distraction or opportunity? 

The benefits described in this presentation are general, and not specifically related to scholarly publishing. 

MyCelia (http://myceliaformusic.org) looks interesting, a platform for managing music for artists. It’s in alpha test, so it’s very early to tell whether it will work. It provides data around ownership contracts and payments for music artists. It looks a lot like the Eureka initiative. 

Louise mentions the following scholarly related initiatives (most of which I had head of before, so that’s cool).:

* https://www.scienceroot.com - they have launched an ICO that is now completed 
* Pluto - [Sci-napse | Academic search engine for paper](https://scinapse.io) search engine (based in Korea, a not for profit) 
* [ScientificCoin](https://scientificcoin.com) - a blockchain based funding platform (I quite like this idea, kind of). 
* [Orvium - Open and Transparent Science Powered By Blockchain](https://orvium.io) - authors gain instantaneous “proof of existence” by publishing on this platform. 
* [Katalysis](https://www.katalysis.io) I have heard of before, and is about sharing review information amongst publishers. 


### Alice Fleet - from Sofas to SAFe; agility empowerment and the heat treat oven - head of technology Emerald Publishing 

This is a great talk looking at how to improve the process of a development team within an organisation, following trying to implement process improvement based on the theory of constraints (with an actual picture of a heat-treat oven, referencing “The Goal”). 

They re-organised their development teams, while at the same time allowing for space to look at consistency across teams for things like testing and security (this is called the squad model). ([Can Product Squads Improve Your Agile Development Process?](https://www.productplan.com/product-squads/))

They put in place a freeze on work to allow them to find the bottlenecks, and looked at how to reduce the work in progress in the teams. 

They introduced the three amigos conversation when it needed to be rather than at a specific point in the process. 

They worked on making work visible, and worked on bringing in smaller units of work into the pipeline. 

They are only about two months into this process, but they are already seeing work completion rates going up, even though they are taking less work into the system. 

They want to make this system of work scale, so they are looking at introducing the SAFe framework - Scaled Agile. 

This is a great talk. 



### Blockchain panel - some reflections 

Lynsy Haire and Joris van Rossim who are involved in the Katalysis pilot project presented the problems they are trying to address in relation to peer review are:

* Call for transparency.
* Aid to peer review.
* Better Infrastructure. 

The panel discussion was good natured, and I offered some objections_questions_challenges to the use of blockchain. Joris was articulate on why he believes that blockchain, and blockchain-related  technologies are the right kind of technologies to address these problems, and was also clear that they are investigating these in the pilot, bur are not wedded to them if they find better alternatives. I do think that by getting researchers publishers and funders involved they will learn a lot, but I still think that blockchain is possibly not the right technology for this. My points were the following (but as ever I could be wrong). 

* The technology is opaque, the coding and algorithms are non trivial and have proven to be frequency insecure. 
* Other forms of distributed databases or distributed append only logs can provide the same benefits for less complexity - DAT / bit torrent. Append only databases - Kafka has a much better developed infrastructure for  event subscriptions, and architectures like fan outs. 
* The claim of independence, in my mind does, not hold water. I think that would lead to vendor lock in as I don’t think that publishers will implement this tech on their own, without some standardisation we are going to end up depending on a vendor. That’s not decentralised in practice.  
* There is a tech utopian issue here : tear down the publisher vs fix the rights and permissions issue. Both points of view are converging on blockchain, both cannot be right. 

HOWEVER 

There is a need for creating new sharing, anonymization and metadata standards and  if blockchain acts as a catalyst for people to do that, then this is grand, but just please don’t actually use blockchain core Technologies. I guess I’m calling for - BINO - Blockchain In Name Only. 
