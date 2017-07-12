---
layout: post
title: IC2s2 Wikipedia track, Wednesday  
categories:
- ic12s2
- computational social science 
- conference 
---

# Ic2s2 wikipedia track 
### Studying Content Survival, Authorship & Controversy – By Tracing Every Word Change on Wikipedia - Fabian Flöck, Kenan Erdogan and Maribel Acosta

Arriving late to this talk. 

[TokTrack]([TokTrack: A Complete Token Provenance and Change Tracking Dataset for the English Wikipedia | Zenodo](https://zenodo.org/record/345571#.WWXuT8aQ3dQ)) - data is available on Zenodo, 13.5B tokens. There is a [wikiwho]([GitHub - wikiwho/WikiWho: An algorithm to compute token-level provenance and changes for Wiki revisioned content. Tested for EN.Wikipedia.](https://github.com/wikiwho/WikiWho)) API. This is an accurate dataset of all provennced changes in English wikipedia. 

They can look at survival rates for edits. If an edit survives for 48 hours, then it’s probably safe and will live on in wikipedia. 

They can also look at how much people agree or disagree with the content that they are editing. 

You can do an n-gram like analysis on text. 

You can look at the most conflicted parts of a wikipedia page. 

Basically, this is an amazing dataset. 


###  Even Good Bots Fight - Milena Tsvetkova, Ruth Garcia Gavilanes, Luciano Floridi and Taha Yasseri

There are a lot of bots. In wikipedia there are a lot of bots that assist in the process of wikipedia, and 

[They created a typology of internet bots]([Even good bots fight: The case of Wikipedia](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0171774)). Wikipedia are built out of python code, on top of the wikipedia API. 

There are a small number of bots, but they generate a large number of edits (often they are doing tiny simple things, but still in volume they make up a large number of edits). 

An example of what one of the bots do is to revert previous edits (they are trying to eliminate vandalism). They found that even bot reverts get reverted, but if the bot is a “good” bot, why are its actions getting reverted? Bot logic is basically creating contentions, and bots are reverting each other, in an endless cycle. People are basically not paying attention, so this activity just continues at a low level, which leads to lots of interesting questions around goals and efficiently of the system. 

In thinking about the ecosystem of bots, we should expect bot—bot interactions to become complex. 

### Why We Read Wikipedia - Florian Lemmerich, Philipp Singer, Robert West, Leila Zia, Ellery Wulczyn, Markus Strohmaier and Jure Leskovec

They wanted to know why people read wikipedia, and they took a taxonomic and survey approach to understand why. They survey ran on wikipedia. 

They generated a three class taxonomy around motivation, information need and prior knowledge of the topic pages. 

They were able to generate 30k responses to their survey. This is subject to non-response bias. 

They did some bias correction using inverse propensity score weighting. 

They also looked at wikipedia log data, and extracted features about the articles that were being read. 

We see some unsurprising results e.g. during work hours people are using wikipedia for work or study related reasons. 

They correlated information from the survey with traces they observed across logs and article features. 

Topics of articles cluster around the kinds of motivations that people have reported. When bored they look at sport articles, when they are studying they are looking at technical pages, e.g. physics or mathematics. 

They are now extending the survey to other languages other than English. 

They hope that they might be able to allow editors to better understand the kind of motivations that people might have for the kind of articles that they are writing. This could inform writing style or interface design. 


### Modeling collective attention on promoted content in Wikipedia - Marijn ten Thij, David Laniado, Andreas Kaltenbrunner and Yana Volkovich

Looking at “Today’s featured article” in wikipedia (today’s is about the [Battle of Prokhorovka](https://en.wikipedia.org/wiki/Battle_of_Prokhorovka)!) .

These articles get more page views during the day that they are featured! 

In redistributed time page views have an exponential decay, and you can model with a Poisson distribution. The first hour of page views will give you a good estimator for future page views. 


### Linguistic neighbourhoods: Explaining cultural borders on Wikipedia through multilingual co-editing activity - Anna Samoilenko, Fariba Karimi, Daniel Edler, Jérôme Kunegis and Markus Strohmaier

Is showing how language concepts are used in argument, and how the theory of cognitive balance and dissonance is used to analyse political speech (apparently for some positions bicycles are in the bad category of things). 

The empirical evidence for this balance theory has been mixed. 

They think they can test some of this theory using wikipedia data. 

Each article can be considered as a project with a network of people who contribute to, or produce the article. These contributions can be negative or positive. 

What they have found is that the articles on climate change and on racism are different. 

They looked at the bi-polarity of all articles that were produced with sufficient user interactions. 

They found that polarised teams product low-quality output, but need to do more work to uncover the core reasons for the existence of that polarity. 

### Linguistic neighbourhoods: Explaining cultural borders on Wikipedia through multilingual co-editing activity- Anna Samoilenko, Fariba Karimi, Daniel Edler, Jérôme Kunegis and Markus Strohmaier

I like this talk, looking at concepts, as the concept gets narrowed, the number of languages that cover this in wikipedia narrow down. 170 languages describe beer, bit only 4 languages describe Kölsch beer! 

At the moment this kind of observation is anecdotal, but they have generated a systematic way to investigate these kinds of relationships. 

They are looking a the 110 larges language editions of wikipedia, with about 3M concepts (the articles). 

They have list of languages per concept. They create a bipartite network of concept co-editing and then create a network of significant links. 

This creates the network of shared interest for concepts across languages. 

You can find which languages edit similar concepts. After clustering you find language families. Some of the closers are clearly formed by geographic clustering. 

There are also clusters forming around the linga franca of a multilingual region, e.g. Hindi and Sanskrit, Sundanese and Malay. 

They can quantify the contribution of different hypotheses to the overall effect of language clustering. 

It would be super interesting to look at whether there are temporal shifts in editing across languages. 

### The Evolution and Consequences of Peer Producing Wikipedia’s Rules- Brian Keegan

 What are the governance rules on wikipedia, and how do they way they are constituted contribute to it’s resiliency, and how have they changed over time? 

The rules are just pages, and can be edited at any time. 

(There is a “[no angry mastodons](https://en.wikipedia.org/wiki/Wikipedia:No_angry_mastodons)” rule !?) .

Rule making activity mirrors historical wikipedia activity. 

Early rules are still very active sites of editing. 

New rule editors between 2006 and 2008 made the most edits, but make few edits now. 

People who participated in rule making participate in more namespaces and make smaller edits than before having been involved in rule making. 

