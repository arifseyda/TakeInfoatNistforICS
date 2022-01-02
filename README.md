# Take Information in NIST NVD

This project develops with Python.

When you search in the NIST NVD data, you write a keyword which is explain your research.(https://nvd.nist.gov/vuln/search) After that, you see the vuln ID, description, Published time ,and CVSS severity (Version 2 and Version3) fields. 

I use the BeautifulSoup library for taking this fileds. The library parse the htlm codes in web sites for what do you want to take.
I write the results Sqlite database and json format.

I run the project with -w parameter. This parameter is that what dou you want the search in NIST NVD databse.

<img width="524" alt="Screen Shot 2022-01-02 at 23 41 12" src="https://user-images.githubusercontent.com/47140243/147889009-ee4110bc-1856-4ef4-82b5-eded85e7a9e4.png">

You can see the research results in the json and database files. 

<img width="1130" alt="Screen Shot 2022-01-02 at 23 41 31" src="https://user-images.githubusercontent.com/47140243/147889071-521b6952-7213-4a33-8ce8-8149ef6d6c74.png">

<img width="864" alt="Screen Shot 2022-01-02 at 23 57 51" src="https://user-images.githubusercontent.com/47140243/147889292-71d1cd8f-2f40-49e4-bcb4-3808cbab511d.png">


You can see the NVD result numbers are same with my results.

![Screen Shot 2022-01-02 at 23 53 29](https://user-images.githubusercontent.com/47140243/147889205-ef5847c5-ccf2-4615-a67b-6ffadd3d9184.png)

You use this project in the blue team opportunities. For example, you want to monitor which products have vulnerabilities. When the product has a new vulnerability, you will see this problem and take a solution. 

I used this result in ELK Stack.

![image](https://user-images.githubusercontent.com/47140243/147889405-519c4f28-58e9-454a-aa69-828f719f0bd3.png)

