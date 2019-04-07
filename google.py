from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(storage={'root_dir': 'google_img'})
google_crawler.crawl(keyword='cat.gif', max_num=10)
