# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiPolicyFunctionBase:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'function_urn': 'str',
        'invocation_type': 'str',
        'network_type': 'str',
        'version': 'str',
        'alias_urn': 'str',
        'timeout': 'int',
        'req_protocol': 'str'
    }

    attribute_map = {
        'function_urn': 'function_urn',
        'invocation_type': 'invocation_type',
        'network_type': 'network_type',
        'version': 'version',
        'alias_urn': 'alias_urn',
        'timeout': 'timeout',
        'req_protocol': 'req_protocol'
    }

    def __init__(self, function_urn=None, invocation_type=None, network_type=None, version=None, alias_urn=None, timeout=None, req_protocol=None):
        r"""ApiPolicyFunctionBase

        The model defined in huaweicloud sdk

        :param function_urn: 函数URN
        :type function_urn: str
        :param invocation_type: 调用类型 - async： 异步 - sync：同步
        :type invocation_type: str
        :param network_type: 对接函数的网络架构类型 - V1：非VPC网络架构 - V2：VPC网络架构
        :type network_type: str
        :param version: 函数版本   当函数别名URN和函数版本同时传入时，函数版本将被忽略，只会使用函数别名URN
        :type version: str
        :param alias_urn: 函数别名URN   当函数别名URN和函数版本同时传入时，函数版本将被忽略，只会使用函数别名URN
        :type alias_urn: str
        :param timeout: API网关请求后端服务的超时时间。函数网络架构为V1时最大超时时间为60000，V2最大超时时间可通过实例特性backend_timeout配置修改，可修改的上限为600000。  单位：毫秒。
        :type timeout: int
        :param req_protocol: 函数后端的请求协议：HTTPS、GRPCS，默认值为HTTPS，前端配置中的请求协议为GRPCS时可选GRPCS。
        :type req_protocol: str
        """
        
        

        self._function_urn = None
        self._invocation_type = None
        self._network_type = None
        self._version = None
        self._alias_urn = None
        self._timeout = None
        self._req_protocol = None
        self.discriminator = None

        self.function_urn = function_urn
        self.invocation_type = invocation_type
        self.network_type = network_type
        if version is not None:
            self.version = version
        if alias_urn is not None:
            self.alias_urn = alias_urn
        if timeout is not None:
            self.timeout = timeout
        if req_protocol is not None:
            self.req_protocol = req_protocol

    @property
    def function_urn(self):
        r"""Gets the function_urn of this ApiPolicyFunctionBase.

        函数URN

        :return: The function_urn of this ApiPolicyFunctionBase.
        :rtype: str
        """
        return self._function_urn

    @function_urn.setter
    def function_urn(self, function_urn):
        r"""Sets the function_urn of this ApiPolicyFunctionBase.

        函数URN

        :param function_urn: The function_urn of this ApiPolicyFunctionBase.
        :type function_urn: str
        """
        self._function_urn = function_urn

    @property
    def invocation_type(self):
        r"""Gets the invocation_type of this ApiPolicyFunctionBase.

        调用类型 - async： 异步 - sync：同步

        :return: The invocation_type of this ApiPolicyFunctionBase.
        :rtype: str
        """
        return self._invocation_type

    @invocation_type.setter
    def invocation_type(self, invocation_type):
        r"""Sets the invocation_type of this ApiPolicyFunctionBase.

        调用类型 - async： 异步 - sync：同步

        :param invocation_type: The invocation_type of this ApiPolicyFunctionBase.
        :type invocation_type: str
        """
        self._invocation_type = invocation_type

    @property
    def network_type(self):
        r"""Gets the network_type of this ApiPolicyFunctionBase.

        对接函数的网络架构类型 - V1：非VPC网络架构 - V2：VPC网络架构

        :return: The network_type of this ApiPolicyFunctionBase.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        r"""Sets the network_type of this ApiPolicyFunctionBase.

        对接函数的网络架构类型 - V1：非VPC网络架构 - V2：VPC网络架构

        :param network_type: The network_type of this ApiPolicyFunctionBase.
        :type network_type: str
        """
        self._network_type = network_type

    @property
    def version(self):
        r"""Gets the version of this ApiPolicyFunctionBase.

        函数版本   当函数别名URN和函数版本同时传入时，函数版本将被忽略，只会使用函数别名URN

        :return: The version of this ApiPolicyFunctionBase.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ApiPolicyFunctionBase.

        函数版本   当函数别名URN和函数版本同时传入时，函数版本将被忽略，只会使用函数别名URN

        :param version: The version of this ApiPolicyFunctionBase.
        :type version: str
        """
        self._version = version

    @property
    def alias_urn(self):
        r"""Gets the alias_urn of this ApiPolicyFunctionBase.

        函数别名URN   当函数别名URN和函数版本同时传入时，函数版本将被忽略，只会使用函数别名URN

        :return: The alias_urn of this ApiPolicyFunctionBase.
        :rtype: str
        """
        return self._alias_urn

    @alias_urn.setter
    def alias_urn(self, alias_urn):
        r"""Sets the alias_urn of this ApiPolicyFunctionBase.

        函数别名URN   当函数别名URN和函数版本同时传入时，函数版本将被忽略，只会使用函数别名URN

        :param alias_urn: The alias_urn of this ApiPolicyFunctionBase.
        :type alias_urn: str
        """
        self._alias_urn = alias_urn

    @property
    def timeout(self):
        r"""Gets the timeout of this ApiPolicyFunctionBase.

        API网关请求后端服务的超时时间。函数网络架构为V1时最大超时时间为60000，V2最大超时时间可通过实例特性backend_timeout配置修改，可修改的上限为600000。  单位：毫秒。

        :return: The timeout of this ApiPolicyFunctionBase.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this ApiPolicyFunctionBase.

        API网关请求后端服务的超时时间。函数网络架构为V1时最大超时时间为60000，V2最大超时时间可通过实例特性backend_timeout配置修改，可修改的上限为600000。  单位：毫秒。

        :param timeout: The timeout of this ApiPolicyFunctionBase.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def req_protocol(self):
        r"""Gets the req_protocol of this ApiPolicyFunctionBase.

        函数后端的请求协议：HTTPS、GRPCS，默认值为HTTPS，前端配置中的请求协议为GRPCS时可选GRPCS。

        :return: The req_protocol of this ApiPolicyFunctionBase.
        :rtype: str
        """
        return self._req_protocol

    @req_protocol.setter
    def req_protocol(self, req_protocol):
        r"""Sets the req_protocol of this ApiPolicyFunctionBase.

        函数后端的请求协议：HTTPS、GRPCS，默认值为HTTPS，前端配置中的请求协议为GRPCS时可选GRPCS。

        :param req_protocol: The req_protocol of this ApiPolicyFunctionBase.
        :type req_protocol: str
        """
        self._req_protocol = req_protocol

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
        if not isinstance(other, ApiPolicyFunctionBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
