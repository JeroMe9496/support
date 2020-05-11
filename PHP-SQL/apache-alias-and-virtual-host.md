# Apache *aliases* and *virtual hosts*
Convert any folder into a "server" folder on WINDOWS / MAC<br>


<br>


## WINDOWS → LARAGON

### 1. *Alias* variant
> Your URL will be: *`localhost/name-of-the-alias`*

  1. Right-click on Laragon icon in the taskbar and navigate to: `Apache/site-enabled/dir: alias`. This will open a folder.
  2. Duplicate an existing file
  3. Rename the new file into `poco_work.conf`
  4. Open it and change :
      - The name of the alias → change it to `work`
      - The path to the directory (linux style, with slashes)

      You should have something like this :
      ```bash
      Alias /work "C:/path/to/workshop/php/folder"

      <Directory "C:/path/to/workshop/php/folder">
        Options Indexes FollowSymLinks MultiViews
        AllowOverride all
        Require local
      </Directory>
      ```
      Save the file.

<br>

### 2. *Virtual Host* variant (advanced)
> Your URL will be: *`work.dev`*

  1. Open file with a text editor<br>
    `"C:\Windows\System32\drivers\etc\hosts"`
  
  2. Add this at the end of the file :
   
      ```bash
      127.0.0.1      work.dev
      127.0.0.1      blog.dev
      ```
      Save the file.

  3. Right-click on Laragon icon in the taskbar and navigate to: `Apache/site-enabled/dir: site-enabled`. This will open a folder.

  4. Duplicate an existing file
  5. Rename the new file into `work.dev.conf`. No *auto* in the name!
  6. Open it and change ONLY the first 2 lines on top :
      ```bash
      define ROOT "C:/path/to/workshop/php/folder"
      define SITE "work.dev"
      ```
      Save the file.

  7. Duplicate `work.dev.conf` file and change the name into `blog.dev.conf` and repeat the step 6 → customize the first 2 lines...
   
  8.  Restart the server


<br>

---

<br>


## MAC → MAMP
### 1. *Alias* variant
> Your URL will be: *`localhost/name-of-the-alias`*
1. Open this file in VS Code:
  `/Applications/MAMP/conf/apache/httpd.conf` :

2. Add this **at the end** of the file :
    ```bash
    # work alias and directory
    Alias /work "/the/path/to/your/workshop/php"
    <Directory "/the/path/to/your/workshop/php">
        Options Indexes MultiViews
        AllowOverride None
        Order allow,deny
        Allow from all
    </Directory>

    # dev-blog alias and directory
    Alias /dev-blog "/the/path/to/your/dev-blog"
    <Directory "/the/path/to/your/dev-blog">
        Options Indexes MultiViews
        AllowOverride None
        Order allow,deny
        Allow from all
    </Directory>
    ```

<br>

### *Virtual Host* variant (advanced)
> Your URL will be: *`local.name-of-the-host`*

1. Open Terminal and type 
    ```bash
    $ sudo nano /private/etc/hosts
    ```
    The `sudo` command will ask you for your password. Enter you password to open "nano editor"

2. Enter this in your nano editor, at the end of the file:
    ```bash
    # VIRTUAL HOSTS
    127.0.0.1       local.work
    127.0.0.1       local.blog
    ```
    Save changes with `CTRL + O` (o letter, not zero)<br>
    Exit with `CTRL + X`

3. Edit this file:
  `/Applications/MAMP/conf/apache/httpd.conf` :
    - **Remove** the `#` comment for the line :<br>
    `Include /Applications/MAMP/conf/apache/extra/httpd-vhosts.conf`

    - **Add** this at the very end, just before the line `</IfModule>` : <br>
    it should look like this now:<br>
      ```bash
        NameVirtualHost *
      </IfModule>
      ```

4. Edit this file:
  `/Applications/MAMP/conf/apache/extra/httpd-vhosts.conf` :
    - **Remove** everything and add this instead :

      ```bash
      #
      # Virtual Hosts
      # -----------------------------------------------------------
      # This will replace MAMP default
      #
      NameVirtualHost *:80

      # localhost - whatever folder you want to use as a root folder
      <VirtualHost *>
          ServerName localhost
          DirectoryIndex index.html index.php
          DocumentRoot "/whatever/root/folder"
          <Directory "/whatever/root/folder">
              Options Indexes FollowSymLinks Includes execCGI
              AllowOverride All
              Order Allow,Deny
              Allow From All
          </Directory>
      </VirtualHost>

      # local.work
      <VirtualHost *>
          ServerName local.work
          DirectoryIndex index.html index.php
          DocumentRoot "/the/path/to/your/workshop/php"
          <Directory "/the/path/to/your/workshop/php">
              Options Indexes FollowSymLinks Includes execCGI
              AllowOverride All
              Order Allow,Deny
              Allow From All
          </Directory>
      </VirtualHost>


      # local.blog
      <VirtualHost *>
          ServerName local.blog
          DirectoryIndex index.html index.php
          DocumentRoot "/the/path/to/your/dev-blog"
          <Directory "/the/path/to/your/dev-blog">
              Options Indexes FollowSymLinks Includes execCGI
              AllowOverride All
              Order Allow,Deny
              Allow From All
          </Directory>
      </VirtualHost>
      ```
   