---
title: blockchain in STEM - part 2
url: 2018/06/26/blockchain_in_STEM_-_part_2/
date: 2018-06-26T00:00:00Z
categories:
- blockchain
- stem
- publihsing
- hype-machine
---

In my last post I gave an [overview of what blockchain is](http://partiallyattended.com/2018/06/19/blockchain_in_stem_-_part_1/), while also confusing [House of Pain](https://www.youtube.com/watch?v=XhzpxjuwZy0) and [Cypress Hill](https://www.youtube.com/watch?v=RijB8wnJCN0). (These posts are probably best read whilst listening to either of those songs). 

In this post I’m going to look at potential use cases for blockchain in STEM and scholarly publishing. 

# Scholarly communications use cases. 
When thinking about any use cases in STEM I think the questions we need to answer are:

1. What are the kinds of records that we want to place on a pubic log, and if those records deal with “transactions” what kind of transactions make sense within the context of scholarly comms?   
2. Who might take part in the verification network for a given transaction type?     
3. How are those participants going to see value in the tokens of exchange sot that they are incentivised to participate?  
4. Crucially, for any given transaction type, how is a blockchain based system better than the system we already have?  

There is also another key element at play in the world of scholarship, and that is that we already have a global decentralised, self correcting, append only log file that has been fairly robust against attack since the middle of the seventeenth century, and thats the published scholarly record. (Some people are claim that this is under threat due to the growth of poorly reviewed papers, or non reproducible research, but in the long run as Feynamn said

> *For a successful   technology, reality must take precedence over public relations, for nature cannot be fooled*  

OK let’s enumerate a few potential scholarly use cases and apply our four key questions above to them. I’m know that this list is not exhaustive but it should give us fairly broad coverage for what are probably typical use cases, and so should be instructive about whether blockchain could fit in somewhere. 

### Priority Claims

We can kind of think of knowledge claims as a transaction of sorts. Certainly when we talk about “standing on the shoulders of giants” we naturally think of new discoveries as adding to an existing logbook of knowledge. We know that there are sometimes problems with verifying claims of priority, so let’s look at some claims-based use cases. 

#### Claims about authorship of a paper 

Currently we use CrossRef as a centralised repository for information around publication, with a close link to authorship claims (made tighter if authors use an ORCID). To replace, or even supplement, this system with a blockchain based system we have a few options on who might  participate to verify the blockchain- publishers, authors, funders, institutions or a mix of these. 

The current system defers the writing of records in to the system to publishers only, so getting authors involved too could be good, however the current gatekeepers provide validation onto the record though existing peer review and I think there would need to be some kind of post-claim review system in place for a blockchain based system to be useful. 

A robust post claim system and post publication review system would also add value to the existing system, and their existence is not dependant the existence of a blockchain system, however I do think that the blockchain system is dependant on some post pub system before it could be valuable, as we would essentially allow any writes to the log, and look for verification later. 

(We might be seeing that emerge with the way discovery is happening around preprint servers, so maybe we don’t have to wait that long at all, but right now it remains a punt). 

One reason why you need to build that in to your blockchain design is the current system has evolved workarounds to do with how we retract papers or how we tombstone them, and though these systems can be a bit messy, the affordance to do this is there. That would have to be designed in to a new system, probably from the get go, as the record, once created, cannot be altered, you can’t have a do-over in terms of the key metadata that you record for your early transactions, though you could have “correcting“ transactions later (you can see I’m trying to work my way through this as I write). 

Unless the system is almost frictionless to setup (in terms of pushing claims onto this chain) I don’t see any significant numbers of academics taking part. That friconlessness will need to look something like a copy of the work or claim being routed to the public chain as part of the authoring or submission software. That requires either all authors to adopt one similar plugin or extension to their writing environments, or all submissions vendors to offer this as an affordance to authors in a way that does not add complexity to the existing article submissions process. Probably the default outcome is that it will just be institutions and publishers who might take part, and they will probably do so by adopting a platform or tech solution offered to them by a vendor. 

That vendor interaction is probably going to constrain the creation of a truly open network, as the given vendor is probably going to deploy and run “independent nodes” on behalf of their clients. Any yet theses clients already have trust in each other and enhance that trust through participating in standards like ORICD and CrossRef. 

Any vendor solution has to be built on top of an open protocol, because distributed trust, remember, so some independents could run nodes. What then is the “token” that we exchange for writing and verifying claims of ownership. If its a general token that can be used for tracking any transaction then how do we constrain this network to only be abut this one STEM use case? If its a token related solely to claims about ownership how do we get people to value that? Were this system to scale it would need to be able to keep tabs on several million transactions per year. 

Lets say I am an independent and I run my node, it adds records about verified authorship claims and I get given what? A token I can use to submit my paper? Do I stop running nodes when I stop being an active academic? Do I only run the node when I’m getting ready to submit? Does my research grant come with a % that can be used to solve proof of work algorithms so allow me to get published, what if I hack my local university supercomputer in order to get “published” faster? Does that lock out people from publishing from “energy poor” and “compute poor” institutions? 

I’m not seeing this system as cleanly solving some of the existing problems that we have in expanding access to claims of ownership, and I’m not seeing this as being an area that is currently a low trust one. 

In addition I think there is a potential to lock in an existing danger. We trump priority claims in science, and yet what we know about how science operates tells us that it is ultimately a collaborative activity. The existing publish or perish system puts too much pressure on priority, many people have recognised that we should be working harder to eliminate the risk of gazumping in publishing, yet I fear that by encoding this kind of behaviour onto a global public unchangeable record we will only exacerbate that problem. 

#### Reviews of articles 

There is a problem around being able to verify whether a reviewer is real. A blockchain system could make a public record of all published reviews, but this runs into a couple of issues. Reviewers are still mostly unwilling to sign and publish reviews (that issue could be significantly helped by requiring all reviewers to have an ORCID, and that would probably help more than having a crypto token of the review pushed into a public log). 

For review transfers if a publisher want to send a manuscript to another publisher, a public log around metadata of reviews might help, but can you add to that log for a paper that is not published yet? For a blockchain like system to work for review transfers we would probably first need to be in a situation where all authors are willing to have metadata around their manuscripts made public before publication, so a kind of cloaked crypto version of F1000 Research. Hmmm. I’ll just leave that thought there and gently step away from it. 


#### Tracking article versions from preprint to publication 

If the artefact is in a preprint server then we could use a blockchain to track metadata about the version history of the article. On the other hand, instead of trying to figure out who should participate in running nodes, we could just use the existing support for preprints that [Crossref provides](https://www.crossref.org/categories/preprints/), so here our choice is to build an unknown architecture at scale that faces significant adoption problems, or use an existing scalable solution that is already being used by everyone. 

#### Claims about generation of data

I think there might be a potential use case here. It could be of value for labs to be able to advertise that they have kinds of data,  or have generated kinds of data, without making the data itself available. 

Where there is a need to be able to make claims around priority of data then being able to put a hash of your data set into a public ledger and then verify later that you have the underlying data, even if your papers come out after papers from other groups who might have the same data, could be beneficial. 

There are a couple of problems with this though. Data management is at a stage where if you are dealing with biological data it is almost impossible for two groups to end up with exactly the same data. The hashes that you produce as a representation of your data will be different to a hash of even almost indistinguishably different data, so even if there are data records on the blockchain, as a lab I’ll have no way of knowing if another group has already published a similar data set to mine :(. 

Given that it will be hard to check I won’t check so there won’t be much utility in this chain for the purpose of finding connections between research groups. Also, some labs will jump on the shiney new and start posting lots of entries to the chain, while many labs won’t. 

What a record on the chain will tell us is that a given lab was the first to add to the chain not the first to discover a specific data set. For this to work it would need to be blessed by a funder who would need to make appending to this chain be a requirement of funding. 

If we had lab equipment that did this anyway, then that might help, but we don’t have this kind of equipment. Moreover who is going to check? Those who check are most likely to be running centralised systems (i.e. funders who are trying to tack outputs) rather than this being a check being constantly done by the community. The funder could just ask for hashes of the data to be sent to them directly, or better yet, the actual data being deposited in a dark archive until publication. 

#### Linking research artefacts together 

If I want to create a record of all of my contributions, and create links between them (publishing the network of scholarly artefacts that I generate as a researcher) why would I not put those links into the public domain on to a blockchain? This does not require the entire ecosystem to come along with me, so we don’t have a cold start problem. I think the problem here is that this is just a derivative issue of the core issue around trust in the act of publication. So if you trust the authors on the key published elements you will trust them on these network claims, but publishing these network claims will not solve the problem of whether you trust them on the key publishing claims, so you are building a trust network where the verification of that trust for these links is largely meaningless as you have skipped over the core problem of trust. 

#### Claims about facts and micro statements 

What if I want to make claims about parts of a paper, make public claims on statements, facts or micro-publications? Why would I not push these onto a blockchain? Though here the use case is an interesting one, and is about creating a publishing system for something that we don’t handle well at this point in time in our infrastructures, I’m again finding it hard to understand what I would use the tokens for that get generated by the nodes who are validating these writes. Where this become powerful is in finally allowing fine grained credit to be assigned, a grand automation of the research object, however there are currently no incentive systems in place for doing this, and so adding a technological barrier to publishing something where the incentive becomes even more abstract is possibly not going to solve that incentive problem. 


### Resources 

The second category I want to think about is resource tracking and sharing. Where has a resource been used? Who has used it in the past? How might a set of resources be pooled and bid on? There are potentially a lot of ways that a public ledger could help with these kinds of questions. 

#### Access to compute time 

If we have a distributed set of computing resources, people who hold those resources could offer them out and compute time could be exchanged for tokens. In this case the actual history contained in the ledger is probably only of interest in terms of ensuring that the tokens being exchanged are validated, and I could image that those tokens could be used in the future for requesting compute time. 

I think there are a couple of problems with this approach. The first is that compute time within the academy is already well provisioned, with many nations putting resource in creating supercomputing networks. Also cloud providers provide cheap scalable compute resources. 

Creating an open market place where there is a public history of transactions, but where that history is probably of no intrinsic interest seems wasteful when the existing alternatives seem to be getting the job done. Why create a “token” of exchange for compute time, when the exiting token of exchange — money — does very well. If we say that people have plenty of spare computing time sitting around, and a blockchain system will allow that spare capacity to be used, well, I’d need to be convinced that our core resource shortage is compute time, and I don’t believe that this is the case. (For what it;’s worth I think the key resource constraint that we are gong to be facing soon is going to be human attention time, and for now I’m unwilling to tokenise parts of my brain). 


#### Access to lab time 

This is a similar use case to the previous one. We are just using a public ledger to create a kind of currency. I don’t see much reason to replace existing currencies with a crypto currency here. 


###  Tracking of physical reagents 

I think there really might be some kind of use case here. Blockchain is finding a lot of interest in the world of international logistics, and indeed where experiments are using reagents, or other equipment, being able to produce a provenance file of where everything came from could be really useful. Moreover, if as a lab you create a new resource for public consumption, being able to register that resource while at the same time showing how it is connected to elements in the supply chain that came before it might be interesting. This is a use case that I can speculate on, but I also recognise that I really don’t know much about this area of lab work. 

I guess what participants in this network are hoping for is that by making their materials more traceable, and by having others sign up to doing the same, they can have an expectation of eventually receiving more reliable and more traceable elements themselves, so there is a gradient that could push more and more people to participate. 

What we are almost looking for here is a hope that various players will move towards transparency and standardisation and use the blockchain as a technology for converging on to drive that standardisation. 

So what then is the unit of transaction, the token? How does that play in this use case? 

I’m genuinely at a loss to answer that question. 


### Rights 

The last broad use case is about rights management. How do I know that I have the rights to an object, and how do I know that I can transfer those rights? At the moment we need to base this on contracts and central clearing houses, however could blockchain greatly simplify this for the academic market? 

#### Rights transfers around copyright, articles or journals 

When authors transfer copyright to journals could this be pushed to a blockchain? I think we can be sure that the authors won’t do this, so it will be up to the publishers to do this. Other actors supporting the network of validation will be the publishers, so there has to be a sufficient cost saving for publishers to do this in terms of how they currently advertise rights to libraries and to each other. 

The key thing here is the former - I think. The current system of how rights and holdings files, and access to content via IP restriction is filled with bogey men, and as I understand it from speaking to colleagues the system is somewhat complex. So if we had all of that information in a public ledger then granting access to rights might be something that could be automated — but, and I think this is a big but — one of the reasons the current system is complicated is that there are many players, so gaining adoption is going to be hard. 

We would have to run this “rights blockchain” in parallel for some time. Initially you would have a small number of participants. What you would need to do is create a small collaboration of publishers who would sign up to keeping this chain up to date, would commit to ensuring the blockchain is valid, and would be willing to invest in getting good data into that system. 

You would ideally like some pilot librarians to come on-board, but they would probably need to be bank rolled by this “STM blockrighs consortium” for the initial phase of roll out. I mean, I think this would be interesting, but I think it’s moving against the grain where libraries, institutions and funders are seeking universal open access, so I would not put my money or resources into a project like this. 

The following two tweets capture some of the problems with blockchain for rights 

``` ”We'll put ownership of IP rights on a blockchain"

Translation: "we want to privatise the IP system, create a monopoly who will charge high, unpredictable fees, and remove any judicial oversight from a system that relies on that to curb the worst abuse".

Make it stop.
```
[Tom Morris  🏳️‍🌈 on Twitter: “”We’ll put ownership of IP rights on a blockchain”Translation: “we want to privatise the IP system, create a monopoly who will charge high, unpredictable fees, and remove any judicial oversight from a system that relies on that to curb the worst abuse”.Make it stop.”](https://twitter.com/tommorris/status/1006478693273882624) 

[꧁Terence Eden꧂ ⏻ on Twitter: “I don’t understand the blockchain hype.A startup has certified my artwork & placed their verification on the bitcoin blockchain.Now art dealers & auctioneers can feel secure that I am the original artist.One small problem… I am not Leonardo da Vinci!https://t.co/9219OcPsVW… https://t.co/3huflle9La”](https://twitter.com/edent/status/1006248586395508737)


### An addendum on pessimism 

As I write up these use cases, I recognise that I am being deliberately pessimistic, and perhaps that’s not fair. I’m seeing problems and barriers, and the truth is that for a new technology to mature to utility it does have to overcome a lot of barriers, and it’s the dreamers and enthusiasts that drive forward and find solutions. One the other hand, it’s got to be good to have an open debate about the kinds of problems that these technologies might need to face. In his [presentation on ten ear futures](https://www.ben-evans.com/benedictevans/2017/11/29/presentation-ten-year-futures)  Benedict Evans talks about how we often think about how a new technology will be applied to existing use cases at the start of the adoption curve, but at the end of the adoption curve if a new platform or technology is truly transformative then the use cases that end up being used are totally different to ones we imagined. My take on blockchain in STEM is broadly that there are no existing use cases that are a compelling fit for the tech, but that is not to say that there won’t be other new use cases in the future. Im my next post I’m going to compare some of my own thinking with what other people are saying abut blockchain in this space and wrap up with some final thoughts, I should get that post out sometime next week. 

