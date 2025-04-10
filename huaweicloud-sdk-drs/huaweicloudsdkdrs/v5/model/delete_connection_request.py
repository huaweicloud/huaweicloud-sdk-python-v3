# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteConnectionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connection_id': 'str',
        'x_language': 'str'
    }

    attribute_map = {
        'connection_id': 'connection_id',
        'x_language': 'X-Language'
    }

    def __init__(self, connection_id=None, x_language=None):
        r"""DeleteConnectionRequest

        The model defined in huaweicloud sdk

        :param connection_id: 连接ID。
        :type connection_id: str
        :param x_language: 请求语言类型。
        :type x_language: str
        """
        
        

        self._connection_id = None
        self._x_language = None
        self.discriminator = None

        self.connection_id = connection_id
        if x_language is not None:
            self.x_language = x_language

    @property
    def connection_id(self):
        r"""Gets the connection_id of this DeleteConnectionRequest.

        连接ID。

        :return: The connection_id of this DeleteConnectionRequest.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        r"""Sets the connection_id of this DeleteConnectionRequest.

        连接ID。

        :param connection_id: The connection_id of this DeleteConnectionRequest.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def x_language(self):
        r"""Gets the x_language of this DeleteConnectionRequest.

        请求语言类型。

        :return: The x_language of this DeleteConnectionRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this DeleteConnectionRequest.

        请求语言类型。

        :param x_language: The x_language of this DeleteConnectionRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, DeleteConnectionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
