---
layout: post
title: mini-review of "Measuring the User Experience on a Large Scale"
categories:
- paper
- user experience
- data
- google
---

[Measuring the User Experience on a Large Scale:
User-Centered Metrics for Web Applications][paper] by Kerry Rodden, Hilary Hutchinson, and Xin Fu

Rodden, Hutchinson and Fu describe [a framework for measuring the user experience of web apps through mining server logs][paper]. Since they are based at Google one assumes that the framework that they are describing has been battle tested. 

They focus on metrics that measure user centric aspects of the online experience, in contrast to business centric (such as PULSE metrics: Page-views, Uptime, Latency, Seven day actives, Earnings). They maintain that the metrics they propose are better suited to products that have been launced, rather than being used in the design stage. They maintain that these metrics should be used in conjunction with other measures, such as direct user studies. 

They name their metrics HEART metrics: Happiness, Engagement, Adoption, Retention, and Task success. 

Happiness is measured through user surveys. An interesting insight is that the iGoogle team introduced a new design, and saw a drop in happiness scores with the design, but these improved over time, indicating that the initial drop was due to change aversion. They measure this score weekly through in-app surveys that can be deployed at scale, and so they have a historic record of user happiness.

Engagement is some activity per volume of users, such as average number of visits or actions per user over a time frame. This is best reported on an average per user basis.

Adoption and retention are rather self-evident metrics. 

Task success seems more problematic to track, as one needs to set up the metric around task success beforehand, and then A/B test a set of potential variable scenarios. 

Overall this is a nice little paper that articulates well the challenges around understanding user interaction with one's site. The clear challenge remains deciding what one's goals are, and then coming to an agreement about what the signals are that can be tracked that will inform you about whether your goals are being met. 

[paper]: http://www.mendeley.com/research/measuring-user-experience-large-scale-usercentered-metrics-web-applications/
