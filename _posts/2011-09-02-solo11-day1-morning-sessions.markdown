---
layout: post
title: SOLO11, day1, morning sessions. 
categories:
- solo11
- science-online
- science
- API
- nature
- peer-review
---

# Session on engaging with peer review

This is a very nice panel discussion. For my money there are a number of key points that arose during the discussion:

- discussions with the public needs to happen where the public is
- being half assed about engaging the public discourse around papers, and then hiding behind peer review when you run into criticism is really bad, as for example what happened with the arsenic story nasa and science
- the public needs to be educated that peer review is not binary
- peer review comments should be made public (not everyone agrees)
- where we have representations of papers we should look to link to conversations about those papers (trackbacks and so forth)

There is a very interesting comment in the Q&A from [Martin Fenner][mf] about peer review in clinical medicine. Peer review is not as important in clinical medicine as I had assumed, far more iportant are conferences and clinical trials, and there have been cases of drugs getting approval before the peer review system completes. I found that really interesting. 

One of the other interesting things about this discussion is that it avoided discussion on how long the peer review system can take.

# NPG API session

Interesting, lot's of interest in the API session. It looks like [NPG][npg] is going to be working with [Mashery][msh] to improve the interface to their APIs. I hope some of these people make it to the dev session that is being planned for [Sunday][session]. It looks at the moment that they are making a portal for some of their opensearch infrastructure, which is a nice thing. From the perspective of NPG, being able to see what happens through issuing API keys is a good thing, but of course it adds one layer between the developer and the data. On the whole I think it's probably a sensible approach in today's world as it gives you the ability to control against DDOS attacks, and when you have content that _could_ be considered controversial by any sector of society (think climate change, think evolution), you have to be careful at some level.

I wonder if they are going to also pull in info about the open social APIs that Nature Network sits on top of? I was quite involved with rolling those out while I was still at Nature so they have a place in my heart.

Ah, interesting, NPG are putting their data onto a triple store. I _think_ this could be important, but I just don't know many people consuming triples compared to consuming JSON (and I say that somewhat tongue in cheek at the moment). My point though is rather that someone who is interested in institutional impact probably wants examples of some simple queries and does not really want to negotiate a triple store. 

Interestingly NPG is also going to be including blog data through their APIs. They have an example of visualisations of Neuroscience blog citations. The nice thing about this data set is that it is not journal specific. I could imagine mashing this API up with the [mendeley api][map] and getting a comparison between 

The dev portal will be at [http://developers.nature.com](http://developers.nature.com)

(It's a bit weird writing this post with [@spanx][sp] looking over my shoulder, - he just pointed out a typo, does that make this pair blogging?). 


[mpg]: http://www.nature.com
[msh]: http://www.mashery.com
[session]: http://lanyrd.com/2011/solohack11/
[sp]: https://twitter.com/#!/spanx
[map]: http://dev.mendeley.com 
