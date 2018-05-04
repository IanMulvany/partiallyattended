---
title: choice magazine podcast Questions 
url: 2018/05/04/choice_magazine_podcast_Questions_/
date: 2018-05-04T00:00:00Z
categories:
- computational-socical-science
- research
- big-data
- tools
- software
---

This week I was interviewed for the [ALA](http://www.ala.org) choice podcast, a podcast that the that is

> a weekly program featuring in-depth conversations about contemporary trends, best practices, and case studies important to academic librarians. Hosted by Bill Mickey, the Editorial Director at Choice  

The topic was about trends in big data and the role of the library, and it was really fun to participate in, and the panel I was on included Caroline Muglia from the University of Southern California Libraries as well as Andy Rutkowski and Eimmy Karina Solis from USC libraries. 

We got a slate of questions to look through before the podcast. We didn’t get through all of these during the podcast, but I sketched out replies to some of them. Also, during the podcast the actual answers that I gave to some of these questions ended up being a bit different, but in any case, here are the thoughts I had ahead of the podcast session to the topics we covered: 


*Episode 1: Defining and Contextualizing Big Data*

1. *The term big data can mean a variety of things. What are some of the ways we can define big data? Are there fundamental elements that these definitions have in common? And what does big data mean in an academic context? Ian, how are you defining it at SAGE? Caroline, likewise, how has USC defined it in a way that works for you?* 


Matt Salganik (Princeton) has a great overview of attributes of big data sets in the social sciences — ([Bit By Bit - Observing behavior - 2.3 Ten common characteristics of big data](http://www.bitbybitbook.com/en/1st-ed/observing-behavior/characteristics/)) — where he talks about the difference between repurposing found data, and collecting data specifically for your own needs. He also provides a great analysis of attributes of data that are helpful for social research, like being always on, non-reactive, and being big enough to be able to observe rare events. 

In contrast there are lots of kinds of attributes that are less helpful, like being incomplete, inaccessible, changing over time. 

But even before getting into these kinds of definitions, we think at SAGE that there is a basic level of data management and competence, that applies equally to big and small data, that would be helpful for researchers to achieve. I like to think about it in terms of asking at what point does the size of the data present a problem for the researcher. That specific point varies depending on the technical competence of the researchers. We should be aiming to raise that level of competence across the board. 


2. *Ian, why is it we’re talking about big data now? What’s been happening in the broader tech market that’s brought this concept “mainstream?”* 

There have been three trends here, the cost of storage has plummeted, the cost of computing power has also dropped, making it cheap to store huge amounts of data, and cheap to process that data, in near real time. 

Combined with that the wider industry has created a ton of open source tools that make is possible to work with data at this scale, from things like HBase, to MongoDB and Apache Spark, through to highly preformant libraries for doing machine learning on larger data sets, like sk-learn in python. 

Initially all of these tools required quite a bit of setup to get working, but increasingly large platform vendors like Google Microsoft and Amazon are making these tools available in a platform as a service model, where you just have to bring your data and your research question, and they provide the storage, compute and machine learning models to run over that data. 

This move to commoditisation of technology is nicely captured by Wardley Value Maps - [An introduction to Wardley ‘Value Chain’ Mapping | IT Strategy | CIO UK](https://www.cio.co.uk/it-strategy/introduction-wardley-value-chain-mapping-3604565/) 


3. *Many of the techniques for mining and utilizing big data come from the STEM fields. Could you talk a little about what a traditional definition of big data is in the STEM environment? How has this helped to push big data into the humanities and social sciences?*


Up to now I think its more the tools and techniques for working with data that have started to move across. The actual data sets are obviously quite different. Critically there are a host of ethical and consent issues that arise when the core units of study are people and not just atoms. 

At SAGE we think that social sciences may go through an evolution like we saw in the life Sciecne with the advent of bioinformatics and the need for specialised skills to work with this kind of data. 

We recently launched [Concept Grants](https://ocean.sagepub.com/concept-grants/) to support researchers who are creating tooling to help with this transition, and one of the first winners are  Stefano Cresci and Maurizio Tesconi from the Institute for Informatics and Telematics, Italian National Research Council for building a tool — Digital DNA Toolbox — that helps to make bioinformatics algorithms work on social data sets.  


4. *What specific skills, tools, and best practices are transforming big data research in the humanities and social sciences?*

Many of the skills you need to work with these kinds of data are skills that might traditionally have come from computer science. That’s why at SAGE we have launched a series of online courses - [SAGE Campus](https://campus.sagepub.com) - specifically designed to teach social scientists how to program. 

That said we don’t think that these new skills are going to replace the need for mastering the existing skills in the field. 

It’s probably best to think of social data at scale as acting like the development of a new kind of tool. My background is in astronomy, and there the analogy would be that any time a telescope was built that could detect a new wavelength of light, our understanding of the universe increased. It didn’t replace any of the exiting technique or knowledge, but just augmented those. Likewise in the social sciences the availability of massive social data sets can augment the tools and techniques and knowledge that the field has already developed. 

The twitter historical record, for example, can let you see how populations interacted before, during and after specific events. It can almost acts like a social time machine. 


5. *What are some of the transformations those fields are seeing because of these new techniques?*

I think there is an increased interest in collaborations around data at scale across different boundaries, from government to private companies to the academy. 

Some people have voiced a concern that maybe the big tech giants are going to poach all of the technically competent social scientists, but we are seeing a lot of universities rolling out masters level courses in computational social Sciecne, so there is a clear effort to meet that demand. 

I think projects like Julia Lanes’ [The Coleridge Initiative](https://coleridgeinitiative.org) which brings together academics and people from government to develop data analysis skills is really interesting. 

Also the recently announced initiative to make Facebook data available to researchers with the SSRC acting as a mediator is clearly an important and interesting development. 

Episode 2: Big Data and the Library

4. *How does, or should, big data or collections data come up in vendor meetings? Some get it, some don’t. Sometimes what might seem like a simple request from the library is very difficult on the vendor side to accommodate. At the collection level, what does USC (or other libraries) need from its vendors in order to readily facilitate big data research?*

SAGE allows data mining of our content. My colleagues tell me that

> If a user has access to an article on SJ, they can download it via the CrossRef API and perform text mining on it for academic/educational purposes. If users want to perform commercial text mining, we also participate in the CCC’s Rightfind XML service, which is a search and discovery platform that allows you to mass download life science articles for mining. We think it’s better to participate in cross-publisher services than offer our own API, which a researcher would have to learn separately.  

> For non-journal content like SK and SRM, we don’t offer an API but we do still allow users to download and mine content for non-commercial use. They either have to screen scrape or ask us for help.   


8. *Ian, what is Sage looking to develop to fit into these sorts of user workflows? What sorts of strategic questions is Sage pursuing? What areas within the academic setting are most interesting to you right now?*

At the moment there are a couple of answers to that.

In the researcher setting with [SAGE Ocean](https://ocean.sagepub.com) we are focussing on figuring out how to support researchers to get the tools and skills they need to work with this kind of data, we are also supporting some researchers who are creating those tools through our concept grant program. 

We are trying to build some bridges amongst many stakeholders, so we have been working on some events to bring some key people together to discuss these issues and we have collaborated with representatives from the software industry like O’Reilly media and Facebook, as well as with funders like the SLOAN Foundation in the US and NESTA in the UK. 

Finally, we think some of the tools that we are seeing emerge could have a role to play in the library space, and that’s something that we are going to be continuing to work on over the next year or so. 




Episode 4: Looking Ahead

1. *You’ve been making attempts to get students and faculty to free their data up—not hiding it. When it’s open and available, what are the benefits to that? How can using open repositories and open source improve the process for more people? *


-> comment about being able to re-use your own data later. 

-> also evidence in STEM that open data leads to more citations, 

-> opens up pathway to collaboration. Social sciences remain behind the curve on this




2. *Researchers are very protective of their data and they often build data tools to facilitate their research, but the funding is for the primary research, not the tools. Subsequently, the tech is often left to expire. How are those two characteristics hindering progress with big data research and support within the academy? How was the Apache SPARK an exception to this pattern? What needs to happen moving forward to build sustainability into the process?*

COSMOS based out of Cardiff in the UK, built a tool for social media analysis. The funding ran out and now that tool is no longer being updated. Researcher who had been using the tool need to find alternatives, new researchers coming in to the field will use different tools, leading to heterogeneity in the analysis. This is an obvious example of the challenge that lack of funding for tools presents. It’s a long standing problem across all of research. There might be space to provide more support to researcher in helping them bridge form tool creation to the creation of small business that can support sustaining tools, but clearly not all tool creators will want to go down that route. 

Another route is to try to get a large enough community involved to support the tooling.  [BioJS](https://biojs.net) in the life science are doing well by building on top of many exiting research networks in the life sciences. 

Spark gained rapid adoption outside of the research community as it solved a problem that many people who had been using Hadoop were facing - being able to quickly run computations across distributed data, without being blocked by disk reads. There are some R and python libraries that have had a similar path, and the general trend is that they tend to be highly useful within a commerical or startup context which leads to more contributors. 

That’s not always the case, even for very popular open source tools (like homebrew), so this is far from a solved problem, and what makes it particularly hard in academia is that researchers rarely get funding for tools, in contrast to finding for projects. 

Groups like the [Software Sustainability Institute](https://www.software.ac.uk) in the UK are trying to help address this problem. 
