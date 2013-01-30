----
layout: post
title: ENCODE: an example of open publication and data integration.
categories: 
- publishing
- data
- open-access
- ENCODE
- threads
----

On Monday the 14th of January we met at the PLOS offices in Cambridge to hear a talk from [Euan Birney][eb] on lessons learned from publishing data rich publications though the [encode project][enc].

This was the first time that Euan was far less worried about the print, and far more worried about how well the online version was going to work. 


[eb]: http://genomeinformatician.blogspot.de/
[enc]: http://encodeproject.org/ENCODE/

## Dimensions of the project

- 5 TeraBases
- 1715 times the size of the Human Genome
- 3k experiments
- 410 authors on the main paper
- 6 high profile papers
- ~35 companion papers

The output should not be thought of as papers, but as the raw data. The organisation and display of that data required non-paper publication methods. 

## Publishing innovations

- Threads
- iPad app
- Interactive Figures
- Virtual Machine for making the data available 


### Threads

[Threads][th] are basically paragraph level tagging. It was built by creating a HTML5 app, and the core interactivity model is the same for the website and the iPad app. A big question in the mind of the authors was would this be useful. Would reading a paragraph and a figure from different papers be too incoherent without the overall narrative of a single paper? Euan was really excited when he talked to someone who had printed an entire thread, and she asked questions about the thread. He has had more people talking to him about their use of threads, over the number of people talking about interactive figures. 

One of the main points behind doing threads was to bring the companion papers together with the main papers. To make it work you needed to make all of the papers open access. This could just not be done without the papers being open access. The tagging was done by the authors, they created 13 word documents, and they copy and pasted and curated the threads into these word documents. (it sounds like the worst process in the world, but the reader doesn't care, to Euan this is just an implementation detail). They were never going to be in a position to get the different publishers to align their internal XML tagging processes so they went with the dumbest method that was guaranteed to work.


For Science, Nature etcetera, they needed to make a "Special Case" to make these papers open access to allow this to work. There is an opportunity for OA publishers to be able to say "this is just what we do". CC-BY makes the rights aspect of this trivial.

##### Some lessons  

- Could be supported by an open tagging and mash-up site.
- The tagging must be paragraph level, and not papers
- You need ownership of tags, at individual and group levels. You might possibly need to include hierarchies. 
- The two way nature of this is interesting, threads point to papers, papers to threads.
- The ordering of the tags is interesting. 
- A nice well executed site that scales in terms of UI is critical - what to do with thousands of threads?

This sounds like what [storify][stor] does for Tweets and Blogs. 

In this scenario, should one just be publishing at the level of paragraphs and tags? Euan feels that the paper provide an important narrative structure. 

It was a decision that the threads did not require independent review, as each atom within them had already been reviewed. 

People have started to cite the threads via the URL of the thread, however Nature did not ask for DOI's for the threads. (this would cause a problem for ISI and traditional citation counting practices). 

[th]: http://www.nature.com/encode/
[stor]: http://storify.com/


### Interactive figures

This was not the most successful part of the project. There needs to be more investment into the widget creation process. There needs to be more standardisation. 

There was a lot of back and forth between the coders and the academics and the publishers on the creation of the interactive figures, but what does this actually give you? "It sort of doesn't really change the world". There could be a lot more if you could click on a data point, and drill down on that point. The authors spent a large amount of time, and created some JavaScript prototypes, and these were then refined, but they didn't really get to a thing that they thought was useful. 

They tried to make every figure interactive, but they ran out of time, and perhaps lost a bit of focus around this. 

There needs to be an open library of JS with standard formats to go into the backed. 

[Biojs][bij] is a ground-up EBI widget group, something like this which is domain specific, targeted at specific standard data sets, could be more useful than doing custom visualisations. 

[bij]: http://www.biojs 

### Virtual machine

This is the ultimate materials and methods for computational papers. This is not a sophisticated thing to publish, it's just a big file. Euan is very proud of this as a scientist. It should be trivial to do from a publishing point of view. 

The only thing you have to worry about is the size of your supplementary file limits. Ideally one should deposit it before review, and allow reviewers to spin up for review.

The thing that has been most used have been the tarballs for each individual figures, rather than the VM of the entire machine. 

The biggest piece of computation can't be placed into a single VM, but they did put in one example pipeline (a bit like blue peter - here is one we did earlier).


### Data integration.

* Majority of structured databases have deposit during review
* A few systems allow reviewer accounts, but they are not much used. The VM concept might be a better approach. 
* BioStudy database is piece of re-factoring for all data types - a new project coming out of the EBI in 2013. 


### BioStudy

This is a new initiative from EBI as a way to allow the weaving of multiple data intensive studies together. Each will have it's own access number. These could be tied to individual papers, but not always. 


### Lessons

* This kind of approach only makes sense if it's Open Access. 
* The interactive figures will be harder to run if you have to make the data access hack proof.

At the outset, most people were interested in the interactive figures, the threads were known about, but not the main focus, however in the end the threads have been more successful. When they started curating threads they started out with about 26, these were collapsed down to 13 final threads. There was a balance between thin threads and thick threads, where you could think of a thin thread of being a hyper-focussed thread.



### Message

He now thinks that digital publishing is truly the future, and for open access publishers this kind of thing should be easy, but it is soul searching for closed access publishers.

This really highlights the difference between free to read and free to use. You can only do this when you are in the free to use domain. 

It has to be done generically, it can't be done in a publishing house kind of way, as the science is not published though just one publishing house.


