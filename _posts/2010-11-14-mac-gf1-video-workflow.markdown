---
layout: post
title: Video workflow with a mac using iMovie and capturing with a Lumix GF1
categories:
- photography
- video
- iMovie
- mac
- GF1
- mp4
- MOV
- Handbrake
- AVCHD
---

I'm figuring out the best way to shoot video with my Lumix GF1 on a mac using iMovie.  The GF1 offers two main options for video capture, HD JPEG, and AVCHD.  There is a great post describing the pros and cons of these two formats here [], and based on that I decided to experiment with AVCHD. After playing around a little I found a few oddities.
JPEG capture writes the files onto the device as .MOV files inside the relevant directory, along with any images that you capture.  By manually looking through the memory card from my camera I found these files in /DCIM/102_PANA, where the number before the _PANA will be specific to which set of images you are capturing. 


When I tried adding the .MOV files directly to iMovie by opening the camera as an attached device from within iMovie iMovie didn't see these .MOV files. I was only able to add these files to iMovie, either manually, via image capture, or via adding these videos first to iPhoto. 


On the other hand, when I look at the device from iMovie, iMovie does see the videos that I captures as AVCHD, and imports them.  From the post that I read to see what the differences are between these two formats I was expecting videos that were captures as AVCHD to be much smaller that JPEG videos, but on first examination that was not the case. I shot about one minute of the same scene in both formats, and I got the following file sizes:


JPEG HD capture: sample.MOV 293 MB
ACHVD capture, after import to iMovie: sample.mov 383.7 MB


The ACHVD file is on the camera device in the following folder: /PRIVATE/AVCHD/BDMV/STREAM/sample.MTS and has a size of 129 MB.


There is obviously some conversion going on during the iMovie import. iMovie will also not directly import the .MTS file, but needs to be looking at the camera as an attached device. 


I decided to try converting the .MTS file via handbrake, and import the converted file.


- original sample.MTS 129MB
- handbrake converted file sample.mp4 20.6 MB
- iMovie imported mp4 file sample_converted_imported.mov 368.6 MB

So I gained a little, but not very much at all.

Taking this clip and exporting it as a HD movie using iMovie I get the following file: imove_export.mov 119.1 MB, and this is actually pretty close in size to the original .MTS file stored on the camera. I can use handbrake again on this file to get an mp4 file of the size 20.9 MB.

I don't know what is going on under the hood when iMovie makes it's internal conversion from the .MTS format to the .MOV format, so I don't know whether going straight into iMovie from the camera, or going via a conversion with Handbrake will end up with a better quality movie at the end or not.  I'm lazy, so I'll probably use the following workflow, suck up files using iMovie, at the same time store the .MTS files locally in case I want to clear out the iMovie archive, and work on the originals later. That seems to give me the best balance between a low friction workflow, and having manageable files. When I get some sample video out, I'll post some of them on this blog.

