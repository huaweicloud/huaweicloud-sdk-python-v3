# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteRdSforMySqlProxyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'proxy_id': 'str',
        'x_language': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'proxy_id': 'proxy_id',
        'x_language': 'X-Language'
    }

    def __init__(self, instance_id=None, proxy_id=None, x_language=None):
        r"""DeleteRdSforMySqlProxyRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，严格匹配UUID规则。
        :type instance_id: str
        :param proxy_id: 数据库代理ID，严格匹配UUID规则。
        :type proxy_id: str
        :param x_language: 语言。
        :type x_language: str
        """
        
        

        self._instance_id = None
        self._proxy_id = None
        self._x_language = None
        self.discriminator = None

        self.instance_id = instance_id
        self.proxy_id = proxy_id
        if x_language is not None:
            self.x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this DeleteRdSforMySqlProxyRequest.

        实例ID，严格匹配UUID规则。

        :return: The instance_id of this DeleteRdSforMySqlProxyRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this DeleteRdSforMySqlProxyRequest.

        实例ID，严格匹配UUID规则。

        :param instance_id: The instance_id of this DeleteRdSforMySqlProxyRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def proxy_id(self):
        r"""Gets the proxy_id of this DeleteRdSforMySqlProxyRequest.

        数据库代理ID，严格匹配UUID规则。

        :return: The proxy_id of this DeleteRdSforMySqlProxyRequest.
        :rtype: str
        """
        return self._proxy_id

    @proxy_id.setter
    def proxy_id(self, proxy_id):
        r"""Sets the proxy_id of this DeleteRdSforMySqlProxyRequest.

        数据库代理ID，严格匹配UUID规则。

        :param proxy_id: The proxy_id of this DeleteRdSforMySqlProxyRequest.
        :type proxy_id: str
        """
        self._proxy_id = proxy_id

    @property
    def x_language(self):
        r"""Gets the x_language of this DeleteRdSforMySqlProxyRequest.

        语言。

        :return: The x_language of this DeleteRdSforMySqlProxyRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this DeleteRdSforMySqlProxyRequest.

        语言。

        :param x_language: The x_language of this DeleteRdSforMySqlProxyRequest.
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
        if not isinstance(other, DeleteRdSforMySqlProxyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
