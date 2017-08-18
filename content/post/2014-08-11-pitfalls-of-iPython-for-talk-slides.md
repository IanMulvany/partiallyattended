---
categories:
- iPython
- iPython notebook
- python
- slides
- reveal.js
- talks
- wikimania2014
date: 2014-08-11T00:00:00Z
title: Some pittfalls in using iPython to generate talk slides
url: /2014/08/11/pitfalls-of-iPython-for-talk-slides/
---

Yesterday I gave a talk using iPython notebook to generate the talk slides. You can get the [notebook on github](https://github.com/IanMulvany/wikimania-open-scholarship-tools), and you can 
see a [live version of the slides](http://www.mulvany.net/presentations/WikimaniaOpenScholarshipTalk.slides.html#/).

It succeeded in generating an artefact that was somewhat literate, in that the code and documentation are nicely woven together, 
so anyone who has the time can get to exactly the same point that I got to, with this repo, however there were also
a couple of problems that I ran into that make me feel that this is not yet ready for mainstream use, specifically: 

- While I was waiting for my talk to begin I had loaded the slides in Chrome. The chrome window crashed just before I started
the slideshow, and I had to switch over to using Safari, right at the last moment.  
- I was using the `from IPython.display import HTML` function to show screenshots, none of the screenshots showed up during the 
presentation.   
- I didn't figure out how to hide cell input on slides where I would have prefered to only show the cell output. I've since 
found a [post](http://hannes-brt.github.io/blog/2013/08/11/ipython-slideshows-will-change-the-way-you-work/) that describes 
how to do this, but it was too late for me.  
- I'm used to laying out concepts using shapes in Keynote, there is nothing equivalent to that in this stack.  
- I failed to correctly convert my slides to PDF. I followed the docs from reveal.js, but it just didn't work for me.  


This system is probably a step up from using LaTeX to create slides, but I don't think it's ready for mass market use yet. I
had more success with this than with running a presenation from evernote, which I tried earlier in the year, but I'm unlikley to 
use this again in the near future. 

I think if you were creating a very code-tutorial driven presentation then this would be a reasonable tool to consider using. 


