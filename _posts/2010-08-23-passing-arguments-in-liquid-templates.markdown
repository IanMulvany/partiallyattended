---
layout: post
title: Passing arguments in liquid templates.
categories:
- ruby 
- liquid
- templating
---

I've recently moved my blog over to hosting on github using the Jekyll templating system.  I was intrigued by the ability of Jekyll to create a listing for related posts, but in the end the quality was poor.  There are two methods avilable, the more robust uses latent semantic indexing, but this is not supported by github.  I can understand this, as the processing required is a bit too much of an overhead for a lightweight hosting service.  The other method is a fast method, but for all of the posts that I tried it against it only ever produced the last three posts that I had created.

I really liked the idea of having some related content after each post, so I decided to pull out posts that were related by tags. I like tags a lot.  In order to do this I needed to iterate over each set of posts for each category from the categories for the given page.  This looks something like:

<pre>
&#123;% highlight html %&#125; 
&#123;% for category in page.categories %&#125;
  do stuff
&#123;% endfor %&#125;
&#123;% endhighlight %&#125;
</pre>

The problem that I was having is trying to figure out how to pass the value of 'category' to the next loop.  I didn't find any documentation, but after trying out some random syntax hit on the following, which seems to work:

<pre>
&#123;% for category in page.categories %&#125;
  &#123;% for post in site.categories.[category] %&#125;
	do stuff
  &#123;% endfor %&#125;
&#123;% endfor %&#125;
</pre>

The important line is:
<code>
  &#123;% for post in site.categories.[category] %&#125;
</code>

And the piece of syntax that make is work is encasing category in brackets <code>[category]</code>.


