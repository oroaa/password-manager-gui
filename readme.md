# PyPasswordManager

**Password Manager built using python**

## Features

- Form a master password and create your own encypted password vault
- Email, Username, and Passwords are encrypted using SHA256 and Fernet
- Password generator for creating completley random and secure passwords
- Embedded password stregth algorthm to test your utilized passwords
- SQLite database file export for portabilit

## Images
### Login 
![Login Screen](/images/login.png )
### Password Vault
![Password Vault](/images/theVault.png)
### Add Login Entry
![Adding a Login Entry](/images/addItem.png)
### Password Generator 
![Generate Random Passwords](/images/pwGenerator2.png)
### Stregth Estimation
![Test Stregth of your Passwords](/images/pwGenerator.png)

## Tech
PyPasswordManager uses a number of open source projects to work properly:

- [PySimpleGUI] - A modern GUI framework for Python!
- [SQLite] - portable SQL databases
- [Fernet] - Symetric ecryption with Python
- [SHA256] - hashing with SHA256 algorthms
- [Pyperclip] - Python library for copying to clipboard
- [zxcvbn] -  realistic password strength estimation made by DropBox

## Installation

In order to run PyPasswordManager you'll need to 
install the dependencies listed below.

```sh
pip install PySimpleGUI
pip install cryptography
pip install zxcvbn
pip install Pyperclip
```
Development was done on MacOS, remains untested for Windows machines.

## License

MIT

