---
layout: post
title: Data literature integration workshop.
categories: 
  - data
  - literature
  - publishing
  - STM
  - EBI
  - workshops
published: true
---

# Literature Data integration workshop 2012-10-10

There are many people attending today. I'm not sure whether the attendee list will be released. I've taken notes, but rather rapidly. I may have ended up mis appropriating comments, missed comments, or inserted comments that didn't happen, so take the below with the appropriate health warnings. I still need to check on the links, and pull together a link list at the bottom, but I wanted to get the write up out while it was still in front of me. I'll also do a scan later for typos and grammatical errors. 

## sessions<a id="top">:</a>
- [13.05 - 13.30 Workshop scope and goals. Thomas Lemberger](#intro)
- [Session 1: Data Reuse, Reproducibility and Discoverability](#rrd)
- [13.30-13.40 Wolfgang Huber: Executable articles - publishing data with data analysis code and narrative](#ea)
- [13.40-13.50 Jason Swedlow: Data Reuse, Sharing and Publication with the Open Microscopy Environment](#drsp)
- [13.50-14.00 Timo Hannay: Text Mining and Data Publishing for Journals](#timo)
- [14.00-14.10 Lee-Ann Coleman DataCite: discover, access and re-use research](#dcd)
- [14.10-15.10 Discussion](#discss)
- [Session 2: Quality and Data Stewardship](#s2)
- [15.30-15.40 Alvis Brazma Structured vs unstructured data](#unst)
- [15.40-15.50 Norbert from Gottingen](#gott)
- [15.50-16.00 Todd Vision Will authors care about the quality and stewardship of their data?](#qas)
- [16.00-16.10 Alex Bateman Crowd-sourcing literature data for Biological Databasesi](#wiki)
- [16.10-17.10 Discussion](#d2)
- [Thursday 11th October](#thursday)
- [Session 3: Journal Strategies for Data Management](#jsdm)
- [9.00 - 9.10 Iain Hrynaszkiewicz Current and future approaches to data publication in scholarly journals](#pub)
- [9.10 - 9.20 Laurie Goodman Article Publication & Data Hosting to Improve Release, Reuse, & Reproducibility](#rrr)
- [9.20 - 9.30 Theo Bloom Current situation and future ideas for data associated with PLOS journals](#plos)
- [9.30 - 9.40 John Sack Data: Publish, Post, or Perish](#ppp)
- [9.40 - 9.50 Mike Rossner JCB viewer, Rockefeller University Press](#jcbv)
- [11.00 - 11.15 Summing up. Led by: Ewan Birney & Mark Patterson](#end)

## Welcome & Opening Remarks
#### 13.00 - 13.05 Welcome Jo McEntyre
#### 13.05 - 13.30 Workshop scope and goals. Thomas Lemberger<a id="intro">.</a> ([top](#top))

Some opening comments. A lot of data is unstructured, there are structured repositories too. Many of the unstructured repositories mostly live separately from the papers that are related to the data. Key point for this workshop, how can we bring ideas and evidence together again? A serious point is that there is a fear that most of the data in drug discovery cannot be reproduced, can have potential significant impacts on global health. What is a paper? - some tables, some figures, a lot of text. Providing the text as OA is fantastic, yet text mining has limitations. e.g. in extracting pathways. Figures are mostly data convolved into pixels in a way that makes it hard to extract that data. Figures are central to a formal scientific demonstration. They are part of the natural scientific workflow, they represent the structure of scientific investigation. [JCB data viewer][jcb] is an example of how to move beyond this situation. Making the underlying data for tables and figures available is key. What underlying data should be made available? The underlying data, the original blots? What of very large underlying data? What of data about the data? There are some common characteristics among figures within biology papers. Think of figures as structured digital objects, they can be though of as objects that draw connections between the literature, curated dbs, datasets. The EMBO SourceData project is mentioned (I can't find a link to this project yet). The paper of the future? It will probably remain something similar to the cognitive unit that we are used to today. OA to the underlying text will be there, but we need to go beyond that, where in the back there will be a machine readable version of the paper - data, methods, claims etc. 

There are alway tradeoffs. Some listed: 

<table cellpadding="5" width="55%">
	<tr><td>structured</td><td>vs.</td><td>unstructured</td></tr>
	<tr><td>raw</td><td>vs.</td><td>processed</td></tr>
	<tr><td>data</td><td>vs.</td><td>metadata</td></tr>
	<tr><td>centralised</td><td>vs.</td><td>distributed</td></tr>
	<tr><td>scale</td><td>vs.</td><td>quality</td></tr>
	<tr><td>automatic</td><td>vs.</td><td>manual</td></tr>
	<tr><td>benefit &amp; incentive</td><td>vs.</td><td>cost &amp; burden</td></tr>
	<tr><td>idealism</td><td>vs.</td><td>pragmatism</td></tr>
	<tr><td>public</td><td>vs.</td><td>credit attribution</td></tr>
	<tr><td>legal requirements</td><td>vs.</td><td>community norms</td></tr>
	<tr><td>bottom-up</td><td>vs.</td><td>top-down</td></tr>	
	<tr><td>openness</td><td>vs.</td><td>privacy</td></tr>		
</table>

The goal of this workshop is to propose some pragmatic suggestions towards 'intelligently open data', within the context of basic biomedical research, and not clinical epidemiological data. 

Focus on low-hanging fruit, that we could reach within one year, such as for example: 
* data availability statement in a paper
* dedicated data reference list
* figure source data
* bi-directional links between db's and papers
* other ideas ...

[jcb]: http://jcb-dataviewer.rupress.org/

<br>

### Session 1: Data Reuse, Reproducibility and Discoverability<a id="rrd">.</a> ([top](#top))
CHAIR: David Shotton

The problem is that most research data rots on the hard-drives of postdocs. The problem is not lack of resources, but rather that the researchers are too busy doing things that are more important to them, they have few skills in data curation, and they are not rewarded for data curation. We need good tools, practices, and more sustainable publication sites for data. They have made citation data for a good chunk of the OA literature available at [http://opencitations.net/source-data/][ocp]. One of the formats that they make this data avilalbe as are [N-quads][nq] and [bibJson][bjson] (though today the N-quad link seems to be broken). 

David presents an interface that they have created to make it easier to capture metadata about datasets. It's a web-form tool that can take the submitted data and convert it into an XML or RDF representation of the metadata. This is no doubt makes the downstream processing of data a lot easier, but I have to say that the screen shot presented looked like the usability of the form was fairly low. (A qustion of ease of use came up during the discussion, some researchers are placing data into unstrucutred repositories because it is easier to do, than to fill in the forms to get their data into more appropriate structured repositories. It is suggested that this is not a good excuse, almost that researchers have a duty to go through these hoops, however I strongly feel that unless we as tool makers taker the issue of usability seriously, then our tools are destined to fail.

[ocp]: http://opencitations.net/source-data/ 
[nq]: http://sw.deri.org/2008/07/n-quads/ 
[bjson]: http://www.bibjson.org/

##### 13.30-13.40 Wolfgang Huber: Executable articles - publishing data with data analysis code and narrative<a id="ea">.</a> ([top](#top))

Wolfgang presents a tool called [Sweave][sw]. Encode provide the full [virtual machine][evm], which can either be downloaded locally (as an 18GB vm!!!!), or spun up in AWS. (I think another tool that is like this is [dexy][dx])

[sw]: http://www.statistik.lmu.de/~leisch/Sweave/
http://www.bioconductor.org/
http://www.bioconductor.org/packages/release/BiocViews.html#___ExperimentData 
[evm]: http://scofield.bx.psu.edu/~dannon/encodevm/
[dx]: http://www.dexy.it/


##### 13.40-13.50 Jason Swedlow: Data Reuse, Sharing and Publication with the [Open Microscopy Environment][ome]<a id="drsp">.</a> ([top](#top))

One of the problems is that images are now used as measurements. In a lab it is routine for a single post-doc to generate up to 50Gigs of data in an afternoon. In OME what they do is provide 'glue'. This could be a common file format. The first of these is OME-TIFF. It is really dumb, it just adds some MD into the top of a TIFF file. The XML they now place in these files is supported by many vendors. [Bio-Formats][bf] is a java library, is open source, reads about 120 image formats. They have up to 70K data sets, up to 1TB of data. They have a data management platform - [OMERO][om]. It's a java application with a lot of code generation. OMERO also has some nice tools, like a slice viewer. The JCB data viewer is also backed by OMERO. ASCB created a CELL library, where anyone could submit data, and a human curation interface was built on top of this.

Some lessons:

* image data publication is now
* re-use is anecdotal
* download does not make the data accessible - you need the applications
* do you want just some data, or do you want peer reviewed data
* there is not substitute for manual curation of submissions  

[ome]: http://www.openmicroscopy.org/site
[bf]: http://loci.wisc.edu/software/bio-formats 
[om]: http://www.openmicroscopy.org/site/products/omero

<br> 

##### 13.50-14.00 Timo Hannay: Text Mining and Data Publishing for Journals<a id="timo">.</a> ([top](#top))

Timo describes [figshare][fs] and [SureChem][sc]. 

Likes to think of figshare as like a youtube for data, a place where you can put your data. Each item gets a DOI, there are metrics available on the items. Part of the business model for figshare is being able to provide this functionality to publishers. Publishers want to provide these services, but it's not as easy to do as you would like. There has been a lot of interest amongst publishers, since launch, in having figshare providing this functionality and data hosting, for the journal. They are currently providing this for F1000 research. 

SureChem provides chemical patent search. Provides search over 80M documents. Underlying SureChem is some really smart technology, it will do entity identification, including items that is has never seen before. Lots of heuristics for dealing with fuzzy text. Will do the same with bitmapped images. You can draw a structure of sub-strucure, and you can use that to draw a structure to search by. 

They have started to link SureChem to the journals, and link the journals to the patent information, and link both to databases.  

[fs]: http://figshare.com/
[sc]: http://SureChem.com/


##### 14.00-14.10 Lee-Ann Coleman DataCite: discover, access and re-use research<a id="dcd">.</a> ([top](#top))

[DataCite][dc] was founded in 2009. It is a member of the international DOI foundation. It is a registry for DOI names. Not for profit, 16 full members, members work with data centres within their own countries. They provide a shared infrastructure for DOIs. There is also a social community element. At a global level members work to agree on standards, but at a local level people work together to swap ideas and new services. The [British Library][bl] is an allocating agent. They provide DataCite infrastructure to enable UK data centres to mint DOIs. They do not work with individuals, but rather with organisations. 

DOIs are global, widely adopted, most widely used identifier for research articles, there is a good governance and infrastructure, it is now an ISO standard. 

They expect mandatory metadata for datasets. Provide a landing page for each dataset, can maintain working URLs and has trust that the organisation has  curation and preservation policies in place. 116 active data centres. 1M records in the data store, 1.5M DOIs in total. 50k resolutions a months. There is a nice tool called [crosscite][cs], which is currently under construction. 

[dc]: http://www.datacite.org/
[cs]: http://crosscite.org/


##### 14.10-15.10 Discussion <a id="discss">.</a> ([top](#top))

There was an interesting discussion, I didn't capture any of it. 


Levels of reuse - citation, meta-analysis, computational analysis
Metadata  - who needs it, how much and which data? (fundability - meta-analysis)
Attribution and credit (citation)
Computation - text mining, semantic web (computational analysis)
The importance of data reproducibility - executable figures & articles

##### 15.10-15.30 Tea

### Session 2: Quality and Data Stewardship<a id="s2">.</a> ([top](#top))
CHAIR: Wolfram Horstmann  

####### 15.30-15.40 Alvis Brazma Structured vs unstructured data<a id="unst">.</a> ([top](#top))

At what level do we want to structure data? [MIAME][mie] is presented as a project that got it right. There us an experiment, and there are some well described characteristics if this. [ArrayExpress][ae] gives as MIAME score, see the example here: []. Reviewers and journal editors just don't care about whether data is data is MIAME complete. MIAME is important, it has enabled the creation of a data refinery such as [ATLAS][at]. Alvis is now the most least structured advocate at the EBI. New technologies are emerging, you have to be able to combine the new with the old. The data is growing to such an extent that it becomes challenging for one institute to say that they have "all the data", but at the same time you want to link of all of the data together. EBI will not have a database for unstructured data. There is no name for this yet, but it is planned ot be released in 2013. At the centre of the idea will be a "study". This will become the key identifier for a linked object. Can be linked to data files, bio-samples, assays, external databases, publications, etc., etc., etc.. 

[mie]: http://www.mged.org/Workgroups/MIAME/miame.html
[ae]: http://www.ebi.ac.uk/arrayexpress/
[at]: http://www.ebi.ac.uk/gxa/

##### 15.40-15.50 Norbert from Gottingen<a id="gott">.</a> ([top](#top))

Talking about the role of libraries, the institutional role, it's education and training role, and the interoperability role. 

They have been spending quite some time talking about research data management. At the institutional level, you need to look across disciplines. ARe there generic infrastructures that you need to bring into existence. A library will not speak of the discussions within a community, they have to seek commonalities across discipline. He mentions an interesting initiative that happened in the early 90s to create identifiers for single journal articles. He mentions the importance of interoperability. Institutional archives are just emerging, China, South America, are just building out their repositories. Already in Europe there are over 50 research infrastructure initiatives. How do we make sure people do not spend their time in 10 working groups at different levels, talking about the same thing? 



##### 15.50-16.00 Todd Vision Will authors care about the quality and stewardship of their data?<a id="qas">.</a> ([top](#top))

Todd is involved with [Dryad][dyd]. This aimed at capturing the long-tail of data. Will researchers care about data stewardship? We really don't know. An excellent example of a problem mentioned was where the data was provided, but it was not made clear which sub-set of provided data was used for the analysis in the journal article. Others trying to re-use this ran into trouble. This leads to dissatisfaction, and a tendency to not caring about data stewardship. How can we create a virtuous circle? How can authors compete to get good marks for stewardship of the data. At the moment we have a binary acceptance criteria, either the data is available or not. We need to have some kind of mark of data quality, if there was a competition amongst researchers to get this mark of quality for grant awards or promotion, then this could lead to a much better ecosystem. Todd is not sure that the solution is, but he sees two things that are promising, one is the use of altmetrics (he mentions [impact story][is]). Another element might be to have greater gradation of quality stamps for long-tail data. Dryad is guilty of this, as they only have accepted or non-accepted. They don't have tiers of quality.  

[dyd]: http://datadryad.org/ 
[is]: http://impactstory.org/

##### 16.00-16.10 Alex Bateman Crowd-sourcing literature data for Biological Databases<a id="wiki">.</a> ([top](#top))


Alex wants to get all of the good data out of the literature with relatively small teams of people. They would like the biologists to do this work for them, this is called community annotation, and it has been pretty disastrous over the last 20 years. 

With [rfam][rf]: their database is composed of wikipedia articles. In the past year they have had about 15k edits. They have managed to capture a long tail of people who have made edits. (the wikipedians tend to come along and delete a lot of stuff, they they also do a lot of formatting).

They struck a deal with the journal RNA Biology. They had to submit a Wikipeida article along with the journal articles, but they have only had 20 articles submitted in the past 3 years.

They have been creating stub-articles in wikipedia. They provide suggestions of papers that might be relevant. If you give people no motivation, you get on average 13% in growth in size of the articles. You get patchy results. You can get motivation by homework assignment to PhD studies. Increase in articles by 211% on a small number of articles. Of these people, none became regular contributors. 

If you want to ratchet up the motivation levels, you can make your job depend on it. This led to a 355% increase in the size of the articles, but this does not scale well. 

It's hard to motivate scientists to do this. You get contributions, but it's patchy. The bio-curators in the group are really the backbone of this. You need a core of people who will be there checking 

Another experiment was run by [flybase][fly], they did direct emailing of authors. They were asking authors, in a simplified way, to identifier what the elements were in their papers, and asking them to say something simple about the things in their papers.

If they emailed authors within a few weeks of publication they got a response rate of about 50%, if they got the author in that sweet-spot. 

Rate of response against time dropped exponentially. 

One of the reasons this works is that this is a small community of people, helping to annotate a core community resource. If it is a small community, then then you can get that buy-in. 

[rfam]: http://rfam.sanger.ac.uk/
[fly]: http://flybase.org/



##### 16.10-17.10 Discussion<a id="d2">.</a> ([top](#top))

Again a very nice discussion, that I didn't capture, and a very nice dinner in Cambridge with much jovial discussion. 

## Thursday 11th October<a id="thursday">.</a> ([top](#top))

#### Session 3: Journal Strategies for Data Management<a id="jsdm">.</a> ([top](#top))
CHAIR: Véronique Kiermer 


##### 9.00 - 9.10 Iain Hrynaszkiewicz Current and future approaches to data publication in scholarly journals<a id="pub">.</a> ([top](#top))

Additional files are archiving 'gaps in the market' There is a really long tail of file types that are available. More best practices are needed. There are lots of examples of sub-optimal use, lots of things like tables in pdfs, but it is still a useful thing to be providing. 

How can we incentivise people to follow best practice for publishing data? [bopsharing[bios] provide a good set of interoperable formats. BMC has been trying to make authors make use of these. They allow authors to publish for free if the author uses an interoperable format. People are not organically identifying this as a good initiative.

A solution for a publisher is to not worry about managing data, just send it to a repository. [datcite repolist][drl] lists over 100 repositories in life sciences.

There is an 'availability of supporting data' section. Designed as a flexibly section, could just be a link to the repository, it is a standard section, you can do a free text search. It is optional for the most part, authors can use it if they want to demonstrate that they are being transparent, still need to do a lot of work to get authors to use best practices in citing data. A great example of a shit practice is authors only naming the repo and not providing a URI.

Biomedcentral has a collaboration with [labarchives][larc]. (people, labarchives rocks, it really does). A nice integration is that there are links straight from labarchives to the BMC submission system. 

BMC opened a [public conslutation on the licensing structure of data in OA publications][].

There are some technical challenges, but I missed the slide. 

!! Concern regarding CCO allowing people to not cite work. Some academics are afraid that CC0 will mean that other researchers do not need to cite them. We need to work hard to stop this idea from taking hold, as it is wrong. There is also a fear that people are going to plagiarise, if work is in the public domain or that organistations may make money off of items in the public domain (which is you know, not at all like pubishers making money off of items behind paywalls). 

A nice counterpoint is the open data initiative from Nigel Shadbolt and Tim Berneres-Lee. 

We need to find better ways to educate authors about these issues. 

What will be the sustainability model for data journals and repositories. 

[bios]: biosharing.org  
[drl]: http://datacite.org/repolist
[larc]: http://www.labarchives.com/


##### 9.10 - 9.20 Laurie Goodman Article Publication & Data Hosting to Improve Release, Reuse, & Reproducibility<a id="rrr">.</a> ([top](#top))

[Gigasciecne][gsc] has a novel publishing platform, in that they combine the data platform with the publishing platform. How do we do data review - that gigascience are already doing. How can we cite data and how can we create active papers.

They will only accept data under a CC0 licence - easy! They include how one should cite the paper, they include related manuscripts, they include information on related DOIs. They also include accession numbers for data that is not housed in GigaDB. 

There are papers that have cited the data - in the references, and there are papers that have cited the data as released. This has required a cultural shift (it needs work on educating the academic community the editorial community of our journals). A list of publishers were asked whether they would accept data citations, may publishers - including Elsevier - said yes. Cell said they would not publish a paper that cites data. 

In terms of reviewing the data, they often select specific reviewers for the job of just looking at the data. They are trying to put in all of the tools that people use to do their analysis in place where reviewers can get to them, to aid reproducibility. 

[gsc]: http://www.gigasciencejournal.com/



##### 9.20 - 9.30 Theo Bloom Current situation and future ideas for data associated with PLOS journals<a id="plos">.</a> ([top](#top))

It is now very rare for people to do science today not on a computer. There is instant capture. Then they put it in a box. Then they take some of it out of a box and throw away information by pushing information through some kind of Microsoft product. 

What would be better? An integration collection of methods results data and metadata. How close are we to the perfect world, and how much are we just bolting on things to the old world?

What is data? PLOS are working with the following:

The digital material collected and generated in the process of doing research.

It does not include the bibliographic metadata
Not non-digital materials

# layers of data associated

1. essential to replicate the major findings
2. all of the data that went into the pot to make the data, raw, unprocessed, replicated.
3. from beginning to end, the soup-to-nuts. Every single trace, and digital trail.

Sometimes we are not clear which level we are talking about.

Where should it all go? In a nut - not on that author's website. Bigger is better. 



##### 9.30 - 9.40 John Sack Data: Publish, Post, or Perish<a id="ppp">?</a> ([top](#top))

Highwire work with 150 publishers (including eLife), 1700 journals, 1k+ books. They work with so many publishers. 

There are a lot of stakeholders involved in data publication. Search engines are a key stakeholder (first time anyone mentioned this today, but it's a great point). 

In terms of roles - data repositories - journals - search engines - funders.

Are we re-inventing the problem of journals with data repositories. 

John raises the issue or centralisation vs federation, in terms of the rise of the number of data repositories. Authors just see the diversity of application-level interfaces, raises the question for the author of "where should I deposit". John is advocating for fewer uniform larger deposit locations, with the applications layer built on top of those, and with authors having to worry about fewer places to place their data.

The journal becomes an index to the data.

The search engine in the index to the journal - google - google scholar - pubmed - etc. 

One of the issues that journals have is with the issue of "publishing data". Most journals do not want to take on the responsibility of peer reviewing the data data. Perhaps better to think about the journals as being a conduit to get to posted or deposited data. 

They wonder whether people actually reuse data?

In terms of preservation there should be no dead links. There is a lot of link-rot in scientific journals. The link rot is 20% every two years. After about five years half of the links are dead. Typically these are author locations, or links to research projects. Author locations are definitely transient. 

What would google do with these transient links? Google recommends that we not use only opaque identifiers to point to data, but that we use textual descriptions in addition. This is a kind of belt and braces approach. Textual citations have worked for centuries, the link citation text can lead to a computed path to the location if the URI or ID goes dead. (that is a great point). 



##### 9.40 - 9.50 Mike Rossner JCB viewer, Rockefeller University Press<a id="jcbv">.</a> ([top](#top))

Data need context. Funder policies say very little about implementation, enforcement of funding. People as a resort, have turned to the standard of publishing. 

Journals have always been drawing from the data, or connecting to it but what do you do if you publish a type of data for which there was no public repository. In 2007 this was the case, and led to the creation of [JCB][jcb]

Issues facing microscopy:

* more than 100 file formats, many proprietary (.META is a real player format).
* multi-dimensional - 5d
* sheer volume of data - numbers and size of images (a single z-stack can generate 12k images).


High content screens can produce 1M images. Recently they posted a 300 Gigapixel image. That was 20GB in size. The final resolution of the image was 16M dpi. 

The JCB data viewer is a browser based app for viewing these kind of images. 

For authors it gives them the opportunity to present the data as they have collected - no whiff of photoshop. In general this is a good thing. 

This tool is simply amazing, the hope is that it becomes a standard for publishing image data, and gains adoption across publishers. I was too busy looking at how amazing the tool is, to write up great notes on it. 

There are discussions with Stanford to set up a repository for this data. If that happens then there will be a large amount of curation and hand holding. 


##### Session 4: Concluding Discussion and Workshop Outcomes
CHAIR: Andrew Sugden

#### 11.00 - 11.15 Summing up. Led by: Ewan Birney & Mark Patterson<a id="end">.</a> ([top](#top))

That was a really great day and a half. Euan and Mark sum up with suggestions for next steps, we still have a bit of work to do to pin down exactly what the next steps will be, but there are some clear next steps:

* writing group to sum up the discussions and recommendations with a representative from structured data, unstructured data, publisher and funder.
* promotion of use of a data citation format
* hi-lighting good examples, find a way to inspire researchers to do this
* think about the complexities in the ecosystem, we talked little about non-OA publishers, the role of institutions.

Some other suggestions:

* journals should ask authors for the underlying data for figures. 
> this leads to a good discussion, should this be the role of the funder or the institute, facilitated by the journal? It is good that there is a diversity of approaches out there. We don't like top down approaches, there is the issue of integrity. The EU would like authors who have EU money to comply with standards around data standards. The Commission is not only a funder, but also a legislative body, so they have to be careful about how they approach directives. They have to label their explorations as pilots, and then make a decision after seeing the effects, after a number of years. Having a central structured global archive within a research discipline is a boon, but there are many disciplines where these archives do not exist, and institutional archives are emerging. We don't want to penalise researchers who are using global archives. It is a challenge to make the language about data access be applicable pan-science.
* a proposal to convince non-oa publishers to make anything that is machine readable immediately open access?
> John Sack says that most publishers within the Highwire set feel that data fundamentally an open resource. NPG makes the supplementary data available. The part of the paper that lists where the data is, is often behind the firewall. Could we get publishers to place this statement in front of the firewall. (Could we recommend that this information be published as part of the article metadata?). 
* Get an agreement between publishers on how accession numbers, grants and data are tagged within scholarly articles. 
* Look at a few case studies on something. 
* Recommend that data repositories expose usage data. 
* Get journals to ask for data, upon final submission to the journal. 

## Conclusions

I learnt a lot at the meeting, there is a lot of will, it feels like there is a growing sense that there is a critical mass, there is still  some way to go, but perhaps it is not as far as it might seem. 


## Resources linked to from this post: