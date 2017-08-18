---
categories:
- apple
- mail
- applescript
date: 2010-10-18T00:00:00Z
title: save mailfolder messages to a file using applescript
url: /2010/10/18/save-mailfolder-messages-to-a-file-using-applescript/
---

I'll just start by explaining that I hate applescript. I wanted to create a script that would take a specific folder withing the script and save each message from that folder to a text file on my machine for post-processing.

This is what I came up with.

{{< highlight applescript >}}
set fileRoot to "Macintosh HD:Users:path:"
set messageList to {}
tell application "Mail"
	set messageList to messageList & (messages of mailbox "mailbox name" of account "account" of application "Mail")
	set counter to 1
	repeat with theMessage in messageList
		set fileNum to counter as string
		set theFilePath to fileRoot & "mailcontent" & fileNum & ".txt"
		set p to POSIX path of theFilePath
		do shell script "touch " & p
		set theFileReference to open for access theFilePath with write permission
		set messageText to content of theMessage as string
		set sent to date sent of theMessage as string
		write sent to theFileReference starting at eof
		write "\n" to theFileReference starting at eof
		write messageText to theFileReference starting at eof
		close access theFileReference
		set counter to counter + 1
	end repeat
end tell
{{< / highlight >}}

It breaks down like this, the following script sets a list to be the messages in our names mailbox folder. We can then iterate over that array, getting attributes of each message, such as the message content or the sent date of the message:

{{< highlight applescript >}}
set messageList to {}
tell application "Mail"
	set messageList to messageList & (messages of mailbox "mailbox name" of account "account" of application "Mail")
	repeat with theMessage in messageList
		set messageText to content of theMessage as string
		set sent to date sent of theMessage as string
	end repeat
end tell
{{< / highlight >}}

Taking the creation of the file root out of the loop, and also adding a looping variable out of the loop the content inside the loop now looks like:

{{< highlight applescript >}}
set fileNum to counter as string
set theFilePath to fileRoot & "mailcontent" & fileNum & ".txt"
set p to POSIX path of theFilePath
do shell script "touch " & p
set theFileReference to open for access theFilePath with write permission
set messageText to content of theMessage as string
set sent to date sent of theMessage as string
write sent to theFileReference starting at eof
write "\n" to theFileReference starting at eof
write messageText to theFileReference starting at eof
close access theFileReference
set counter to counter + 1
{{< / highlight >}}

Looking in a bit more detail, we convert the counter (an int) into a string. We set the filepath to a base filename, the string version of the counter, and a file extension.  In order to ensure that the file exists we pass this path to a shell script, and "touch" the file. That's right, in order not to get fucked over by applescripts error handling, I've just called out to the system shell as the most useful way of creating a filehandler to a file that might not extist. Jesus.

{{< highlight applescript >}}
set fileNum to counter as string
set theFilePath to fileRoot & "mailcontent" & fileNum & ".txt"
set p to POSIX path of theFilePath
do shell script "touch " & p
{{< / highlight >}}

The second part of the loop now creates the file handler, writes some of the properties of the mail message into the file, closes the file handler, and iterates our loop counter.

{{< highlight applescript >}}
set theFileReference to open for access theFilePath with write permission
set messageText to content of theMessage as string
set sent to date sent of theMessage as string
write sent to theFileReference starting at eof
write "\n" to theFileReference starting at eof
write messageText to theFileReference starting at eof
close access theFileReference
set counter to counter + 1
{{< / highlight >}}
