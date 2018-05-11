---
title: Hunting for structure in nested JSON with python just got a whole lot easier 
url: 2018/05/11/Hunting_for_structure_in_nested_JSON_with_python_just_got_a_whole_lot_easier_/
date: 2018-05-11T00:00:00Z
categories:
- asilearn
- python
- python
- glom
- json
- programming
- tips
---

A very common python task that I find myself stumbling over repeatedly is trying to get the syntax right to address or retrieve a specific value to a key in a dented JSON document, in particular if that key is some way down the tree. 

I’ve just found the library https://github.com/mahmoud/glom which is written up really nicely here:  https://sedimental.org/glom_restructured_data.html

Before looking at this modele in detail I had thought that I could pass a reference to a key to glom without specifying its location fully in the structure of the input file, but after looking at this for a moment it became clear that this is not what it does, but rather is good at helping to remap nested data structures into new structures, and accessing the data you want via path like queries. 

I immediately thought about jmsepath, and I was wondering what the different is between the two. Just as I got to that thought  https://sedimental.org/glom_restructured_data.html
Answered my question 

> With glom, you have full access to Python at any given moment. Pass values to functions, whether built-in, imported, or defined inline with lambda. But glom doesn't stop there   

It seems the key idea is that you can include native python expressions in your query, giving you a more powerful query language, than jmsepath or jq. 

From reading the above doc I didn’t quite get an example of this working, so I don’t fully understand it, but I _think_ it looks promising. If I have any heavy lifting JSON or JSON transformations to do in the future from within python I will try to remember to come back and give this a go. 

