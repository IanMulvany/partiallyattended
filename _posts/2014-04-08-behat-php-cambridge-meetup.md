---
layout: post
title: Php user group March 2013 - BeHat.
categories: 
- php
- testing
- gherkin
- behat
---

# Background. 

On Monday the 31st of March I attended the [Cambridge PHP Meetup](http://www.meetup.com/phpcambridge/events/168024132/), the topic was BeHat testing. Johnathan Gough gave the talk.  

This is something we are getting started with in eLife. We have a few small tests in place, we have a few regressions on the site that we want to tackle, and we are looking to use it as a way of pinning down requirements from the company for new features that we want to roll out. After attending this talk I also found this great blog post on why BDD is [the world's most misunderstood collabroation tool](https://cucumber.pro/blog/2014/03/03/the-worlds-most-misunderstood-collaboration-tool.html).

# NOTES:

- lots of reasons to test
- some reasons not to
- it's suggested that TDD can be quite brittle
- BDD via BeHat is introduced as outside-in testing, a user story is introduced
- one should use behat with composer  

An interesting thing is that behat will create a /bin directory in the project directory. (I wonder whether that is something that can be set to system level, probably. (I would image that would be much nicer)).  

behat creates a `/features` directory.  

Behat lives in a universe of other tools, it sits on top of `Behat Context` and `Mink Context`. The `Behat Context` is a vanilla file in which you write your own context for how behat should interpret the tests. `Mink` provides web browser functionality. It can sit on top of  

- seleneum  
- goutte
- zombie  
- sahi   

If you are using a framework, you can fire up the framework, inject the request, and get the response out, and this kind of customisation is available to people writing their own contexts. An open question is whether one can mock up Drupal requests to insert into the manual contextual scripts. 

Mink exposes descriptive commands that you can use to describe how your web application should work.  

- Selenium: popular, multi-browser, js, slow  
- goutte: défaut, native PHP, fast, no javascript  
- sahi: multi-browser, js, slow, easier setup than selenium - maybe?  
- zombie: headless browser in js written in node.js   

You can specify at the level of an individual tests or scenarios as to which context that scenario should use (that sounds potentially really useful).   

Bottom line, Behat makes testing a lot easier, makes testing fun, and can be quite revolutionary. 


Questions:  
- how compliant is this user story language to the python/ruby equivalents - lettuce/cucumber
    the answer is they all use the same language - gherkin, so tests are cross system writable. 

- can one get to a level of creating these kinds of stories for extremely fine grained visual elements?  
	the answer to this is how do you get the balance between brittle tests, and tests that are too loose to
	be of use. If can do this, it might not be the best idea to do this.   
