# GITHUB MISC
Some tips useful to know

<br>

## Ignore file and folders when pushing to remote
Git have a special file named *.gitignore* that we can use to keep files and folders only on your local machine. They will be "ignored" when you use the **push** command.<br>

   1. **Create a file named *.gitignore* at the root of your local repo**<br>

   2. **Add one ignored file or folder by line**<br>
      For example, I want to ignore the *.gitignore* file itself and a folder named *.vscode*. So I'll open the file *.gitignore* and type :

      ```bash
      .gitignore
      .vscode/
      ```
   Save the file and you're good to go. When pushing to remote those two will be ignored.

<br>

---

<br>

## "Force" local files to match the remote files

   Sometimes you want to level up with the remote content and you don't care if you loose local changes. This can happen when you use another computer and you have some old files that you want to update (or remove).

   Go to your local folder :

   ```sh
   $ cd the/path/to/your/local/folder
   ```
   
   Fetch the the remote origin and reset local files by entering these commands in order :<br>
   
   ```sh
   $ git fetch origin master
   $ git reset --hard origin/master
   $ git clean -f
   ```

   > *See more [here](https://stackoverflow.com/a/1628334).*

   *<span style="color:red">Attention!</span> The last command (clean -f) will delete any files/folders that are not present on the remote. if you want to keep those files, backup them first or don't use the ```clean -f``` command.<br><br>
   Usually, **you don't want to do this** when working with a team. This will remove all the changes (and the hard work) from your colleagues. You can be fired ;-). But, if you are working alone, you should be fine.*

   <br>

   ---

   <br>

## "Force" remote files to match the local files

   This is the opposite of above. Use it if you want to have the remote files exactly as your local files.

   Go to your local folder :

   ```sh
   $ cd the/path/to/your/local/folder
   ```
   
   Reset remote files using ```-f``` "force" argument when using push :<br>
   
   ```sh
   $ git push -f origin master
   ```

   > *See more [here](https://stackoverflow.com/a/10510482).*

   <br>

   ---

   <br>

## Remove stuff from remote repo but keep them on local machine
If you are like me and you create the *.gitignore* file **after** you already pushed some files/folders on the remote that you don't want to see there, you can remove the like this :

   ```bash
   # The commands bellow "stage" the deletion of the directory/file, 
   # but doesn't touch anything on disk.

   # Remove a directory from remote (replace "somedir" with your dir name)
   $ git rm --cached -r somedir 

   # Remove a file from remote (replace "somefile.ext" with your file)
   $ git rm --cached somefile.ext
   ```

   After this, when you'll add/commit/push your changes, the directories/files will be deleted from remote (if they exist).<br>

   > *Source [here](https://stackoverflow.com/a/3469805).*
   
<br>

---

<br>

## Change the active SSH key on the fly
If you are like me and you have several Github accounts and two (or more) SSH keys, sometimes the active SSH key doesn't correspond with the repository you are currently in. You can specify *the good* key like this :

```bash
# Call the SSH agent
$ ssh-agent bash

# Add the SSH key to your agent (my key here is "id_rsa_powercoders")
$ ssh-add ~/.ssh/id_rsa_powercoders
```
