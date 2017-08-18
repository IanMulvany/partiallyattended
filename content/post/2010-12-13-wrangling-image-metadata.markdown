---
categories:
- exif
- picasa
- lightroom
- leap
- mac
- images
- raw
date: 2010-12-13T00:00:00Z
title: Wrangling image metadata
url: /2010/12/13/wrangling-image-metadata/
---

I'm trying to move away from iPhoto because I have lost too many pictures over the years from having multiple versions of an image lying around, from metadata being plopped all over the place. It is time to move to a more sustainable simple way of naming foldering and tagging my image archive.

In the course of looking at this I have been playing around with Lightroom, and I want to ensure that I can add tags at a system level on my mac, and have them show up in Lightroom, and at the same time have Lightroom tags discoverable through spotlight searches.

There are obviously many strategies.

What I have discovered so far is the following:

When you write metadata to a file from Lightroom, it writes that metadata into an associated xmp file.

When Lightroom reads metadata from a file it will read it straight from the exif profile in the file.

[exiftool][et] by Phil Harvey is the best commandline tool for interrogating and manipulating metadata at a low level. 

If I add a keywork in Picassa to a Raw file, nothing happens on disk, until I save my changes, and then Picassa creates a jpg version of the Raw file, and adds the keywords into the exif under both the "Subject" and "Keyword" tags. I guess I should just not use Picassa to edit keywords for a while. In fact from [this description][nuts] you see that Picassa does some hiding of the original versions of the files and you can't see the originals anymore. I don't really like this. 


[et]: http://www.sno.phy.queensu.ca/~phil/exiftool/
[nuts]: http://groups.google.com/group/Picasa/web/original-photo-files
