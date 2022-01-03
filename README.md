# Take Information in NIST NVD for ICS

This project developed with Python.

When you search in the NIST NVD data, you write a keyword which is explain your research.(https://nvd.nist.gov/vuln/search) After that, you see the vuln ID, description, Published time ,and CVSS severity (Version 2 and Version3) fields. 

I use the BeautifulSoup library for taking this fileds. The library parse the htlm codes in web sites for what do you want to take.
I write the results Sqlite database and json format.

I run the project with -w parameter. This parameter is that what dou you want the search in NIST NVD databse.

<img width="567" alt="Screen Shot 2022-01-03 at 15 13 21" src="https://user-images.githubusercontent.com/47140243/147929249-4e9bcf06-1192-415d-9c38-dde6a218b171.png">

You can see the research results in the json and database files. 

<img width="1132" alt="Screen Shot 2022-01-03 at 15 13 41" src="https://user-images.githubusercontent.com/47140243/147929270-8899c796-2e45-441b-afd8-016c0b51f1ec.png">

<img width="895" alt="Screen Shot 2022-01-03 at 15 14 41" src="https://user-images.githubusercontent.com/47140243/147929286-982a091a-93ec-4f33-8863-c41e13ee8756.png">

You can see the NVD result numbers are same with my results.

![Screen Shot 2022-01-03 at 15 16 17](https://user-images.githubusercontent.com/47140243/147929359-558847f7-af4f-4ac3-943e-2c3adbbadf00.png)

You can use this project in blue team opportunities. For example, you want to monitor which products have vulnerabilities. When the product has a new vulnerability, you will see this problem and take a solution. 

I used this results for ICS Security. I developed this project at the National Testbed Center for Critical Infrastructures (https://center.sakarya.edu.tr). I developed another project called Asset Management in ICS Systems in there. I got ip addresses, mac addresses, vendor names, protocols, version numbers to identify ICS products. I used the vendor name to submit to "Learn about NIST NVD for ICS project"

![image](https://user-images.githubusercontent.com/47140243/147889405-519c4f28-58e9-454a-aa69-828f719f0bd3.png)

