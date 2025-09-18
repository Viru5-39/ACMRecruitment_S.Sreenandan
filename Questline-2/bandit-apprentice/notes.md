OverTheWire Wargame levels 0-10

LEVEL-0

This level was pretty simple.
I first connected to overthewire using ssh (secure shell) command and used the cat(short for concatenate) command to read the readme file to get the password to the next level

LEVEL-1

I first logged in using ssh command with the appropriate username and password required for this level.
This level involved getting the password to the next level from a file.
So I listed out all the files using the ls(list) command.
Then there was a file named '-'. Since it was the only file present, I instantly knew it contained the password
And finally, with the cat command, I had to use the './' symbol so that the bash could treat the - symbol as a file name.

LEVEL-2

I logged in with the required username and password by using the ssh command.
In this level, the name of the file included spaces. 
So, for the bash to consider the file name flawlessly, I enclosed the file name in double quotes("") along with the ./ symbol in the cat command so that the bash considers it as one entity.

LEVEL-3

I logged in with the required username and password for this level by using the ssh command.
This level involved retrieving password from a hidden file in a directory named inhere.
So, I changed directory to inhere using cd(change directory) command.
Then, I listed out all files using ls -a, meaning list all storage. This displays all the hidden files.
From the files, There was only one non-root file, whose name actually included dots.
Then while using the cat command, I enclosed the file name in double quotes.

LEVEL-4

I logged in with the required username and password for this level by using the ssh command.
Then I changed the directory to inhere using the cd command.
Thereafter I long listed all files using ls -l.
Then I used the file command and the wildcard ./* To check the correct type of all files.
There was only one file which had ASCII text type. I realised that should be the one.
And finally, I used the cat command to extract the password.

LEVEL-5

I logged in with the required username and password for this level by using the ssh command.
Then I changed directory to inhere.
I long listed out all the files in it only to realize they were directories.
So, I used the find command to filter out the correct file matching the given criteria(size=1033 bytes and non executable).
Finally, I used the cat command and enclosed the obtained path in double quotes.

LEVEL-6

I logged in with the required username and password by using the ssh command.
Then I used the find command to filter out the password since there were a lot of files.
This was the exact command I used:
find / -user bandit7 -group bandit6 -size 33c 2>/dev/null -exec cat {} \;
Breaking down the command;
 find / → search from root
 -user bandit7 → file owner
 -group bandit6 → group owner
 -size 33c → exactly 33 bytes
 2>/dev/null → hide permission errors
 -exec cat {} \; → directly show the contents of each matching file.

LEVEL-7

I logged in with the required username and password for this level by using the ssh command.
This involved a text file named data.txt, in which the password was lying near a word 'millionth'.
So, since the grep command is used for pattern detection, I used it to track down the password seamlessly.

LEVEL-8

I logged in with the required username and password for this level by using the ssh command.
The main challenge was to find the password, which was unique, from a file which had recurring strings.
So, I used the sort command and uniq command together to sort the data.txt file and retrieving the only unique string.

LEVEL-9

I logged in with the required username and password for this level by using the ssh command.
This challenge involved retrieving the password from a bunch of unreadable and readable strings.
So, I used the strings command to filter out the readable strings from the lot.
I easily spotted the right password since it had preceding = symbols.

LEVEL-10

I logged in with the required username and password for this level by using the ssh command.
From the description of the challenge, I realized that the password was encoded in base64 format.
Then I used the base64 -d(base64 decode) command to retrieve the password.
