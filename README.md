# Python Shopee Scraping

![Shopee-Logo](/shopee_logo.png?raw=true)

### About
Updated as of 2021/06/06 since I constantly use this script to track my spending
on Shopee.

This repository contains Python automation programs to web scrape shopee.ph 
and gather information about the items you purchased in your Shopee account. 
Note, the link is  shopee.ph. I have not tested it in another shopee website
of another country.

This program will generate a PDF report of all the items you bought in Shopee,
including its name and price in tablular format, and the total money you spent 
in the platform.

As of now, it allows you to enter username/email, password, and OTP sent from 
your phone using the command line, then the report will be generated.

Warning: Using it multiple times consecutively will block your account by a certain minutes. 
This is a security feature in Shopee when you try to send OTP too many times.

### Disclaimer
I do not save any personal info you will enter in this program. I just used
the 3rd party Python modules to automate the process. I'm not responsible for
any trouble you may face when using this script. I tested this using my own
Shopee account. 

### How to Use 
As of now, it is only available in Linux and Windows. 
You need the following installed:
* python3 (python2 won't work)
* pip
* firefox browser

Then you need to install the requirements.txt in the terminal. Navigate to
this directory when you download it then type:

```pip install -r requirements.txt```

or you configured your system to use pip3 command then:

```pip3 install -r requirements.txt```

Then simpy run the main.py script by typing in the terminal:

```python main.py```

or if you configured your system to use python3 command then:

```python3 main.py```

The program will ask for the usrname/email, password. Then if you logged in
successfully, it will send and OTP to your phone and the program will request 
it. Wait a little bit then the report will be generated.

Output directory of PDF file for Linux:

```/home/username/Desktop/generated_reports```

Output directory of PDF file for Windows:

```C:\Users\username\Desktop\generated_reports```
