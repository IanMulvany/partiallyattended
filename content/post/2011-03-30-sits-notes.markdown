---
categories:
- sits
- jisc
- DLF2010
date: 2011-03-30T00:00:00Z
title: Sits meeting notes, November 2010.
url: /2011/03/30/sits-notes/
---

2010-11-04 sits

Right, the meeting is starting, it's an open meeting, so we don't have
a specific agenda, but as the day goes on topics for discussion will
emerge, and these will be time-boxed for discussion.

As the participation list is available on the [eventbrite][ebs] site,
I'm not going to capture that here.

[ebs]: http://sits-dlf.eventbrite.com/

# Some topics from the last meeting
- signatures on digital objects
- correct identifiers on digital objects
- author identifiers
- lightweight languages
- toolsets
- sword, sword2

</br>

# Some potential topics for this meeting
- authentication and access control
- rdf and linked data within institutions and repositories
- data curation
- reasonable workflow components, best practices
- lightweight tool sharing
- web archiving
- sustainable storage
- tool sharing
- data curation, big data, and what the concept of curation means for
repositories  
</br>
# Actual topics discussed
* [Authentication](#auth)
* [Linked data](#link)
* [Web Archiving](#arch)
* [Identifiers for people](#id)
* [Microservices](#ms)
* [SEO and search engine optimisation](#seo)
* [Lightweight Languages](#light)


</br>

# topic discussions

<h2 id="auth">Authentication</h2> 

The first option that is discussed is shibboleth. Generally authentication breaks down according on one of the following mechanisms:

- shib
- non-shib
- ip based

One of the questions is how does service host have trust in 3rd party
services, and understand whether that other provider is doing a good
job?

A problem with ldap is that groups within ldap could go out of date.

:question: has shibboleth provided support for services yet?
:answer: it's an interesting question

Are there approaches on service to service authentication that have worked
3 concrete examples:

- j2k service, it retrieves content over http
- integrating with JOVE, pass in to it a url source, and if that content
is protected it will be the same issue
- fedora

So there are social, and technological problems

How does one manage individual level access on a lightweight basis,
for instance, allowing people to pass something off to an iPhone. How
do you enable content owners to set the access permissions of their
own data.

If you deliver all of your content with Drupal, you can just hook into
drupal's authentication systems, and this makes it look to the end
user that they are just managing a part of their site.

So there are a couple of things going on here:

- institute to institute
- institute to end users around content held by the institute
- data owner within institute to 3rd party applications for that user,
e.g. iPhone apps
- data owner within institute setting permissions around their own data

An interesting use case is how you allow anonymous local users on a
campus wide system to access content.
Shib2 has a way of allowing an ip address to skip the authentication
step, it's a pretty static list.
This use case was designed for kiosk machines

There are [ezproxy][ezproxy] campuses and non-ezproxy campuses. This use case is
slightly different from the normal experience of a web user because
when they go to a 3rd party service we need to figure out a way that
would enable them to assert the university rights at that end point.


### takeaways from this talking point:
- think about pushing the authentication down into the stack, so that
the front layer can be plugged into a number of different areas? (I
didn't capture that point well)
- articulate how openauth does or does not work within institutions
(what does [saml][saml] give you that [oauth][oauth] does not give you?)
- are there any examples of universities that are using [openid][oid]?
- think about creating a microservices driven layer for
multi-authentication systems

[oauth]: http://oauth.net/
[shib2]: http://shibboleth.internet2.edu/
[oid]: http://openid.net/
[ezproxy]: http://www.oclc.org/ezproxy/
[saml]: http://en.wikipedia.org/wiki/Security_Assertion_Markup_Language

</br>

 <h2 id="link">Linked data</h2>

What is happening and what is not happening, what could easily happen,
and why is it not happening?

In [blacklight][bl] search repositories there is a lot of content
aggregating there, and these could be exposed as [rdf][rdf]. I ask what is
the advantage or disadvantage of rdf over [opensearch][os]. This is answered
quite nicely, linked data is about known content, and opensearch is
about finding content when you don't know exactly where it might be.
Think of linked data a bit like rss.

[bl]: http://projectblacklight.org/
[rdf]: http://www.w3.org/RDF/ 
[os]: http://www.opensearch.org/Home

Another question, is there other content that we should be thinking
about pushing out too, is there local content, what would that look
like, and how would that help in the open world?

Is there a spec for exposing triples as linked data. There are
hundreds of specs, and many different ontologies. The best thing to do
might be to wait and see what the big players are doing. A good
example is Google's recent adoption of [GoodRelations][gr].

[gr]: http://www.heppnetz.de/projects/goodrelations/

One thing that really bit Southampton is to think about how it is
going to be consumed, and ideally consume it yourself.  A good analogy
is to create a user interface, and never use that user interface
yourself.  It's the only way where one will find the minor but really
annoying errors.

Something to look for are javascript tools and restful apis for
playing with the semantic web. [Jenny Tennison][jtb] is working on some of
these tools like [redfquery][rdq].

[jtb]: http://www.jenitennison.com/blog/
[rdq]: http://code.google.com/p/rdfquery/

Another issue is what namespace do you link to, and where is the
trust.  (I'm in sameas, yay!
[http://sameas.org/html?q=ian+mulvany&x=0&y=0][me])

[me]: http://sameas.org/html?q=ian+mulvany&x=0&y=0)

How do you decide what you want to link to?  



## some ontologies that might be useful

The BIBO ontology seems to be a good first place to look, and here are a bunch:

- [SemanticOverflow](http://SemanticOverflow.com) is a good ontology
- [bibontology](http://bibliontology.com/)
- [Good Relations](http://www.heppnetz.de/projects/goodrelations/)
- [HCLE](http://www.w3.org/2001/sw/hcls/)
- [Sindice](http://sindice.com/)
- [SameAs](http://sameas.org/)
- [Freebase](http://www.freebase.com/)
- [DBPedia](http://dbpedia.org/About)  


## Action Items

- have noted that we need to identify promising formats and vocabularies
- a low hanging fruit is to have a community effort to identify, even
at the predicate level, what terms to use (there is a lot of
discussion going on in the UK between various groups, but there is no
formal ...
- we will set up a freebase page for collecting ideas around this


</br>

<h2 id="arch">Web Archiving</h2>

From the [maemento][mmo] perspective, an archive is no different from the
rest of the web, it just has content from the rest of the web.  That
includes CMS's, these are just archives systems, as they have the
content from the past sitting in their databases.

[mmo]: http://www.mementoweb.org/news/

## Issues:

- versioning requirements
- accessibility

As a starting point it would be interesting to see what the Duraspace
people are thinking.

It seems like making a repository a time gate for itself is a great
idea.  Dspace, however, does not do versioning. As a part of the
re-architecting there is a hope to get versioning into Dspace via the
fedora component, but it is a little way off.

Hydra would be dependant on the fedora component, but it is not
implemented at a high level yet.

What % of revisions in repository systems at the moment are ones that
could be exposed, compared to ones that are just typos?

This is a decision that one has to make in general, there may be legal
restrictions, for instance. But if you do expose them, then doing so
in a way that is browsable is probably a good idea.

An interesting question, if something like google becomes maemento
aware then it's likely that this will take care of this issue.

There seems a lot of years between now, and when google is going to
provide time aware content.

There is a difference between doing a historic search, and currently
available history.

An interesting thing might be to be able to get a list of recent uris
from an archive, and find a way to preserve the content at those uris.

There is a "wayn" protocol for handing over web archives from one
place to another.

A question comes up for how do you archive rapidly moving web sites.
There is no good approach for this yet. Transactional archiving is an
approach that might be investigated.



## Action Items

- if you want to be well behaved, it can be hard to archive social
media sites (one could look at consuming feeds)


</br>
# Lunch

Now we have a discussion about what we will talk about in the evening session.  


 <h2 id="id">Identifiers for people</h2>

In terms of author identifiers, Southampton have gone for a local
approach, and are creating linked data identifiers. Where two people
are the same, use sameas to link them. They do make them available.

The ORCID project is going to go and push ORCIDs onto people that
publishers know about. This won't happen immediately, but will get
better as time goes on. Disambiguating authors is costly, so there is
a large advantage from doing this as early in the publication process as you can.

ORCID will also act as a registry, so one can lookup things like a
REPEC and other identifiers that an author might have.

The big question is whether ORCID should just be an identifier, or
whether it should contain information like bibliographies. The issue
is if it is an identifier service only, how will it get paid for.

Right now thee is a testbed, the code from Thompson has been
submitted, does not cover every use case yet.

There is a hope that this will be available in 2011 at some level.
There is a big stakeholders group meeting in London on November 18th.

There will be APIs for deposit and search, as well as a web protocol

Independent researchers will be able to register themselves.

There will be provenance for who made different assertions, whether,
for example, a publisher or an institution the independent researcher.

Some questions: has there been any discussion around assuming that
this needs to be a central vs distributed blob of information?

isni is another initiative, it's an iso standard. A number of music.
isni's require that you have published something that people consider
to be authoritative. The names project seems to be working with the
isni project.

There is work ongoing to test ORCIDs against Dspace.


### Resources

- [ORICD](http://www.orcid.org/)
- [ReaderMeter](http://readermeter.org)
- [NAMES](http://namesproject.wordpress.com/)  
- [ISNI](http://www.isni.org/)


</br>
 <h2 id="ms">Microservices</h2>

What do we mean by micro-services? It's becoming a buzz word because
it is identifying an emerging pattern.

There seems to be some confusion over microservices as just being the
CDL implementation in contrast to a general architectural approach.

I'm going to skip out and talk to my wife now ;)
OK, I'm back from the conversation with my wife.


## Resources
- [CDLIB](http://www.cdlib.org/services/uc3/curation/)

We are now onto the final session.

 <h2 id="seo">SEO and search engine optimisation</h2>

Dspace is working with google scholar, and Anurag at google.
Essentially there are a list of tags that google scholar wants, and if
you fill those out then google scholar will give you more coverage.

Scholar has a citation meta-tag schema, and so the exercise is to map
dublin core to that schema. Many of the local repositories (what they
really want are the pdfs, and have metadata around those pdfs).  What
google scholar want is totally different from what Google news wants,
and what the main google search engine wants.

They already had google site maps, but google scholar don't use those.

You ask scholar to crawl your site. You email Anurag.

An interesting question is how much traffic comes in from google,
there is data that about 90% of the repo traffic comes in from google
scholar, and more and more of the faculty are now using google scholar
over web of science, so this is really really important.

What's interesting is that google scholar are trying to encourage
people to use the de-facto Google Scholar standard

An interesting use of testing is to use cucumber and a subject
specific expert to write tests like:

"when I search for blah"
"I should get back search result blah"

There is an interesting conversation about how would this community
propose as a better way to organise metadata on the web, and
potentially look to propose something in RDF.

## Resources

* [Drupal](http://drupal.org/node/641580)
* [Publishing Tags](http://www.ghastlyfop.com/blog/2008/05/meta-analysis.html)
* [Google Scholar for Publishers](http://scholar.google.com/intl/en/scholar/publishers.html)
* [Inclusion in Google Scholar](http://scholar.google.com/intl/en/scholar/inclusion.html)

## Actions

Perhaps take this issue to NISO, to determine whether there is space
for publishers and repositories to push back against google for
adoption of better metadata tags. An example would be to propose
possibly RDFa (perhaps under the bibo ontology)


 <h2 id="light">Lightweight Languages</h2>

A discussion ensues about adopting new tools, and how to convince IT
managers to adopt new tools.

- security holes will almost always come from customisations
- setting expectations, and having a regular patch cycle
- ensure that there is a good shared install base with the same dependancy trees
- can you turn something old off
- log inbound requests for software stacks
- bundle your stuff as a war file and make it pretend that it's a java program

We have not talked about developer retraining. Why should people learn
a new language?


## Resources
- [Squid-cache](http://www.squid-cache.org/)
