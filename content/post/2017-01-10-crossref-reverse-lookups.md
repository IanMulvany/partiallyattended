---
categories:
- publishing
- citations
- doi
- programming
- crossref
date: 2017-01-10T00:00:00Z
title: Reverse DOI lookups with Crossref
url: /2017/01/10/crossref-reverse-lookups/
---

Today I had a need to think about how to do a reverse lookup of a formatted citation to find a DOI. 

[@CrossrefOrg](https://twitter.com/crossreforg) helped out and pointed me to the `reverse` api endpoint. It workes like this:


`http://api.crossref.org/reverse`

Created a json payload file “citation.json” formatted as follows:

```json 
[
  "	Curtis, J. R., Wenrich, M. D., Carline, J. D., Shannon, S. E., Ambrozy, D. M., & Ramsey, P. G. (2001). Understanding physicians’ skills at providing end-of-life care: Perspectives of patients, families, and health care workers. Journal of General Internal Medicine, 16, 41-49.
  "
]
```

Call the API using CURL (you need to set the Content-Type header to application/json)

>
   $ curl -vX POST http://api.crossref.org/reverse -d @citation.json --header "Content-Type: application/json"

I then got the following response:

```json
{"status":"ok","message-type":"work","message-version":"1.0.0","message":{"indexed":{"date-parts":[[2016,10,25]],"date-time":"2016-10-25T11:17:12Z","timestamp":1477394232160},"reference-count":21,"publisher":"Springer Nature","issue":"1","content-domain":{"domain":[],"crossmark-restriction":false},"short-container-title":["J Gen Intern Med"],"cited-count":0,"published-print":{"date-parts":[[2001,1]]},"DOI":"10.1111\/j.1525-1497.2001.00333.x","type":"journal-article","created":{"date-parts":[[2004,6,9]],"date-time":"2004-06-09T16:44:02Z","timestamp":1086799442000},"page":"41-49","source":"CrossRef","title":["Understanding Physicians' Skills at Providing End-of-Life Care. Perspectives of Patients, Families, and Health Care Workers"],"prefix":"http:\/\/id.crossref.org\/prefix\/10.1007","volume":"16","author":[{"given":"J. Randall”,"family":"Curtis","affiliation":[]},{"given":"Marjorie D.","family":"Wenrich","affiliation":[]},{"given":"Jan D.","family":"Carline","affiliation":[]},{"given":"Sarah E.","family":"Shannon","affiliation":[]},{"given":"Donna M.","family":"Ambrozy","affiliation":[]},{"given":"Paul G.","family":"Ramsey","affiliation":[]}],"member":"http:\/\/id.crossref.org\/member\/297","container-title":["Journal of General Internal Medicine"],"original-title":[],"deposited":{"date-parts":[[2011,8,10]],"date-time":"2011-08-10T15:39:02Z","timestamp":1312990742000},"score":120.61636,"subtitle":[],"short-title":[],"issued":{"date-parts":[[2001,1]]},"alternative-id":["10.1111\/j.1525-1497.2001.00333.x"],"URL":"http:\/\/dx.doi.org\/10.1111\/j.1525-1497.2001.00333.x","ISSN":["0884-8734","1525-1497"],"citing-count":21,"subject":["Internal Medicine"]}}
```

From this we can see that crossref suggests the following DOI lookup with a score of “120” 
http:\/\/dx.doi.org\/10.1111\/j.1525-1497.2001.00333.x 

There is some backslash escaping going on here, so the actual lookup url is:
[http://dx.doi.org\/10.1111/j.1525-1497.2001.00333.x](). 

This directs us the the following [article](http://onlinelibrary.wiley.com/doi/10.1111/j.1525-1497.2001.00333.x/abstract;jsessionid=12FD9F17A25B963F3E7D03C42AB137A7.f03t03?systemMessage=Wiley+Online+Library+Journal+subscribe+and+renew+pages+for+some+journals+will+be+unavailable+on+Wednesday+11th+January+2017+from+06%3A00-12%3A00+GMT+%2F+01%3A00-07%3A00+EST+%2F+14%3A00-20%3A00+SGT+for+essential+maintenance.+Apologies+for+the+inconvenience), which does seem to be the one that we are interested in.



