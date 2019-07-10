import json 
from icrawler.builtin import GoogleImageCrawler

data = json.loads(open("catalog.json").read())
categories_dict = {}
for category in data['data']:
    index = category['id']
    categories_dict.setdefault(index) 
    categories_array = category['items']
    categories_dict[index] = [item['name'] for item in categories_array]
# print(categories_dict)

for key in categories_dict.keys():
    name = categories_dict[key]
    print(name)
    if key != '0':
        for item in name:
            google_crawler = GoogleImageCrawler(storage={'root_dir':'train_data/'+key+"/"+item})
            google_crawler.crawl(keyword=item, max_num=200)

