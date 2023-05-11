# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDatabasesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'instance_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, x_language=None, instance_id=None, offset=None, limit=None):
        """ListDatabasesRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言
        :type x_language: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param offset: 偏移量表示从此偏移量开始查询, offset大于等于0，默认0。
        :type offset: int
        :param limit: 每页显示的条目数量,取值范围[1, 100]，默认10。
        :type limit: int
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def x_language(self):
        """Gets the x_language of this ListDatabasesRequest.

        语言

        :return: The x_language of this ListDatabasesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListDatabasesRequest.

        语言

        :param x_language: The x_language of this ListDatabasesRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        """Gets the instance_id of this ListDatabasesRequest.

        实例ID。

        :return: The instance_id of this ListDatabasesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListDatabasesRequest.

        实例ID。

        :param instance_id: The instance_id of this ListDatabasesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        """Gets the offset of this ListDatabasesRequest.

        偏移量表示从此偏移量开始查询, offset大于等于0，默认0。

        :return: The offset of this ListDatabasesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDatabasesRequest.

        偏移量表示从此偏移量开始查询, offset大于等于0，默认0。

        :param offset: The offset of this ListDatabasesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListDatabasesRequest.

        每页显示的条目数量,取值范围[1, 100]，默认10。

        :return: The limit of this ListDatabasesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDatabasesRequest.

        每页显示的条目数量,取值范围[1, 100]，默认10。

        :param limit: The limit of this ListDatabasesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListDatabasesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
