# GIT MOST USED/USEFUL COMMANDS

A customized list of most useful commands with GIT.<br>
Git is (incredibily) complex. We have a lot of tutorials online where everybody tries to summarize "the best Git commands".<br>
The content bellow is what I believe to be the most useful for us, @Powercoders.

<br>

## Basic operations
  ### cd
  Not related to Git but, **the first thing to do, always, is to go into the target folder**
  ```bash
  # Generic
  $ cd <path>

  # Example
  $ cd ~/powercoders/my-project
  ```

  <br>
  ---
  <br>

  ### clone
  Cloning a remote repository from Git. A clone is an exact replica of the target repo.
  
  ```bash
  # Generic
  $ git clone <url>
  
  # Example :
  $ git clone https://github.com/powercoders-lausanne/support.git
  ```

  <br>
  ---
  <br>

  ### add + commit + push
  Those 3 come together, in this order.<br>
  Adding the latest changes to Git while describing what these changes are.
  
  <figure align="center"><img src="assets/git-add-commit.png" alt="Git add and commit" width="360">
    <figcaption>Illustration of the process. <a href="https://dev.to/sublimegeek/git-staging-area-explained-like-im-five-1anh">Source</a></figcaption>
  </figure>

  #### 1. add

  ```bash
  # Generic
  $ git add <file name 1> <file name 2>
  
  # Examples
  $ git add README.md                         # a file at the root (same level as .git folder)
  $ git add css/styles.css                    # a file inside a folder
  $ git add index.html about.html             # add two (or more) files
  $ git add .                                 # add ALL the files (who changed)
  ```

  #### 2. commit
  ```bash
  # Generic
  $ git commit -m "short description of the change you made to the file(s)"
  
  # Examples when adding/updating "styles.css"
  $ git commit -m "Initial commit"            # Only once, when the file is created
  $ git commit -m "Updated helper classes"
  $ git commit -m "Removed repetead styles"
  ```
  
  #### 3. push
  ```bash
  # Generic
  $ git push <-flag>
  
  # Examples
  $ git push
  $ git commit -m "Updated helper classes"
  $ git commit -m "Removed repetead styles"
  ```
  
  #### [TIP] Add and commit all in one step
  ```bash
  # First, create a Git config alias. In this case the alias is "coa" :
  git config --global alias.coa '!git add -A && git commit -m'
  
  # After restarting your bash console, use the alias like this :
  $ git coa "your message..."
  ```

  > **[Remember] Git do not add empty folders.**

  <br>
  ---
  <br>

  ### pull
  Getting the latest changes from Git
  
  ```bash
  # Generic
  $ git pull
  
  # Example :
  $ git clone https://github.com/powercoders-lausanne/support.git
  ```

  <br>
  ---
  <br>

  