---
title: Using Datasette to publish data
url: 2020/07/02/Using_Datasette_to_publish_data/
date: 2020-07-02T00:00:00Z
categories:
- data
- data-publishing
- datasette
- crossref
- notebook
- jupyter
---

In my department we have started to make a bit of space to allow for self learning to
happen. I took the time to look at [https://datasette.readthedocs.io/en/stable/](https://datasette.readthedocs.io/en/stable/), an ecosystem of tools that support
data publishing. These tools are from Simon Willison, and they are fantastic.

I'd been meaning to look at the them for some time now. I used a jupyter notebook
to work my way around getting some data together, and working with the tool.

In the notebook I:

- get some data about 100 BMJ articles using the crossref API
- take a selection of the metadata from those articles
- install Datasette locally
- use sqlite_utils to create a local sqlite database
- use datasette running locally to explore and interact with this data
- export to CSV from my local instance
- upload this CSV to an online instance of Datasette running on Glitch
- configure the Glitch instance to enable full text search on some of the fields

The final output can be seen running at  [https://watery-alder-carpenter.glitch.me/data/article](https://watery-alder-carpenter.glitch.me/data/article).

Overall it went really well, and I'm excited about Datasette.

You can grab a copy of this notebook from [https://github.com/IanMulvany/datasette-testing-bmj-articles](https://github.com/IanMulvany/datasette-testing-bmj-articles).
