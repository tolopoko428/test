import requests
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    html = response.text 
    return html


def get_pages(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    list_view = soup.find('div', {'class':'list-view'})
    item = list_view.find_all('div', {'class':'item product_listbox oh'})
    for i in item:
        listbox_img = i.find('div', {'class':'listbox_img pull-left'})
        url = listbox_img.find('a')['href']
        urls = 'https://www.kivano.kg' + url
        links.append(urls)
    return links

def get_page_data(post):
    soup = BeautifulSoup(post, 'html.parser')
    wrap = soup.find('div', {'class':'wrap'})
    product_view = wrap.find('div', {'class':'product-view oh'})
    right_side = product_view.find('div', {'id':'right_side'})
    
    title = right_side.find('h1', {'itemprop':'name'}).text # Название телефона
    
    shop_text = right_side.find('div', {'class':'shop_text'})
    content = shop_text.find('span').get('content') # Описание
    
    product_price2 = shop_text.find('div', {'class':'product_price2'})
    price = product_price2.find('span', {'itemprop':'price'}).text # Цена
    
    tabs_wrap = product_view.find('div', {'class':'tabs_wrap'})
    full_discreption = tabs_wrap.find('div', {'id':'desc'}).text # full_description # нужно передедать
    about = f'''
    Name: {''}
    Discription; {''}
    Price: {price}
    Full_discription: {''}
    '''
    return about



def get_pagers(url):
    for i in url, range(1, 5):
        html_page = url + '?page={}'.format(i)
        yield html_page
        
def get_max_pages(url):
    soup = BeautifulSoup(url, 'html.parser')
    wrap = soup.find('div', {'class':'wrap'})
    container = wrap.find('div', {'class':'container'})
    print(container)
    
    # print(itemtype)




def main():
    url = 'https://www.kivano.kg/mobilnye-telefony'
    html = get_html(url)
    links = get_pages(html)

    for i in links:
        page_html = get_html(i)
        
        # print('New Publication:')

        get_page_data(page_html)
    
    # for i in get_pagers(url):
    #     page_html = get_html(i)
    #     get_page_data(page_html)
    #     print('page')
    #     get_max_pages(url)
    


if __name__ == '__main__':
    main()





