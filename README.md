#subdomain_spider
git clone https://github.com/xiaoyecent/subdomain_spider
子域名爬虫 接口  http://i.links.cn/subdomain/  -o支持写入文件 不加默认打印在shell中
```
Usage: subdomain_spider.py [options]

Options:
  -h, --help            show this help message and exit
  -o OUTFILE, --out=OUTFILE
                        output filename
  -d DOMAIN, --domain=DOMAIN
                        main domain
```
example:
```
sudo python subdomain_spider.py -d vip.com -o vip.txt
```
or 
```
sudo python subdomain_spider.py -d vip.com 
```
