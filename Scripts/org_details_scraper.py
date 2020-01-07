import requests, bs4, xlwt

wb = xlwt.Workbook()

# urls = ['https://summerofcode.withgoogle.com/archive/'+str(x)+'/organizations/' for x in range(2016,2018)]

for year in range(2016, 2020):
    url = 'https://summerofcode.withgoogle.com/archive/'+str(year)+'/organizations/'
    sheet = wb.add_sheet('Sheet ' + str(year))
    soup = bs4.BeautifulSoup(requests.get(url).text, "html.parser")
    org_links = ['https://summerofcode.withgoogle.com'+x['href'] for x in soup.select('a.organization-card__link')]
    print(str(len(org_links)) + ' organizations in year ' + str(year))

    for j in range(len(org_links)):
        print('Organization ' + str(j+1) + '/' + str(len(org_links)) + ' processing...')
        res = requests.get(org_links[j])
        newsoup = bs4.BeautifulSoup(res.text, "html.parser")
        orgname = newsoup.select('.banner__title')[0].text.strip()

        sheet.write(j, 0, orgname)  # write organization name
        sheet.write(j, 1, org_links[j])  # write organization link

        # write org website link other than gsoc
        weblink = newsoup.select('.org__link')[0].text.strip()
        sheet.write(j, 2, weblink)  # write organization website link

        # write topics
        topics_list = newsoup.select('li.organization__tag--topic')
        topics_list = [x.text for x in topics_list]
        sheet.write(j, 3, ' - '.join(topics_list))

        # write technologies/languages
        technologies_list = newsoup.select('li.organization__tag--technology')
        for k in range(len(technologies_list)):
            sheet.write(j, k+5, technologies_list[k].text)
    print()

wb.save("sample.xls")