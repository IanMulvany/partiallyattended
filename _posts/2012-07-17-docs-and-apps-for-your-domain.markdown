---
layout: post
title: sharing documents with google apps for your domain
categories:
- google
- gdrive
- gdocs
---

I've just rolled out google apps for your domain for eLife. At about the same time google rolled out gdrive. We were having difficulty figuring out how to share documents across the domain without having to invite people individually to the document. The document sharing options provide the ability to make documents findable by other members of the domain, but when we tried to search for these documents, we were not finding them.

Finally I found the solution in a [support question][sup] form google, but it took me longer to find than I expected.

> "Sharing a document such that it automatically appears in the document lists for all users in the domain is not currently supported."

> Sharing a document or collection with a domain allows users in the domain to find the item by searching, but it doesn't automatically add the document to all users' document lists. <font color="green">To search for a document that has been shared with your domain, open Google Docs, type the relevant keywords into the search bar, then click the triangle on the right side of the search bar and choose Search [your domain] Docs.</font>

> Alternately, you can share the document with a group that contains all users in the domain. Note that group members need to click the link in the notification email for the document to show up in their document lists.

> Sharing a document such that it automatically appears in the document lists for all users in the domain is not currently supported. However, you can use the Documents List API to share the document explicitly with all users. This method ensures that the document shows up for all current users, but it requires familiarity with using APIs.

[sup]: http://support.google.com/a/bin/static.py?hl=en&ts=2404805&page=ts.cs