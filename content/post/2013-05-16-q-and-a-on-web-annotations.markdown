---
categories:
- annotation
- open annotation
- iannotate
- elife
date: 2013-05-16T00:00:00Z
title: Some Thoughts on web scale annotation.
url: /2013/05/16/q-and-a-on-web-annotations/
---

[Mark Ware][mw] recently asked me some questions about the state of web scale annotation, based on my impressions from the recent [iannotate][ianno] conference (at which I gave a short talk on the idea of [research threads][rt])

[mw]: http://www.markwareconsulting.com/
[ianno]: http://iannotate.org/
[rt]: https://www.youtube.com/watch?v=PI-Xek9M2gU  


What is the eLife view of annotation systems? 

> We like the fact that there is now a W3C standard for Open Annotations (OA). We are encouraged that so many projects out there are looking to make their annotations interoperable with this standard.

Are you planning to support open annotation on the eLife site?

> We implemented discussion using Disqus, and we are happy with that so far, but we are looking at (OA) for some other potential products. If there were a way to make other annotations from other sources apparent
to our readers on our article pages we would definitely look into supporting that. We have been looking at some of the work of the [open citations project][ocp] , and my understanding is that there is a move to make data from this project available under the OA framework.

[ocp]: http://opencitations.wordpress.com/


If so, which platform would you use, Hypothes.is or something else?

> We would probably use Hypothes.is, [Domeo][dom] or [annotator][ano], but it would come down to the pros and cons when it got to the point of implementation. We need to look at all of these tools more closely, but all three of these tools are excellent.

Do you see open annotation as offering something distinctively
different from earlier commenting approaches, which (I think) have had
rather limited success?

> Yes. Two things mainly:

> 1) many tools are looking to make their data cross functional through the OA W3C spec, that could be huge if many academic players adopt tools that support this. Think of like being RSS for scientific assertions, that would just be huge. It opens the door to all sorts of applications that simple RSS of comments don't support.

> 2) the ability to tie an activity to a specific location in the text. Though frequency of annotation may not be higher than commenting, location specific activity is intrinsically more valuable, being able to see quickly, for example, the location of a paper that has interested the most people. In addition this framework is ideally suited to making machine learning runs over the literature connect well to the human reading experience.

How critical is the reputation management part? Hypothes.is have
made a big deal of this, with a workshop last year and a lot of
reputation experts in their advisers, but I wonder if it will add
unnecessary complexity for STM annotation? I think Hypothes.is see as
an important part of ensuring quality though?

> This was not the focus of the recent workshop, which was far more about implementing the underlying infrastructure of annotation. That said I personally think you can look at three broad use cases around annotation.

> Personal annotation (public or private). In this case reputation is not a concern.

> Public annotation as a signifier of activity. In this case you are looking that there is annotation, rather than looking at what the annotation says. In this case reputation is required only at the level of determining whether the annotation is span or not. We have a reasonable handle on how to deal with this in other web scale systems.

> Annotation as a guide to insight. In this case reputation is critically important, and it seems that the key is going to be making annotation systems interoperable, so that karma can flow from one system to another. It's a subtle issue, and one that we will need to address going forward. John Perry Barlow made the great point that information is not the same as knowledge and not the same as insight, and it is knowledge systems that we should be striving to create.

Do you have any concern about pseudonymous commenting at eLife?

> We do. We allow anonymous comments on eLife, but only where the commenter has explained who they are, and justified why their comment should be anonymous. In terms of pseudonymous commenting, this is something I am less worried about in the academic sphere, as name, identity reputation and prestige are so deeply linked. Were one academic to impersonate another I feel that this would be uncovered very quickly. In the few cases where there has been high profile sock puppetry there is usually a fairly clear smell around the topic area.

Are there any concerns about long term preservation of annotations
alongside the original article, i.e. is there any danger of them not
being as robustly preserved as journal content (e.g. with dark
archives etc.) and/or getting separated from the content?

> This is a subtle question. It's not clear that you want all comments available all the time. A new student might be better served by the text being presented as a blank slate (something that rapgenius is not yet able to do). On the other end, were we to be able to see every annotation that had ever been made on the the bible, the annotation corpus would significantly outweigh the underlying corpus. Perhaps our systems will need to be able to selectively forget, or fumble the information? I'm not sure.

> In terms of preservation, this is something that came up in the talk and was mooted as one of the fundamental "Hilbert problems" for the annotation community. Other people felt that the majority use cases were going to be personal. I think it is fair to say that there are indeed concerns, but how those concerns break down is not clear, and what we do about them is also not clear.

> One of the deep insights in the conference was that we have not created a web, but rather a directed graph. The architecture of the internet does not allow resources to know what other resources are saying about them, or what other resources are pointing at them. Perhaps this is the problem that annotation can solve?







