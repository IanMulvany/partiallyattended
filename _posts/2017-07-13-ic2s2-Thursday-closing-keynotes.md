# ic2s2 - Thursday, closing keynotes 

### Economic AI - Matt Taddy 

Economic AI breaks complex systemic questions into simple sets of prediction tasks, that can be attacked with off the shelf ML techniques. 

Today economists are being asked to answer basic economic questions but at a ridiculous scale (within companies like Microsoft or Amazon). There are just not enough economists out there to do all the work being asked of them. 

Applied economics can be done via experimentation (like A/B tests on pricing), but it can be expensive and lengthly to do, and the results still need a high level of sophistication to interpret. 

In applied econometrics the kinds of natural experiments that we might look for only occur in special settings. 

The claim here is that machine learning can automate and accelerate tasks in each of the described workflows. 

The state of econometrics won’t be improved, but the efficiency of the work will. 

In the beer sales example the data is messy, and using all the data provides a sample that is too undifferentiated, so we use a ML technique to cluster beers based on their text description. If you use naive machine learning you run into problems. Selecting the controls and also predicting the response based on those controls is hard. The answer is to use Orthogonal Machine Learning. 

The two things you want to know, prices and sales, are co-dependant on the of the variables. You can do prediction on these two things, and then take account of the regression between them. The two prediction problems are easy ML tasks. 

The key thing here is a causal question is being broken down into earlier machine learning tasks. 

Another area they are looking at is the area of instrumental variables. 

He now talks about using deep nets. Can be really useful when we have images of products. 

Deep learning is a good low development cost off the shelf ML. The next big gains in AI are coming from domain context. What we want to do is to break questions into the kinds of shapes that will fit well into the affordances of these cheap tools. 

In the Q&A there is a great question from Matt Jackson asking what the real benefit is for the economist that the ML system is doing. Very simply, previously an economist would have spent a lot of time building a model, including or excluding features. Machine learning just ploughs through the data and fits models that work, taking away the need to do that manual labour. 

### Learning to be nice, social norms as a result of adjusting expectation - Maria Pereda 

Maria describes the Dictator game, where one player can donate to another player. The receiving player has no agency. In these games when asking people about their expectations, they have expectations for reasonable levels of generosity. 

Expectations are a key factor in how people play. They want to understand the role of expectations in outcomes in the dictator game. 

There is a nice way to model the dynamics of how experiences and stimuli can modify actors in this game in terms of their expected behaviour. The developed a constraint to connect global aspirations with the stimuli that the players experience in the game. 

So in the network of players we might expect behaviour to head towards some equilibrium status. The randomly play this game with about 1000 players. 

They have compared the results of their simulations with the “expected” result from the literature. They also included imperfect decision making in the agents. 

They find that for low numbers of items to donate the simulation matches the model, but at higher numbers of items to donate the simulations match actual experiments with people better than the analytic model suggests. 

They can also introduce “inequity-averse” individuals (greedy people, who never donate more than half of the pie). Introducing these people makes the entire population a little bit more selfish. 

You can also introduce “free-riders” Just one free rider can destroy the social norm, and it makes everyone in the population really selfish (damn those nasty free-riders). 

They are engaged in an online pilot -[IBSEN](https://ibsen-h2020.eu), conducting large-scale experiments with about 23k volunteers (If you are in an associated lab you can [sign up here](https://participants.ibsen-h2020.eu/en/site/select-lab). 

### Matt Jackson - Folk Theories of Cyber-Social Systems: Understanding People’s Understanding 

The work he did with Facebook looked at how information spread through Facebook. The result of the study was highly controversial and Matt received about 1000 pieces of hate mail. They violated user expectations of what their newsfeed was. He did a text analysis on the respondents that he received. 

The reasons from users spread into a different class of responses:

* queries about the newsfeed being manipulated 
* the newsfeed is important 
* emotions are important 
* big data is personal 

The biggest theme that came through was about the sense of manipulation. 

They also looked at the reaction in the media for up to six months after the event. Most of the media’s response were emotional. 

Evan other academics who cited the studies tended to write is a personal way. 

Clearly they violated people’s expectation, as was the issue around expectations and the personal nature of the work. 

It got them thinking about what do people think about these systems, and this connected to his interest in folk theories. These theories are intuitive informal theories that people develop to explain systems that guide their behaviour. 

He gives a great example about how we create a “folk theory” about gravity. Few people can explain gravity, and yet we understand how to operate in a gravitational field. We don’t need to go into depth about these systems, it’s not about being dumb, we just need to know enough about them to work with them. 

Large social technical systems are complex, and yet people behave with them, and navigate their use, but we don’t really know what people think about these systems (like FB, online dating, Uber etc. etc.). 

Some people have done this through interviews (previous work has found the people don’t really think about the existence of algorithms in these systems). 

The work that Matt and his group took on started to look at the use of Metaphors. 

They have developed a “discover-identity-specify” (DIS) method. 

You need to discover the metaphors people use, then you reduce those into factors, and then look at the qualities of those factors. 

They used a [wiki-survey](https://www.allourideas.org) to find a way to enable users to generate metaphors in the system. 

They found a bunch of data, and got Facebook down to four factors. They also see four factors for twitter. 

You can find out how people feel about these factors. They found very similar results for the Facebook feed and for twitter. 

Matt is arguing that there are four folk theories about social feeds, they are:

* rational assistant that works for me
* a transparent platform that is not manipulated
* unwanted observer - is prioritising the company 
* corporate black box - not sure how it works, it’s all on FB 

They looked at how strongly people hold different folk theories about the system, and you can compare those scores against platforms (twitter vs Facebook). 

(What’s interesting to me about the data presented is that the scores are close to each other for different platforms even if one platform is slightly ahead on one measure than another). 

Now they want to know:

* how does your folk theory affect your behaviour? 
* what will update your folk theory? 
* how are these theories stable across types of algorithms and over time? 
