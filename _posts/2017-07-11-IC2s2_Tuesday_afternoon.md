---
layout: post
title: IC2s2 Tuesday Afternoon Keynotes
categories:
- ic2s2
- computational socical science
- conference 
---


# IC2s2 Tuesday afternoon 
---
### Dashun Wang - Predictive Signals Behind Success

Dashun starts by talking about weather predictions, natural phenomena can be observed, modelled and predicted. Can success be measured modelled and predicted? Obviously Dashun thinks so, and we are gong to be looking at the result of a number of studies in this talk. 

###### Science of Science 

Aim is to build on top of the work of others, but add to it the massive data that we now have access to, along with the tools that we have developed. 

First question, is there a mechanistic model that can predict future citations of papers? There are three factors:

	* 	preferential attachment -> fitness
	* ageing -> immediacy 
	* novelty -> longevity 

You get to a formula that shows the future citation for any papers. What changes on a paper if the “scaled time“ for that paper.

Given this function you can give high resolution future prediction for that paper. 

Can we now look at patterns for careers as well? We can look at the best paper for a person’s career. His work shows that your “best” paper can arrive at any time in your career. This is based on looking at the random impact rule. 

There is a Matthew effect. Does the location of your biggest work affect where your second biggest work is? If we know where your biggest work is then your next biggest is gong to be close to your biggest. This is sometimes called the “Hot Hand” period. This pattern can appear randomly in your career. Most people have one of these, and it usually lasts 4 to 5 years. 

Your google scholar profile is highly affected by whether or not a scholar has experienced this hot and period. 

### diffusion and adoption of technology 

He is talking about how many things we talk about as adoption of technology is substitution. Not everything is, but many things are. 

What do systems driven by substitution look like? 

Many of these systems follow power law growth. 

The model for future growth is also captured by three parameters, which look a lot like the parameters from citation analysis. 

---

## Ulrik Brandes - The Space of All Centralities 
This is going to be a methodological talk. There are hundreds of centrality measures. He goes on to describe what  a centrality index is and shows that we can write a number of centralises to share the small nature of the relationship between objects in our network. 

```
	c(i) = \Sum_t \tau(s,t)
```

You can think of this relation as being expressed in a path algebra. Different operators on the paths will produce different values. 

If the property is to be a centrality, then any property must do worse as we move away from the “central” position, and we say that this means we say that neighbourhood-inclusion is respected. 

We can look at the position of the node in the network, and compare the measure based on the location of the node in the network. 

We can map social spaces into network spaces by using variables in the social space as positions in the network space. 

When thinking of the space of all centralities we can think about ranking only. All rankings are defined by the number of items in the network, and there are about k! Items in a k sized network (just the permutation factor). This is quite a lot. 

Remember though, we want to support neighbourhood-inclusion, otherwise we get a ranking, but not one that perseveres the property of a centrality. It turns out that this will then depend on the network structure, but it will probably be lower than just the permutation of nodes. 

Remember, we are trying to understand how to get to centrality measures, and we have looked at some of the constraints of networks on what it means to be a centrality measure. 

Now we look at some examples. 

Looking at the Medici network. By looking at the neighbourhood-inclusion requirement we get an initial baseline for ordering of members on this network. It doesn’t provide full ranking, but all other centralities must at least preserver the ordering we get from this analysis. 

This provides an interesting new way to look at centralities. 

This was quite a technical talk, and I appreciated the cleanest of the analysis, but without a deeper dive on some networks to analyse I’m not going to be able to fully grok the content. 



