# PyPasswordManager

**Simple Password Manager Build with Python**

## Features

- Form a master password and create your own encypted password vault
- Email, Username, and Passwords are encrypted using SHA256 and Fernet
- All entries stored in SQLite database file for ultra portability
- Password generator for creating completley random and secure passwords
- Embedded password stregth algorthm to test user-inputted passwords
- Easily copy passwords and usernames with a right-click

## **Images**

### Login 
<img src="https://github.com/eospo/password-generator-gui/blob/main/images/SCR-20230212-49r.png?raw=true"  width="50%" height="50%">

### Password Vault
<img src="https://github.com/eospo/password-generator-gui/blob/main/images/SCR-20230212-4a7.png?raw=true"  width="50%" height="50%">

### Right-Click to Quick Copy, Delete Entry, or Exit
<img src="https://github.com/eospo/password-generator-gui/blob/main/images/SCR-20230212-4am.png?raw=true"  width="50%" height="50%">

### Add Logins
<img src="https://github.com/eospo/password-generator-gui/blob/main/images/SCR-20230212-4cc.jpeg?raw=true"  width="50%" height="50%">

### Generate Passwords 
<img src="https://github.com/eospo/password-generator-gui/blob/main/images/SCR-20230212-4cp.jpeg?raw=true"  width="50%" height="50%">

### Test Your Passwords!
<img src="https://github.com/eospo/password-generator-gui/blob/main/images/SCR-20230212-4cv.jpeg?raw=true"  width="50%" height="50%">

### Ecrypted SQLite Database Entries
<img src="https://github.com/eospo/password-generator-gui/blob/main/images/SCR-20230212-4ez.png?raw=true"  width="100%" height="100%">

## Tech
PyPasswordManager uses a number of open source projects to work properly:

- [PySimpleGUI] - A modern GUI framework for Python!
- [SQLite] - Portable SQL databases
- [Fernet] - Symetric ecryption with Python
- [SHA256] - Hashing via SHA256 algorthm
- [Pyperclip] - Cross-Platform copying to clipboard
- [zxcvbn] -  Realistic password strength estimation

## Installation

In order to run PyPasswordManager you'll need to 
install the dependencies listed below:

```sh
pip install PySimpleGUI
pip install cryptography
pip install zxcvbn
pip install Pyperclip
```
Development was done on MacOS, remains untested for Windows machines.

## License

MIT

