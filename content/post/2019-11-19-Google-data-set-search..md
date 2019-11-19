---
title: Google data set search. 
url: 2019/11/19/Google_data_set_search._/
date: 2019-11-19T00:00:00Z
categories:
- data
- repositories
- google
- discovery
---

I’ve just got back from a fantastic workshop looking at infrastructure for research data discovery. I’ll blog about the workshop in due course, but I was asked to comment about Google Dataset Search - [Dataset Search](https://toolbox.google.com/datasetsearch).  

I had the change to meet with Natasha Noi from Google who is behind the service. [Natasha Noy – Google AI](https://ai.google/research/people/NatalyaNoy/). 

As with many google services, it has been created by a small team, but with the underlying web scale infrastructure of Google to build on top of. They look for data sets on the web that have been identified using [Home - schema.org](https://schema.org) tags. Data repositories that expose these tags will get indexed by google dataset search (this includes both Figshare and DataDryad). 

Natasha said the following about the service: 

> There are thousands of data repositories on the Web, providing access to millions of datasets. Google’s  [Dataset Search](https://urldefense.proofpoint.com/v2/url?u=http-3A__g.co_datasetsearch&d=DwMFaQ&c=slrrB7dE8n7gBJbeO0g-IQ&r=omwcNBUqPba9pikmkXZXk2bFQ7zxZPhI5OH9dd8lFDA&m=AFklQ01ByxTiruuR_qSMkwBS-yjywt47u9stg6e4iCQ&s=Fk_6LE_tXUImuSF9yYHnJvRPH8uRSa4rlwJrInQHXm8&e=)  provides search capabilities over dataset descriptions (metadata) in all of these repositories, enabling the users to find datasets, wherever they are. You can think of Dataset Search as “Google Scholar for datasets”. Dataset Search includes open-government datasets from many local and federal governments across the globe, a large number of repositories for scientific data, economics data, data for machine learning, and so on. It includes both commercial and noncommercial providers.    

While any other group _could_ in principle replicate this by extracting all schema related pages from something like common crawl, in reality there are probably only a handful of other organisations that might feel like they have a mandate or the resources to look at doing something like this. I could imagine Archive.org, Microsoft or Allen.ai having a crack at something like this. In the meantime, google dataset search is there, and it’s great that someone is doing this. 

Peter Kraker has been vocal in his concerns about this project ([Update on the #DontLeaveItToGoogle campaign | Science and the Web](https://science20.wordpress.com/2019/03/28/update-on-the-dontleaveittogoogle-campaign/)). While I agree with Peter that there should be better support for the research and discovery infrastructures, I’m not opposed to the existence of google data set search. I had a chance to talk to Peter briefly about his views on this at the Force2019 conference, and my takeaway from that discussion is that he was less concerned about the potential for Google to capture researcher attention (I mean surfacing these data sets is broadly a good thing) but was a more concerned that the existence of something like google dataset search potentially acts as a suppressor of research and innovation support. The argument could go — well GDS exists, so why should we fund anything like it? That is a fair point, but the overall landscape of how we allocate funding decisions is a complex one. As much as we might with things to be different, we can’t wish away the existence of web scale players.

What I like about what Natasha is doing is that she is asking for repositories to use schema.org, which is an open standard, and which, as I mentioned above, opens the door for others to replicate what they have done. A project like Hyphe - [Hyphe](https://hyphe.medialab.sciences-po.fr) - shows that there are interesting open tools out there to address crawling, but in the end we are left with having to compete with researcher attention, so I’m not totally convinced by the argument that were GDS not to exist we would be in a place to create an alternative that would gain both funding and researcher attention. I say that due to the very large amounts of scar tissue that I carry around from many years of trying to get academics to draw their attention to the tools that I have had the opportunity to work on. 

One note of caution that I would strike is that how we chose what represnets a trust metric, and how we report back how data is being used are both increasingly critical aspects of the impact discussion, and are beginning to be built into how researchers are being assessed. I don’t know anything about how dataset creators get any indication of whether their datasets are being used from GDS, but as the community starts to create standards and norms around this I think its important to get all players to adopt those standards and norms. 


