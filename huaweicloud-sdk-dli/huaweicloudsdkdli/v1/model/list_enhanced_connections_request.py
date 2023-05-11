# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEnhancedConnectionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'name': 'str',
        'offset': 'int',
        'status': 'str',
        'tags': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'name': 'name',
        'offset': 'offset',
        'status': 'status',
        'tags': 'tags'
    }

    def __init__(self, limit=None, name=None, offset=None, status=None, tags=None):
        """ListEnhancedConnectionsRequest

        The model defined in huaweicloud sdk

        :param limit: 查询最大连接个数，默认100。
        :type limit: int
        :param name: 连接名。
        :type name: str
        :param offset: 查询结果偏移量，默认为0（连接以创建时间进行排序）
        :type offset: int
        :param status: 连接状态，包括以下两种状态： ACTIVE：已激活 DELETED：已删除
        :type status: str
        :param tags: 标签
        :type tags: str
        """
        
        

        self._limit = None
        self._name = None
        self._offset = None
        self._status = None
        self._tags = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags

    @property
    def limit(self):
        """Gets the limit of this ListEnhancedConnectionsRequest.

        查询最大连接个数，默认100。

        :return: The limit of this ListEnhancedConnectionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEnhancedConnectionsRequest.

        查询最大连接个数，默认100。

        :param limit: The limit of this ListEnhancedConnectionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        """Gets the name of this ListEnhancedConnectionsRequest.

        连接名。

        :return: The name of this ListEnhancedConnectionsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListEnhancedConnectionsRequest.

        连接名。

        :param name: The name of this ListEnhancedConnectionsRequest.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        """Gets the offset of this ListEnhancedConnectionsRequest.

        查询结果偏移量，默认为0（连接以创建时间进行排序）

        :return: The offset of this ListEnhancedConnectionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListEnhancedConnectionsRequest.

        查询结果偏移量，默认为0（连接以创建时间进行排序）

        :param offset: The offset of this ListEnhancedConnectionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def status(self):
        """Gets the status of this ListEnhancedConnectionsRequest.

        连接状态，包括以下两种状态： ACTIVE：已激活 DELETED：已删除

        :return: The status of this ListEnhancedConnectionsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListEnhancedConnectionsRequest.

        连接状态，包括以下两种状态： ACTIVE：已激活 DELETED：已删除

        :param status: The status of this ListEnhancedConnectionsRequest.
        :type status: str
        """
        self._status = status

    @property
    def tags(self):
        """Gets the tags of this ListEnhancedConnectionsRequest.

        标签

        :return: The tags of this ListEnhancedConnectionsRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListEnhancedConnectionsRequest.

        标签

        :param tags: The tags of this ListEnhancedConnectionsRequest.
        :type tags: str
        """
        self._tags = tags

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
        if not isinstance(other, ListEnhancedConnectionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
