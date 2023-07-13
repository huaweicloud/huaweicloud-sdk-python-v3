# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteGetVideosListRequest:

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
        'offset': 'int'
    }

    attribute_map = {
        'limit': 'limit',
        'name': 'name',
        'offset': 'offset'
    }

    def __init__(self, limit=None, name=None, offset=None):
        """ExecuteGetVideosListRequest

        The model defined in huaweicloud sdk

        :param limit: 范围：大于等于1 默认：10
        :type limit: int
        :param name: 长度小于63
        :type name: str
        :param offset: 范围：大于等于0 默认：0
        :type offset: int
        """
        
        

        self._limit = None
        self._name = None
        self._offset = None
        self.discriminator = None

        self.limit = limit
        self.name = name
        self.offset = offset

    @property
    def limit(self):
        """Gets the limit of this ExecuteGetVideosListRequest.

        范围：大于等于1 默认：10

        :return: The limit of this ExecuteGetVideosListRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ExecuteGetVideosListRequest.

        范围：大于等于1 默认：10

        :param limit: The limit of this ExecuteGetVideosListRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        """Gets the name of this ExecuteGetVideosListRequest.

        长度小于63

        :return: The name of this ExecuteGetVideosListRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExecuteGetVideosListRequest.

        长度小于63

        :param name: The name of this ExecuteGetVideosListRequest.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        """Gets the offset of this ExecuteGetVideosListRequest.

        范围：大于等于0 默认：0

        :return: The offset of this ExecuteGetVideosListRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ExecuteGetVideosListRequest.

        范围：大于等于0 默认：0

        :param offset: The offset of this ExecuteGetVideosListRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ExecuteGetVideosListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
