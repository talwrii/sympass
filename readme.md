# sympass - Symmetric password store

This is a very feature-incomplete reimplementation of the [pass](https://www.passwordstore.org) utility with one difference: passwords are encrypted in a symmetric fashion using a master password.

This also happens to use xkcd multiple word passwords

## Motivation

I experienced problems with corrupted files using the graphical tool [keepass](https://www.keepassx.org/) - albeit after using a python library to try to access it.  I also prefer command-line utilities. I also have had machines break and wanted to quickly get at passwords.

This made me want to build a password store that:

* Is command-line
* Supports easy backups 
* At a pinch allows you to read password using the command line

The pass command-line utility is very nearly what I need apart from it uses a key which is stored in your keychain on a machine. This replaces pass's gpg key, with a symmetric master password used to encrypt your passwords.

## Alternatives

* You could backup your `gpg` key together with the password directory in [pass](https://www.passwordstore.org)
* You could use commercial online password stores like [LastPass](https://www.lastpass.com/) and friends. I am not comfortable storing banking passwords in these.
* There are GUI clients like [keepass](https://www.keepassx.org/). I would prefer not to be dependend on a client and like command line tools. The password format is also quite complicated.
* There may well be dozens of similar hacky command line scripts that do this. I made the decision to write my own rather that get others working. Caveat emptor.

# Using

1. Check out this repo (I haven't got round to making this pip installable)
1. Install the requirements `pip install -r requirements.txt`
1. In this directory run `./set-master` to create a master password
1. `./new-pass test` will create a new password
1. `./get-pass test` will print this password to standard out (You can use this with `xclip` on linux, and `pbcopy` on mac
1. Copy the entire directory somewhere for backup.

You can manually view a password without this tool using: `gpg -d test.pass`

# Bugs and feature requests

I'm not sure I'm that likely to implemented that many features of bugs or indeed accept yours. Since... password stores don't fill me with passion. However, I need one so if something you suggest is relevant for my use of this I may well pay attention. Also feel free to fork with attribution.
