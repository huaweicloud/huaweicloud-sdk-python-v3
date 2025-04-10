# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SessionPersistence:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'cookie_name': 'str',
        'persistence_timeout': 'int'
    }

    attribute_map = {
        'type': 'type',
        'cookie_name': 'cookie_name',
        'persistence_timeout': 'persistence_timeout'
    }

    def __init__(self, type=None, cookie_name=None, persistence_timeout=None):
        r"""SessionPersistence

        The model defined in huaweicloud sdk

        :param type: 会话保持的类型。SOURCE_IP：根据请求的源IP，将同一IP的请求发送到同一个后端云服务器上。HTTP_COOKIE：客户端第一次发送请求时，负载均衡器自动生成cookie并将该cookie插入响应消息中，后续请求会发送到处理第一个请求的后端云服务器上。APP_COOKIE：客户端第一次发送请求时，后端服务器生成cookie并将该cookie插入响应消息中，后续请求会发送到处理第一个请求的后端云服务器上。当后端云服务器的protocol为TCP时，只按SOURCE_IP生效当后端云服务器的protocol为HTTP时，只按HTTP_COOKIE或APP_COOKIE生效
        :type type: str
        :param cookie_name: cookie的名称。只有当会话保持的类型是APP_COOKIE时可以指定。
        :type cookie_name: str
        :param persistence_timeout: 会话保持的超时时间。取值范围：[1,60]（分钟）：当后端云服务器的protocol为TCP、UDP时[1,1440]（分钟）：当后端云服务器的protocol为HTTP时。当type为APP_COOKIE时该字段不生效。
        :type persistence_timeout: int
        """
        
        

        self._type = None
        self._cookie_name = None
        self._persistence_timeout = None
        self.discriminator = None

        self.type = type
        if cookie_name is not None:
            self.cookie_name = cookie_name
        if persistence_timeout is not None:
            self.persistence_timeout = persistence_timeout

    @property
    def type(self):
        r"""Gets the type of this SessionPersistence.

        会话保持的类型。SOURCE_IP：根据请求的源IP，将同一IP的请求发送到同一个后端云服务器上。HTTP_COOKIE：客户端第一次发送请求时，负载均衡器自动生成cookie并将该cookie插入响应消息中，后续请求会发送到处理第一个请求的后端云服务器上。APP_COOKIE：客户端第一次发送请求时，后端服务器生成cookie并将该cookie插入响应消息中，后续请求会发送到处理第一个请求的后端云服务器上。当后端云服务器的protocol为TCP时，只按SOURCE_IP生效当后端云服务器的protocol为HTTP时，只按HTTP_COOKIE或APP_COOKIE生效

        :return: The type of this SessionPersistence.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SessionPersistence.

        会话保持的类型。SOURCE_IP：根据请求的源IP，将同一IP的请求发送到同一个后端云服务器上。HTTP_COOKIE：客户端第一次发送请求时，负载均衡器自动生成cookie并将该cookie插入响应消息中，后续请求会发送到处理第一个请求的后端云服务器上。APP_COOKIE：客户端第一次发送请求时，后端服务器生成cookie并将该cookie插入响应消息中，后续请求会发送到处理第一个请求的后端云服务器上。当后端云服务器的protocol为TCP时，只按SOURCE_IP生效当后端云服务器的protocol为HTTP时，只按HTTP_COOKIE或APP_COOKIE生效

        :param type: The type of this SessionPersistence.
        :type type: str
        """
        self._type = type

    @property
    def cookie_name(self):
        r"""Gets the cookie_name of this SessionPersistence.

        cookie的名称。只有当会话保持的类型是APP_COOKIE时可以指定。

        :return: The cookie_name of this SessionPersistence.
        :rtype: str
        """
        return self._cookie_name

    @cookie_name.setter
    def cookie_name(self, cookie_name):
        r"""Sets the cookie_name of this SessionPersistence.

        cookie的名称。只有当会话保持的类型是APP_COOKIE时可以指定。

        :param cookie_name: The cookie_name of this SessionPersistence.
        :type cookie_name: str
        """
        self._cookie_name = cookie_name

    @property
    def persistence_timeout(self):
        r"""Gets the persistence_timeout of this SessionPersistence.

        会话保持的超时时间。取值范围：[1,60]（分钟）：当后端云服务器的protocol为TCP、UDP时[1,1440]（分钟）：当后端云服务器的protocol为HTTP时。当type为APP_COOKIE时该字段不生效。

        :return: The persistence_timeout of this SessionPersistence.
        :rtype: int
        """
        return self._persistence_timeout

    @persistence_timeout.setter
    def persistence_timeout(self, persistence_timeout):
        r"""Sets the persistence_timeout of this SessionPersistence.

        会话保持的超时时间。取值范围：[1,60]（分钟）：当后端云服务器的protocol为TCP、UDP时[1,1440]（分钟）：当后端云服务器的protocol为HTTP时。当type为APP_COOKIE时该字段不生效。

        :param persistence_timeout: The persistence_timeout of this SessionPersistence.
        :type persistence_timeout: int
        """
        self._persistence_timeout = persistence_timeout

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
        if not isinstance(other, SessionPersistence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
