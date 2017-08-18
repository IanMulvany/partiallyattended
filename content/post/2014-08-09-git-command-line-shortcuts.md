---
categories:
- git
- command line
date: 2014-08-09T00:00:00Z
title: shortcuts that I use for the git command line
url: /2014/08/09/git-command-line-shortcuts/
---

I use git a lot, it's pretty complicated, and it has a lot of command line optoins that I can never remember. I've copied
a couple of shortcuts from the web, and here are two that I use a lot. These are presented in the form of [fish shell](http://fishshell.com) scripts.

>
function gl
        git log --graph --abbrev-commit 
        --decorate --date=relative 
        --format=format:'%C(bold blue)%h%C(reset) 
        - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset)
        %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)' 
        --all
end

This provides a nicer view on the git log, with the brancing tree also displayed. 


>
function branches
git for-each-ref --sort=-committerdate refs/heads/
git for-each-ref --sort=-committerdate refs/heads/ 
  --format='%(refname) %(committerdate) %(authorname)'
  | sed 's/refs\/heads\///g'
end

This shows two lists of current brances in the repo, in reverse chronological order. The first list provides the full sha, 
and the second list shows the last commit message. This is useful when coming back to repo that has a few branches, to help you get an
overview of the activity that's happened in the different branches. 

I put these examples into a [gist file](https://gist.github.com/IanMulvany/3591216fb05b18f97b98)
