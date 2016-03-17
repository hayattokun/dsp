# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > `touch <fileName>` = create an empty file
> > `cat <fileName>` = streams content of file (i.e. in-line)
> > `less <fileName>` = lets you view content of file (w/ paging)
> > `find . -name ".txt"` = search for files whose names end in ".txt"
> > `cat > <filename>` = cat will read whatever you type and then write it to that file
> > `grep <someText>` <fileName> = searches in file and prints lines that include <someText>
> > `man <command>` = shows manual for command
> > `>` at the end of a command to redirect the result to a file
> > `>>` to redirect the result to the end of a file
> > `|` at the end of a command to enter another command that operates on the output of the first command

---

###Q2.  List Files in Unix   

What do the following commands do:  

> > `ls`  = lists files in working directory
> > `ls -a`  = lists files in working directory (incl. files starting with '.')
> > `ls -l`  = lists files in working directory (shows list in long format)
> > `ls -lh`  = lists files in working directory (shows list in long format with unit suffixes: Byte, Kilobyte, Megabyte, Gigabyte, etc.)
> > `ls -lah`  = combines above commands
> > `ls -t`  = lists files in working directory (sorted by time modified starting w/ most recently modified file)
> > `ls -Glp`  = lists files in working directory (shows list in long format w/ colors and "/" after any directory name)

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > `ls -R` = lists subdirectories as well
> > `ls -1` = displays each entry on separate line
> > `ls -m` = displays the names as a comma-separated list
> > `ls -t` = displays newest files first
> > `ls -r` = displays entries in reverse order

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > `xargs` reads items from the standard input, delimited by blanks or newlines, and executes the command one or more times with any initial-arguments followed by items read from standard input.
> > (ex) `find . -name "*.txt" -print0 | xargs -0 -p rm`

 

