# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatabaseInfoItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'data_size': 'str',
        'storage_size': 'str',
        'collection_num': 'int'
    }

    attribute_map = {
        'name': 'name',
        'data_size': 'data_size',
        'storage_size': 'storage_size',
        'collection_num': 'collection_num'
    }

    def __init__(self, name=None, data_size=None, storage_size=None, collection_num=None):
        r"""DatabaseInfoItem

        The model defined in huaweicloud sdk

        :param name: 数据库名称, config admin 库不做展示。
        :type name: str
        :param data_size: 数据库存储大小（以GB为单位）,保留两位小数。 存储大小: 实际磁盘上占用的物理空间大小，包括数据文件、日志文件、索引文件等。
        :type data_size: str
        :param storage_size: 数据库逻辑大小 （以GB为单位）,保留两位小数。 逻辑大小指的是数据库中实际存储的数据大小，不包括索引大小、日志大小等。
        :type storage_size: str
        :param collection_num: 数据库中的集合数。
        :type collection_num: int
        """
        
        

        self._name = None
        self._data_size = None
        self._storage_size = None
        self._collection_num = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if data_size is not None:
            self.data_size = data_size
        if storage_size is not None:
            self.storage_size = storage_size
        if collection_num is not None:
            self.collection_num = collection_num

    @property
    def name(self):
        r"""Gets the name of this DatabaseInfoItem.

        数据库名称, config admin 库不做展示。

        :return: The name of this DatabaseInfoItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DatabaseInfoItem.

        数据库名称, config admin 库不做展示。

        :param name: The name of this DatabaseInfoItem.
        :type name: str
        """
        self._name = name

    @property
    def data_size(self):
        r"""Gets the data_size of this DatabaseInfoItem.

        数据库存储大小（以GB为单位）,保留两位小数。 存储大小: 实际磁盘上占用的物理空间大小，包括数据文件、日志文件、索引文件等。

        :return: The data_size of this DatabaseInfoItem.
        :rtype: str
        """
        return self._data_size

    @data_size.setter
    def data_size(self, data_size):
        r"""Sets the data_size of this DatabaseInfoItem.

        数据库存储大小（以GB为单位）,保留两位小数。 存储大小: 实际磁盘上占用的物理空间大小，包括数据文件、日志文件、索引文件等。

        :param data_size: The data_size of this DatabaseInfoItem.
        :type data_size: str
        """
        self._data_size = data_size

    @property
    def storage_size(self):
        r"""Gets the storage_size of this DatabaseInfoItem.

        数据库逻辑大小 （以GB为单位）,保留两位小数。 逻辑大小指的是数据库中实际存储的数据大小，不包括索引大小、日志大小等。

        :return: The storage_size of this DatabaseInfoItem.
        :rtype: str
        """
        return self._storage_size

    @storage_size.setter
    def storage_size(self, storage_size):
        r"""Sets the storage_size of this DatabaseInfoItem.

        数据库逻辑大小 （以GB为单位）,保留两位小数。 逻辑大小指的是数据库中实际存储的数据大小，不包括索引大小、日志大小等。

        :param storage_size: The storage_size of this DatabaseInfoItem.
        :type storage_size: str
        """
        self._storage_size = storage_size

    @property
    def collection_num(self):
        r"""Gets the collection_num of this DatabaseInfoItem.

        数据库中的集合数。

        :return: The collection_num of this DatabaseInfoItem.
        :rtype: int
        """
        return self._collection_num

    @collection_num.setter
    def collection_num(self, collection_num):
        r"""Sets the collection_num of this DatabaseInfoItem.

        数据库中的集合数。

        :param collection_num: The collection_num of this DatabaseInfoItem.
        :type collection_num: int
        """
        self._collection_num = collection_num

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
        if not isinstance(other, DatabaseInfoItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
