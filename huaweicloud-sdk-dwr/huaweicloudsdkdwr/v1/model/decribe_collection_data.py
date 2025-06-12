# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DecribeCollectionData:

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
        'fields': 'list[FieldData]',
        'load_status': 'str',
        'description': 'str',
        'params': 'dict(str, object)',
        'indexes': 'list[IndexParams]',
        'entity_num': 'int'
    }

    attribute_map = {
        'store_name': 'store_name',
        'collection_name': 'collection_name',
        'fields': 'fields',
        'load_status': 'load_status',
        'description': 'description',
        'params': 'params',
        'indexes': 'indexes',
        'entity_num': 'entity_num'
    }

    def __init__(self, store_name=None, collection_name=None, fields=None, load_status=None, description=None, params=None, indexes=None, entity_num=None):
        r"""DecribeCollectionData

        The model defined in huaweicloud sdk

        :param store_name: 知识仓实例名称
        :type store_name: str
        :param collection_name: collection名字
        :type collection_name: str
        :param fields: collection各个field信息
        :type fields: list[:class:`huaweicloudsdkdwr.v1.FieldData`]
        :param load_status: 标识当前Collection加载状态。 1、LoadStateLoaded：表示当前Collection已准备就绪，可正常使用。 2、LoadStateLoading：表示当前Collection正在load。 3、LoadStateNotLoad：表示collection未加载。
        :type load_status: str
        :param description: Collection 的描述信息
        :type description: str
        :param params: collection参数： shards_num partitions_num max_length
        :type params: dict(str, object)
        :param indexes: collection中各个索引信息
        :type indexes: list[:class:`huaweicloudsdkdwr.v1.IndexParams`]
        :param entity_num: collection中的entity数量
        :type entity_num: int
        """
        
        

        self._store_name = None
        self._collection_name = None
        self._fields = None
        self._load_status = None
        self._description = None
        self._params = None
        self._indexes = None
        self._entity_num = None
        self.discriminator = None

        self.store_name = store_name
        self.collection_name = collection_name
        self.fields = fields
        if load_status is not None:
            self.load_status = load_status
        if description is not None:
            self.description = description
        if params is not None:
            self.params = params
        if indexes is not None:
            self.indexes = indexes
        if entity_num is not None:
            self.entity_num = entity_num

    @property
    def store_name(self):
        r"""Gets the store_name of this DecribeCollectionData.

        知识仓实例名称

        :return: The store_name of this DecribeCollectionData.
        :rtype: str
        """
        return self._store_name

    @store_name.setter
    def store_name(self, store_name):
        r"""Sets the store_name of this DecribeCollectionData.

        知识仓实例名称

        :param store_name: The store_name of this DecribeCollectionData.
        :type store_name: str
        """
        self._store_name = store_name

    @property
    def collection_name(self):
        r"""Gets the collection_name of this DecribeCollectionData.

        collection名字

        :return: The collection_name of this DecribeCollectionData.
        :rtype: str
        """
        return self._collection_name

    @collection_name.setter
    def collection_name(self, collection_name):
        r"""Sets the collection_name of this DecribeCollectionData.

        collection名字

        :param collection_name: The collection_name of this DecribeCollectionData.
        :type collection_name: str
        """
        self._collection_name = collection_name

    @property
    def fields(self):
        r"""Gets the fields of this DecribeCollectionData.

        collection各个field信息

        :return: The fields of this DecribeCollectionData.
        :rtype: list[:class:`huaweicloudsdkdwr.v1.FieldData`]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this DecribeCollectionData.

        collection各个field信息

        :param fields: The fields of this DecribeCollectionData.
        :type fields: list[:class:`huaweicloudsdkdwr.v1.FieldData`]
        """
        self._fields = fields

    @property
    def load_status(self):
        r"""Gets the load_status of this DecribeCollectionData.

        标识当前Collection加载状态。 1、LoadStateLoaded：表示当前Collection已准备就绪，可正常使用。 2、LoadStateLoading：表示当前Collection正在load。 3、LoadStateNotLoad：表示collection未加载。

        :return: The load_status of this DecribeCollectionData.
        :rtype: str
        """
        return self._load_status

    @load_status.setter
    def load_status(self, load_status):
        r"""Sets the load_status of this DecribeCollectionData.

        标识当前Collection加载状态。 1、LoadStateLoaded：表示当前Collection已准备就绪，可正常使用。 2、LoadStateLoading：表示当前Collection正在load。 3、LoadStateNotLoad：表示collection未加载。

        :param load_status: The load_status of this DecribeCollectionData.
        :type load_status: str
        """
        self._load_status = load_status

    @property
    def description(self):
        r"""Gets the description of this DecribeCollectionData.

        Collection 的描述信息

        :return: The description of this DecribeCollectionData.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DecribeCollectionData.

        Collection 的描述信息

        :param description: The description of this DecribeCollectionData.
        :type description: str
        """
        self._description = description

    @property
    def params(self):
        r"""Gets the params of this DecribeCollectionData.

        collection参数： shards_num partitions_num max_length

        :return: The params of this DecribeCollectionData.
        :rtype: dict(str, object)
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this DecribeCollectionData.

        collection参数： shards_num partitions_num max_length

        :param params: The params of this DecribeCollectionData.
        :type params: dict(str, object)
        """
        self._params = params

    @property
    def indexes(self):
        r"""Gets the indexes of this DecribeCollectionData.

        collection中各个索引信息

        :return: The indexes of this DecribeCollectionData.
        :rtype: list[:class:`huaweicloudsdkdwr.v1.IndexParams`]
        """
        return self._indexes

    @indexes.setter
    def indexes(self, indexes):
        r"""Sets the indexes of this DecribeCollectionData.

        collection中各个索引信息

        :param indexes: The indexes of this DecribeCollectionData.
        :type indexes: list[:class:`huaweicloudsdkdwr.v1.IndexParams`]
        """
        self._indexes = indexes

    @property
    def entity_num(self):
        r"""Gets the entity_num of this DecribeCollectionData.

        collection中的entity数量

        :return: The entity_num of this DecribeCollectionData.
        :rtype: int
        """
        return self._entity_num

    @entity_num.setter
    def entity_num(self, entity_num):
        r"""Sets the entity_num of this DecribeCollectionData.

        collection中的entity数量

        :param entity_num: The entity_num of this DecribeCollectionData.
        :type entity_num: int
        """
        self._entity_num = entity_num

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
        if not isinstance(other, DecribeCollectionData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
