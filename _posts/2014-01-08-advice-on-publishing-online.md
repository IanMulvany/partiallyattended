---
layout: post
title: advice on publishing research online
categories: 
- publishing
- science
- software carpentry
---

I have posted this post as a comment on the thread over at software carpentry in answer to the question [What do we teach about writing/publishing papers in a webby world?](https://github.com/swcarpentry/bc/issues/199)

I ended up writing a bit more than I expected, so here are the main peices of advice:

tl;dr:  
	- use a reference management tool  
	- try to find the fastest venue to publish in   
	- try to publish in an OA journal  
	- have a look for the best preprint server for your discipline, and add your work there too (might be a university archive)  
	- add as much supporting material as you can to the right locations, e.g. [github]() for code, [figshare]() for anything, [vimeo]() or [you tube]() for videos  
	- do register for an [ORCID]() and add your newly minted publication to your ORCID profile  
	- don't be afraid to screw around with copyright transfer statements   
	- use version control for your own sanity  
	- remember that all the time you spend pretty formatting your paper will be ignored and thrown away by large publishing companies, especially the work you do on reference formatting, so don't do it  
	- if the collaborative environment of your choice is not working for the group, be pragmatic, drop it, get the damn paper finished already  

I would start by advising people to keep in mind the goals of publishing. You want to get your work out into a venue that will be respected by your peers, and noticed by them. In most cases - but not all cases - this will be a journal published by one of the large STM publishers. Elsevier, Springer, Wiley, Taylor & Francis, PLOS and Sage represent a very large part of that market. 

You want this process to happen as quickly as possible. Aside from the act of writing, and constructing your story, the act of publishing - getting it onto the web - is pure schlep. Every minute longer that you spend in this process is a minute wasted, as it's not adding value to your research or your ability to put yourself in the position of being able to get the resources you need to do the research you are interested in.

Your first priority is to understand the most appropriate venue and then understand the system that this venue uses to get the work online. Tailor your process to lower the friction between the artefact you create and the process that will be used to get it online. 

The great failure of my industry in the face of the web has been to make allow this process to remain orders of magnitude harder than publishing a post on blogger or wordpress.  

I'll step through some advice covering these topics now. 


## The most appropriate venue

Ask your colleagues, confer with your coauthors, it's usually not hard to determine. A tool like the [Journal author name estimator](http://www.biosemantics.org/jane/) has been around for years and it can suggest a journal based on the text of your abstract. In addition the following resources can also help [Journal Finder](http://www.miketaylor.org.uk/tmp/journal-finder.html), [http://www.edanzediting.com/journal_selector](http://www.edanzediting.com/journal_selector), [http://www.journalguide.com/](http://www.journalguide.com/) and [http://etest.vbi.vt.edu/etblast3](http://etest.vbi.vt.edu/etblast3). Most of these are for the life sciecnes. 

If your publication is an OA publication the [Eigenfactor Journal Rank tool](http://www.eigenfactor.org/openaccess/index.php) will tell you if you are getting good value for money. This ranks cost of the article processing fee against a rank of the journal determined by their own algorithm. 

## Speed of publication

It might be worth checking if there is an alternative venue that might be a lot faster than your first choice. 

A common approach is to submit to a high profile journal, and on rejection submit to PLOS one. This is done in order to reduce the thrashing around within the peer review system. Perhaps consider submitting to PLOS one first? You could also look for a journal that is smaller, and might be more responsive. In the life sciences the journal I work for - [eLife](http://elife.elifesciences.org) - is both prestigious and fast. 

For the life sciences [Anna Sharman]() has a great resrouce for a selection of journals giving information about [decision times](http://www.sharmanedit.co.uk/resources/decision-times), [OA charges](http://www.sharmanedit.co.uk/resources/open-access-charges) and [journal metrics](http://www.sharmanedit.co.uk/resources/journal-metrics-spreadsheet). 

It might be interesting to encourage people attending your courses to contribute to these, or to create similar resources for their own disciplines. 

## Preprint servers / archives

Your discipline may have a discipline specific archive. Make sure a copy of your work is deposited there. If the full stext is deposited in one of these venues Google Scholar will be able to provide readers with a link to a full text version of your article - even if you have had to publish in a paywalled journal. 

Often you can get your work in draft up there before the peer review process is complete (if that's considered Kosher in your field). This can give you priority on an idea, even before the idea has been formally reviewed.  

- Physical sciences, astronomy, mathematics - [ArXiV](http://arxiv.org)  
- Biomedicine - [Pub Med Central](http://www.ncbi.nlm.nih.gov/pmc/)  
- Social Sciences - [Social Sciences Research Network](http://www.ssrn.com)   
- Economics - [Repec](http://repec.org)   
- High energy Physics - [inspirehep](http://inspirehep.net/?ln=en)

Also, check with your university library and find out what archives they run, deposit there for the same reasons as above. 

## The OA advantage

Keeping control of your own content is a significant advantage that authors can derive from publishing in an OA journal. I'll touch on that a bit later. 

There is another advantage, and that's the advantage of discoverability. 

Currently - as of writing this post, the Google main search bot does not index content that is behind an academic paywall for users who do not have access. That means if you publish at an non paywalled venue more people have a chance to find your content. 

Now most of your immediate peers will probably be able to access your content by virtue of having it in either the appropriate venue or in an appropriate repository, but it can't hurt to make it even easier to find. 

If your coauthors will not agree to publishing in an OA venue, you can always try to modify the copyright transfer agreement that the publishing company will ask you to sign. 

You can follow these examples to allow you to retain the right to distribute the paper in any way that you see fit. This is the one piece of advice that I'm giving that might slow down the process of publication, but go on, you know you want to do it, don't you? 

## What happens to my paper in a big publishing company, and why should I care?

During the reviewing stage a very badly formatted version of your article will be created to be sent to the reviewers of your article. If you have a preprint of your article available, that might even be an easier artefact for the reviewers to use, and it might speed up the review process, though I don't have any evidence to suggest that it will. 

If your manuscript is accepted for publication then it will be sent to a large typesetting company, where it will be digitally torn apart and converted to XML. All of the formatting that you do on figures, text and on the reference lists, will be thrown away. I'll just say that again. All of the work and hours you spend carefully formatting your reference lists will be ignored as the content goes through an automated typesetting system. (That's why at eLife we don't have a proscriptive requirement on the format of the references that we get sent, we will take them in any format). 

All of your specially chosen fonts, and special text alignment will be mostly ignored. 

Depending on the state of the manuscript and the quality of the language in the manuscript it may be checked by a copy editor, either for internal journal style, or for the quality of the language. Much of this work is undertaken by highly educated graduates in developing countries, particularly India, the Philippines and increasingly China - globalisation in action.  

Why is this? For the most part the systems that run our global publication infrastructure are old, many of them have code bases that are older than 20 years. Back in the day XML was the only reliable transfer format, and it remains the industry standard today. A slow evolution has been happening with the XML that publishers are using, and under the gentle pressure to deposit into PubMed and PubMedCentral most publishers and typesetters are starting to target one of the many dialects of the NLM DTD. This has become a de-facto standard in the industry, however no writing tools export natively to this format, and the DTD supports, and is designed for, archiving print material. One of the very many consequences of this is that code that is typeset in this DTD is usually typeset as dumb text. On the other hand it does allow a resource like PMC to archive millions of articles, from thousands of publishers, and provide a very fine grained search interface on top of all of this content. I'll mention writing tools a little later.

In order to potentially reduce the time to review your manuscript, and in order to reduce your the time your manuscript takes in the copy editing / typesetting process the following things could help:

- As mentioned -having a preprint version of your article available that the reviewer may know about, e.g. on the ArXiVe.
- If English is not your first language, have the manuscript proofed by a native speaking colleague, or pay to have the proofing done.
- Use a tool for managing your references, and don't sweat the formatting details. Tools you might consider using any of:

	- [bibtex](http://www.bibtex.org)
	- [mendeley](http://www.mendeley.com)
	- [zotero](http://www.zotero.org)
	- [papers](http://www.papersapp.com/mac/)

Remember, this is probably a lifestyle choice, my main advice is pick a tool that does not have too much lock in. I used to work at Mendeley and believe it to be as good as any tool out there. 

## But wait! I want to do iPython, interactive, open data, virtual machines, 3D printed DNA dinosaur replication and what you have just told me sound like like I can't do that - that sucks :( 

Yes, yes, it does suck, and I hear what you are saying, but remember, at the moment of publishing, your priority is to get the damn work published, and unfortunately that still means interacting with a system that has changed little since the late 17th century. There are moves in the right direction, oaises of sanity, but there is a long long way to go. 

If you feel really passionate about this then the best thing you can do is to keep the rights to your own work, get the paper out as a CC-BY paper in a boring old venue, and then do the kind of publication that you really want to on your own academic home page, and build your own audience around your work that way. In that case you want the boring route to take up as little time as possible.

You should also deposit artefacts of your paper in the best possible place for them. Code to a location like [github](github). Videos to [youtube](youtube) or [Vimeo](Vimeo). Images to [flickr](http://www.flickr.com). Data to [Figshare](http://figshare.com), [DataDryad](http://datadryad.org), [Zenodo](http://zenodo.org), or one of the very many other subject specific data repositories that may be appropriate for your field. 

Try and keep your artefacts well organised, and backed up off of your machine. You can back a lot up to github as part of a git repo, but that's not it's main use case. You can use a service like [EverNote](https://www.evernote.com), or get a licence for a research specific asset management tool like [Projects](http://www.digital-science.com/products/projects) or [LabArchives](http://www.labarchives.com).

The aim here is to reduce the friction in getting instances of these resources into the hands of others - if you believe that this is a critical part of doing research. 

It can also to make it possible to recover this informaiton in the instance of losing your main machine. (I decomissioned my main machine last summer via cup of coffee).

For the purposes of archiving your work you should also check with your institution and library to see if they can provide support or systems. Librarians in many institutions are mustard keen to help, as it provides a way for them to prove value to the academy in a world in which library subscriptions are under extreme pressure. You may find yourself with the problem of having too many options - which is not a bad problem at all.

# Authoring tools, and why does this all suck so much? 

I noticed that there was some discussion in the thread about collaborative tools for authoring. Again, I'll just stress, get the work published as soon as possible. This might mean sending a PDF of the article to a publishing house, or having to just send in a Word file.

On the other hand, there are a new generation of online tools emerging for writing, and also tools emerging for writing on the iPhone and iPad. I think we have more viable options now at our fingertips than at any time in the past. I don't believe that there are any serious contenders yet ready to oust the Word/LaTeX duopoly, but it would not hurt to take some of the following for a test drive to help with the authoring experience. It's too broad a topic to go into a detailed review of each one, I'll leave an investigation of these tools as an exercise for the interested reader. The list below is just a smaple, there are a bunch of others out there. 

- [writelatex](https://www.writelatex.com)  
- [sharelatex](https://www.sharelatex.com)  
- [fidus wrtiter](http://fiduswriter.org)  
- [google docs/drive](http://www.google.com/drive/)  
- [panodc](http://johnmacfarlane.net/pandoc/)
- [scholarly markdown](http://blog.martinfenner.org/2013/06/17/what-is-scholarly-markdown/)
- [authorea](https://www.authorea.com)
- [WriteRoom](http://www.hogbaysoftware.com/products/writeroom) (iOS/Mac)
- [nvALT](http://brettterpstra.com/projects/nvalt/)  
- [drafts](http://agiletortoise.com/drafts/) (iOS)  
- [Vesper](http://vesperapp.co) (iOS)  

The tool that I see emerging at some time on the horizon, and that I have a lot of excitement for, is the work on the [substance reader and composer](http://about.substance.io) and [eLife lens](http://lens.elifesciences.org). What's really nice about this is that to get started you can import NLM XML directly, or markdown via panodoc. It does a great job of separating the view, logic and control of the writing experience, and so it should also be possible to write directly in browser, and export to a publication ready format directly - but some work remains. 
	
In my own ideal world you can submit an idea to a journal as part of a pull request to the publication, peer review takes place in some system similar to how we do code review today. On acceptance the full digital artefact is published instantly. The writing and collaboration happens in almost any tool that the user likes, modifications are synced via something like dropbox. In this world writing tools support offline, as well as online modes, and content logic and views can be assembled independantly. In my ideal world the source is open. We are a little bit away from that at the moment, but there is no doubt in my mind that we are moving in that direction. [this great post by plos] has some great insights discussing what the native format for publihsing on the web should be. 

# About this post.

As we are discussing publishing on the web, I thought it might be useful to describe the tools I used to write this post. The body of the text is stored on my machine as a plain text file, and I store all of these in one directory using [nvALT](http://brettterpstra.com/projects/nvalt/) to manage them. This directory is also held under a Dropbox account, and I can access the content from my iPhone through a variety of editors, but in this case I didn't use any of these. 

For writing this post I used WriteRoom for mac in distraction free mode. I often use [SublimeText](http://www.sublimetext.com) in distraction free mode too. For some shortcuts in formatting I used [TextExpander](http://smilesoftware.com/TextExpander/index.html). To format the links I write the post in markdown, and did the formatting in SublimeText. I previewed the post using [Marked](http://marked2app.com). I also used Marked to verify that all of the links were working, at the time of writing. In order to publish the post on my blog I posted it directly into a github repo using [github pages](http://pages.github.com) to render the content. You can see the result at ... . I used the [GrabLinks](http://brettterpstra.com/2013/07/04/grablinks-bookmarklet-2-dot-0/) bookmarklet to gather all of the links from this post to add in as a resources list at the end of this post. 

# Final thoughts

I realise that I have mostly been answering the question about what shlould people know about the world as it is now, and not so much about what tools or approahces we should advocate to make the world a better place, but I hope that we can have a clear view on what is bad, so that this can help people make pragmatic decisions about how to change things for the better. 

# resources

- [github](http://partiallyattended.com/2014/01/08/advice-on-publishing-online/)
- [Journal author name estimator](http://www.biosemantics.org/jane/)
- [Journal Finder](http://www.miketaylor.org.uk/tmp/journal-finder.html)
- [http://www.edanzediting.com/journal_selector](http://www.edanzediting.com/journal_selector)
- [http://www.journalguide.com/](http://www.journalguide.com/)
- [http://etest.vbi.vt.edu/etblast3](http://etest.vbi.vt.edu/etblast3)
- [Eigenfactor Journal Rank tool](http://www.eigenfactor.org/openaccess/index.php)
- [eLife](http://elife.elifesciences.org/)
- [decision times](http://www.sharmanedit.co.uk/resources/decision-times)
- [OA charges](http://www.sharmanedit.co.uk/resources/open-access-charges)
- [journal metrics](http://www.sharmanedit.co.uk/resources/journal-metrics-spreadsheet)
- [ArXiV](http://arxiv.org/)
- [Pub Med Central](http://www.ncbi.nlm.nih.gov/pmc/)
- [Social Sciences Research Network](http://www.ssrn.com/)
- [Repec](http://repec.org/)
- [inspirehep](http://inspirehep.net/?ln=en)
- [bibtex](http://www.bibtex.org/)
- [mendeley](http://www.mendeley.com/)
- [zotero](http://www.zotero.org/)
- [papers](http://www.papersapp.com/mac/)
- [github](http://partiallyattended.com/2014/01/08/advice-on-publishing-online/github)
- [youtube](http://partiallyattended.com/2014/01/08/advice-on-publishing-online/youtube)
- [Vimeo](http://partiallyattended.com/2014/01/08/advice-on-publishing-online/Vimeo)
- [flickr](http://www.flickr.com/)
- [Figshare](http://figshare.com/)
- [DataDryad](http://datadryad.org/)
- [Zenodo](http://zenodo.org/)
- [EverNote](https://www.evernote.com/)
- [Projects](http://www.digital-science.com/products/projects)
- [LabArchives](http://www.labarchives.com/)
- [writelatex](https://www.writelatex.com/)
- [sharelatex](https://www.sharelatex.com/)
- [fidus wrtiter](http://fiduswriter.org/)
- [google docs/drive](http://www.google.com/drive/)
- [panodc](http://johnmacfarlane.net/pandoc/)
- [scholarly markdown](http://blog.martinfenner.org/2013/06/17/what-is-scholarly-markdown/)
- [authorea](https://www.authorea.com/)
- [WriteRoom](http://www.hogbaysoftware.com/products/writeroom)
- [nvALT](http://brettterpstra.com/projects/nvalt/)
- [drafts](http://agiletortoise.com/drafts/)
- [Vesper](http://vesperapp.co/)
- [substance reader and composer](http://about.substance.io/)
- [eLife lens](http://lens.elifesciences.org/)
- [SublimeText](http://www.sublimetext.com/)
- [TextExpander](http://smilesoftware.com/TextExpander/index.html)
- [Marked](http://marked2app.com/)
- [github pages](http://pages.github.com/)
- [GrabLinks](http://brettterpstra.com/2013/07/04/grablinks-bookmarklet-2-dot-0/)
