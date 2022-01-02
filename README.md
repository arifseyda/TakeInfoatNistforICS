# Take Information in NIST NVD

This project develops with Python.

When you search in the NIST NVD data, you write a keyword which is explain your research.(https://nvd.nist.gov/vuln/search) After that, you see the vuln ID, description, Published time ,and CVSS severity (Version 2 and Version3) fileds. 

I use the BeatifulSoup library for taking this fileds. The library parse the htlm codes in web sites for what do you want to take.
I write the results Sqlite database and json format.


