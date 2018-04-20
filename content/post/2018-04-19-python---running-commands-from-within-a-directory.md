---
title: python - running commands from within a directory
url: 2018/04/19/python_-_running_commands_from_within_a_directory_/
date: 2018-04-19T00:00:00Z
categories:
- asilearn
- python
---

A neat python snippet for jumping into a directory, running a script, and jumping out again, found on Stackoverflow, provided by [Brian Hunt.](https://stackoverflow.com/users/19212/brian-m-hunt)

```python
from subprocess import Popen, PIPE
import os
import sys

class cd:
  """Context manager for changing the current working directory
  see https://stackoverflow.com/questions/431684/how-do-i-cd-in-python
  """
  def __init__(self, newPath):
    self.newPath = os.path.expanduser(newPath)

  def __enter__(self):
  self.savedPath = os.getcwd()
    os.chdir(self.newPath)

  def __exit__(self, etype, value, traceback):
    os.chdir(self.savedPath)

with cd("~/blog/partiallyattended"):
  title = new_post.title
  process = subprocess.call(["git", "commit", "-m","`new post: `"+title], \
  stdout=subprocess.PIPE)
```
