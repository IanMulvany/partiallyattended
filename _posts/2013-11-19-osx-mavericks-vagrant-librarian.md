---
layout: post
title: Setting up Vagrant, Librarian-Chef and Vagrant aws plugins on OSX Mavericks. 
categories: 
- OSX
- Mavericks
- mac
- development
- chef
- ruby
- vagrant
- aws
- sys-ops
- tutorial
- librarian
- rvm
---

I have a new macbook pro. I want to install vagrant, chef and librarian, with the vagrant-aws plugins. I'm working on OSX Mavericks, and I want to get as clean an install as possible. For the most part I am also using the fish shell. This is what I've just run through over the last 20 minutes. 

1. Install command line tools from the terminal  
	`$ xcode-select --install`

Next we are going to install homebrew, with homebrew we will install `rvm` and with `rvm` we will install ruby. The goal is to have a ruby avilable at `/usr/local/bin` and to avoid using the system provided ruby, which is at `/usr/bin`.

2. install homebrew  
	`$ ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"`

3. update homebrew  
	`$ brew doctor`
	`$ brew update`

`$ brew doctor` will do a healthcheck. As a result of running this I was reminded to re-order my `$PATH` to point to `\usr\local\bin` over '\usr\bin'.

4. Install prequisites for rvm  
	`$ brew install autoconf automake libtool libyaml readline libksba openssl`

5. Install `rvm`  
	`$ curl -L https://get.rvm.io | bash -s stable`

6. Install a ruby  
	`$ rvm install ruby-2.0.0-p247`   
	`$ which ruby` will now return something like `/Users/ian/.rvm/rubies/ruby-2.0.0-p247/bin/ruby`

7. I use the [fish](http://fishshell.com) shell, and for some reason after intalling ruby with rvm the order of my `$PATH` got rearranged, so I rest `\usr\local\bin` to the front with   
	`$ set PATH /usr/local/bin $PATH`

8. OK, now we can try to install librarian with
	`$ gem install librarian-chef`

9. This installs 31 gems on my system - fun! I immediatly tested this in a repo with a working `Cheffile`, for a long running project that is ongoing withing [eLife](http://elife.elifesciences.org). 
	`$ librarian-chef install` 

This worked, and downloaded 21 `chef` repositories, as expected. I'm feeling pretty good at this point.   

10. Let's also get vagrant. I downloaded the latest version of vagrant - [version 1.3.5](http://downloads.vagrantup.com/tags/v1.3.5), and installed it via dmg. 
After this `$ which vagrant` returns `\usr\bin\vagrant`, and `$ vagrant -v` returns `Vagrant 1.3.5`.  

11. Let's install the aws-plugin for vagrant. We do this with   
	`$ vagrant plugin install vagrant-aws`

That gets me `Installed the plugin 'vagrant-aws (0.4.0)'!`, yay!!. We still need to install chef, and check that vagrant up works on the project. 







