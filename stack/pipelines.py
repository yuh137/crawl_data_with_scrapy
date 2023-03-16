# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging  
import pymongo 
# from scrapy.utils.project import get_project_settings
# import settings
from scrapy.exceptions import DropItem
import stack.settings as settings


class MongoDBPipeline(object):
    def __init__(self):
        # settings = get_project_settings
        connection = pymongo.MongoClient(
            settings.MONGODB_SERVER,
            settings.MONGODB_PORT
        )
        db = connection[settings.MONGODB_DB]
        self.collection = db[settings.MONGODB_COLLECTION]
        self.logger = logging.getLogger(__name__)

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert_one(dict(item))
            self.logger.debug("Question added to MongoDB database!")
        return item


# class StackPipeline:
#     def process_item(self, item, spider):
#         return item
