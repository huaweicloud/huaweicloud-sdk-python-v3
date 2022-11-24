# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetPrivateZoneProxyPatternRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'proxy_pattern': 'str'
    }

    attribute_map = {
        'proxy_pattern': 'proxy_pattern'
    }

    def __init__(self, proxy_pattern=None):
        """SetPrivateZoneProxyPatternRequestBody

        The model defined in huaweicloud sdk

        :param proxy_pattern: 内网Zone的子域名递归解析代理模式。  取值范围：  AUTHORITY：当前Zone不进行递归解析 RECURSIVE：开启递归解析代理
        :type proxy_pattern: str
        """
        
        

        self._proxy_pattern = None
        self.discriminator = None

        self.proxy_pattern = proxy_pattern

    @property
    def proxy_pattern(self):
        """Gets the proxy_pattern of this SetPrivateZoneProxyPatternRequestBody.

        内网Zone的子域名递归解析代理模式。  取值范围：  AUTHORITY：当前Zone不进行递归解析 RECURSIVE：开启递归解析代理

        :return: The proxy_pattern of this SetPrivateZoneProxyPatternRequestBody.
        :rtype: str
        """
        return self._proxy_pattern

    @proxy_pattern.setter
    def proxy_pattern(self, proxy_pattern):
        """Sets the proxy_pattern of this SetPrivateZoneProxyPatternRequestBody.

        内网Zone的子域名递归解析代理模式。  取值范围：  AUTHORITY：当前Zone不进行递归解析 RECURSIVE：开启递归解析代理

        :param proxy_pattern: The proxy_pattern of this SetPrivateZoneProxyPatternRequestBody.
        :type proxy_pattern: str
        """
        self._proxy_pattern = proxy_pattern

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
        if not isinstance(other, SetPrivateZoneProxyPatternRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
