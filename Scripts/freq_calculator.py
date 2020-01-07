import requests
import xlwt
import bs4

wb = xlwt.Workbook()
sheet = wb.add_sheet('Frequencies')
freq_list = {}

for year in range(2009, 2016):
    url = 'https://www.google-melange.com/archive/gsoc/' + str(year)
    soup = bs4.BeautifulSoup(requests.get(url).text, "html.parser")
    org_names = [x.text.strip()
                 for x in soup.select('li.mdl-list__item > span > a')]
    # print(org_names)
    for org in org_names:
        if org in freq_list:
            freq_list[org].append(year)
        else:
            temp = [org, year]
            freq_list[org] = temp

for year in range(2016, 2020):
    url = 'https://summerofcode.withgoogle.com/archive/' + \
        str(year) + '/organizations/'

    soup = bs4.BeautifulSoup(requests.get(url).text, "html.parser")
    org_names = [x.text.strip()
                 for x in soup.select('h4.organization-card__name')]

    for org in org_names:
        if org in freq_list:
            freq_list[org].append(year)
        else:
            temp = [org, year]
            freq_list[org] = temp


i = 0
for item in freq_list:
    # if freq_list[item] > 2:
    print(item + " " + str(freq_list[item]))
    # sheet.write(i, 0, str(freq_list[item][0]))
    for j in range(len(freq_list[item])):
        sheet.write(i, j, freq_list[item][j])
    i += 1

wb.save('freq_collected.xls')
