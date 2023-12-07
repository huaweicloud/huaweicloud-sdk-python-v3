# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListControlsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('x_security_token')

    openapi_types = {
        'x_security_token': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'x_security_token': 'X-Security-Token',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, x_security_token=None, limit=None, marker=None):
        """ListControlsRequest

        The model defined in huaweicloud sdk

        :param x_security_token: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。
        :type x_security_token: str
        :param limit: 分页页面的最大值。
        :type limit: int
        :param marker: 页面标记。
        :type marker: str
        """
        
        

        self._x_security_token = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        if x_security_token is not None:
            self.x_security_token = x_security_token
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def x_security_token(self):
        """Gets the x_security_token of this ListControlsRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :return: The x_security_token of this ListControlsRequest.
        :rtype: str
        """
        return self._x_security_token

    @x_security_token.setter
    def x_security_token(self, x_security_token):
        """Sets the x_security_token of this ListControlsRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :param x_security_token: The x_security_token of this ListControlsRequest.
        :type x_security_token: str
        """
        self._x_security_token = x_security_token

    @property
    def limit(self):
        """Gets the limit of this ListControlsRequest.

        分页页面的最大值。

        :return: The limit of this ListControlsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListControlsRequest.

        分页页面的最大值。

        :param limit: The limit of this ListControlsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListControlsRequest.

        页面标记。

        :return: The marker of this ListControlsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListControlsRequest.

        页面标记。

        :param marker: The marker of this ListControlsRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListControlsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
