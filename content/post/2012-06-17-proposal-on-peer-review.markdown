---
categories:
- peer review
- altmetrics
- publishing
- open-access
date: 2012-06-17T00:00:00Z
title: Augmented Peer Review
url: /2012/06/17/proposal-on-peer-review/
---

Last year I was asked to contribute to a special issue on the evolution of peer review. I got quite excited about doing this, but then realised that I really didn't have the time to write a paper. I'm not a practicing academic, I build products, and while at Mendeley I really had far too much on my plate to find the time to write up a paper. However the topic does interest me, and I am a strong believer that web scale technologies can help with the scientific communication process though a large number of avenues. I was looking through my folder of draft blog posts, and I found the skeleton of the proposal that I had started to put together. I'm posting this up now, including the editoral comments I got on the very rough draft. I remain lucky enough to be in a position to continue to build out the parts of the infrastrucutre that I think can help with all of this. I'll probably not get around to finishing my thoughts on this proposal in exactly the way that I had been thinking about it last year, but I might flesh out some related thoughts over the coming months. 



# Delivering an Augmented Peer Review System, one piece at a time. 

## Summary 
Rather than trying to replace peer review, I will argue that we should create an augmented version of the system. I  propose that web scale technologies can be used to deliver this Augmented Peer Review. I will describe some of the functions of the peer review system and show some of these can already be helped with existing systems, and describe how some of the other functions may be helped in the near future. 
I will describe in detail how Mendeley has created a technology that can help with one core aspect of the peer review system, assisting in filtering the literature, and I will describe some of our upcoming plans to go further with this. I'll describe some of the weaknesses of our approach and contrast these to weaknesses in the existing system. I will also describe some experiments that we are planning on running that may validate the predicative power of newly coined metrics. Finally I will argue that getting access to the citation and review graph is the biggest factor in holding back the improvement of the peer review system.


## Introduction
There is little doubt that peer review is a topic of particular interest to academics. The Mendeley search catalog returns over 20 000 items with "peer review" in the title. There is a growing sentiment that "peer review is broken" ([I hate your paper][bpr] ), but broken or not, is it worth asking whether we can improve the current system in any way by applying social or technological changes to the practice of peer review? As a technologist I'm in the lucky position of working on systems that can have an impact on the peer review system from a technological point of view, and so those are the solutions that I will focus on in this paper. 

[bpr]: http://www.the-scientist.com/templates/trackable/display/article1.jsp?a_day=1&index=1&year=2010&page=36&month=8&o_url=2010/8/1/36/1

## What is peer review anyway?
One of the great problems with offering solutions to the problem of peer review is that it is actually a many headed beast, a Hydra of a system. It is many different things to different people. Some of it's core functions we can think of as being required, and others are more flexible depending on the policy of the peer review body. 

Generally Required:
    
- A cross-check of correctness.
    We assume that once past peer review an article is telling us something that is true about the world.
    
- A cross-check of novelty.
    We assume that the work has not been presented before, or by other people.

- Ensuring the correct link to related literature.
    We assume that the reviewer will inform the author of any missing credits that the author should have included in their paper to prior work.

- The creation of a pre-filtered body of literature, though the understanding of the filtering is not necessarily clear to the reader.  
    It is assumed that the literature that passes through the gate-keeping of peer review represents a special body of knowledge that can be depended upon for quality and accuracy. For the vast majority of content that passes peer review this is probably true, but not for all. 

- Providing a record of prestige for the author.
   Getting the "peer reviewd" hit is the cornerstone of building a career in academia. The more exclusive the journal, the better for the author. 

Generally Optional:

- Screening for suitability criteria for a given journal, either subject or impact based.
    Some journals will reject a work not because the work itself is in any way wrong, but because the work does not fit the subject space of the journal. Other journals, notable the Nature stable of journals, will reject a work if the editor of the journal does not feel that the work is of sufficient "impact" or of general enough of a nature. The main Nature journal also has a policy of publishing works that relate to the physical sciences, and so does not accept literature in the computational or mathematical sciences. PLoS One takes exactly the opposite view on impact, and checks only for rigour in the reporting, however it also has a strong subject bias and does not publish in areas of pure physics.

- An opportunity to help improve the quality of the work.
    Though optional, many researchers put much time into helping to improve the quality of the manuscripts that they are reviewing. One of the main reported benefits of the peer review system is this improvement that authors feel of their work. This is almost entirely social, as there is rarely a published record of the reviewers comments.

- An opportunity to build or block the creation of social connections though contributed work.
    By contributing to the good peer reviewing of an article a researcher participates in the society of academia. This position can also be abused and used as a way to hinder the publication of competing researchers. 



 ## Augmenting parts of the functionality of Peer Review

- a cross-check of novelty
- ensuring the correct link to related literature

Both of these functions are under the pressure of the scale of the literature. In 2008 the Research Information Network assessed that researches in the UK read up to 260 articles each per year (Anon, 2008. Activities , costs and funding flows in the scholarly communications system in the UK Report commissioned by the Research Information Network ( RIN ) Full Report. , (May).). At this rate, assuming no further research were published, it would take a researcher approximately 77000 years to read their way through the items cataloged in PubMed. Nowadays even a well read well connected researcher can only hope to have a deep familiarity with a fraction of the literature, however even hundreds of millions of documents can be scalably compared with the kinds of data structures and algorithms that have been created for indexing the web, such as schema-less data stores like HBase, and algorithms like map-reduce.  
    
The productisation of checking for similarity in the literature has already begun with the introduction of the [cross check][cc] service from cross ref 
. Online services like the [journal author name estimator][jane] can tell you what journals or articles are like the one you are currently writing . The next step will be to see such services integrated into the writing tools of the researcher. 

[cc]: http://www.crossref.org/crosscheck.html
[jane]: http://www.biosemantics.org/jane/

- providing a record of prestige for the author

This is actually where the majority of this article will focus, and it discuss the following:

- altmetrics
- the work of Bollen et al
- graph theory applied to impact

- Tools for processing large graphs
The emergence of 3rd generation programming tools have driven the creation of libraries for managing graph structures that have realtivly humanly readable APIs. An example of this is [networkx][nx], a graph library in python. Robust scalable databases for processing large graphs have emerged, such as [neo4j][n4j]. The social web has driven the creation of very scalable systems for storing relational and non-relational data, such as [flockdb][fdb].  

[nx]: http://networkx.lanl.gov/
[n4j]: http://neo4j.org/
[fdb]: https://github.com/twitter/flockdb

- readership statics, and compare Mendeley readership statistics to those provided by services such as Connotea
- the Mendely API and the type of queries that can be resolved on the back of it
- plans for future work around individual impact based on Mendeley statistics
- moving from a central data store to a distributed model, the web of linked data

## References
 
[alt metrics manifesto][aman] 
 
[Radicchi, F. et al., 2009. Diffusion of scientific credits and the ranking of scientists. Physical Review E, 80(5), p.11. Available at: http://arxiv.org/abs/0907.1050 [Accessed August 16, 2010].][ref1]

[Bollen, J. et al., 2009. A principal component analysis of 39 scientific impact measures. Methods, pp.1-19.][ref2]

[Beel, J. & Gipp, B., 2010. Academic Search Engine Spam and Google Scholarâs Resilience Against it. Journal of Electronic Publishing, 13(3).][ref3]

[Arnold, D.N. & Fowler, K.K., 2010. Nefarious Numbers. , p.5. Available at: http://arxiv.org/abs/1010.0278 [Accessed October 6, 2010].][ref4]


[aman]: http://altmetrics.org/manifesto/

[ref1]: http://www.mendeley.com/research/diffusion-of-scientific-credits-and-the-ranking-of-scientists/

[ref2]: http://www.mendeley.com/research/a-principal-component-analysis-of-39-scientic-impact-measures/

[ref3]: http://www.mendeley.com/research/academic-search-engine-spam-google-scholar-s-resilience-against-it/

[ref4]: http://www.mendeley.com/research/nefarious-numbers/

## Editorial Comments 

This abstract/outline contains a lot of highly relevant background and several good ideas and important observations. Services like Mendeley and Zotero are in a key position for providing the web-tools for realising open post-publication peer review. What I’m still missing in your outline is a coherent vision for how new papers can be openly evaluated by the community with these tools. Imagine you had infinite resources, what system for open evaluation of the scientific literature would you build?
I would like to invite you to contribute a full paper with the hope that you will describe a detailed vision for open evaluation (e.g. Mendeley users rating and reviewing papers and sharing their ratings and reviews). The vision should include a description of the required web-based infrastructure as well as mechanisms of motivating reviewers. Consider including a step-by-step description of the process by which a paper is evaluated. Make sure to address the design decisions listed in the email. Feel free to use figures to communicate the key concepts and processes of your vision. Please note that the innovative features that distinguish your approach from those described in other contributions to this special topic should be clearly communicated in the title, in the abstract, and through the headings and terminology used in the paper.








