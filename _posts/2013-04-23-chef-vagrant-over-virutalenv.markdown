---
layout: post
title: Communicating better, moving from virtualenv to vagrant/Chef
categories: 
- python
- chef
- vagrant
- sysops
- ipython
- development
- communication
---

I've been using [virtualenv][vev] for a while, but in the past few months, since taking up the role of head of technology for eLife, I've been giving much more thought about how to build scalable development environments. 

Ever since I was managing [connotea][con], one of the biggest pains has been [configuration management][conconfig]. I seem to have spent almost more time on configuring environments than on actually doing any development work (disclaimer, I don't actually do much coding, I usually do more product management, but it's really useful to know the development pain points). 

[con]: http://en.wikipedia.org/wiki/Connotea
[conconfig]: http://www.mulvany.net/files/README.osx.html 

For sure package installation has gotten a lot easier over the past couple of decades. In the 1990's I was up to my next in make files, now I usually just `pip install` something. 

[virtualenv][vev] has been really nice for working with different versions of the same library on the same system, but this week I ran into a problem when trying to make [iPython][ipy] aware of the packages installed within a virtual environment. The result was an afternoon of faff. 

At the same time I've been learning about [vagrant][vagrant], [chef][cs] and that toolchain. Over the weekend I wondered if it could provide a replacement for virtualenv. After mucking around for a few hours
with [librarian][lib], [Vagrant][vagrant] and [chef solo][cs] I ended with a virtual machine with a number of python packages installed, running an instance of [iPython Notebook][ipn] that can be accessed from the host browser via port forwarding. 

[ipy]: http://ipython.org/
[ipn]: http://ipython.org/ipython-doc/dev/interactive/htmlnotebook.html
[lib]: https://github.com/applicationsonline/librarian
[cs]: http://wiki.opscode.com/display/chef/Chef+Solo
[vagrant]: http://www.vagrantup.com/
[vev]: http://www.virtualenv.org/en/latest/

If you have already have [Vagrant][vagrant], [chef solo][cs] and [librarian][lib] installed you can have it too by following these steps  

>   $ git clone git://github.com/elifesciences/elife-template-env.git
>   $ cd elife-template-env
>   $ librarian-chef install
>   $ vagrant up
>   $ vagrant ssh
>   $ ipython notebook --ip=192.168.33.10  


Then in your host browser open [http://192.168.33.10:8888](http://192.168.33.10:8888). 

The [elife-template-env][ete] repo contains a longer description of the setup.

[ete]: https://github.com/elifesciences/elife-template-env

It strikes me that this way forward is a much friendlier way of packaging code. With an upcoming release of Vagrant one would also be able to deploy immediate to AWS. I was chatting to someone last night about good development practices. When we write code in a team we are communicating with other developers. How we decide to package our work is also an act of communication. I think that the vagrant approach has a lot going for it. You take a definite performance hit in setting up the VM on first run , so I'm already planning on upgrading my setup. On the other hand, in principle you get systems that can be shared really painlessly, and on balance that feels like the more important aspect. 

It will be interesting to see if the packaged approach also has any hope of uptake in the distribution of scientific research. We are already in discussion with a number of researchers who are interested in this idea, but I'm not sure there enough familiarity with the tools to make it take off super quickly. I'm hopeful though, as the tools are getting easier to use all the time.