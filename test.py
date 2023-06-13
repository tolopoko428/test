def get_pagers(url, page):
    while True:
        for i in range(1, page):
            page_url = url + '?page={}'.format(i)
            print(page_url)
            return page_url
        

a = get_pagers('https://www.kivano.kg/mobilnye-telefony', 5)



# ukjsagfjhkjhkj 'mnf p'nj vh    vb h =