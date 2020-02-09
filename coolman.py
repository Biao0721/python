import requests
import re
import os

def getHTML(url):
        try:
            kv={'user-agent':'chrome/10'}
            r=requests.get(url)
            r.raise_for_status()
            html=r.text
            return html
        except:
            return '访问失败'
        finally:
                print (r.status_code)

def getIMG(html):
        #解析网址
        reg = r'src="(.*?\.jpg)" alt'  
        imgre = re.compile(reg)
        imglist = re.findall(imgre,html)
        return imglist

if __name__ == "__main__":
    
        #设置爬取次数最大值max，以及设置初始值num
        num=1
        max=eval(input('输入想要爬取的次数：'))
    
        while num <= max:

            url=input('请输入要爬取的网址：')
            html=getHTML(url)

            if html!='访问失败':
    
                for imgurl in getIMG(html):

                        #设置根目录
                        root="F:/coolman"
                        path=root+'/sneaker-'+imgurl.split('/')[-1]
    
                        try:
                                #判断是否存在coolman文件夹，若不存在则新建文件夹
                                if not os.path.exists(root): 
                                        os.mkdir(root)
                                #开始下载
                                if not os.path.exists(path):
                                        r=requests.get(imgurl)
                                        #下载图片到F://coolman 
                                        with open(path,'wb')as f:
                                                f.write(r.content)
                                                f.close()
                                                print('图片保存成功')
                                #文件已存在
                                else:
                                        print('图片已存在')
                        except:
                                print("爬取失败")
    
            else:
                print(html)
    
            num+=1