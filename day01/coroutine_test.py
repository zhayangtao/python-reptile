# 协程
from gevent import monkey
import gevent
import urllib.request

monkey.patch_all()


def run_task(url):
    print('Visit --> %s' % url)
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            print('%d bytes received from %s.' % (len(data), url))
    except Exception as e:
        print(e)


urls = ['https://github.com/', 'https://www.python.org/', 'http://www.cnblogs.com']
if __name__ == '__main__':
    greenlets = [gevent.spawn(run_task, url) for url in urls]
    gevent.joinall(greenlets)


# 使用 gevent.pool
from gevent.pool import Pool

pool = Pool(2)
results = pool.map(run_task, urls)
print(results)