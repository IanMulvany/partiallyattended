---
title: thoughts on GetFTR 
url: 2019/12/11/thoughts_on_GetFTR_/
date: 2019-12-11T00:00:00Z
categories:
- getftr
- wtfgetftwt
- access
- saml
- publishing
- libraries
---

### what does it do? 

By using a single sign-on system (like SAML, or OAuth) a researcher can have their browser remember who they are. Today most access to subscription content is done via IP authentication. A university pays a publisher to access the content that the publisher hosts, and the university sends over a list of the IP ranges that cover the university buildings. Any researcher on campus just gets access. The big problem is that when you are off campus that doesn’t work any more. 

If researchers log in to the publisher site via a university authenticated single sign on system, then the browser can remember that the researcher has access to the content, on their behalf.  This allows the researcher to get access to the publisher site, even when they are off campus. (It also allows the publisher to have a much better understanding of who is accessing their content). 

That’s the key idea behind ”seamlessaccess.org”, but there could be concerns about the publisher now knowing who the researcher is. 

So far, so good, but what does GetFTR do that’s different. As I understand it, from reading what’s on the GetFTR site, GetFTR has an API and when any website that shows a DOI on it wants to, that website can send a request to this API with the DOI, and if the website has it, it can also send information about the institution from where the request is coming. Now rather than the identification of the university being any old identifying string, it needs to be one backed by a single sign on system, like SAML. The API will then send  some information back that can allow the website to create a ”WAYFless URL”. That lest the person clicking the link get directly to the content without having to go through the payday. Now GetFTR have said that they don’t need or receive any user specific information, they just need the institutional authentication. 

OK, so what is the difference, for the user, between seamlessaccess and GetFTR? I _think_ that the difference is the following - with seamless access you the user have to log in to the publisher site. With GetFTR if you are providing pages that contain DOIs (like on a discovery service) to your researchers, you can give them links they can click on that have been setup to get those users direct access to the content. That means as a researcher, so long as the discovery service has you as an authenticated user, you don’t need to even think about logins, or publisher access credentials. 

On the other hand, the links that you are being presented are now determined by the publisher. 

If you are on campus, and your institution has access to the publisher site, then the end result should be indistinguishable  from just clicking on the DOI and getting a redirect to the publisher site (unless the publisher decides to stop supporting IP authentication, and maybe that is a long term goal of this initiative, but who knows ¯\_(ツ)_/¯). 

If you are off campus the experience could be different for paywalled journals, in that if you are logged in to your discovery service you should now get links that will work for you without you needing to log in to specific publisher sites, whereas just clicking on the DOI won’t necesscarily get you that access. 

How about using unpaywall, the open access button, or some other browser extension for finding alternative links for that article that you need (like links to repository versions, for example?). Well the good folks behind GetFTR _could_ also provide those links if they were to wrap around the unpaywall API, for example, but what will happen is that some publishers will have the idea of wanting to provide researchers with some form of bronze version of the article, perhaps through platforms that restrict the ability of the researcher to copy and paste form the text, or to share onwardly, all presumable with the aims of being able to “count” usage while at the same time reducing the surface area from which content can “leak” from the publisher site. In a world in which contracts with university libraries is focussed on data like COUNTER usage, then this is a perfectly reasonable concern from publishers, however the choices that publisher make about how to present “alternative” versions to reachers is going to vary. 

One example of how this could suck, lets imagine that there is a very usable green OA version of an article, but the publisher wants to push me to using some “e-reader limited functionality version” that requires an account registration, or god forbid a browser exertion, or desktop app. If the publisher shows only this limited utility version, and not the green version, well that sucks. 

OK, so that’s my understanding of what GetFTR does (if I’m wrong, then I hope I’ll get corrected quickly. 



### why is it doing that? 

OK, so, I’ve covered what it does, but why are the big five doing this? Weeeeeellllll. It’s not totally clear, but the elephant in the room is sci-hub - the website where everyone in the world can go and get an illegal copy of any research article. That combined with the economic system of value exchange in scholarly publishing, probably gives sufficient motivation for publishers to create this service. 

I think there are two things that make it possible for sci-hub to be possible. 

The first is there is a huge fragmentation of publishers in the world, and the user experience of navigating all of these sites, and systems is a pain. There is no one clear unified experience for interacting with the scholarly research, and in the googlified world we live in, that just does not gel with the kind of experience that people want, so to start with sci-hub just provides a better user experience (I’m told, I’ve actually only used sci-hub once, and I found it a pain to use back then). 

The second thing that makes sci-hub possible is a combination of IP access (no-authentication access) along with weak on-campus security for researcher logins. That allows sci-hub to attack researcher accounts to enable them to scrape all of the content that they put on their servers. 

A service like GetFTR kind of targets both of the above. 

The motivation is probably mostly to try to get the industry on board to try to get beyond IP authentication, and to allow publishers to “count” usage so that the “usage” numbers they present to libraries look higher and allow them to justify either price rises or indeed, just simple renewals of contracts. 

I have to say, the moving beyond IP authentication is a really good idea for a whole host of security reasons, and it will indeed require a big shift across the whole industry, so if this initiative could be run in a way the builds trust amongst all parties, then that would be no small thing, and should be applauded. 


### what would make this succeed? 

So, in order for this to work for a cohort of researchers, every place that they look for research will need to be to implement calls to this API, and will need to have information about that researchers authenticated access to their universities. 

That sounds like a tall order, but there are some services, and pieces of infrastructure, that have wide deployment footprints in the world, so if you can convince them to implement this, then maybe you get to a critical mass. 

Oh, you also need all the publishers to implement this too, and for publishers to do this, then they are going to need to be provided with a very low cost, turn-key solution to be able to implement it. 

To keep a service like this running, I would expect that you would want to have a small dedicated team (maybe 5 — 10 people), and support a reasonable volume of API queries, with a good response rate. I’d benchmark the cost of running this service to be on the order of a few hundred thousand dollars. With maybe 14k publishers in the world, then the cost of joining this service should be on the order of a few thousand dollars per year, not withstanding the cost of implementation and integration. That seems like a reasonable ball park. 


### what would make this fail? 

I’ve not done anything like a full analysis on this, in terms of looking at a lean canvas and trying to tease out the riskiest assumptions around the sustainability of this service, but the one thing that sticks out that could make this fail is lack of researcher adoption. If researchers use different discovery systems, and they don’t see these links everywhere, then they may just fall back to using a behavioural route that works everywhere. (That’s a totally untested hypothesis on my part, and indeed, the very reasonableness of it means that it should be tested). 

Contributing to lack of adoption could be if GetFTR is complex or costly for institutions and publishers to implement. 


### what would make this irrelevant? 

If publishing moves to being fully OA then this service is irrelevant. 


### what are the concerns that we might think about with this, and do they hold water? 

OK, hold on to your hats, this is where we get into tin-foil hat territory. 


### Will google scholar implement this, will other discovery services do so? 

Well, that’s a question. I suppose that publishers could coerce GS to implement this by threatening to rescind access to their full text, but would they really want to take the hit to their traffic? I don’t see that as being worth the risk. GS is a small team, if all publishers were implementing this, they might join in, they might not, they have their own effort to try to solve this for users. 

Someone on twitter way saying the the big five could coerce discovery services to implement this through contractual enforcement. If the system is easy enough to implement and truly adds value, then you should not need to enforce implementation, and if it is not/does not, then enforced implementation is not where your key problems are with this service. 


#### concern - this could replace crossref 

This was my first thought when I head about it, and joined up this with some of the comments that were reported from Crossref Live. The thinking is that is this a way for publishers to provide a routing system independent of the handle system that corssref redirects are based off of? Well, yes it does do that, however the entire service depends on DOIs, so while it could replace some of the existing infrastructure, it as the same time remains dependant on the existing infrastructure. I can appreciate that to move fast sometimes its good to just get on and do things, but I would advocate that if this service were to become a true replacement for IP authentication then it should hand governance over to someone like NISO or some other independent body. 


#### concern - this could kill green OA 

As I mentioned earlier, this could enable publishers to decide to provide links to restricted access, but free to read, versions of articles, in place of GreenOA. I don’t think this is going to be a big concern for two reasons. The first is that not all publishers will be able to do this, and secondly the motivation to deposit into institutional repositories is not currently driven by usage data from those repositories, but rather from mandates from funders, who are unlikely to be influenced by this service in how they decide to modify their mandates in the future. 


#### concern - this could leak proprietary publisher information 

OK, so I’m not sure how the API is provisioned, but I am assuming that it is provisioned by a single end point. Who owns that endpoint and the logged data that this endpoint collects? That endpoint will have information about what resources different publishers have provided to institutions, combined with usage data from those institutions. If I am publisher A and have a journal close to that from publisher B, but that is “lower tier”, then if I could access usage data from publisher B I could modify my sales price. How am I going to be sure that my own usage data does not leak to other publishers signed up to this service? 


#### concern - this does no look like the kind of initiative that a publisher who is on a transformative journey to Open Access would invest in. 

If I am sitting in the European Commission or in JISC I am probably not going to look at this initiative as something that proves publishers are on a journey to becoming open access. I think GetFTR do need to make clear what the overall benefits to the scholarly ecosystem are with this initiative, because at the moment the information on their FAQ seems to mostly support the creation of publisher value. 


#### concern - this will allow publishers to track users, and behaviourally target them. 

If the users are now logging in to some service directly, won’t this mean that the publisher can now track that person directly? Actually GetFTR explicitly states that they don’t get any information about the user, and given that this needs to be implemented server side, then there are actually fewer potential security concerns compared to using a browser plugin based solution. 


### What do I think about it all? What are my recommendations? 

I don’t really know yet. Doing anything is hard, doing so in coordination amongst large competitors is even more so, so the team behind this should be recognised for having put tougher a well executed initial proposal for how to move on access management. 

I think if you are a researcher I would recommend continuing to use a bag of tools to get access to your research. For the interim this will only be a partial solution. 

If you are a publisher I would recommend calculating cost of implementation, time to implement against expectations around how much additional usage it is going to give you, and how much revenue that is going to translate to. Basically I would advocate using a cost of deals analysis on whether to implement this or now. 

I have two other recommendations for the GetFTR team. Both relate to building trust. First up, don’t list orgs as being on an advisory board, when they are not. Secondly it would be great to learn about the team behind the creation of the Service. At the moment its all very anonymous. 


### Links that I referred to when putting this together. 

[Seamless Access Description - GN4-3 Work Package 5 - GÉANT federated confluence](https://wiki.geant.org/display/gn43wp5/Seamless+Access+Description). 

[GitHub - TheIdentitySelector/thiss-js: The identity selector software source](https://github.com/TheIdentitySelector/thiss-js). 

[Welcome to The Identity Selector Service’s documentation! — The Identity Selector Service 1.0.0 documentation](https://thiss-js.readthedocs.io/en/latest/). 

[Publishers going-it-alone (for now?) with GetFTR | Disruptive Library Technology Jester](https://dltj.org/article/publishers-alone-with-getftr/)   

[Welcome to SeamlessAccess.org | SA Site](https://seamlessaccess.org)

https://www.getfulltextresearch.com/faqs/

https://scholarlykitchen.sspnet.org/2019/12/10/why-are-librarians-concerned-about-getftr/

[Get To Fulltext Ourselves, Not GetFTR. - openaccessbutton](https://blog.openaccessbutton.org/get-to-fulltext-ourselves-not-getftr-e952e798564b)




