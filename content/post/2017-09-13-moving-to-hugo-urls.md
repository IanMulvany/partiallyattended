---
title: Moving from Jekyll to Hugo - urls
date: 2017-09-13T00:00:00Z
url: 2017/09/13/Moving_from_Jekyll_to_Hugo_-_urls/
categories:
- hugo
- jekyll
- blogging
- scripting
- python
---

I've been changing the static blog generator that I use and am slowly moving from Jekyll to Hugo. My main reason is the better support for tags and categories that Hugo supports, but I'm not finding the templating as intuitive in Hugo as in Jekyll, so it's not a slam-dunk.

There are a couple of small differences between the two systems that are making me reconfigure my blogging workflow a bit.

One of these is how the out of the box version of two systems set the publication date, and the path structure of posts (they both provide a lot of flexibility, but I'm kind of moving from a default to default configuration, so I have to make some changes.)

My setup in Jekyll takes the publication date from the file name, and then sets the path of the publication post to a structure based on the file name, and it also expects the publication date to be derived from this filename too. Files should reside in a `/posts` folder so for example a post in the following file `/posts/2017-09-13-my-shiney-post.md` will appear at the url [/2017/09/13/my-shiney-post/](/2017/09/13/my-shiney-post/).

In contrast Hugo expects posts to be in a folder inside a content folder, so it would expect to find our post in the following location `/content/post/2017-09-13-my-shiney-post.md`. It generates the url based on the location of the post in the folder structure, and it requires the publication date to be included in the `yaml` or `toml` header metadata of the individual post. The above post will appear at a url like the following one:
[post/2017-09-13-my-shiney-post/](post/2017-09-13-my-shiney-post/).

An example of post metadata that Hugo expects is like the following:

```
---
date: 2017-09-12T14:47:22+01:00
title: My Shiney Post
categories:
- one
- two
- three
---
```

Hugo chooses which template to use for the post based on it's directory location. In contrast Jekyll puts that information into the metadata, so the equivalent `yaml` header info in a jekyl post would look like

```
---
type: post
title: My Shiney Post
categories:
- one
- two
- three
---
```

So I like the url structure that Jekyll provides. It's a bit of a tossup, but pegging the post mostly against a date structure is closer to being a [cool url](https://www.w3.org/Provider/Style/URI) than a post with the type in the url.

On the other hand, after some experience with over-loading metadata into file names for another project, I am now convinced that having that kind of data in a filename is less good than putting that information into a structured metadata field.

I have to admit that one of the benefits of the Hugo system is you can easily partition the content on your site based on what kind of content it is by location on the file system, and having that reflect in the URL. That aside, given my posting archive already has the URL format `/YYYY/MM/DD/some-description/` then I want to try to preserve that for future content. I'm also going to keep the filename structure the same as before, as it's just nice to `ls` within a content directory and get a chronological listing of the content in the directory.

Hugo does allow you to set the publish url within the metadata, so I've decided to use that for my future posts.

The `yaml` will now look like:

```
---
date: 2017-09-12T14:47:22+01:00
title: My Shiney Post
url: /2017/09/21/my-shiney-post/
categories:
- one
- two
- three
---
```

In order to support generating this metadata, whilst on the train from Schiphol this morning to Den Haag I knocked up the following python script:

{{< gist IanMulvany fe2a728166e471537058d222a545304c >}}

This conveniently pushes the `yaml` data into the mac clipboard, so I can just paste it into the top of the document.
