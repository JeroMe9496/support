# COMMAND LINE INTERFACE
<h3>Must known bash commands</h3>
<p>Bash is an acronym for "Bourne Again Shell" named after Stephen Bourne, the creator of the Unix shell "sh."
</p>

<hr style="margin-bottom: 4em;">


## USEFUL FILE SYSTEM COMMANDS
<div style="padding: 0 0 0 2em; margin:0 0 4em;">

## **pwd** - Print Working Directory
```
$ pwd
/PowerCoders/GitHub/support/CLI
```

---

## **ls** - List (files and folders of the current working directory)
```
$ ls
dir1/  dir2/  README.md
```
add option -a to display also hidden files and folders 
```
$ ls -a
./  ../  .bob/  dir1/  dir2/  README.md
```

---

## **cd** - Change directory
```
$ cd /path/to/your/folder
```
*Note: if the path is too long, you can type **cd** and drag the folder into the bash window*

**cd ..** - *go to parent dir (one step above)*
```
$ cd ..
```
*or, go two or more steps above*
```
$ cd ../..
$ cd ../../..
etc.
```

---

## **touch** - Create a file
```
$ touch index.html
```
*creates a file named "index.html" into the current dir*
```
$ touch dir1/index.html
```
*creates a file named "index.html" into "dir1" (if dir exists)*

---

## **mkdir** - Make Directory
```
$ mkdir dir3
```
*creates a folder named "dir3" into the current dir*

---

## **rm** - Remove file/directory
```
$ rm index.html
```
*removes the file "index.html" (if exists)*
```
$ rm dir3
```
*removes the folder "dir3" (if exists and not empty!)*
```
$ rm dir3 -r
```
*removes the folder "dir3" even if not empty. **-r** stands for recursive*

---

## **mv** - Move file/directory
```
$ mv style.css dir1
or
$ mv style.css ./dir1
```
*moves "style.css" from current directory to dir1*

```
$ mv dir1/style.css .
or
$ mv dir1/style.css ./
```
*moves "style.css" from "dir1" to current directory*

---

## **cp** - Copy file/directory
```
$ cp style.css dir1
```
*to copy the file "style.css" to "dir1"*
```
$ cp -r dir1 dir2
```
*to copy "dir1" into "dir2" (-r option is for recursive)*

---

## **clear** - Clear bash window
```
$ clear
```

</div>


<hr style="margin-bottom: 4em;">


## OTHER USEFUL COMMANDS
<div style="padding: 0 0 0 2em; margin:2em 0 4em;">

## **nano** - Edit a file
```
$ nano file.txt
```
*will open "file.txt" inside bash editor*

### Inside nano editor
`CTRL + X` - to quit the editor (will be asked to save the file)

`Y/N` - to save or not the content

`ENTER` - to validate

---

## **cat** - See (the content of a) a (text) file
```
$ cat file.txt
```
if you want to see also the line numbers, add the option **-n**
```
$ cat file.txt -n
```

</div>


<hr style="margin-bottom: 4em;">


## USEFUL KEYBOARD SHORTCUTS
<div style="padding: 0 0 0 2em; margin:2em 0 4em;">

  1. **Up** / **Down** arrows **↑ ↓** - Use bash history
  2. **TAB** - 

</div>