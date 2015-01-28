---
layout: post
title: FuturePub Jan 2015 - Lens Next
categories: 
-  #LDNOpendrinks
- #FuturePub
- lens
- "elife lens"
- publishing 
- STM
- lens
- elife
---

On 2015-01-27 I gave one of the short talks at the FuturePub event. My slidedeck is [here](https://speakerdeck.com/ianmulvany/futurepub-jan-2015-lens). I wanted to give a quick update on where the Lens viewer for research articles is heading. Lens is a great platform for experimentation, and we have been iterating on some ideas towards the end of 2014 that have now made it into the 2.0 release. 

The main update is that Lens can now be configured to accept information from a 3rd party source and display that information in the right hand resources pane. Lens converts an XML version of a research article into JSON, and then renders the JSON in it's distinct two column layout. Up until now Lens was only able to get information from the article XML source file. We have added the ability for lens to check and API, and if there is a result returned, then Lens can be configured to show that information. As part of this you can define a new right-hand column for the specific source of information that you are interested in showing next to the article. 

Here you see a screenshot of an image with a related articles feed, and you can check out the [example](http://elife-static-web-host-test.s3-website-eu-west-1.amazonaws.com/future-pub-talk-jan-2015/lens-next-linked-article-examples/doc.html?url=https://s3.amazonaws.com/elife-cdn/elife-articles/03251/elife03251.xml).  

![related articles pane example](https://farm8.staticflickr.com/7403/16195259380_41af48db01_z_d.jpg)

Here you can see an example of version of Lens that taps into the altmetric.com API, and you can [play with the example](http://bit.ly/lens-alm-dist). 

![altmetrics pane example](https://farm8.staticflickr.com/7306/15762642783_f56e21424e_z_d.jpg) 

You can get started with this new version of Lens right now, and there is a starter repository with an example customisation ready to play with.  

In addition to this major change, there has been a big improvement to the way Lens handles mathematics (thanks to contributions from the American Mathematical Society), and there have been a number of other smaller improvements too. 

# Other speakers in the evening 

## Christopher Rabotin from Spahhro
	- they currently have 1.7 M pieces of content in the platform at the moment 
	- they are launching a publisher API, so that people can push content into their platform, and see usage of that data

I'm looking forward to seeing this, I'm very interested in seeing what usage eLife content gets out of this platform. 

## Kaveah - Rivervalley Technologies 

	- Kaveah demonstrates his XML end to end workflow
	
This tool has come along nicely since the last time I looked at it. This is definitely the future of the interaction between authors and production, but the big gap remains in getting the original manuscript into this form. There are some moves in that direction, people moving to tools like authorea and writelatex, there are a number of other typesetters offering this online proofing environment, it's an area of fairly rapid iteration at the moment, and I wish Kaveh good luck with this toolchain. 

## Scientific literacy tool - Keren Limor-Waisberg

This is a chrome extension that helps readers understand the context of the article that they are reading. You can check it out [here](http://www.literacytool.com). I'm going to take it for a spin over the next week. 

## Overleaf offline - Winston Li

This was technically the most impressive demonstration of the evening. A group of students have worked with Overleaf to connect it to git. You can now git clone your paper and work on it offline, and send a git push to update your online version. There are a few limitations, but this is a huge step for the product, and these students did it in about 3 months. What can you do with it? As Winston reminded us

> As Turing tells us, you can do anything that is computable, it's the command line!, it's git! 
