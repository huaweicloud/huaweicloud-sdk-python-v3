# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchEntitiesBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'store_name': 'str',
        'collection_name': 'str',
        'output_fields': 'list[str]',
        'top_k': 'int',
        'offset': 'int',
        'filter': 'str',
        'vector': 'list[float]',
        'vector_field': 'str',
        'params': 'dict(str, object)'
    }

    attribute_map = {
        'store_name': 'store_name',
        'collection_name': 'collection_name',
        'output_fields': 'output_fields',
        'top_k': 'top_k',
        'offset': 'offset',
        'filter': 'filter',
        'vector': 'vector',
        'vector_field': 'vector_field',
        'params': 'params'
    }

    def __init__(self, store_name=None, collection_name=None, output_fields=None, top_k=None, offset=None, filter=None, vector=None, vector_field=None, params=None):
        r"""SearchEntitiesBody

        The model defined in huaweicloud sdk

        :param store_name: 知识仓实例名称
        :type store_name: str
        :param collection_name: collection名称
        :type collection_name: str
        :param output_fields: 配置需返回的字段。
        :type output_fields: list[str]
        :param top_k: 返回个数限制
        :type top_k: int
        :param offset: 搜索结果中要跳过的entity数。
        :type offset: int
        :param filter: 设置过滤表达式。 filter的表达式格式为详见Filter规则
        :type filter: str
        :param vector: 需要搜索的向量数据
        :type vector: list[float]
        :param vector_field: 表示要查询的向量列名字
        :type vector_field: str
        :param params: 向量查询自定义参数:  ef:每个查询的邻居候选集大小。候选集越大，搜索的精度越高，但是搜索时间也会随之增加。（对HNSW生效） - search_list: 候选列表的大小，越大召回率越高，但性能会下降。（对HANNS生效） - nprobe: 返回的最近的聚类单元的数量。（对IVF_FLAT生效） - radius：查询范围的半径，若指定则进行range查询。
        :type params: dict(str, object)
        """
        
        

        self._store_name = None
        self._collection_name = None
        self._output_fields = None
        self._top_k = None
        self._offset = None
        self._filter = None
        self._vector = None
        self._vector_field = None
        self._params = None
        self.discriminator = None

        self.store_name = store_name
        self.collection_name = collection_name
        if output_fields is not None:
            self.output_fields = output_fields
        if top_k is not None:
            self.top_k = top_k
        if offset is not None:
            self.offset = offset
        if filter is not None:
            self.filter = filter
        self.vector = vector
        self.vector_field = vector_field
        if params is not None:
            self.params = params

    @property
    def store_name(self):
        r"""Gets the store_name of this SearchEntitiesBody.

        知识仓实例名称

        :return: The store_name of this SearchEntitiesBody.
        :rtype: str
        """
        return self._store_name

    @store_name.setter
    def store_name(self, store_name):
        r"""Sets the store_name of this SearchEntitiesBody.

        知识仓实例名称

        :param store_name: The store_name of this SearchEntitiesBody.
        :type store_name: str
        """
        self._store_name = store_name

    @property
    def collection_name(self):
        r"""Gets the collection_name of this SearchEntitiesBody.

        collection名称

        :return: The collection_name of this SearchEntitiesBody.
        :rtype: str
        """
        return self._collection_name

    @collection_name.setter
    def collection_name(self, collection_name):
        r"""Sets the collection_name of this SearchEntitiesBody.

        collection名称

        :param collection_name: The collection_name of this SearchEntitiesBody.
        :type collection_name: str
        """
        self._collection_name = collection_name

    @property
    def output_fields(self):
        r"""Gets the output_fields of this SearchEntitiesBody.

        配置需返回的字段。

        :return: The output_fields of this SearchEntitiesBody.
        :rtype: list[str]
        """
        return self._output_fields

    @output_fields.setter
    def output_fields(self, output_fields):
        r"""Sets the output_fields of this SearchEntitiesBody.

        配置需返回的字段。

        :param output_fields: The output_fields of this SearchEntitiesBody.
        :type output_fields: list[str]
        """
        self._output_fields = output_fields

    @property
    def top_k(self):
        r"""Gets the top_k of this SearchEntitiesBody.

        返回个数限制

        :return: The top_k of this SearchEntitiesBody.
        :rtype: int
        """
        return self._top_k

    @top_k.setter
    def top_k(self, top_k):
        r"""Sets the top_k of this SearchEntitiesBody.

        返回个数限制

        :param top_k: The top_k of this SearchEntitiesBody.
        :type top_k: int
        """
        self._top_k = top_k

    @property
    def offset(self):
        r"""Gets the offset of this SearchEntitiesBody.

        搜索结果中要跳过的entity数。

        :return: The offset of this SearchEntitiesBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this SearchEntitiesBody.

        搜索结果中要跳过的entity数。

        :param offset: The offset of this SearchEntitiesBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def filter(self):
        r"""Gets the filter of this SearchEntitiesBody.

        设置过滤表达式。 filter的表达式格式为详见Filter规则

        :return: The filter of this SearchEntitiesBody.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this SearchEntitiesBody.

        设置过滤表达式。 filter的表达式格式为详见Filter规则

        :param filter: The filter of this SearchEntitiesBody.
        :type filter: str
        """
        self._filter = filter

    @property
    def vector(self):
        r"""Gets the vector of this SearchEntitiesBody.

        需要搜索的向量数据

        :return: The vector of this SearchEntitiesBody.
        :rtype: list[float]
        """
        return self._vector

    @vector.setter
    def vector(self, vector):
        r"""Sets the vector of this SearchEntitiesBody.

        需要搜索的向量数据

        :param vector: The vector of this SearchEntitiesBody.
        :type vector: list[float]
        """
        self._vector = vector

    @property
    def vector_field(self):
        r"""Gets the vector_field of this SearchEntitiesBody.

        表示要查询的向量列名字

        :return: The vector_field of this SearchEntitiesBody.
        :rtype: str
        """
        return self._vector_field

    @vector_field.setter
    def vector_field(self, vector_field):
        r"""Sets the vector_field of this SearchEntitiesBody.

        表示要查询的向量列名字

        :param vector_field: The vector_field of this SearchEntitiesBody.
        :type vector_field: str
        """
        self._vector_field = vector_field

    @property
    def params(self):
        r"""Gets the params of this SearchEntitiesBody.

        向量查询自定义参数:  ef:每个查询的邻居候选集大小。候选集越大，搜索的精度越高，但是搜索时间也会随之增加。（对HNSW生效） - search_list: 候选列表的大小，越大召回率越高，但性能会下降。（对HANNS生效） - nprobe: 返回的最近的聚类单元的数量。（对IVF_FLAT生效） - radius：查询范围的半径，若指定则进行range查询。

        :return: The params of this SearchEntitiesBody.
        :rtype: dict(str, object)
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this SearchEntitiesBody.

        向量查询自定义参数:  ef:每个查询的邻居候选集大小。候选集越大，搜索的精度越高，但是搜索时间也会随之增加。（对HNSW生效） - search_list: 候选列表的大小，越大召回率越高，但性能会下降。（对HANNS生效） - nprobe: 返回的最近的聚类单元的数量。（对IVF_FLAT生效） - radius：查询范围的半径，若指定则进行range查询。

        :param params: The params of this SearchEntitiesBody.
        :type params: dict(str, object)
        """
        self._params = params

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SearchEntitiesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
