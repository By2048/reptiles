import logging
import datetime

logging.basicConfig(level=logging.INFO)


class Meizi:
    def __init__(self, id, title, link, category='none', date=datetime.datetime.now()):
        self.id = id
        self.title = title
        self.link = link
        self.category = category
        self.date = date

    def info(self):
        logging.info('{0:<15}{1}'.format('title', self.title))
        logging.info('{0:<15}{1}'.format('link', self.link))

    def all_info(self):
        logging.info('{0:<15}{1}'.format('id', self.id))
        logging.info('{0:<15}{1}'.format('title', self.title))
        logging.info('{0:<15}{1}'.format('link', self.link))
        logging.info('{0:<15}{1}'.format('category', self.category))
        logging.info('{0:<15}{1}'.format('date', self.date))


class MImage:
    def __init__(self, name, path, type, size, width, heigth, visit_date, create_date, change_date):
        self.name = name
        self.path = path
        self.type = type
        self.size = size
        self.width = width
        self.height = heigth
        self.visit_date = visit_date
        self.create_date = create_date
        self.change_date = change_date

    def info(self):
        logging.info('{0:<15}{1}'.format('name', self.name))
        logging.info('{0:<15}{1}'.format('path', self.path))
        logging.info('{0:<15}{1}'.format('type', self.type))
        logging.info('{0:<15}{1}'.format('size', self.size))
        logging.info('{0:<15}{1}'.format('width', self.width))
        logging.info('{0:<15}{1}'.format('height', self.height))
        logging.info('{0:<15}{1}'.format('visit_date', self.visit_date))
        logging.info('{0:<15}{1}'.format('create_date', self.create_date))
        logging.info('{0:<15}{1}'.format('change_date', self.change_date))


class MFolder:
    def __init__(self, name, path, date, num, size):
        """ 图片存储文件夹信息

        :param name: 文件夹名
        :param path: 绝对路径
        :param date: 创建日期
        :param num: 文件中图片数量
        :param size: 文件夹大小
        """
        self.name = name
        self.path = path
        self.date = date
        self.num = num
        self.size = size

    def info(self):
        logging.info('{0:<10}{1}'.format('name', self.name))
        logging.info('{0:<10}{1}'.format('path', self.path))
        logging.info('{0:<10}{1}'.format('date', self.date))
        logging.info('{0:<10}{1}'.format('num', self.num))
        logging.info('{0:<10}{1}'.format('size', self.size))


if __name__ == '__main__':
    pass
