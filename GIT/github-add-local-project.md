# Adding an existing project to GitHub

You can "convert" any folder into a a git repository with the command `git init`. This will create a ".git" 🗀 folder inside your target folder.
<br>
However, if you want to link the local dir with a remote repository, there is a little more work to do.

> *Note: if you "clone" the remote repo **you don't have to do the bellow steps**, the cloned dir will already have the .git folder inside*

<br>


1. **First, create a Github repository**
    
    If you don't know how to do this, [follow the steps here](https://github.com/powercoders-lausanne/support/blob/master/GIT/git-account.md#2-in-the-new-repository-page).

<br>

2. **Go to your local folder. For example, I'll go into my local project :**

    ```sh
    $ cd ~/POWERCODERS/my-project
    ```
    This folder is a "normal" folder, nothing special about it. Maybe it's my website, a simple

<br>

3. **Initialize the current dir :**<br>
    > *Initialize/Convert any folder to support git commands and upload the files*

    ```sh
    $ git init
    Initialized empty Git repository in C:/Users/Administrator/POWERCODERS/my-project/.git/

    # This command will create a ".git" folder inside your current dir.
    ```
<br>

4. **Set up the remote URL**

    ```sh
    # Add remote origin (copy the link from Github)
    $ git remote add origin https://github.com/sorinpoco/my-project.git

    # check the remote origin
    $ git remote -v
    origin  https://github.com/sorinpoco/my-project.git (fetch)
    origin  https://github.com/sorinpoco/my-project.git (push)
    ```
<br>

5. **Create a file and push the changes to the remote**

    ```bash
    # Optional: create a readme file (or whatever file you want)
    $ touch README.md

    # Optional: open the file with VS Code and put something inside
    $ code README.md
    
    # Add, commit
    $ git add .
    $ git commit -m "First commit"

    # Push: for the first push you MUST indicate the remote branch.
    $ git push origin master
    # After, you can use just "push"
    ```

    [Github help : Adding an existing project to GitHub using the command line ➚](https://help.github.com/en/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line)