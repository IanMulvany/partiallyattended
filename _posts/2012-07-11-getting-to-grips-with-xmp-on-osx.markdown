---
layout: post
title: XMP wrangling on OS X
categories: 
- xmp
- pdf
- adobe
- metadata
---

# XMP

[XMP][xmp] is the extensible metadata platform from Adobe. It can be used to embed structured metadata into a file. I think it's most common usage is for storing image metadata in image files, but it also has a use in embedding metadata in PDF files. 

Adobe provide an [SDK][xmpsdk] that you can use to start coding applications for working with XMP. They provide a guide for developers, and I've posted a [copy][dev] so you can have a quick look if you are interested, without downloading the full SDK.

[xmp]: http://www.adobe.com/products/xmp/
[xmpsdk]: http://www.adobe.com/devnet/xmp.html
[dev]: https://dl.dropbox.com/u/2270414/XMPProgrammersGuide.pdf

In this post I will look at compiling the SDK on OSX 10.7.4 with Xcode 4.3.2, and run through getting one of the demo applications provided in the SDK working. This was my first time working with Xcode, so I have certainly done some stupid things with setting up the environment, however in the end it worked. YMMV.

# Compiling the XMP libraries on OSX 10.7.4 with Xcode 4.3.2

I was unable to get the provided SDK to compile on my machine with Xcode 4.3.2. I kept running into issues that I just didn't understand in how the distributed Xcode project was set up. I was bitching about this on Twitter and the amazing [Matias Piipari][mz2] offered to have a look. He said:

[mz2]: https://twitter.com/mz2

>They'd done this silly thing where they require you to download 3rd party code and place it inside the project root, and then they hard-code the relative paths to those 3rd party source files in the #includes. Both expat and zlib are actually available as part of the OSX SDK, but was easier to just download zlib and unpackage them both into that 3rd-party directory rather than fix the includes to use systemwide header search paths and to set up dynamic linking for expat and zlib.

He modified the distributed project as described, and sent me a [copy][working]. Downloading this, and following the build instructions from the programmers guide compiles the libraries, raising about 54 warnings on my machine.

[working]: https://www.dropbox.com/sh/gceyj2ieuvme1aa/9FONH2OF2b

# Building a demo application using the compiled libraries. The 

First step, we need to set up a project in Xcode.

## Creating an Xcode project to read XMP metadata

The following is based on the instructions from the developers guide, which start on page 62, however there are quite a few differences between the provided instructions, and what I did to get the sample code working.

1. Create a new project `File > New > Project ...` or &#8679;&#8984;N
2. Select the `Command Line tool` option.
3. Hit `next`.
4. Name your product, pick your company name and choose `C++` for the project type.
5. You will then be asked to chose where to save the project. I'm saving my project in `/Users/ian/code/private-code/xmp/XMP-Toolkit-SDK-5.1.2/samples/build/Xcode3/`, with the project name `MyReadingXMP`. Hit `save`.
I have git installed on my system, and Xcode offers to place the project under source control, why not, let's go with that.
6. In the project window, highlight the file main.cpp and delete it by choosing `Edit > Delete` or &#8984;&#9003;. In the
confirmation dialog select `Move to Trash`.
7. Add a new file, there are many options for adding a new file, &#8984;N works. This brings up the file template chooser.
8. Pick a `C++` file, hit `Next`.
9. Name the file `MyReadingXMP.cpp`. The instructions in the programmers guide tell you to deselect the option to create a header file, however the version of Xcode that we are working with does not offer to create a header file, so you can ignore this step. 

## Compiling the application. 

Selecting the project in the left hand pane of Xcode will show the project info and build settings in the central pane:

![Xcode settings](/images/xcode-settings.jpg "Xcode settings")

For finding the various options in the build settings, the search field is convenient.

1. Select `Build Settings` and under `Build Locations`select `Per-configuration Build Products Path`.
2. Insert `$(PROJECT_DIR)`, you should see Xcode expand this to point to the directory that contains the project files. 
3. Under `Search Paths` select `Header Search Paths`. The XMP developer documentation says to include `${SDKROOT}/public/include`. This is where things started to go tits up for me. There is a [bug report][bug] on the adobe forums pointing out that the developer documentation is broken at this step, and that one should insert `<xmpsdk>` in place of `${SDKROOT}`, but I didn't get it to work with this substitution either, so I started to hard code the paths. This is a bad practice, but it was the way that I got it to work. If I knew a little more about Xcode I am sure this would be trivial to fix, but for now I started to use `/Users/ian/code/private-code/xmp/XMP-Toolkit-SDK-5.1.2/` in every place in the documentation where you are advised to use `${SDKROOT}`, so we put in `/Users/ian/code/private-code/xmp/XMP-Toolkit-SDK-5.1.2/public/include` for this variable.
4. Select Framework Search Paths and enter `/Users/ian/code/private-code/xmp/XMP-Toolkit-SDK-5.1.2/System/Library/Frameworks`. When I finally got to the compile stage I was getting a warning that this directory didn't exist, so I manually created that directory inside of the project.
5. Deselect `Precompiled Header Uses Files From Build Directory`.
6. Select Other Linker Flags and add the paths to both the XMP Toolkit SDK static libraries:
`/Users/ian/code/private-code/xmp/XMP-Toolkit-SDK-5.1.2/public/libraries/macintosh/debug/libXMPCoreStaticDebug.a`
`/Users/ian/code/private-code/xmp/XMP-Toolkit-SDK-5.1.2/public/libraries/macintosh/debug/libXMPFilesStaticDebug.a`
7. In Other Linker Flags, at the end of the paths to the static libraries enter the flag `-framework CoreServices`. At this point I may have tried compiling the empty project, or I may have toggled some other interaction with Xcode, in any case Xcode began downloading the CoreServices framework.
8. Select `Preprocessor Macros` and enter `MAC_ENV=1`
9. The instructions provided direct you to set the Preprocessor Macros for the target, however in this version of Xcode when I looked, this setting carried over from the project setting, and I didn't need to do anything.

[bug]: http://forums.adobe.com/message/3234962

I tried compiling the empty project, but ran into some bugs. I then cut and pasted the entire sample XMP reader code into the my empty project. I also manually linked the CoreServices library against the target using the `Build Phases` option Xcode. 

![Link Xcode target to CoreServices](/images/set-services.jpg "Link Xcode target to CoreServices")

I honestly don't know what I am doing at this point, and I don't know whether this helped, but on the next attempt to compile the project compiled fully, and I got an executable. 

It took me a while to find where the executable was located, but eventually I found it located in 

	~/Library/Developer/Xcode/DerivedData/
	MyXMPReader-dzqqlyrtudnrpsganqbsozskatkp/
	Build/Products/Debug /Users/ian/code/
	private-code/xmp/XMP-Toolkit-SDK-5.1.2/
	samples/build/Xcode3/MyXMPReader

Obviously I've made a typo in the name of the target, you can see that I have an extra space next to the `../Debug /..` part of the path, and I had expected the executable to land in the project directory, rather than in the system Library, but we have the working executable 'MyXMPReader'.

## Running the application

It's a command line application, and takes a path to a file as an argument. To run this, point it at a PDF like so:

`$ MyXMPReader test.pdf` 

It produces some terminal output, and writes the XMP data into a local `XMPDump.txt` file. I verified the tool works by running it against a nature communications pdf, and you can see some of the output here:

{% highlight xml %}
$ head -40 XMPDump.txt 
Dumping XMPMeta object ""  (0x0)

   dc:  http://purl.org/dc/elements/1.1/  (0x80000000 : schema)
      dc:format = "application/pdf"
      dc:identifier = "
            doi:10.1038/ncomms1828"
      dc:creator  (0x600 : isOrdered isArray)
         [1] = "Zhong Yan"
         [2] = "Guanxiong Liu"
         [3] = "Javed M. Khan"
         [4] = "Alexander A. Balandin"
      dc:description  (0x1E00 : isLangAlt isAlt isOrdered isArray)
         [1] = "Nature Communications 3, 827 (2012). doi:10.1038/ncomms1828"  (0x50 : hasLang hasQual)
               ? xml:lang = "x-default"  (0x20 : isQual)
      dc:publisher  (0x200 : isArray)
         [1] = "Nature Publishing Group"
      dc:rights  (0x1E00 : isLangAlt isAlt isOrdered isArray)
         [1] = "<C2 A9> 2012 Nature Publishing Group, a division of Macmillan Publishers Limited. All Rights Reserved."  (0x50 : hasLang hasQual)
               ? xml:lang = "x-default"  (0x20 : isQual)
      dc:title  (0x1E00 : isLangAlt isAlt isOrdered isArray)
         [1] = "Graphene quilts for thermal management of high-power GaN transistors"  (0x50 : hasLang hasQual)
               ? xml:lang = "x-default"  (0x20 : isQual)

   pdf:  http://ns.adobe.com/pdf/1.3/  (0x80000000 : schema)
      pdf:Producer = "Adobe PDF Library 7.0"

   prism:  http://prismstandard.org/namespaces/basic/2.0/  (0x80000000 : schema)
      prism:copyright = "
            <C2 A9> 2012 Nature Publishing Group, a division of Macmillan Publishers Limited. All Rights Reserved."
      prism:doi = "10.1038/ncomms1828"
      prism:eIssn = "2041-1723"
      prism:endingPage = "8"
      prism:publicationName = "Nature Communications"
      prism:rightsAgent = "permissions@nature.com"
      prism:startingPage = "827"
      prism:volume = "3"
      prism:publicationDate  (0x200 : isArray)
         [1] = "--"
      prism:url  (0x200 : isArray)
{% endhighlight %}

I'll explore some other tools that you can use to look at XMP data in pdfs in a later post, and I'll also look at what we can find inside some recently published academic PDFs with an eye to deciding what we should be putting into the documents that we will be producing at [eLife][elife] (don't forget to [submit][submit]).

[elife]: http://elifesciences.org/ 
[submit]: http://submit.elifesciences.org/cgi-bin/main.plex
