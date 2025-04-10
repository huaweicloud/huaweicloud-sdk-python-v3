# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCreateAccountStatusesRequest:

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
        'states': 'list[str]',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'x_security_token': 'X-Security-Token',
        'states': 'states',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, x_security_token=None, states=None, limit=None, marker=None):
        r"""ListCreateAccountStatusesRequest

        The model defined in huaweicloud sdk

        :param x_security_token: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。
        :type x_security_token: str
        :param states: 要包含在响应中的一个或多个状态的列表。如果此参数不存在，则所有请求都包含在响应中。
        :type states: list[str]
        :param limit: 页面中最大结果数量。
        :type limit: int
        :param marker: 分页标记。
        :type marker: str
        """
        
        

        self._x_security_token = None
        self._states = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        if x_security_token is not None:
            self.x_security_token = x_security_token
        if states is not None:
            self.states = states
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def x_security_token(self):
        r"""Gets the x_security_token of this ListCreateAccountStatusesRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :return: The x_security_token of this ListCreateAccountStatusesRequest.
        :rtype: str
        """
        return self._x_security_token

    @x_security_token.setter
    def x_security_token(self, x_security_token):
        r"""Sets the x_security_token of this ListCreateAccountStatusesRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :param x_security_token: The x_security_token of this ListCreateAccountStatusesRequest.
        :type x_security_token: str
        """
        self._x_security_token = x_security_token

    @property
    def states(self):
        r"""Gets the states of this ListCreateAccountStatusesRequest.

        要包含在响应中的一个或多个状态的列表。如果此参数不存在，则所有请求都包含在响应中。

        :return: The states of this ListCreateAccountStatusesRequest.
        :rtype: list[str]
        """
        return self._states

    @states.setter
    def states(self, states):
        r"""Sets the states of this ListCreateAccountStatusesRequest.

        要包含在响应中的一个或多个状态的列表。如果此参数不存在，则所有请求都包含在响应中。

        :param states: The states of this ListCreateAccountStatusesRequest.
        :type states: list[str]
        """
        self._states = states

    @property
    def limit(self):
        r"""Gets the limit of this ListCreateAccountStatusesRequest.

        页面中最大结果数量。

        :return: The limit of this ListCreateAccountStatusesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCreateAccountStatusesRequest.

        页面中最大结果数量。

        :param limit: The limit of this ListCreateAccountStatusesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListCreateAccountStatusesRequest.

        分页标记。

        :return: The marker of this ListCreateAccountStatusesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListCreateAccountStatusesRequest.

        分页标记。

        :param marker: The marker of this ListCreateAccountStatusesRequest.
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
        if not isinstance(other, ListCreateAccountStatusesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
