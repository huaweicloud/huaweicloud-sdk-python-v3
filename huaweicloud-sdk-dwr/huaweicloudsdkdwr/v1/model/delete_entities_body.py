# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteEntitiesBody:

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
        'filter': 'str'
    }

    attribute_map = {
        'store_name': 'store_name',
        'collection_name': 'collection_name',
        'filter': 'filter'
    }

    def __init__(self, store_name=None, collection_name=None, filter=None):
        r"""DeleteEntitiesBody

        The model defined in huaweicloud sdk

        :param store_name: 知识仓实例名称
        :type store_name: str
        :param collection_name: collection名称
        :type collection_name: str
        :param filter: 自定义删除条件，设置过滤表达式。 filter的表达式格式为详见Filter规则 注：删除指定primary_key需将过滤条件设置在filter中。
        :type filter: str
        """
        
        

        self._store_name = None
        self._collection_name = None
        self._filter = None
        self.discriminator = None

        self.store_name = store_name
        self.collection_name = collection_name
        self.filter = filter

    @property
    def store_name(self):
        r"""Gets the store_name of this DeleteEntitiesBody.

        知识仓实例名称

        :return: The store_name of this DeleteEntitiesBody.
        :rtype: str
        """
        return self._store_name

    @store_name.setter
    def store_name(self, store_name):
        r"""Sets the store_name of this DeleteEntitiesBody.

        知识仓实例名称

        :param store_name: The store_name of this DeleteEntitiesBody.
        :type store_name: str
        """
        self._store_name = store_name

    @property
    def collection_name(self):
        r"""Gets the collection_name of this DeleteEntitiesBody.

        collection名称

        :return: The collection_name of this DeleteEntitiesBody.
        :rtype: str
        """
        return self._collection_name

    @collection_name.setter
    def collection_name(self, collection_name):
        r"""Sets the collection_name of this DeleteEntitiesBody.

        collection名称

        :param collection_name: The collection_name of this DeleteEntitiesBody.
        :type collection_name: str
        """
        self._collection_name = collection_name

    @property
    def filter(self):
        r"""Gets the filter of this DeleteEntitiesBody.

        自定义删除条件，设置过滤表达式。 filter的表达式格式为详见Filter规则 注：删除指定primary_key需将过滤条件设置在filter中。

        :return: The filter of this DeleteEntitiesBody.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this DeleteEntitiesBody.

        自定义删除条件，设置过滤表达式。 filter的表达式格式为详见Filter规则 注：删除指定primary_key需将过滤条件设置在filter中。

        :param filter: The filter of this DeleteEntitiesBody.
        :type filter: str
        """
        self._filter = filter

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
        if not isinstance(other, DeleteEntitiesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
