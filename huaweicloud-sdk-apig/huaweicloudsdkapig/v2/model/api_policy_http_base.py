# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiPolicyHttpBase:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'url_domain': 'str',
        'req_protocol': 'str',
        'req_method': 'str',
        'req_uri': 'str',
        'timeout': 'int'
    }

    attribute_map = {
        'url_domain': 'url_domain',
        'req_protocol': 'req_protocol',
        'req_method': 'req_method',
        'req_uri': 'req_uri',
        'timeout': 'timeout'
    }

    def __init__(self, url_domain=None, req_protocol=None, req_method=None, req_uri=None, timeout=None):
        """ApiPolicyHttpBase

        The model defined in huaweicloud sdk

        :param url_domain: 策略后端的Endpoint。 由域名（或IP地址）和端口号组成，总长度不超过255。格式为域名:端口（如：apig.example.com:7443）。如果不写端口，则HTTPS默认端口号为443， HTTP默认端口号为80。 支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、“_”、“-”组成，且只能以英文开头。 
        :type url_domain: str
        :param req_protocol: 请求协议：HTTP、HTTPS
        :type req_protocol: str
        :param req_method: 请求方式：GET、POST、PUT、DELETE、HEAD、PATCH、OPTIONS、ANY
        :type req_method: str
        :param req_uri: 请求地址。可以包含请求参数，用{}标识，比如/getUserInfo/{userId}，支持 * % - _ . 等特殊字符，总长度不超过512，且满足URI规范。  支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、中划线、下划线组成，且只能以英文开头。 &gt; 需要服从URI规范。
        :type req_uri: str
        :param timeout: API网关请求后端服务的超时时间。最大超时时间可通过实例特性backend_timeout配置修改，可修改的上限为600000。  单位：毫秒。
        :type timeout: int
        """
        
        

        self._url_domain = None
        self._req_protocol = None
        self._req_method = None
        self._req_uri = None
        self._timeout = None
        self.discriminator = None

        if url_domain is not None:
            self.url_domain = url_domain
        self.req_protocol = req_protocol
        self.req_method = req_method
        self.req_uri = req_uri
        if timeout is not None:
            self.timeout = timeout

    @property
    def url_domain(self):
        """Gets the url_domain of this ApiPolicyHttpBase.

        策略后端的Endpoint。 由域名（或IP地址）和端口号组成，总长度不超过255。格式为域名:端口（如：apig.example.com:7443）。如果不写端口，则HTTPS默认端口号为443， HTTP默认端口号为80。 支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、“_”、“-”组成，且只能以英文开头。 

        :return: The url_domain of this ApiPolicyHttpBase.
        :rtype: str
        """
        return self._url_domain

    @url_domain.setter
    def url_domain(self, url_domain):
        """Sets the url_domain of this ApiPolicyHttpBase.

        策略后端的Endpoint。 由域名（或IP地址）和端口号组成，总长度不超过255。格式为域名:端口（如：apig.example.com:7443）。如果不写端口，则HTTPS默认端口号为443， HTTP默认端口号为80。 支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、“_”、“-”组成，且只能以英文开头。 

        :param url_domain: The url_domain of this ApiPolicyHttpBase.
        :type url_domain: str
        """
        self._url_domain = url_domain

    @property
    def req_protocol(self):
        """Gets the req_protocol of this ApiPolicyHttpBase.

        请求协议：HTTP、HTTPS

        :return: The req_protocol of this ApiPolicyHttpBase.
        :rtype: str
        """
        return self._req_protocol

    @req_protocol.setter
    def req_protocol(self, req_protocol):
        """Sets the req_protocol of this ApiPolicyHttpBase.

        请求协议：HTTP、HTTPS

        :param req_protocol: The req_protocol of this ApiPolicyHttpBase.
        :type req_protocol: str
        """
        self._req_protocol = req_protocol

    @property
    def req_method(self):
        """Gets the req_method of this ApiPolicyHttpBase.

        请求方式：GET、POST、PUT、DELETE、HEAD、PATCH、OPTIONS、ANY

        :return: The req_method of this ApiPolicyHttpBase.
        :rtype: str
        """
        return self._req_method

    @req_method.setter
    def req_method(self, req_method):
        """Sets the req_method of this ApiPolicyHttpBase.

        请求方式：GET、POST、PUT、DELETE、HEAD、PATCH、OPTIONS、ANY

        :param req_method: The req_method of this ApiPolicyHttpBase.
        :type req_method: str
        """
        self._req_method = req_method

    @property
    def req_uri(self):
        """Gets the req_uri of this ApiPolicyHttpBase.

        请求地址。可以包含请求参数，用{}标识，比如/getUserInfo/{userId}，支持 * % - _ . 等特殊字符，总长度不超过512，且满足URI规范。  支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、中划线、下划线组成，且只能以英文开头。 > 需要服从URI规范。

        :return: The req_uri of this ApiPolicyHttpBase.
        :rtype: str
        """
        return self._req_uri

    @req_uri.setter
    def req_uri(self, req_uri):
        """Sets the req_uri of this ApiPolicyHttpBase.

        请求地址。可以包含请求参数，用{}标识，比如/getUserInfo/{userId}，支持 * % - _ . 等特殊字符，总长度不超过512，且满足URI规范。  支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、中划线、下划线组成，且只能以英文开头。 > 需要服从URI规范。

        :param req_uri: The req_uri of this ApiPolicyHttpBase.
        :type req_uri: str
        """
        self._req_uri = req_uri

    @property
    def timeout(self):
        """Gets the timeout of this ApiPolicyHttpBase.

        API网关请求后端服务的超时时间。最大超时时间可通过实例特性backend_timeout配置修改，可修改的上限为600000。  单位：毫秒。

        :return: The timeout of this ApiPolicyHttpBase.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this ApiPolicyHttpBase.

        API网关请求后端服务的超时时间。最大超时时间可通过实例特性backend_timeout配置修改，可修改的上限为600000。  单位：毫秒。

        :param timeout: The timeout of this ApiPolicyHttpBase.
        :type timeout: int
        """
        self._timeout = timeout

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
        if not isinstance(other, ApiPolicyHttpBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
