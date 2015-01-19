---
layout: page
title: Posts by date
---

  
{% for post in site.posts %}
  <span>{{ post.date | date_to_string }}</span> &rarr; <a href="{{ post.url }}">{{ post.title }}</a>
{% endfor %}
  
