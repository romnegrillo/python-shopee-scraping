# Python Shopee Scraping

### About
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

***For Linux:***

* Download the file for Linux in the "Release" link at the right of this page, or click [here](https://github.com/romnegrillo/Python-Shopee-Scraping/releases).
* Unzip the file.
* Open terminal.
* Change directory to unzipped folder then the folder named "main" inside it.
* Example if you're in Downloads directory: ```cd ~/Downloads/python-shopee-scraping-linux/main```
* Run using the command ```./main```
* A command line interface will open that will ask for the needed information.

***For Windows:***

* Download the file  for Windows in the "Release" link at the right of this page, or click [here](https://github.com/romnegrillo/Python-Shopee-Scraping/releases).
* Unzip the file.
* Open the unzipped folder then open the folder named "main".
* Find the file named "main.exe" and double click it.
* A command line interface will open that will ask for the needed information.

The program will then ask for your email/username, password and OTP sent in your
mobile then the report will generated on a folder named "reports_generated" on 
a folder named "generated_reports" on your Desktop.

Output directory for Linux:

```/home/username/Desktop/generated_reports```

Output directory for Windows:

```C:\Users\username\Desktop\generated_reports```
