---
categories:
- aws
- amazon
- machine learning
- elife
- elife-bot
- storage
- conference
- london
date: 2015-04-16T00:00:00Z
title: aws london summit notes
url: /2015/04/16/aws-london-summit-notes/
---

# Amazon Web Summit London 2015

## Keynote  

There were about three thousand people at the summit. I chatted to a few people throughout the day. Their experience with AWS ranged from moderate use through to just being at the evaluation stage.

The keynote highlighted AWS's approach of wanting to put the customer in control, and to remove all unnecessary work from the customer in terms of managing IT.

AWS has grown enormously, they are estimated to have five times the compute power on hand than all other cloud providers combined. They have over one million active customers, and many of their services have more than doubled in terms of usage in just the last year alone.

Most of the keynote was given over to hammering home this message and to having companies that use AWS services come up and talk about their usage.

There were two products discussed in the keynote that piqued my interest.

## Elastic File Storage

AWS now offers an NFS service. When hearing this my thought is that this might be able to replace our NFS box in the office. I went to a session on this later in the day, and it needs a bit more investigation.

## Amazon Machine Learning

AWS now provides a simple console for creating machine learning models. What is nice about the service is that once you have trained your model you can choose to either put it into a data processing pipeline, or you can create a REST endpoint that can act as a decision endpoint.

We don't have any use cases for this at eLife right now, but there are somethings that might be fun to experiment with:

### Picking papers that need an insight

We have a collection of papers that received insights, and we have a collection of papers that don't have any insights. We could use this training data to see if we can build a model that can predict whether a new paper might get an insight. This might provide a way to give support to the human curation process of picking papers that get insights by pointing to new papers that have insight-like characteristics.

### Predicting highly read papers

We could feed reading data about papers with author, paper or institution data to see if we can predict which of our papers might be read widely in the future based on any features of the papers that we can identify. This might give our marcomms team advance warning about papers that might be worth investing attention in.

### Predicting whether a paper will get accepted or rejected

Since we have accepted and rejected manuscripts we could use this information to create an acceptance model. The hope would of course be that this model will be useless, and that only full proper peer review can do the job of deciding whether a paper can be accepted or rejected. It would be interesting to see if that null hypothesis holds, or whether we might uncover any bias in acceptance.

An interesting side effect of attempting to create these models might be the creation of a requirement for the kinds of API endpoints that we might like to be able to  make available to access eLife content, in order to hit this machine learning service.

# Other thoughts from the Keynote

It's increasingly common to have a pattern where state information about the system is coming from many different sources, whether that be information about user behaviour, inventory or resources. In this world how one manages ones single source of truth becomes an interesting question. It seemed like some companies are using Amazon Redshift to manage this issue.

# Sessions

After lunch I managed to get to three sessions.

## Amazon Container Service

This is a service for hosting docker containers, and deploying them in an efficient way across a cluster of Ec2 instances. The container service is responsible for ensuring efficient allocation of resources is taking place, and it can provide a monitoring and control layer for your containers deployed at massive scale. The requirement is that you have to build your Ec2 instances with an AMI that supports the Docker protocol. You can use a schedular provided by Amazon, or you can use your own scheduler which understands you business needs.

A philosophy behind using containers is that instead of patching software in production, you get to a point where you development pipeline outputs new containers, that are versioned, and you never patch software in a production environment, you just swap in a new container, making it easier to go back to an old container if you need to.

The main AWS talk on this topic was mediocre, and mainly just a product pitch, but after the head of automation from Hailo talked about how they had adopted this service. For me the most interesting thing from his talk was how he described their move to a micro-services architecture. They run about 200 independent services at any point in time. He didn't go into detail, but he described how each service gets deployed in a way that automatically provide entry points to the developer for logging, AB testing and test coverage. That means the application developer can spend most of their time working on the business logic.

It got me thinking about our [elife-bot](https://github.com/elifesciences/elife-bot). Our elife-bot has a master controller in the [cron.py](https://github.com/elifesciences/elife-bot/blob/master/cron.py) part of the bot. Also, each of the components are tightly coupled by being in the same codebase, and by having coupling via the [SWF](http://aws.amazon.com/swf/) task queues.  If elife-bot were truly micro-services architected, then we would be able to deploy an update to any single task on our processing pipeline without affecting in any way any of the other processes, other than via the data that gets passed from one process to another. At the moment all of these process are deployed in the same repo to the same Ec2 instance. I'd like to see us move to a situation where they are more separated than they are now.

In the Q&A the advice on how to do this came down to seeking a component of your system that can be removed with low risk from your system and put that in to a container.

Another approach is to look at using  the Amazon Lambda service, and I happened to go to that as my next session.

## Amazon Lambda

I went into this session with a skeptical frame of mind. Lambda allows you to put code into lambda, and that code is run when a certain event happens. You can trigger these events via a number of routes, including changes to an S3 bucket, or modifications of a DynamoDB table. You can get other AWS services to trigger a lambda function by getting cloudtrail to log to an S3 bucket, and have that bucket trigger the lambda function (I would expect native support for other services to be released in due course).

What is interesting is that you only get charged per 100ms that your function is running, so you don't have to pay for an Ec2 instance to be up and idly waiting for an event to come along if that event can be sent to a lambda function.

There are some constraints, lambda functions only run on a basic AWS Ec2 instance, and if your function takes longer than 60s to run it will get terminated.

In spite of those limits, most event driven publishing workflows could be modelled fairly well using the lambda service, and it could lead to q responsive low cost service.

The speaker in this session was excellent, and he outlined some really compelling use cases for lambda. One that caught my eye was the one of [creating thumbnail images](http://alestic.com/2014/11/aws-lambda-cli). An image file hits an s3 bucket and that could automatically trigger the creation of a thumbnail of that image, and the population of another s3 bucket with that thumbnail.

When I first heard about lambda as a service I was quite against it, as I thought that is seemed to be just a bit too much magic, and it seemed to be a service that would be hard to move away from. I mentioned my concern to someone at the summit, and their response was that "it's just running an event driven node.js service, I could set that up myself without too much difficulty". So it seems my fears of lock-in are a little overblown. Yes, it would take a bit of work to extract oneself from lambda, but no, it wouldn't be impossible, though it would likely lead to a cost increase.

Given what I saw in this presentation, and given some further thinking on lambda, I'd probably be quite willing to try it out now.

## Elastic File Store

The next session I went to was on a brand new service from Amazon - Elastic File Store. This is basically a NAS that can be attached to VPC. The presentation was OK. I cam out wondering whether one could connect to this NAS system from outside of an AWS VPC, i.e. from a local computer in the office. We have a use case for that at eLife, and I was unable to determine whether we could do that from the presentation. I think the thing here is to sign up for the preview service in order to find out more.


## Deep dive in the aws-cli

The last presentation that I attended was a deep dive into the aws-cli. It was a great presentation, and the most hands on of the day. The aws command line interface supports querying json output using the [jmespath](http://jmespath.org/tutorial.html) syntax. I'd not heard of this before, but it looks amazing, and it comes with a terminal tool that can be used to explore JSON output which can be pipped into the tool. You can get the terminal tool via

	> $ pip install jmespath-terminal

On of the other neat features of aws-cli is that you can pass a JSON config file for fine grained configuration of an AWS service, and the cli tool will also [generate a skeleton JSON](http://docs.aws.amazon.com/cli/latest/userguide/generate-cli-skeleton.html) input file for your given service on request.

# Final thoughts

I came away from the summit wanting to explore and learn more about the following services:

- Amazon Redshift
- DyanmoDB  
- Lambda
- Elastic File Store
- Amazon Machine Learning
