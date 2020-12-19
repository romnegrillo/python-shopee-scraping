# Python Shopee Scraping

### About
This repository contains Python automation programs to web scrape shopee.ph 
and gather information about the items you purchased in your Shopee account. 

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

### Hot to Use - Linux
Open the terminal and change directory to this folder then
execute the following commands:
* ```cd release/linux/dist/main```
*  ```./main```

The program will then ask for your email/username, password and OTP sent in your
mobile then the report will generated on a folder named "reports_generated" on your Desktop.
