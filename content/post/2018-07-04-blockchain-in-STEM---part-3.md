---
title: blockchain in STEM - part 3  
url: 2018/07/04/blockchain_in_STEM_-_part_3__/
date: 2018-07-04T00:00:00Z
categories:
- blockchain#
- hype-machine
- stem
- science
- publihsing
---

Over the last few weeks I’ve been writing up some thoughts on the uses of blockchain in STEM. 

The [first post](http://partiallyattended.com/2018/06/19/blockchain_in_stem_-_part_1/) I gave a general overview of my understand of blockchain.

In the [second post](http://partiallyattended.com/2018/06/26/blockchain_in_stem_-_part_2/) I looked at potential use cases of blockchain in STEM, and came up somewhat short. 

That said, a lot, really, a lot of very smart people are talking about this, and doing things in this space, so in this post I wanted to look at a few of those efforts and see how their thinking lines up or diverges from mine. 

### What do others say? 

###### Artifacts.ai 

http://artifacts.ai/ proves a solution to allow researchers to publish linkages of artefacts, but they don’t explain on their homepage who else is going to participate in the verification network. Indeed they refer to a patent pending solution, which seems to me to defeat the purpose of distributed trust. If they don’t need distributed trust they can use any append only log file format. 

###### Are **Blockchain and STM — a marriage made in heaven?**

https://medium.com/pagemajik/blockchain-and-stm-a-marriage-made-in-heaven-fecf077ea522  

This article pulls out the following problems 

> The industry is plagued with disputes around ownership, provenance, authenticity and credibility, and battles are regularly fought around the plagiarism and misappropriation of scientific endeavours.  

…
> scholarly communication could undoubtedly benefit from unequivocal, time-stamped records for every submission, citation, edit or transaction taking place along the chain. If any industry could do with a “Network of trust”, which is what the STM Association is billing blockchain, it’s STM.  

I agree with this sentiment, but I’m still finding it hard to see how to do this with blockchain, over say improving reliability of metadata deposit into CrossRef. 

The article also says that:

> Scholarly publishers are also discovering that blockchain can offer plenty of benefits in terms of helping them fine-tune and automate day-to-day processes. In a business like STM journal publishing, where a publisher is likely to have a range of journals to manage, with multiple articles and papers on the go, and teams of staff working across editorial and production, blockchain can offer a lifeline when it comes to version control, providing clarity on ownership and navigating digital rights management.  

I’m very interested in speaking to these publishers to find out how blockchain is actively helping today with those problems. If they are just solving internal problems, then of course I hope they have considered using, you know, a database. 

###### Looking at digital educational certificates as a model 

[Lambert Heller](https://github.com/lambo) as a [presentation about educational certificates as a model for a P2P commons of scholarly metadata interaction](https://www.repo.uni-hannover.de/handle/123456789/3285). The presentation available on that page makes the great point that ORCID is mostly a place where other parties push info about authors into it, and authors themselves are largely not doing this. I’d not thought about that aspect of ORCID before. It’s primarily seen as a useful aggregator.  The key of the presentation (I think, and I have huge respect for Lambert), is that ownership of data and claims needs to be returned to academics, and a system of participation with them at the centre needs to be created. A lot of the components of that vision _could_ be supported by a blockchain technology, but a lot of the human problems in getting there will remain to be solved, and for the blockchain specific solution we need to see how participation incentives can be created. 

###### Iris.ai are creating a token and “platform”

http://blocktribune.com/blockchain-ai-project-aiur-hopes-to-boost-science-research-breakthroughs is a bit more interesting, they are creating their own blockchain and token and connecting their “platform” to a DB of 120M articles. It sounds as if they want to create an open market of challenges for people to build AI driven reporting tools on top of the literature, so basically like a Kaggle, but for research questions. You get tokens for participating and then you can do, um, I’m not sure what, with those tokens. 

This sounds interesting, but I’m not seeing the motivation to create a network of nodes on this network, over say, just running a Kaggle-Like competition. Except of course that by raising an ICO they can fund some development to deliver on what they are talking about, but once delivered, I’m not sure how you are going to build a robust set of participants to make your blockchain trustable. 

###### Katalysis are building smart contracts and a way to identify authorship 

https://medium.com/katalysis-io/why-blockchain-because-duh-ce0a18747ede have created smart contracts to indicate who the owner of an article is. It’s not clear which blockchain these contracts operate over, but if you wanted to use this to pay contributors in countries where regular payment mechanisms were blocked, then maybe OK. 

https://www.digital-science.com/press-releases/digital-science-and-katalysis-lead-initiative-to-explore-blockchain-technologies-for-peer-review goes into a bit more detail. They say

> In its initial phase, this initiative aims to look at practical solutions that leverage the distributed registry and smart contract elements of blockchain technologies.  Later phases aim to establish a consortium of organisations committed to working together to solve scholarly communications challenges that centre around peer review.  
> Digital Science will manage the project and looks forward to coordinating with further partners who wish to become involved; Katalysis will use its market-leading expertise in blockchain technologies to implement the test platform; Springer Nature will participate with a selection of its journals and give key input around publisher and peer review workflows; ORCID will provide insights and knowhow around personal identifiers and authentication.  

I’m hopeful that they can answer some of my questions from above. They will face a risk of ending up solving for one publisher, they should try to get a submissions system vendor onboard. In the end though, this sounds like the kind of technology that will be run by a network of publishers. 

###### Po.et are also building a way to identify authorship (will it interoperate with the other efforts to do the same?)

Speaking of platforms for publishing and giving credit to authors Po.et are doing this too. They have a blog post about this (https://blog.po.et/welcome-to-the-gutenberg-era-d38137ae9632), which also seems to pass over the question of who is going to be running the nods on the network? 

I think they need to be careful that they don’t hire any more talented people though. They say in the blog post that 

> Filling these key roles with such strong leaders is a significant achievement that multiplies our ability to deliver exponentially  

If they multiply any more exponentials they might end up with an out of bounds error. 

They also say that 

> It’s clear that creators need a turnkey solution to help them protect and manage their assets in the digital age. Po.et aims to become the ubiquitous media protocol for Web 3.0.   

Now that _sounds_ like a centralised system rather than a decentralised system, which sounds like something that is not very “blockchain” like. I wonder if they have been following what the [Ghost](https://ghost.org) publishing platform has been up to.?

###### Blockchain for science 

There is key document in this space, the [open document on blockchain for science](https://www.blockchainforscience.com). I’ve just skimmed it, and its filled with far more use cases than the ones I discuss over this series of posts. 

I think that at heart of this document is the claim that you don’t need permission-less blockchains for science because there are already trusted players in the science space. 

I think that once you accept that you don’t need to do proof of work, and you just want to have a shared cryptographic ledger, then you open the door to using a lot of off the shelf technology (IPFS, Kafka), but on the other hand you have to be very clear about what problems you are solving and what problems you are not solving, and you have to be very clear about what is and what is not a problem in search of a disruption.  

### Some almost final thoughts 

I think there are two key, and different trends, in the desire to look at block chain in science. 

The first comes from commerical interests where management of rights, IP and ownership is complex, hard to do, and has led to unusable systems that are driving researchers to sites like SciHub, scaring the bejesus out of publishers in the process. 

The other trend is for a desire to move to a decentralised web and a decentralised system of validation and reward, in a way trying to move even further away from the control of publishers. 

It is absolutely fascinating to me that two diametrically opposite philosophical sides are converging on the same technology as the answer to their problems. Could this technology perhaps be just holding up an unproven and untrustworthy mirror to our desires, rather than providing any real viable solutions? 

For the first class of problems I have some hard news for you. One of the reasons that rights management and access control is hard is that clean metadata management is hard, and building delightful usable systems is also hard. Those two hard problems don’t go away with blockchain, if anything they become harder. 

For the second class of problems I have some hard news for you. Decentralised systems require decentralised responsibility, and in a world where people are busy finding ways to financially support decentralised systems is hard (for example see all of open source software, all of it), and incentivising people to keep decentralised systems up to date and to participate in them is also hard (see all Twitter and facebook killers, ever). 

For the former class of problems we just have to keep rolling our sleeves up, getting together as a community and putting in the hard house around initiative like [metadata 2020.](http://www.metadata2020.org)

For the second class of problems now is a time of ripe invention for the decentralised web. I think initiatives like [IPFS](https://ipfs.io) and [Dat](https://datproject.org) are truly exciting. 

Both are worthy challenges, and perhaps blockchain, whatever it is, is providing a useful jargon that allows people to come tougher to tackle such problems, even when not fully aligned.  

### gniht erom eno | one more thing

A final aside, one thing I didn’t really touch on in any depth in my above analysis about how cryptography plays a key role in blockchain technologies. If we did have a situation emerge where academics were making claims of priority on discoveries by posting encrypted messages into the public domain, waiting for later verification, then it would just almost be bringing us full circle back to how [Issac Newton used to publish cyphers of his work, for later verification.](http://www.mathpages.com/home/kmath414/kmath414.htm)
