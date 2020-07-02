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

In my department we have started to make a bit of space to allow fr self learning to
happen. I took the time to look at datasette, an ecosystem of tools that support
data publishing. These tools are from Simon Wilison, and they are fantastic.

I'd been meaning to look at the them for some time now. I used a jupyter notebook
to work my way around getting some data together, and working with the tool.

I've exported the notebook output to markdown for the rest of this blog post,

You can grab a copy of this notebook from [https://github.com/IanMulvany/datasette-testing-bmj-articles]().


---

```python
import json
import pandas as pd
import requests as r
import csv
```


```python
pd.set_option('display.max_colwidth', -1) # see https://thispointer.com/python-pandas-how-to-display-full-dataframe-i-e-print-all-rows-columns-without-truncation/ - to show cells with long strings in them
```

# Learning Datasette with some sample data about BMJ publications.

I am interested in learning about datasette - an open soruce tool for publishing and exploring data. In order to learn about the tool I've decided to see if it can be used to create an interface to explore some informaiton about papers published by the BMJ. The goal is to see if Datasette could be a useful tool for publishing and sharing data.

In this notebook I'm going to:

- get some data about 100 BMJ articles using the crossref API
- take a selection of the metadata from those articles
- install Datasette locally
- use sqlite_utils to create a local sqlite database
- use datasette running locally to explore and interact with this data
- export to CSV from my local instance
- upload this CSV to an online instance of Datasette running on Glitch
- configure the Glitch instance to enable full text search on some of the fields

The final output can be seen running at [https://watery-alder-carpenter.glitch.me/data/article]().

Overall it went really well, and I'm excited about Datasette.

You can grab a copy of this notebook from [https://github.com/IanMulvany/datasette-testing-bmj-articles]().

# Getting some BMJ article data via the CrossRef API.

I want to get infomration on 1000 recent papers published by the BMJ, it's fine if it's across a number of journals. CrossRef provide an API that can be used to get metadata about scholarly articles, and it can be queried by publisher id.

### Getting the BMJ membership id

The crossref [API documentation is good](https://github.com/CrossRef/rest-api-doc). I can get information on BMJ works using the following endpoint `/members/{member_id}/works`, but first I need to determine the member id for the BMJ. I've usually struggled with this, as previously I've hit the members endpoint and searched through the results in that, but after poking around on the crossref site, I can see that there is a page [https://www.crossref.org/reporting/members-with-open-references/]() where you can search for some members and the result includes the members id.

Using that we find that the BMJ id is `239`.

### Getting some sample article metadata to play with.

Let's check our id to see if it looks correct.


```python
url = "https://api.crossref.org/members/239"
results = r.get(url)
response_df = pd.read_json(results.text) # push the json response into a dataframe, just to make it easier to look at in the notebook
```


```python
response_df
```




<div>
<style scoped>
.dataframe tbody tr th:only-of-type {
vertical-align: middle;
}

.dataframe tbody tr th {
vertical-align: top;
}

.dataframe thead th {
text-align: right;
}
</style>
<table border="1" class="dataframe">
<thead>
<tr style="text-align: right;">
<th></th>
<th>status</th>
<th>message-type</th>
<th>message-version</th>
<th>message</th>
</tr>
</thead>
<tbody>
<tr>
<th>breakdowns</th>
<td>ok</td>
<td>member</td>
<td>1.0.0</td>
<td>{'dois-by-issued-year': [[2019, 35998], [2013, 32478], [2018, 31835], [2017, 29277], [2016, 28390], [2014, 28183], [2015, 28043], [2012, 24775], [2011, 22030], [2010, 19796], [2004, 16463], [2005, 15732], [2006, 15533], [2007, 14566], [2003, 14486], [2008, 14390], [2009, 14226], [2002, 12727], [2020, 11051], [2001, 10726], [2000, 10077], [1999, 10069], [1995, 9944], [1998, 9793], [1996, 9649], [1997, 9188], [1994, 9054], [1993, 9052], [1992, 8643], [1991, 8232], [1988, 8095], [1987, 8048], [1989, 7989], [1984, 7918], [1986, 7861], [1985, 7794], [1981, 7679], [1978, 7625], [1983, 7617], [1982, 7563], [1979, 7515], [1977, 7379], [1976, 7366], [1980, 7224], [1990, 7045], [1975, 7034], [1972, 6600], [1973, 6523], [1974, 6507], [1970, 6378], [1971, 6171], [1969, 6128], [1964, 5855], [1968, 5630], [1965, 5618], [1966, 5605], [1967, 5583], [1963, 4884], [1961, 4825], [1962, 4757], [1960, 4745], [1958, 4127], [1955, 4105], [1954, 3975], [1957, 3929], [1959, 3860], [1948, 3855], [1956, 3820], [1950, 3751], [1953, 3733], [1952, 3667], [1951, 3628], [1949, 3464], [1946, 3255], [1947, 3121], [1945, 2953], [1938, 2946], [1936, 2933], [1939, 2905], [1935, 2886], [1944, 2801], [1940, 2741], [1937, 2699], [1943, 2684], [1910, 2679], [1941, 2654], [1907, 2643], [1934, 2617], [1933, 2499], [1942, 2496], [1909, 2479], [1932, 2475], [1929, 2469], [1898, 2447], [1906, 2446], [1897, 2430], [1901, 2421], [1908, 2413], [1927, 2378], [1930, 2374], ...]}</td>
</tr>
<tr>
<th>counts</th>
<td>ok</td>
<td>member</td>
<td>1.0.0</td>
<td>{'total-dois': 942856, 'current-dois': 78884, 'backfile-dois': 863972}</td>
</tr>
<tr>
<th>counts-type</th>
<td>ok</td>
<td>member</td>
<td>1.0.0</td>
<td>{'all': {'journal': 10, 'journal-issue': 32, 'component': 10700, 'proceedings-article': 38875, 'dataset': 1, 'journal-article': 903949}, 'current': {'proceedings-article': 28247, 'journal-article': 50637}, 'backfile': {'journal-issue': 32, 'proceedings-article': 10628, 'journal-article': 853312}}</td>
</tr>
<tr>
<th>coverage</th>
<td>ok</td>
<td>member</td>
<td>1.0.0</td>
<td>{'affiliations-current': 1.267684183403616e-05, 'similarity-checking-current': 1.0, 'funders-backfile': 0.005678424611687, 'licenses-backfile': 0.049050200730562, 'funders-current': 0.16993306577205602, 'affiliations-backfile': 8.102114406938199e-06, 'resource-links-backfile': 0.049035154283046, 'orcids-backfile': 0.007862523198127, 'update-policies-current': 0.9898458719253541, 'open-references-backfile': 1.0, 'orcids-current': 0.303838551044464, 'similarity-checking-backfile': 0.948795795440673, 'references-backfile': 0.21159945428371402, 'award-numbers-backfile': 0.001630839891731, 'update-policies-backfile': 0.176815912127494, 'licenses-current': 0.16405101120471902, 'award-numbers-current': 0.070876225829124, 'abstracts-backfile': 0.011933256871998001, 'resource-links-current': 0.112215407192707, 'abstracts-current': 0.358285576105117, 'open-references-current': 1.0, 'references-current': 0.448861628770828}</td>
</tr>
<tr>
<th>coverage-type</th>
<td>ok</td>
<td>member</td>
<td>1.0.0</td>
<td>{'all': {'dataset': {'last-status-check-time': 1593151940343, 'affiliations': 0.0, 'abstracts': 0.0, 'orcids': 0.0, 'licenses': 0.0, 'references': 0.0, 'funders': 0.0, 'similarity-checking': 0.0, 'award-numbers': 0.0, 'update-policies': 0.0, 'resource-links': 0.0, 'open-references': 1.0}, 'journal': {'last-status-check-time': 1593151937159, 'affiliations': 0.0, 'abstracts': 0.0, 'orcids': 0.0, 'licenses': 0.0, 'references': 0.0, 'funders': 0.0, 'similarity-checking': 0.0, 'award-numbers': 0.0, 'update-policies': 0.0, 'resource-links': 0.0, 'open-references': 1.0}, 'journal-issue': {'last-status-check-time': 1593151933646, 'affiliations': 0.0, 'abstracts': 0.0, 'orcids': 0.0, 'licenses': 0.0, 'references': 0.0, 'funders': 0.0, 'similarity-checking': 0.0, 'award-numbers': 0.0, 'update-policies': 0.0, 'resource-links': 0.0, 'open-references': 1.0}, 'component': {'last-status-check-time': 1593151930206, 'affiliations': 0.0, 'abstracts': 0.0, 'orcids': 0.0, 'licenses': 0.0, 'references': 0.0, 'funders': 0.0, 'similarity-checking': 1.0, 'award-numbers': 0.0, 'update-policies': 0.0, 'resource-links': 0.0, 'open-references': 1.0}, 'proceedings-article': {'last-status-check-time': 1593151926966, 'affiliations': 0.0, 'abstracts': 0.0, 'orcids': 0.0, 'licenses': 0.0, 'references': 5.144694659975358e-05, 'funders': 0.0, 'similarity-checking': 1.0, 'award-numbers': 0.0, 'update-policies': 1.0, 'resource-links': 0.0, 'open-references': 1.0}, 'journal-article': {'last-status-check-time': 1593151923597, 'affiliations': 8.850056474329904e-06, 'abstracts': 0.042671654373407, 'orcids': 0.034029573202133005, 'licenses': 0.061197035014629, 'references': 0.24140964448451901, 'funders': 0.020256673917174003, 'similarity-checking': 0.951095700263977, 'award-numbers': 0.007743799593299, 'update-policies': 0.21237038075923903, 'resource-links': 0.056659169495105, 'open-references': 1.0}}, 'backfile': {'journal-issue': {'last-status-check-time': 1593151920796, 'affiliations': 0.0, 'abstracts': 0.0, 'orcids': 0.0, 'licenses': 0.0, 'references': 0.0, 'funders': 0.0, 'similarity-checking': 0.0, 'award-numbers': 0.0, 'update-policies': 0.0, 'resource-links': 0.0, 'open-references': 1.0}, 'proceedings-article': {'last-status-check-time': 1593151917440, 'affiliations': 0.0, 'abstracts': 0.0, 'orcids': 0.0, 'licenses': 0.0, 'references': 0.0, 'funders': 0.0, 'similarity-checking': 1.0, 'award-numbers': 0.0, 'update-policies': 1.0, 'resource-links': 0.0, 'open-references': 1.0}, 'journal-article': {'last-status-check-time': 1593151913801, 'affiliations': 8.203330253309105e-06, 'abstracts': 0.012082333676517001, 'orcids': 0.007960746064782, 'licenses': 0.049662958830595, 'references': 0.214242860674858, 'funders': 0.005749362520873, 'similarity-checking': 0.9481936097145081, 'award-numbers': 0.0016512131551280002, 'update-policies': 0.166569784283638, 'resource-links': 0.049647726118564, 'open-references': 1.0}}, 'current': {'proceedings-article': {'last-status-check-time': 1593151910755, 'affiliations': 0.0, 'abstracts': 0.0, 'orcids': 0.0, 'licenses': 0.0, 'references': 7.080398063408211e-05, 'funders': 0.0, 'similarity-checking': 1.0, 'award-numbers': 0.0, 'update-policies': 1.0, 'resource-links': 0.0, 'open-references': 1.0}, 'journal-article': {'last-status-check-time': 1593151907016, 'affiliations': 1.974840597540605e-05, 'abstracts': 0.55814915895462, 'orcids': 0.473329782485961, 'licenses': 0.25556412339210505, 'references': 0.69921201467514, 'funders': 0.264727383852005, 'similarity-checking': 1.0, 'award-numbers': 0.11041333526372901, 'update-policies': 0.9841815233230591, 'resource-links': 0.174812883138656, 'open-references': 1.0}}}</td>
</tr>
<tr>
<th>flags</th>
<td>ok</td>
<td>member</td>
<td>1.0.0</td>
<td>{'deposits-abstracts-current': True, 'deposits-orcids-current': True, 'deposits': True, 'deposits-affiliations-backfile': True, 'deposits-update-policies-backfile': True, 'deposits-similarity-checking-backfile': True, 'deposits-award-numbers-current': True, 'deposits-resource-links-current': True, 'deposits-articles': True, 'deposits-affiliations-current': True, 'deposits-funders-current': True, 'deposits-references-backfile': True, 'deposits-abstracts-backfile': True, 'deposits-licenses-backfile': True, 'deposits-award-numbers-backfile': True, 'deposits-open-references-backfile': True, 'deposits-open-references-current': True, 'deposits-references-current': True, 'deposits-resource-links-backfile': True, 'deposits-orcids-backfile': True, 'deposits-funders-backfile': True, 'deposits-update-policies-current': True, 'deposits-similarity-checking-current': True, 'deposits-licenses-current': True}</td>
</tr>
<tr>
<th>id</th>
<td>ok</td>
<td>member</td>
<td>1.0.0</td>
<td>239</td>
</tr>
<tr>
<th>last-status-check-time</th>
<td>ok</td>
<td>member</td>
<td>1.0.0</td>
<td>1593151950376</td>
</tr>
<tr>
<th>location</th>
<td>ok</td>
<td>member</td>
<td>1.0.0</td>
<td>BMA House Tavistock Square Tavistock Square London WC1H 9JP United Kingdom</td>
</tr>
<tr>
<th>names</th>
<td>ok</td>
<td>member</td>
<td>1.0.0</td>
<td>[BMJ, Faculty of Family Planning]</td>
</tr>
<tr>
<th>prefix</th>
<td>ok</td>
<td>member</td>
<td>1.0.0</td>
<td>[{'value': '10.1783', 'name': 'Faculty of Family Planning', 'public-references': True, 'reference-visibility': 'open'}, {'value': '10.1136', 'name': 'BMJ', 'public-references': True, 'reference-visibility': 'open'}]</td>
</tr>
<tr>
<th>prefixes</th>
<td>ok</td>
<td>member</td>
<td>1.0.0</td>
<td>[10.1783, 10.1136]</td>
</tr>
<tr>
<th>primary-name</th>
<td>ok</td>
<td>member</td>
<td>1.0.0</td>
<td>BMJ</td>
</tr>
<tr>
<th>tokens</th>
<td>ok</td>
<td>member</td>
<td>1.0.0</td>
<td>[bmj]</td>
</tr>
</tbody>
</table>
</div>



### now let's get some article metadata

I'm interested in getting articles that have abstract metadata, and I'd like to get a sample, so I can use some filters that the crossref API provide.  


```python
# the query against the endpoint below felt like it took about a minute to run.
url = "https://api.crossref.org/members/239/works?filter=has-abstract:true&sample=100"
results = r.get(url)
response_df = pd.read_json(results.text)
```


```python
bmJ_article_sample = results.json()["message"]["items"]
```

Now I've got a sample of 100 articles from BMJ with associated metadata. Let's look at what metadata we can get from one record.


```python
bmJ_article_sample[4].keys()
```




dict_keys(['indexed', 'reference-count', 'publisher', 'funder', 'content-domain', 'short-container-title', 'abstract', 'DOI', 'type', 'created', 'page', 'update-policy', 'source', 'is-referenced-by-count', 'title', 'prefix', 'author', 'member', 'published-online', 'reference', 'container-title', 'language', 'link', 'deposited', 'score', 'issued', 'references-count', 'alternative-id', 'URL', 'relation', 'ISSN', 'issn-type', 'subject'])



Let's work through these and decide which ones we want to try to view in datasette.


```python
bmJ_article_sample[4]["indexed"] # not interested in this right now.
```




{'date-parts': [[2020, 6, 30]],
'date-time': '2020-06-30T21:41:52Z',
'timestamp': 1593553312745}




```python
bmJ_article_sample[4]["reference-count"] # this is interesting - keep this one
```




29




```python
bmJ_article_sample[4]["publisher"] # we know we are the publisher, so ignore this one for now.
```




'BMJ'




```python
bmJ_article_sample[4]["funder"] # the funder is interesting, but needs a bit more work to extract, let's create a short function to do that for us.
```




[{'DOI': '10.13039/100000009',
'name': 'Foundation for the National Institutes of Health',
'doi-asserted-by': 'publisher',
'award': ['R01NS111119-01A1']}]




```python
def get_funder_info(funders):
award_numbers = []
funder_names = []
funder_dois = []
for funder in funders:
if 'award' in funder:
award_numbers.append(funder["award"])
else:
award_numbers.append([""])
funder_names.append(funder['name'])
if 'DOI' in funder:
funder_dois.append(funder['DOI'])
else:
funder_dois.append([""])
return award_numbers, funder_names, funder_dois
```


```python
bmJ_article_sample[4]["content-domain"] # not interested in this
```




{'domain': ['bmj.com'], 'crossmark-restriction': True}




```python
bmJ_article_sample[4]["short-container-title"] #only keep if the journal title is not available
```




['J NeuroIntervent Surg']




```python
bmJ_article_sample[4]["abstract"] # yes - interested
```




'<jats:sec><jats:title>Background</jats:title><jats:p>The management of unruptured intracranial aneurysms (UIAs) has evolved significantly over the last few decades. Our objective was to evaluate the 100 most cited UIA articles by bibliometric analysis to identify nature, content and shifts over time.</jats:p></jats:sec><jats:sec><jats:title>Methods</jats:title><jats:p>Elsevier’s Scopus database was interrogated for the 100 most cited articles that focused on UIA. Older versus newer articles were compared, with categorical data analyzed using Pearson’s Chi-square, and continuous data analyzed using Wilcoxon’s rank-sum test.</jats:p></jats:sec><jats:sec><jats:title>Results</jats:title><jats:p>The 100 most cited articles were published between 1975 and 2015, with the majority of these reporting patient clinical outcomes (n=69). There were 47/69 (68%) articles that described surgical intervention, with 38/47 (81%) and 18/47 (38%) including endovascular and open approaches, respectively . Publications peaked in 2004 (n=8), and the most common country of correspondence was the United States (n=59). Compared to older articles, newer articles had statistically higher citation rates (P&lt;0.01), higher number of authors (P&lt;0.01) with more multiple institution collaborations (P=0.01), greater disclosures of funding (P&lt;0.01), more focus on endovascular treatments (P=0.04), in more journals with a clinical, non-surgical focus (P&lt;0.01) published under open access policies (P&lt;0.01).</jats:p></jats:sec><jats:sec><jats:title>Conclusions</jats:title><jats:p>In the 100 most cited articles about UIAs to date, there is a distinct shift towards more co-authored efforts utilizing multi-institutional efforts focused on endovascular approaches supported by funding. The emergence of endovascular techniques has refreshed the need for more contemporary rupture risk prediction models and natural history data to validate current attitudes towards clinical management after these minimally invasive procedures for UIAs.</jats:p></jats:sec>'




```python
bmJ_article_sample[4]["DOI"] # yes
```




'10.1136/neurintsurg-2020-016238'




```python
bmJ_article_sample[4]["type"] # no
```




'journal-article'




```python
bmJ_article_sample[4]["created"] # just want the timestamp
```




{'date-parts': [[2020, 6, 30]],
'date-time': '2020-06-30T21:27:03Z',
'timestamp': 1593552423000}




```python
def get_timesstamp(created):
return created["date-time"]
```


```python
bmJ_article_sample[4]["page"] # not interested
```




'neurintsurg-2020-016238'




```python
bmJ_article_sample[4]["update-policy"] # not interested
```




'http://dx.doi.org/10.1136/crossmarkpolicy'




```python
bmJ_article_sample[4]["source"] # not interested
```




'Crossref'




```python
bmJ_article_sample[4]["is-referenced-by-count"] # keep this, though in this example the nubmer is 0, interesting if non zero
```




0




```python
bmJ_article_sample[4]["title"] # yes!
```




['Nature, content and shifts over time of the most impactful unruptured intracranial aneurysms articles: a bibliometric analysis']




```python
bmJ_article_sample[4]["prefix"] # no
```




'10.1136'




```python
bmJ_article_sample[4]["author"] # very interesting, need to get some more data from this!, let's write a quick function
```




[{'ORCID': 'http://orcid.org/0000-0002-9470-5890',
'authenticated-orcid': False,
'given': 'Victor M',
'family': 'Lu',
'sequence': 'first',
'affiliation': []},
{'given': 'Stephanie H',
'family': 'Chen',
'sequence': 'additional',
'affiliation': []},
{'ORCID': 'http://orcid.org/0000-0002-3679-3212',
'authenticated-orcid': False,
'given': 'Christopher C',
'family': 'Young',
'sequence': 'additional',
'affiliation': []},
{'given': 'Robert M',
'family': 'Starke',
'sequence': 'additional',
'affiliation': []}]




```python
def get_author_info(author_data):
author_number = len(author_data)
orcids = []
names = []
for author in author_data:
if 'ORCID' in author: orcids.append(author["ORCID"])
author_name = author["given"] + " " + author["family"]
names.append(author_name)
return author_number, orcids, names
author_number, orcids, names = get_author_info(bmJ_article_sample[4]["author"])
print(author_number, orcids, names)
```

4 ['http://orcid.org/0000-0002-9470-5890', 'http://orcid.org/0000-0002-3679-3212'] ['Victor M Lu', 'Stephanie H Chen', 'Christopher C Young', 'Robert M Starke']



```python
bmJ_article_sample[4]["member"] # not interested
```




'239'




```python
bmJ_article_sample[4]["published-online"] # not interested
```




{'date-parts': [[2020, 6, 30]]}




```python
bmJ_article_sample[4]["reference"] # very interesting, for now let's just look at the number of references
```




[{'key': '2020063014251776000_neurintsurg-2020-016238v1.1',
'DOI': '10.1016/S1474-4422(14)70015-8',
'doi-asserted-by': 'publisher'},
{'key': '2020063014251776000_neurintsurg-2020-016238v1.2',
'DOI': '10.1136/neurintsurg-2019-015418',
'doi-asserted-by': 'publisher'},
{'key': '2020063014251776000_neurintsurg-2020-016238v1.3',
'first-page': '603',
'article-title': 'Unruptured intracranial aneurysms: in search of the best management strategy: editorial',
'volume': '32',
'author': 'Kassell',
'year': '2001',
'journal-title': 'Stroke'},
{'key': '2020063014251776000_neurintsurg-2020-016238v1.4',
'DOI': '10.3171/jns.1990.73.1.0037',
'doi-asserted-by': 'publisher'},
{'key': '2020063014251776000_neurintsurg-2020-016238v1.5',
'doi-asserted-by': 'crossref',
'first-page': '919',
'DOI': '10.1016/j.wneu.2017.07.074',
'article-title': 'Shifting treatment paradigms for ruptured aneurysms from open surgery to endovascular therapy over 25 years',
'volume': '106',
'author': 'Bender',
'year': '2017',
'journal-title': 'World Neurosurg'},
{'key': '2020063014251776000_neurintsurg-2020-016238v1.6',
'DOI': '10.1371/journal.pmed.1000097',
'doi-asserted-by': 'publisher'},
{'key': '2020063014251776000_neurintsurg-2020-016238v1.7',
'DOI': '10.1096/fj.07-9492LSF',
'doi-asserted-by': 'publisher'},
{'key': '2020063014251776000_neurintsurg-2020-016238v1.8',
'DOI': '10.1016/S0140-6736(03)13860-3',
'doi-asserted-by': 'publisher'},
{'key': '2020063014251776000_neurintsurg-2020-016238v1.9',
'DOI': '10.1056/NEJM199812103392401',
'doi-asserted-by': 'publisher'},
{'key': '2020063014251776000_neurintsurg-2020-016238v1.10',
'first-page': '7',
'article-title': 'The microsurgical approach to intracranial aneurysms',
'volume': '3',
'author': 'Yasargil',
'year': '1975',
'journal-title': 'Surg Neurol'},
{'key': '2020063014251776000_neurintsurg-2020-016238v1.11',
'DOI': '10.1161/STR.0000000000000070',
'doi-asserted-by': 'publisher'},
{'key': '2020063014251776000_neurintsurg-2020-016238v1.12',
'DOI': '10.1038/ng.563',
'doi-asserted-by': 'publisher'},
{'key': '2020063014251776000_neurintsurg-2020-016238v1.13',
'DOI': '10.3171/jns.2000.93.3.0379',
'doi-asserted-by': 'publisher'},
{'key': '2020063014251776000_neurintsurg-2020-016238v1.14',
'DOI': '10.3171/jns.1993.79.2.0174',
'doi-asserted-by': 'publisher'},
{'key': '2020063014251776000_neurintsurg-2020-016238v1.15',
'DOI': '10.1161/STROKEAHA.113.001838',
'doi-asserted-by': 'publisher'},
{'key': '2020063014251776000_neurintsurg-2020-016238v1.16',
'DOI': '10.1161/01.STR.32.2.485',
'doi-asserted-by': 'publisher'},
{'key': '2020063014251776000_neurintsurg-2020-016238v1.17',
'first-page': '2550',
'article-title': 'Characterization of cerebral aneurysms for assessing risk of rupture by using patient-specific computational hemodynamics models',
'volume': '26',
'author': 'Cebral',
'year': '2005',
'journal-title': 'AJNR Am J Neuroradiol'},
{'key': '2020063014251776000_neurintsurg-2020-016238v1.18',
'DOI': '10.1109/TMI.2005.844159',
'doi-asserted-by': 'publisher'},
{'key': '2020063014251776000_neurintsurg-2020-016238v1.19',
'DOI': '10.3174/ajnr.A2274',
'doi-asserted-by': 'publisher'},
{'key': '2020063014251776000_neurintsurg-2020-016238v1.20',
'DOI': '10.3174/ajnr.A2419',
'doi-asserted-by': 'publisher'},
{'key': '2020063014251776000_neurintsurg-2020-016238v1.21',
'DOI': '10.1016/S1474-4422(13)70263-1',
'doi-asserted-by': 'publisher'},
{'key': '2020063014251776000_neurintsurg-2020-016238v1.22',
'doi-asserted-by': 'crossref',
'first-page': '145',
'DOI': '10.1016/j.wneu.2016.11.079',
'article-title': 'Neurosurgeons in Japan are exclusively brain surgeons',
'volume': '99',
'author': 'Asamoto',
'year': '2017',
'journal-title': 'World Neurosurg'},
{'key': '2020063014251776000_neurintsurg-2020-016238v1.23',
'doi-asserted-by': 'crossref',
'first-page': '1142',
'DOI': '10.3171/2018.10.JNS171723',
'article-title': 'The global neurosurgical workforce: a mixed-methods assessment of density and growth',
'volume': '130',
'author': 'Mukhopadhyay',
'year': '2019',
'journal-title': 'J Neurosurg'},
{'key': '2020063014251776000_neurintsurg-2020-016238v1.24',
'DOI': '10.3171/JNS/2008/108/5/1052',
'doi-asserted-by': 'publisher'},
{'key': '2020063014251776000_neurintsurg-2020-016238v1.25',
'DOI': '10.1136/jnnp-2016-314477',
'doi-asserted-by': 'publisher'},
{'key': '2020063014251776000_neurintsurg-2020-016238v1.26',
'doi-asserted-by': 'crossref',
'first-page': '461',
'DOI': '10.1016/j.wneu.2019.01.195',
'article-title': 'Cost comparison of surgical clipping and endovascular coiling of unruptured intracranial aneurysms: a systematic review',
'volume': '125',
'author': 'Engele',
'year': '2019',
'journal-title': 'World Neurosurg'},
{'key': '2020063014251776000_neurintsurg-2020-016238v1.27',
'DOI': '10.1109/TMI.2007.901008',
'doi-asserted-by': 'publisher'},
{'key': '2020063014251776000_neurintsurg-2020-016238v1.28',
'DOI': '10.1016/j.wneu.2019.06.231',
'doi-asserted-by': 'publisher'},
{'key': '2020063014251776000_neurintsurg-2020-016238v1.29',
'doi-asserted-by': 'crossref',
'first-page': '766',
'DOI': '10.1016/j.wneu.2013.07.011',
'article-title': 'Part II: should the h-index be modified? An analysis of the m-quotient, contemporary h-index, authorship value, and impact factor',
'volume': '80',
'author': 'Khan',
'year': '2013',
'journal-title': 'World Neurosurg'}]




```python
def get_reference_info(references):
return len(references)

reference_number = get_reference_info(bmJ_article_sample[4]["reference"])
print(reference_number)
```

29



```python
bmJ_article_sample[4]["container-title"] # yes, interested in this
```




['Journal of NeuroInterventional Surgery']




```python
bmJ_article_sample[4]["language"] # not interested
```




'en'




```python
bmJ_article_sample[4]["link"] # not interested
```




[{'URL': 'https://syndication.highwire.org/content/doi/10.1136/neurintsurg-2020-016238',
'content-type': 'unspecified',
'content-version': 'vor',
'intended-application': 'similarity-checking'}]




```python
bmJ_article_sample[4]["deposited"] # not interested
```




{'date-parts': [[2020, 6, 30]],
'date-time': '2020-06-30T21:27:09Z',
'timestamp': 1593552429000}




```python
bmJ_article_sample[4]["score"] # not interested
```




1.0




```python
bmJ_article_sample[4]["issued"] # not interested
```




{'date-parts': [[2020, 6, 30]]}




```python
bmJ_article_sample[4]["references-count"] # yes interested
```




29




```python
bmJ_article_sample[4]["alternative-id"] # not interested
```




['10.1136/neurintsurg-2020-016238']




```python
bmJ_article_sample[4]["URL"] # yes
```




'http://dx.doi.org/10.1136/neurintsurg-2020-016238'




```python
bmJ_article_sample[4]["relation"] # no
```




{'cites': []}




```python
bmJ_article_sample[4]["ISSN"] # yes
```




['1759-8478', '1759-8486']




```python
bmJ_article_sample[4]["issn-type"] # no
```




[{'value': '1759-8478', 'type': 'print'},
{'value': '1759-8486', 'type': 'electronic'}]




```python
bmJ_article_sample[4]["subject"] # yes
```




['Surgery', 'Clinical Neurology', 'General Medicine']



### Picking the fields I want to extract

Looking throuhg the above fields, for the purpose of this demo I want to extract the following:


```
funder -> via function
abstract
DOI
created
is-referenced-by-count
title
author -> via funciton
references # not interested for now
container-title
references-count
URL
ISSN
subject
```

Lets write a little function to extract and flatten this info from an aricle record from BMJ.





```python
def get_demo_info(article_record):
demo_info = []
demo_info.append(article_record["title"][0]) # expected this to be flat, but needed to flatten more
demo_info.append(article_record["DOI"])
demo_info.append(article_record["URL"])
demo_info.append(article_record["created"]["date-time"])
if 'subject' in article_record:
demo_info.append(article_record["subject"])
else:
demo_info.append([""])
demo_info.append(article_record["references-count"])    
demo_info.append(article_record["is-referenced-by-count"])
demo_info.append(article_record["ISSN"])
demo_info.append(article_record["container-title"][0]) # expected this to be flat, but needed to flatten more
demo_info.append(article_record["abstract"])
# now the author info
if 'author' in article_record:
author_number, orcids, names = get_author_info(article_record["author"])
demo_info.append(author_number)    
demo_info.append(orcids)
demo_info.append(names)
else:
demo_info.append(0)    
demo_info.append([""])    
demo_info.append([""])    
# now the funder info
if "funder" in article_record:
award_numbers, funder_names, funder_dois = get_funder_info(article_record["funder"])
demo_info.append(award_numbers[0])    
demo_info.append(funder_names)
demo_info.append(funder_dois)
else:
demo_info.append([''])    
demo_info.append([''])
demo_info.append([''])    
return demo_info
```


```python
demo_info = get_demo_info(bmJ_article_sample[4])
```


```python
demo_info
```




['Nature, content and shifts over time of the most impactful unruptured intracranial aneurysms articles: a bibliometric analysis',
'10.1136/neurintsurg-2020-016238',
'http://dx.doi.org/10.1136/neurintsurg-2020-016238',
'2020-06-30T21:27:03Z',
['Surgery', 'Clinical Neurology', 'General Medicine'],
29,
0,
['1759-8478', '1759-8486'],
'Journal of NeuroInterventional Surgery',
'<jats:sec><jats:title>Background</jats:title><jats:p>The management of unruptured intracranial aneurysms (UIAs) has evolved significantly over the last few decades. Our objective was to evaluate the 100 most cited UIA articles by bibliometric analysis to identify nature, content and shifts over time.</jats:p></jats:sec><jats:sec><jats:title>Methods</jats:title><jats:p>Elsevier’s Scopus database was interrogated for the 100 most cited articles that focused on UIA. Older versus newer articles were compared, with categorical data analyzed using Pearson’s Chi-square, and continuous data analyzed using Wilcoxon’s rank-sum test.</jats:p></jats:sec><jats:sec><jats:title>Results</jats:title><jats:p>The 100 most cited articles were published between 1975 and 2015, with the majority of these reporting patient clinical outcomes (n=69). There were 47/69 (68%) articles that described surgical intervention, with 38/47 (81%) and 18/47 (38%) including endovascular and open approaches, respectively . Publications peaked in 2004 (n=8), and the most common country of correspondence was the United States (n=59). Compared to older articles, newer articles had statistically higher citation rates (P&lt;0.01), higher number of authors (P&lt;0.01) with more multiple institution collaborations (P=0.01), greater disclosures of funding (P&lt;0.01), more focus on endovascular treatments (P=0.04), in more journals with a clinical, non-surgical focus (P&lt;0.01) published under open access policies (P&lt;0.01).</jats:p></jats:sec><jats:sec><jats:title>Conclusions</jats:title><jats:p>In the 100 most cited articles about UIAs to date, there is a distinct shift towards more co-authored efforts utilizing multi-institutional efforts focused on endovascular approaches supported by funding. The emergence of endovascular techniques has refreshed the need for more contemporary rupture risk prediction models and natural history data to validate current attitudes towards clinical management after these minimally invasive procedures for UIAs.</jats:p></jats:sec>',
4,
['http://orcid.org/0000-0002-9470-5890',
'http://orcid.org/0000-0002-3679-3212'],
['Victor M Lu', 'Stephanie H Chen', 'Christopher C Young', 'Robert M Starke'],
['R01NS111119-01A1'],
['Foundation for the National Institutes of Health'],
['10.13039/100000009']]



let's just check to see if this works over all of the article records pulled from corssref in this demo so far!


```python
full_demo_info = []
for article in bmJ_article_sample:
demo_info = get_demo_info(article)
full_demo_info.append(demo_info)
```


```python
len(full_demo_info)
```




100



Now we have some sample data that we can export out to play with in datasette! For starters lets write this to a CSV file.


```python
with open("datasette_bmj_artilces.csv", 'w', newline='') as csvfile:
article_writer = csv.writer(csvfile, delimiter=' ',
quotechar='|', quoting=csv.QUOTE_MINIMAL)
for row in full_demo_info:
article_writer.writerow(row)
```

Now we have our artilce data in a csv file. To be honest, taking a structurd json file, and flattening it to csv is possibly not the best way to go about this work, but as this is an excercise in learning about datasettle let's move on in any case!

# Installing datasette, and getting started with it

We will follow the docs in [https://datasette.readthedocs.io]() and we will try to install using `pip3`: [https://datasette.readthedocs.io/en/stable/installation.html#install-using-pip]()

`$ sudo pip3 install datasette`  works, I have to use `sudo` shhhh!

```
$ datasette --version   
datasette, version 0.45
```

OK, we have datasette installed locally, how do we get started with it? Following the instructions on [https://datasette.readthedocs.io/en/stable/getting_started.html#using-datasette-on-your-own-computer]() there are two paths we could follow now.

1. look at the glitch version, and try to upload the CSV file that we have just created.

2. try to use the tool to convert a csv file into a sqlite db locally, and then run datasette locally.

I'm not confident that our csv is going to be easy to convert so I'm going to start by trying to do that conversion locally, in the hope that I might get some useful error messages. Onece I've gotten a local version working, I'm going to see if I can get a clone of the glitch version working, but with my data, so that we can see if this is a good route for data sharing.

## Getting data into datasetts - using sqlite-utils to push data directly into an sqlite database

Datasette comes with an ecosystem of tools - [https://datasette.readthedocs.io/en/stable/ecosystem.html](). Many of these are for converting data into a format that datasetts can use. When starting on this earlier today I had assumed that I would need to use `csvs-to-sqlite` to convert a csv file, but `sqlite-utils` also sounds interesting.

Since I am already in a jupyter notebook, let's give `sqlite-utils` a go!

I need to get `sqlite-utils` in this anaconda enviornment

`$ ~/anaconda3/bin/pip install  sqlite_utils`


```python
import sqlite_utils
```


```python
db = sqlite_utils.Database("demo_bmj_article_database.db")
```

The documentation says that we can use this as follows:

```python
db["dogs"].insert_all([
{"id": 1, "age": 4, "name": "Cleo"},
{"id": 2, "age": 2, "name": "Pancakes"}
], pk="id")
```

So I should go back, and unflatten my rows of artilce info, create dicts, with keys, and then insert them into the database. This is going to be a bit messy, but pushing ahead in any case, and we can refactor later if we have time. Basically, I'm going to rewrite `get_demo_info` to ouput a dict instead of a list. Probably earlier I could have applied some filtering to the result coming back from crossref, but I think it's OK for now.


```python
def get_demo_info_dict_test(article_record):
"""
We are just seeing if we can get the smallest meaningful example working
"""
demo_info_dict = {}
demo_info_dict["title"] = article_record["title"]
demo_info_dict["DOI"] = article_record["DOI"]
return demo_info_dict
```

Before proceedig any further, I'm just going to do a very quick check to see if I can get this very basic information into datasette, and serve it locally.


```python
demo_info_dict_4 = get_demo_info_dict_test(bmJ_article_sample[4])
demo_info_dict_5 = get_demo_info_dict_test(bmJ_article_sample[5])
```


```python
db["article"].insert_all([
demo_info_dict_4,
demo_info_dict_5
], pk="DOI")
```




<Table article (title, DOI)>



## serving a local squlite db with datasette

We have now created `demo_bmj_article_database.db`. We should be able to serve this with  

```
datasette serve demo_bmj_article_database.db
INFO:     Started server process [11028]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8001 (Press CTRL+C to quit)

```

This worked, and I now have a local instance on datasette! How exciting! Let's go and get all of the info we are interested in and populate all of the rows of our sample data.


```python
def get_demo_info_dict(article_record):
demo_info_dict = {}
demo_info_dict["title"] = article_record["title"]
demo_info_dict["DOI"] = article_record["DOI"]
demo_info_dict["URL"] = article_record["URL"]
demo_info_dict["created"] = article_record["created"]["date-time"]
# subject info
if 'subject' in article_record:
demo_info_dict["subject"] = article_record["subject"]
else:
demo_info_dict["subject"] = []

demo_info_dict["references-count"] = article_record["references-count"]    
demo_info_dict["is-referenced-by-count"] = article_record["is-referenced-by-count"]
demo_info_dict["ISSN"] = article_record["ISSN"]
demo_info_dict["container-title"] = article_record["container-title"][0] # expected this to be flat, but needed to flatten more
demo_info_dict["abstract"] = article_record["abstract"]

# now the author info
if 'author' in article_record:
author_number, orcids, names = get_author_info(article_record["author"])
demo_info_dict["author_number"] = author_number
demo_info_dict["orcids"] = orcids
demo_info_dict["names"] = names
else:
demo_info_dict["author_number"] = 0
demo_info_dict["orcids"] = [""]
demo_info_dict["names"] = [""]

# now the funder info
if "funder" in article_record:
award_numbers, funder_names, funder_dois = get_funder_info(article_record["funder"])
demo_info_dict["award_numbers"] = award_numbers[0]
demo_info_dict["funder_names"] = funder_names
demo_info_dict["funder_dois"] = funder_dois
else:
demo_info_dict["award_numbers"] = ['']
demo_info_dict["funder_names"] = ['']
demo_info_dict["funder_dois"] = ['']      

return demo_info_dict
```


```python
info_dicts = []
for article in bmJ_article_sample:
info_dict = get_demo_info_dict(article)
info_dicts.append(info_dict)
len(info_dicts)
```




100




```python
db = sqlite_utils.Database("demo_bmj_article_database.db")
db["article"].insert_all(info_dicts, pk="DOI")
```




<Table article (title, DOI, URL, created, subject, references-count, is-referenced-by-count, ISSN, container-title, abstract, author_number, orcids, names, award_numbers, funder_names, funder_dois)>



## Hosting our data online on glitch

We have now created a datasette instance with info from 100 BMJ articles. We could create some more tables, e.g. around funder or author info, but let's see if we can get this instance up and running online using the demo glitch project.

[https://glitch.com]() is a site where you can create sites, or copy or clone sites. It's awesomt. Simon the datasette developer has created a demo datasette instance on glitch. You can clone it here: [https://glitch.com/edit/#!/ringed-succulent-silence?path=README.md%3A1%3A0](). Apparently it works by allowing you to drop a CSV file onto the root directory. Datasette also allows you to download your data as scv, so in principle I should be able to:

- download the data I've just put into my local instance of datasette  
- clone the glitch project  
- drop my csv file onto glitch and serve my project

Following these steps I can now serve an example of my data on glitch. Glitch generates a random domain name for each new project, so this project is called [https://watery-alder-carpenter.glitch.me]() and you can inspect the data by clicking into `data` and then into `article`: [https://watery-alder-carpenter.glitch.me/data/article]().






### Enabling full text search on glitch

The datasette ecosystem has a wide range of plugins, and one of these enables full text search. Following the instructions in the README of the glitch project, and applying them to my article table I did the following:

```
app@watery-alder-carpenter:~ 15:47
$ cd .data

app@watery-alder-carpenter:~/.data 15:47
$ ls
data.db

app@watery-alder-carpenter:~/.data 15:47
$ sqlite-utils tables data.db --table --columns
table    columns
-------  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
article  ['title', 'DOI', 'URL', 'created', 'subject', 'references-count', 'is-referenced-by-count', 'ISSN', 'container-title', 'abstract', 'author_number', 'orcids', 'names', 'award_numbers', 'funder_names', 'funder_dois']
example  ['headline', 'body', 'url', 'extra']

app@watery-alder-carpenter:~/.data 15:47
$ sqlite-utils enable-fts data.db article title subject abstract funder_names --fts4
```

This then created a search field on the article table that searches over title, abstract, subjects and funder names.

# Conclusion

I'm really impressed with Datasette. It supports a huge number of features and plugins that I didn't get a chance to look at at all today. These include:

- inspect and modify SQL queries  
- JSON endpoints  
- geo mapping
- saved searches  
- charting
- per database and per-table metadata
- setting default sort orders
- setting which columns can be sorted by
- enabling facets via uri e.g. [https://watery-alder-carpenter.glitch.me/data/article?_facet=created]()  
- support for adding SSO, user accounts or API key  


Overall how we share data, or make data visible online can often be a huge pain. Datasette goes a long way to proiving a set of tools to radically reduce the pain of doing this. I'm really glad that I took a few hours today to look at this tool.


```python

```
