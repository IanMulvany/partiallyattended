---
title: Blockchain in STEM - part 1
url: 2018/06/19/Blockchain_in_STEM_-_part_1/
date: 2018-06-19T00:00:00Z
categories:
- blockchain
- publihsing
- hype-machine
---

A lot of people are taking about “blockchain for science” and “blockchain for publishing”, but I’m skeptical. Some of the people taking about this are really smart, so I could be wrong. 

If we think of scholarly publishing as being like the connective tissue of science, and we accept that this idea is gaining purchase within our community that we have to realise that we are looking at a case of 

> blockchain in the membrane   
> blockchain in the brain  

So, are we going to `jump jump` to a better future, or are we just looking at entering a house of pain? In this short series of posts I’ll explore some of my own thinking about this topic. 

This is the first of a three part series, and I’ll update this post to link across to the other posts when they are ready, hopefully over the next week or so. 

### What do I think blockchain is? 

Heres my understanding of what blockchain is. 

Blockchain is a public “append only“ logfile (or ledger), copies of which can be held by anyone. We can call the collection of people who are participating a network, and we can call any single participant a node in this network. 

There is no central source of truth, but there is an algorithm that aims to allow all copies of this log file to become “eventually consistent”.
This log file is not a database, nor a key-value store. The core log file tends to be a fairly dumb flat file with no support for things like indexing or joins over different parts of the data that might be contained in the file. 

When I talk about a `log` file or a a `ledger` I’m really talking about nothing more sophisticated than a flat file that has time stamped entries on it. 

When I say `append only` what I mean is that given a copy of this file the system _should_ not allow anyone to go in and change any of the things that are already in the file, it should only allow you to add new things to the end of the file. 

By describing this file as being `eventually consistent` what we mean is that two nodes who whose copies get out of sync can find a way to agree which of the two different copies should be discarded in favor of the other one (since all the log files can be tampered with you have to throw one away rather than rewrite it). 

Differences in copies can happen because  one node might get information about changes before a second node, and that second node could write some other data onto the blockchain before the changes that the first node made are seen by the second node. 

this process of picking winners when there are discrepancies works to make sure that in time all copies are the same, and we call this eventual consistency. 

There are some well known important append only data stores (wikipedia, for example, keeps track of every change to every page and makes this data publicly available. A linked data version of wikipedia — [DBPedia](https://wiki.dbpedia.org) — has become a central resource in the linked data world).

There are plenty of databases out there that operate at scale, can be decentralised and have different mechanisms to allow them to get to consistency, however this is not an easy engineering problem at scale (see [Jespen](https://jepsen.io) for example). These distributed databases are usually run by a single organisation that can be spread over a large number of machines in variety of different locations, rather than as a truly open distributed system. 

There are many open distributed peer to peer networks that people participate in, the Tor and Onion networks are good examples, as are the bit torrent and [freenet](https://freenetproject.org/author/freenet-project-inc.html) networks, but these networks are more for data sharing rather than making a system that creates a public log file that anyone can inspect. 

What does blockchain get you that some of these other systems don’t? 

By making this file public on the network, and allowing anyone to take part in storing a copy, and take part in running the algorithm that sets eventual consistency across all copies when new writes come in to the log file, if you get enough people taking part on that open network, you can remove the need for any central source of truth or central authority or gatekeeper on the writes that are added to the log file. 

So getting rid of a central authority, for some use cases, can sound like a really intriguing idea, but what are the costs associated with running a node on this kind of network? 

Well, you need to ensure that your consistency algorithm is immune to attack otherwise there can be little trust in the veracity of the records written to this log file. In order to do this the blockchain protocol involves a thing called “proof of work”. Proof of work makes it artificially slow for any single node to verify the new writes onto the blockchain, and by so doing it allows all of the nodes on the network to have enough time to stay in-sync without a number of them being taken over by a bad 3rd party. This proof of work is computationally expensive and if you run a node on a large blockchain network where the log file is quite big, you end up having a large electricity bill. There is an actual significant cost. 

So you need a mechanism to get people to take part in being on the network, for if there are not enough people on the network, the network could be attacked easily. 

The blockchain protocol does this by rewarding nodes with tokens, and those tokens in turn become the route to adding new entires to the log file. Now rather than just having a log file with dates and some data we have a log file that tracks dates, use of the tokens for writing to the log file, and the data associated with the write. 

If the data we associate with the writes is data about exchanging goods or services, then the tokens become a kind of unit of exchange, and so we often talk about the writes to the blockchain as being transactions. The writes can also just be about moving the ownership of these tokens around the network. 

What do we gain, and what do we lose, by opting for using blockchain over some other data storage mechanism? Well we gain the ability for verified transactions to occur without a central authority — so long as the consistency algorithm is robust. We probably lose the ability to scale quickly, and we certainly lose the ability to verify transactions in a time and cost efficient manner. 

In a way we are trading time and energy for trust. 

What do we need to have in place for a blockchain system to work? Well we need enough independent nodes on our network to make our blockchain tamper proof. We also need all of these nodes to be incentivised to participate, so either the transaction costs have to be really low (making it easy to attack, so not good), or the tokens granted for participation have to be seen to be of sufficient value that those running nodes will continue to do so, even as time and energy costs rise. 

In low trust ecosystems (where there is systemic corruption, or regular payment systems are badly degraded or structural bias exists to prevent people from getting credit), then I can see potential value for blockchain like systems, but I’m not sure if that value has been fully realised yet as the barrier to entry to these systems means that the technical bar itself acts as a kind of bias against the use of these systems by the weak and marginalised. 

In systems where there are many existing traditional actors who have a forrest of standards and interoperability issues I can see value in all players converging on one way to do things as a means to reduce frictions in those systems, but the explosion of ICOs and pennant for any largish blockchain system to end up forking indicates to me that blockchain is not yet the holder of the secret to creating industry-wide standardisation for any systems. 