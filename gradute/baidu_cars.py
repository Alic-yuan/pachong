import requests
import os



class BaiduCars(object):

    # 获取全部页的xhr中的data
    def getManyPages(self, keyword, pages):
        params=[]
        for i in range(30, 30*pages+30,30):
            params.append({
                          'tn': 'resultjson_com',
                          'ipn': 'rj',
                          'ct': 201326592,
                          'is': '',
                          'fp': 'result',
                          'queryWord': keyword,
                          'cl': 2,
                          'lm': -1,
                          'ie': 'utf-8',
                          'oe': 'utf-8',
                          'adpicid': '',
                          'st': -1,
                          'z': '',
                          'ic': 0,
                          'word': keyword,
                          's': '',
                          'se': '',
                          'tab': '',
                          'width': '',
                          'height': '',
                          'face': 0,
                          'istype': 2,
                          'qc': '',
                          'nc': 1,
                          'fr': '',
                          'pn': i,
                          'rn': 30,
                          'gsm': '1e',
                          '1488942260214': ''
                      })
        url = 'https://image.baidu.com/search/acjson'
        urls = []
        for i in params:
            urls.append(requests.get(url, params=i).json().get('data'))

        return urls

    # 下载图片
    def getImg(self, dataList, localPath):

        if not os.path.exists(localPath):  # 新建文件夹
            os.mkdir(localPath)

        x = 0
        for list in dataList:
            for i in list:
                if i.get('thumbURL') != None:
                    print('正在下载：%s' % i.get('thumbURL'))
                    ir = requests.get(i.get('thumbURL'))
                    open(localPath + '%d.jpg' % x, 'wb').write(ir.content)
                    x += 1
                else:
                    print('图片链接不存在')




if __name__ == '__main__':
    bc = BaiduCars()
    dataList = bc.getManyPages('车辆', 10)  # 参数1:关键字，参数2:要下载的页数
    print(dataList)
    # bc.getImg(dataList, '/home/yuan/cars/') # 参数2:指定保存的路径