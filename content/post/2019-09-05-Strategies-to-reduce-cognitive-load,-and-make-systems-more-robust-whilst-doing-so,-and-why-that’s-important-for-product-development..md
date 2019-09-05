---
title: Strategies to reduce cognitive load, and make systems more robust whilst doing so, and why that’s important for product development. 
url: 2019/09/05/Strategies_to_reduce_cognitive_load,_and_make_systems_more_robust_whilst_doing_so,_and_why_that’s_important_for_product_development._/
date: 2019-09-05T00:00:00Z
categories:
- bcm
- engineering
- toil
- cognitive-load
- product-development
- microservices
---

At my current company we are looking at strategies for improving the resilience of our core systems, and looking at the issue of disaster recovery from a broad perspective. This comes under the heading `business continuity management`. 

From a product development perspective these considerations are also important. 

For successful products / product organisations consider these two perspectives:

- Most new business value that we create from innovation projects  comes from improvements or iterations to existing products over the creation of totally new products (from an evolutionary perspective this makes sense, products or services that are already making revenue have proved they they have an environmental fitness function that works, whereas new products are like genetic modifications, the vast majority of which lead towards extinct endpoints. When you find an entirely new nice to exploit, or when the environment changes rapidly enough hat existing products are no longer sufficient, then radially new ideas can be hugely profitable, but for the most part, most of what we do is incremental and iterative, and this is mostly fine.). 

* We often underestimate the effort involved in maintenance and upkeep of new services. There can be an excitement about building something new, but budgeting for the maintenance and upkeep of the service or product is something that can get overlooked. 

OK, but what does business continuity management have to do with either of these perspectives? Well there is one aspect that I want to touch on today that can effect team continuity and project velocity and that is the issue of cognitive load. In both of the above scenarios what can help is finding ways to enable the team to move quickly, or at least to reduce the risk of making moves. 

When making iterations to existing products, being able to do so without breaking things is helpful.

When looking to reduce the burden of ongoing maintenance for new services, finding ways to make those services robust from the get go can be helpful. 

From a `BCM` perspective one of the biggest risks for software systems that we have built and maintain ourselves is the risk of losing implicit knowledge about the project when staff leave or when the project is handed over to other parts of the organisation, or where management for the service is outsources. 

Recently I’ve read some excellent posts about reducing the cognitive load of developing systems. 

In https://techbeacon.com/app-dev-testing/forget-monoliths-vs-microservices-cognitive-load-what-matters Matthew Skelton and Manuel Pais explain why cognitive load is the right framework for thinking about the complexity of our systems, and that this thinning transcends the debate over monoliths vs micro services. They recommend working towards reducing the **intrinsic** cognitive load of systems, e.g. through good choice of systems. You should eliminate **extrinsic** cognitive load e.g. by automatic the boring tasks. This then leaves space for what they describe as **germane** cognitive load - the space to think about how to solve the business problems that your software should be solving. They also have a very nice description of how to configure teams to improve the interaction patterns between teams. 

In [Day 3: Managing Cognitive Load for Team Learning – 12 Devs of Xmas](https://12devsofxmas.co.uk/2015/12/day-3-managing-cognitive-load-for-team-learning/) Jo Pearce describes the value of comments, applied appropriately, as well as the role that code review can play. 

In terms of reducing extrinsic cognitive load a few other blog posts have come up recently that have some very nice approaches for this. Aspects of extrinsic cognitive load include having to remember how to access the servers that systems are running on, managing permissions, and situations where people are blocked getting access to systems when they should have access, configuring logging, configuring backups, and being able to quickly understand how to access those backups. 

In https://medium.com/ft-product-technology/documentation-day-how-the-ft-com-team-improved-our-documentation-to-95-usefulness-in-7-hours-b73d1a7e6f30 Jennifer Jonnson described how a team at the Financial Times used a hack day to improve the documentation of their projects. They built up a system where key documentation lived in the project software repository, and got pulled from those repositories into a central documentation store automatically. In this way the documentation lives near to the software, and at the same time a cereal location is created where people can see documentation across all the projects, but done so in an automated way! This documentation includes the run books and the ops information, critical pieces of information for systems maintenance. 

In [Repository Driven Development | Findmypast Tech](https://tech.findmypast.com/repository-driven-development/) Neil Crawford describes how they use templates within their repositories that are used to wire services together. This requires building up some infrastructure for projects, but once that infrastructure is in place developers don’t have to think about things like logging or metrics, they just get them as part of their project configuration, and as there is consistency across all projects. 

One of my favourite tips that I’ve seen is the `do nothing scripting` approach described here: [Do-nothing scripting: the key to gradual automation – Dan Slimmon](https://blog.danslimmon.com/2019/07/15/do-nothing-scripting-the-key-to-gradual-automation/). The idea is that for boring repetitive tasks, instead of scripting them, start by writing proto-scripts that remind you of the steps you have to take. This helps to reduce error, and is the kind of thing that can be improved gradually over time. It’s a bit like taking a checklist approach to operations, a technique that is critical for airline safety. 

I found many of these links through following [Simon Willison (@simonw) on Twitter](https://twitter.com/simonw), and if you are interested in these kinds of topics I highly recommend following him too! 








