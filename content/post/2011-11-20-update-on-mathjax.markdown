---
categories:
- mathjax
- latex
- github-pages
- javascript
date: 2011-11-20T00:00:00Z
title: Update on MathJax
url: /2011/11/20/update-on-mathjax/
---

[MathJax][mj] has come a long way since I last looked at it. There is now a CDN hosting the js files, which makes calling it 
really really easy. It's being adopted by GiHub for their wiki engine.

Using it with markdown can cause a few bumps, but there seems to be a bunch of ways around this:

* [mathjax in markdown][mim] using some mathjax configuration and custom css
* [amazing implimentation][ai] in a notetaking app
* [php, mathjax and wordpress][phpm]


Writing a block of %%\LaTeX%% like this
<pre>
$$
\begin{aligned}
\dot{x} &amp; = \sigma(y-x) \\
\dot{y} &amp; = \rho x - y - xz \\
\dot{z} &amp; = -\beta z + xy
\end{aligned} 
$$
</pre>

will render like this

$$
\begin{aligned}
\dot{x} &amp; = \sigma(y-x) \\
\dot{y} &amp; = \rho x - y - xz \\
\dot{z} &amp; = -\beta z + xy
\end{aligned} 
$$

[mj]: http://www.mathjax.org/
[news]: http://www.mathjax.org/2010/08/16/news/github-chooses-mathjax-for-math-support/
[mim]: http://doswa.com/2011/07/20/mathjax-in-markdown.html i
[ai]: http://notepag.es/latexdemo
[phpm]: http://www.leancrew.com/all-this/2010/09/php-markdown-extra-math-mathjax-and-wordpress/
