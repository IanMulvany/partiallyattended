---
categories:
- linked-data
- SKOS
- RDF
- RDFa
- pool-party
- conference
- London
- Semantic Web
- data.gov
- postcode paper
date: 2010-09-14T00:00:00Z
title: The Future of Knowledge Organisation on the Web, a one day conference.
url: /2010/09/14/linked-data-london-meeting/
---

I'm attending this event today, and I'm going to keep some notes as the day progresses.  There are a couple of oddities about the event:

 * No Coffee. That's a bit of a pity
 * No power outlets in the conference room. Not many conferences have that, but one would think that it is a no brainer, especially for any meeting about the web, and in particular linked data. 
 * To add to that, there also seems to be no public wifi.  There may well be but we have not been told about it yet.
 * It also seems that there may be construction happening on the roof later.

On the flip side, the speaker line up looks pretty good, so I'm anticipating learning quite a bit today. There is a huge representation from the BBC.  One obviously tends to think of the BBC as an entertainment and news organisation, but at it's core is an enormous flow of information.  There are something like 20 people listed on the attendee sheet from the BBC.  I imagine that linked data is pretty important for them.  On the flip side, there are very few academic publishers represented, just one as far as I can see, Nature Publishing Group.  Their offices are around the corner, and I've just bumped into [@TonyHammond][thtwitter], who has done a huge amount of work in the past on linking repository systems.

There is a packed room ![room][room]. 

[thtwitter]: http://twitter.com/tonyhammond
[room]: /images/iskos.jpg

So we get going!

# Nigel Shadbolt on Government Linked Data, a Tipping Point for the Semantic Web

Wants to talk about policy, the UK is providing a huge opportunity to put Semantic Web to good use. Argues the open government data is a killer sector (in lieu of killer app).  Is talking about the importance of local government data, in the new government there remains a clear commitment to transparency in open data.  

Interesting point that the scale and scruffy nature of the web has a tendency to catch you out.  Hard core AI work often does not scale.  The substrate is linked data.  (It look likes there is still an attempt in the SemWeb to implement the very bottom of the stack proposed in 2010).  

Linked data sets have the same kind of power spectrum as the open way, scale free with a heavy tail.  Some resources are very heavily linked to, e.g. some core facts in DBPedia and government boundary data.

As a community we should consider government data as a gift. 

The first set of data that prompted opening data was the bicycle accident data.  It was opened because someone working in No 10 had a friend who had been killed in a cycling accident.  They were astonished when after opening up the data led to apps that had been created by developers.  Before this Government didn't realise the potential in a citizenry that have the tools at their disposal to manipulate that data.  

(One of the key points emerging out of this talk is that "interesting data" is the data that has some hook.)

They have created a new Crown Licence that covers data release of government data

They are working towards a definition of what public data is.  Basically this is any information that is non-personal and is collected in the course of public service delivery.  If this became an entrenched principle then one could imagine finding it easier to hold public services better to account, and could see the creation of innovative apps around that data. (This leads to the question of the power of the citizenry, how does one ensure equality of access to that data, or at least reduce the barriers to the general public for being able to render and work with that data.) 


Interestingly he points to [NHS dentists][dentist], and that's an app that I used to find my dentist! He also mentions [ASBOrometer][asbo], an app for looking at the ASBO level of your local area.

He mentions the postcode paper, I was at the Guardian developer day that produced that!! When that developer day happened the Ordinance Survey data was not available, and post codes were a paid for service, but those data sets are now available.  

Another example is train and bus time tables.  The franchises that run these services don't have any feeling that information they produce, like the time tables, should be opened.  These franchises are running with public money on behalf of the public, and so there is an argument that they should make data of this kind available, rather than just as a paid for iPhone app. An example is [Spotlight on Spend][spotlight] which hi-lights government spending.

From January every council will have to publish everything they spend over 500 pounds (I'll be interested in looking at data from Hackney Council).

One of the strongest arguments for creating "five star" linked data is that it builds a robust national digital infrastructure.  If you give a school a robust URI, then every data set that uses that namespace can be reconciled. [Enakting][enakting] is a Southhampton demo of linking disparate data resources together.

[dentist]: http://www.elbatrop.com/ukdentists
[asbo]: http://www.asborometer.com/
[spotlight]: http://whatis.spotlightonspend.org.uk/
[enakting]: map.psi.enakting.org/how


# Antoine Isaac, SKOS and Linked Data

Antoine is from the Frije Universitat, Amsterdam. He is working in [Europeana][eup], and is co-charing the W3C Library Linked Data group.  Previously he worked on the W3C group that produced the SKOS specification.  His main focus is on cultural assets.  [SKOS][skos] is the Simple Knowledge Organization System.  The scope is to represent information around systems such as thesauri and dictionaries in RDF.  It is not a language for representing formal semantics, in contrast to OWL.  It is possible to turn Knowledge Organisation Systems into ontologies, but it's kind of hard.  They have soft semantics, but that does not mean that they are not interesting.  It can be useful for things such as semantic search and annotation systems.

This is my first time in a talk about SKOS.  It seems that it underpins something like a thesaurus with terms such as "related", "broader", "preferred label" and other terms that give a relationship between terms.  These relations are pinned down using RDF and URI's.  This then allows you to bridge different thesauri, as the underpinning relationships in both are underpinned with the SKOS vocabulary.  I guess there are tools out there that assist in applying the SKOS vocabulary onto a thesaurus.  Interestingly the SKOS vocabulary is extensible, and I wonder whether there has been any move to joig up SKOS and [SWAN][swan]? 

There are some basic constraints in order to try to avoid chaos.  One of these is that any concept can only have one preferred label per language.  Inference is supported by the concept of "broader" and "narrower" links, and these are inverses of each other, allowing back inference.  

There is a minimal semantic commitment, pinning the meaning on the existing information system.

There is an interesting example using library of congress subject headings, which also bring in links to similar concepts from other vocabularies.  They [stitched][stitch] together vocabularies from the US, France and Germany.

They have a [list of linked data sets][datalist] that have used SKOS. These include New York Times subject headings and a number of sources from the physical sciences. (I wonder how useful it would be to try to extract interesting terms from scientific articles and link them to New York Times subject headings). 

Antoine is starting to run out of time and the convener is standing up and looking leery. Now, time for coffee, yay!

[eup]: http://www.europeana.eu/portal/
[skos]: http://www.w3.org/2004/02/skos/
[swan]: http://swan.mindinformatics.org/ontology.html
[stitch]: http://www.cs.vu.nl/STITCH/
[datalist]: http://www.w3.org/2001/sw/wiki/SKOS/Datasets


# Ricard Wallis from Talis on The Linked Data Journey

"Observations of a fellow traveller"

I recently saw Richard talk at Science Online London, and he gave a great talk there, so I'm looking forward to this.  

"Semantic technology has a reputation for being really useful until you add the second user".

This is very close to the talk that Ricard gave at Science Online, so I'm not going to write up this talk in much detail.  

Some interesting lessons coming from the talk, one of the powerful arguments that got government to open up data was to point out to them that the data may well be subject to freedom of information requests.  These are very time expensive, and can be totally avoided by publishing the data up front.

When the New York Times published their subject headings they got some vitriolic feedback because of the way that they assigned ownership of heading terms.  This was just the result of the naive application of the ontology, but the community got quite upset.

The BBC edit information in Wikipedia for use on their sites. They pull in the data using RDF, and the information goes out into a resource that can be reused by many other people.  

Some interesting links:

 * A site that shows all UK [legislation][legislation]
 * [New York Times data][nytdata]
 * Animals!![animals]
 * [Postcodes!][post]
 * "[Same as][same]" resources 
 * [Pivot][pivot] browser from Microsoft

[legislation]: http://www.legislation.gov.uk/
[nytdata]: http://data.nytimes.com/
[animals]: http://www.bbc.co.uk/nature/species/lion
[post]: http://uk-postcodes.com/postcode
[same]: http://www.sameas.org
[pivot]: http://winspark.net/2009/11/25/microsoft-pivot-a-new-internet-browser-from-live-labs/


# Steve Dale, Linked Data in Local Government: The Knowledge Hub

So, what is the "Knowledge Hub"? They are trying to solve the problem of the proliferation of sources of information.  There are also a proliferation of community web sites.  Conversations are becoming more granular, and increasingly dis-aggregated.  At the same time there is a growth in data, and data availability.  However there is very little connectivity.  Wow, he has just pulled up an overview of the proposed architecture.  They want to aggregate information from many different sources, add a semantic layer, and create an API an apps store on top of this.  They then want to be able to set up a push notification service to users based on context.  I don't believe that this is practically possible at the moment, but if they do build this, then it might well be an interesting innovation.

This general schema is one that could be applied to pushing notifications based on context around many potential contexts, but I don't believe that we have a good experience for ambient information available to us yet.  Aardvark and Foursquare have started to scratch the surface for this, and Tim O'Reilly's idea for an intelligent phone book are pointing in the direction that we may be heading to, but I think we are very far from that.

This idea seems to me to be lacking in specific measurable gals around success.  I notice that they also want to create their app platform on top of the google gadgets platform, so the big question that they have not answered is how to get user and developer engagement.  They are starting development now, using an agile methodology they want to get to a live product in early 2011.  Good luck to them!



# Prof. Dr. Martin Hepp, Linked Data in E-Commerce, The GoodRelations Ontology

From Universität der Bundeswehr München. (Wow, you can really hear the hammering on the roof).  In Market economies finding partners for trade is important.  This selection process is sometimes done implicitly.  The effort for keeping this exchange alive in a market economy is estimated to be more that 50% of GDP in the US.  This includes search for suppliers, the banking system, anything that is needed to sustain a market beyond a trivial barter economy.  (This seems like a strange analysis, for instance many service industries though probably included in this figure, are also ends in themselves).  A key driver for search is specificity of the goods.  How much you loose when you can't use a good for what it was designed.  

In 1920 Merck had a catalog of everything that could be traded.  There were 5158 items that were relevant for a typical business owner.  We are now consuming rather a larger number of types of good.  Now in a bakery, for instance, you can get 30 variations of bread!  As items proliferate, the search space increases.  The effort for advertising, and for searching, for specific items increases with specificity.  (I just posted the wrong power cable along with a hard drive, that I recently sold on e-bay!).  The web has decreased the search cost, and yet we still spend a lot of time of searches.  And yet the web is one of the largest data shredder in history.  Often data starts out in a structured way, for instance the producer has a database containing information about the production process.  When you transfer this to the web all of this extra data gets stripped.  

Linked Data is Data Linked!  Preserving the structure of the data on the web, clustering links by meaning, linking data elements represented by documents and reducing the lookup effort for getting hold of metadata for an element.  These are the four big things that the linked data world are going to bring into the filed of data management. 

Preserving the structure is key, and so the quality of the vocabularies/schemas/ontologies that you use will have an impact on the reusability of the data.  Interestingly may shops update data very quickly.  Crawling the data does not work if the data is changing hourly, as the cache will be invalid quickly.  He makes an interesting point about how a technology will get adopted.  It should get adopted when the perceived benefit outweighs the perceived costs.  If you have to go out and beg people to use linked data, then there is something wrong with the model.

[GoodRelations][gr] is a schema for commerce on the web.  It has been developer over the past 10 years.  You need to realise that an ontology is not just for publishing data, but is also for the structure for reusing the data.  It works by getting suppliers to put a payload of RDFa with structured data into a webpage.  

When creating an ontology one needs to make it as simple as possible, but no simpler.  Getting this balance correct is very important. For instance interestingly in this ontology a price is not a property of a product, but rather of an offer.  Stores and business entities are distinct.  A product is distinct from a product model.

The basic structure is that there is an Agent who makes a Promise around an Object.  

His closing point about making use of RDFa over SPARQl endpoints is brilliant.  As he says, connecting 80 databases using a line call is something any middleware vendor could have done in the 1980's, how do you convince thousands of shop owners to do this? The answer is that you don't.  

[gr]: http://www.heppnetz.de/projects/goodrelations/

# Andy Powell, Eduserv, Linked Data - the long and winding road.

This is a somewhat more sceptical approach, not totally sceptical. If we believe that linked data is the future of the web, then what we are really saying is that RDF is the future of the web.  Looking at one community we can perhaps learn some lessons, let's look at the Dublin Core community.  The key-points of this talk are:

 * DC is originally 15 metadata elements
 * in actual fact its more like 60 properties and classes, that is maintained reasonably well
 * this is all declared using RDF/RDFS
 * it started in 1995, a very librarian-centric view, thinking one could still catalog all of the web pages
	* embedded in meta tags
	* expose this to search engines
 * One of the consequences is that there is a record-centric approach
 * so that you can ship them from one application to another
 * the record is the mechanism for tracking provenance
 * the original elements were thought to be 15 fuzzy buckets
 	* this was a feature, not a bug
 * the data modelling was very naive, e.g. author name was an item in a DC record rather than thinking about it being a property of a person who was the author
 * strings vs. things, a separation between entities, and the labels of those entities was not properly resolved
 * little abstraction of the model from the syntax of the underlying model
 * 
 * Challenges
 * Even still a discussion about adopting an RDF model
 * need to argue towards Open, in that you don't want to be in a silo
 * you need to recognise that everyone can catalog stuff, and for the more traditional cataloging community this can be hard to accept
 * the 'http' URI problem. 
	* people stil think that http URI's are only for locating web pages, need to conceptually get across that you can use them to identify anything
 * modelling
	* modelling is hard, they also need to gain traction within a community
 * [the modeller][modeller] is a great post highlighting some of the issues
 * linked data must be a success on the web if it is to play a future on the web, that means RDF needs to be a success on the web
 * so far it has not been a success on the web, which is not to say that it won't in time.

So far this has been the best talk of the day, it's really great as an overview.


[modeller]: http://blogs.ecs.soton.ac.uk/webteam/2010/09/02/the-modeler/


# John Goodwin from Ordinance Survey, Linking to Geographic Data

Research Scientist with OS.  At OS they are very good at saying where stuff is, but not what stuff is.  Geo data is important, there are still confusing records around place names, e.g. Hampshire.  The OS has decided to open an [authoritative set of linked data][osdata], e.g.

 * boundary-line esri-shape file
 * code-point
 * gazetteer

How do you get that out as linked data when the formats are complex and sometime proprietary?

They have now converted this into linked data.  RDF is not very good for spatial data, but you can do some qualitative relations, and you can put in topological relations, such as containment, and boundary relations.  This administrative info is on the web now.  (The postcode paper gets another mention, yay, go PostCodePaper!!)  

[osdata]: http://opendata.ordnancesurvey.co.uk/


# Andreas Blaumer, [PoolParty][pool]:SKOS Thesaurus Management utilising Linked Data

from punkt.net Services. 

This talk starts off by re-iterating the power of the web.  It looks like many apps are beginning to sit on top of web scale information, and not being based on heay ontologies.  As Jim Hendler says "A little semantic goes a long way".  For a system that seems to be being based on the topology of a large scale network I'm surprised that no-one has been talking about the implications or details of the structure of the network.  No power spectra in this conference yet.  It was alluded to a little by the person who was talking about GoodShopping.

Andreas thinks that SKOS could introduce Web2.0 mechanisms to the Web of Data.  When they developed Pool Party, then the question is how can any person publish information or knowledge, as linked data?  (sounds a bit like the Drupal extension).  

The tool seems to be a web interface that allows for markup and concept tagging of documents.  Can connect to a corporate thesaurus.  Wow, we are going to get a live demo.

They start by taking a text and counting terms. Then they look for terms from DBPedia, as well as calls to a thesaurus for economics.  They also look for related terms based on completing trigrams, and use these to generate a SPARQL query to get even extra terms.  These terms are then presented as a set of possible tags that can be used to semantically mark up the text.  They have a cross-language dictionary that helps cross-tag across languages.  They have exact and close match in searching.  They don't use "sameas".  You can also do a matching between concept schemas.  They can import a number of different kinds of info, N3, N-Triples, RDF etc.  Output is possible in a number of different XML formats.  

He mentions the [LOD2][lod] project from the EU. This is a 4-year EU project. Good luck with that. This is an FP7 project.  The EU is making a lot of data available, perhaps there will be scientifically interesting data sets being made available. 

[pool]: http://www.poolparty.punkt.at/demozone
[lod]: http://lod2.eu/


# Bertrand Vatant, Porting terminologies to the Semantic Web

a.k.a. the Semiotic Web (you can tell that the speaker is French, I think I have only ever heard the word Semiotic being used by French people).  On the slide there is a reference to the "quick off" of [datalift][datal]. (he means "kick off", but it's a pretty cute error).

He has just said that a resource as in 'URI' has become more abstract over the last 20 years. It is now a resource if it is identifiable and worth speaking about (mind you most things that are addressable are really not worth talking about, certainly not most things that are on the web).  He really is talking about semiotics and semiotic triangles.  And this is the last talk of the day.  (The open web, in a way, wallows in it's own existence without too much care for the signifiers.  It's a dynamical process, an infrastructure, along which meaning travels.  Stopping to pin URI's on the evolving mechanisms of the web may not be a viable strategy.  The implication for this is that systems such as twitter will never emerge on the semantic web as the semantic web will not be able to evolve at the scale that a system like twitter can evolve.  That's not a bad thing, it just means that we need to be clear about the potential for these kinds of tools, and to be aware of the correct domains where they should be applied.)

[datal]: http://datalift.org

And at this point it's time for a glass of wine. 

# links mentioned in this post

 * [http://twitter.com/tonyhammond](http://twitter.com/tonyhammond)
 * [http://www.elbatrop.com/ukdentists](http://www.elbatrop.com/ukdentists)
 * [http://www.asborometer.com/](http://www.asborometer.com/) 
 * [http://whatis.spotlightonspend.org.uk/](http://whatis.spotlightonspend.org.uk/)
 * [http://map.psi.enakting.org/how](http://map.psi.enakting.org/how)
 * [http://www.legislation.gov.uk/](http://www.legislation.gov.uk/)
 * [http://data.nytimes.com/](http://data.nytimes.com/)
 * [http://www.bbc.co.uk/nature/species/lion](http://www.bbc.co.uk/nature/species/lion)
 * [http://uk-postcodes.com/postcode](http://uk-postcodes.com/postcode)
 * [http://www.sameas.org](http://www.sameas.org)
 * [http://winspark.net/2009/11/25/microsoft-pivot-a-new-internet-browser-from-live-labs/](http://winspark.net/2009/11/25/microsoft-pivot-a-new-internet-browser-from-live-labs/)
 * [http://www.heppnetz.de/projects/goodrelations/](http://www.heppnetz.de/projects/goodrelations/)
 * [http://blogs.ecs.soton.ac.uk/webteam/2010/09/02/the-modeler/](http://blogs.ecs.soton.ac.uk/webteam/2010/09/02/the-modeler/)
 * [http://opendata.ordnancesurvey.co.uk/](http://opendata.ordnancesurvey.co.uk/)
 * [http://www.poolparty.punkt.at/demozone](http://www.poolparty.punkt.at/demozone)
 * [http://lod2.eu/](http://lod2.eu/)
