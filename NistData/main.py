import sqlite3
from bs4 import BeautifulSoup
import requests
import json

con2 = sqlite3.connect("cvedetails.db")
cursor2 = con2.cursor()

def create_table():
    cursor2.execute(
        "CREATE TABLE IF NOT EXISTS cve (Vuln_ID TEXT, Summary Text, Published_Time Text, Version3_Severity Text, Version2_Severity Text)")
    con2.commit()

def request_process(spesific_keymowrd):
    response = requests.get("https://nvd.nist.gov/vuln/search/results?form_type=Basic&results_type=overview&query={}&search_type=all&startIndex=0".format(spesific_keymowrd))

    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    number = soup.find_all("strong", {"data-testid": "vuln-matching-records-count"})
    vuln_id = soup.find_all("th", {'nowrap': 'nowrap'})

    number_using = 0
    for k in number:
        number_using = k.text

    number_using2 = number_using
    if int(number_using2) > 20:
        number_using2 = 20

    summary_array = []
    for l in range(0, int(number_using2)):
        summary = soup.find_all("p", {"data-testid": "vuln-summary-{}".format(l)})
        for m in summary:
            summary_array.append(m.text)

    version3_number_array = []
    version2_number_array = []
    for k in range(0, int(number_using2)):
        liste = soup.find("tr", {"data-testid": "vuln-row-{}".format(k)})
        version3_not_available = liste.findAll("span", {"id": "Cvss3NAText"})

        for ver3_not in version3_not_available:
            version3_number_array.append(ver3_not.text)
        version3 = liste.findAll('span', {"id": "cvss3-link"})
        for ver3 in version3:
            version3_number_array.append(ver3.find('a').text)

        version2_not_available = liste.findAll("span", {"id": "Cvss2NAText"})

        for ver2_not in version2_not_available:
            version2_number_array.append(ver2_not.text)
        version2 = liste.findAll('span', {"id": "cvss2-link"})
        for ver2 in version2:
            version2_number_array.append(ver2.find('a').text)

    published_time_array = []
    for x in range(0, int(number_using2)):
        published_time = soup.find_all("span", {"data-testid": "vuln-published-on-{}".format(x)})
        for i in published_time:
            published_time_array.append(i.text)

    vuln_id_array = []
    for i in range(2, len(vuln_id)):
        vuln_id_array.append(vuln_id[i].text)

    for vuln, sum, pub, v3, v2 in zip(vuln_id_array, summary_array, published_time_array, version3_number_array,
                                      version2_number_array):

        all_data = {"Vuln ID": "{}".format(vuln),
                    "Summary": "{}".format(sum),
                    "Published Time": "{}".format(pub),
                    "Version 3 Severity": "{}".format(v3),
                    "Version 2 Severity": "{}".format(v2),
                    }

        all_data_json = json.dumps(all_data)

        with open("nist_data.json", "r") as f:
            cont = f.read()

        with open("nist_data.json", "r+") as file:
            if all_data_json not in cont:
                content = file.read()
                content = all_data_json + "\n" + content
                file.seek(0)
                file.write(content)

        cursor2.execute("insert into cve(Vuln_ID, Summary, Published_Time, Version3_Severity, Version2_Severity) select ?, ?,?,?,? where not exists(select 1 from cve where Vuln_ID = ?)", (vuln, sum, pub, v3, v2,vuln))
        con2.commit()

        print(all_data_json)

    if int(number_using) > 19:
        kalan = int(number_using) // 20
        other_page(spesific_keymowrd, kalan)

def delete():
    cursor2.execute("delete from cve ")

def other_page(spesific_keymowrd, kalan):
    for kalan_sayisi in range(kalan, 0, -1):
        response = requests.get(
            "https://nvd.nist.gov/vuln/search/results?form_type=Basic&results_type=overview&query={}&search_type=all&startIndex={}".format(
                spesific_keymowrd, kalan_sayisi * 20))

        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")
        number = soup.find_all("strong", {"data-testid": "vuln-matching-records-count"})
        vuln_id = soup.find_all("th", {'nowrap': 'nowrap'})

        number_using = 0
        for k in number:
            number_using = k.text

        summary_array = []
        number_of_last = int(number_using) - (kalan_sayisi * 20)
        if number_of_last > 20:
            number_of_last = 20

        for l in range(0, number_of_last):
            summary = soup.find_all("p", {"data-testid": "vuln-summary-{}".format(l)})
            for m in summary:
                summary_array.append(m.text)

        version3_number_array = []
        version2_number_array = []
        for k in range(0, number_of_last):
            liste = soup.find("tr", {"data-testid": "vuln-row-{}".format(k)})
            version3_not_available = liste.findAll("span", {"id": "Cvss3NAText"})

            for ver3_not in version3_not_available:
                version3_number_array.append(ver3_not.text)
            version3 = liste.findAll('span', {"id": "cvss3-link"})
            for ver3 in version3:
                version3_number_array.append(ver3.find('a').text)

            version2_not_available = liste.findAll("span", {"id": "Cvss2NAText"})

            for ver2_not in version2_not_available:
                version2_number_array.append(ver2_not.text)
            version2 = liste.findAll('span', {"id": "cvss2-link"})
            for ver2 in version2:
                version2_number_array.append(ver2.find('a').text)

        published_time_array = []
        for x in range(0, number_of_last):
            published_time = soup.find_all("span", {"data-testid": "vuln-published-on-{}".format(x)})
            for k in published_time:
                published_time_array.append(k.text)

        vuln_id_array = []
        for i in range(2, len(vuln_id)):
            vuln_id_array.append(vuln_id[i].text)

        for vuln, sum, pub, v3, v2 in zip(vuln_id_array, summary_array, published_time_array, version3_number_array,
                                          version2_number_array):

            all_data = {"Vuln ID": "{}".format(vuln),
                        "Summary": "{}".format(sum),
                        "Published Time": "{}".format(pub),
                        "Version 3": "{} Severity".format(v3),
                        "Version 2": "{} Severity".format(v2),

                        }

            all_data_json = json.dumps(all_data)

            with open("nist_data.json", "r") as f:
                cont = f.read()

            with open("nist_data.json", "r+") as file:
                if all_data_json not in cont:
                    content = file.read()
                    content = all_data_json + "\n" + content
                    file.seek(0)
                    file.write(content)

            cursor2.execute(
                "insert into cve(Vuln_ID, Summary, Published_Time, Version3_Severity, Version2_Severity) select ?, ?,?,?,? where not exists(select 1 from cve where Vuln_ID = ?)",
                (vuln, sum, pub, v3, v2, vuln))
            con2.commit()


            print(all_data_json)
        print("********************************")


def verial2():
    cursor2.execute("Select * From cve")
    liste = cursor2.fetchall()
    return liste


def tupple_to_array(tupple,number):
    result = []
    array = []
    for s in tupple:
        for x in s:
            result.append(x)
            array = [result[i * number:(i+1) * number] for i in range((len(result)+ number -1) // number)]
    return array

if __name__ == '__main__':

    create_table()
    request_process("Siemens S7-1200")

con2.close()