import os

from elasticsearch import Elasticsearch
from elasticsearch import helpers


class Pes:
    def __init__(self):
        self.client = Elasticsearch([
            {"host": os.getenv("ES_GATEWAY"),
             "port": os.getenv("ES_PORT") or 9200}
        ])

    def create_index(self, index_name: str):
        # 创建 index
        self.client.indices.create(index=index_name, body={
            'settings': {
                'index': {
                    'number_of_shards': 1,
                    'number_of_replicas': 0,
                }
            },
            'mappings': {
                'properties': {
                    'subnet': {'type': 'text'}
                }
            }
        })

    def drop_index(self, index_name: str):
        # 删除 index
        self.client.indices.delete(index=index_name, ignore=[400, 404])

    def get_index_info(self, index_name: str):
        # 获取 index 信息
        index_info = self.client.indices.get(index=index_name)
        return index_info

    def do_bulk(self, index_name: str, op_type: str):
        # bulk
        action = [{
            '_op_type': op_type,
            '_index': index_name,
            '_id': 'test',
            '_source': {
                'subnets': '218038272',
                'mask': '16',
            }
        }]

        helpers.bulk(self.client, action)


# 关闭连接
client.close()
