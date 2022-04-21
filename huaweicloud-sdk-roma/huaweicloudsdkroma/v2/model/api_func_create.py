# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiFuncCreate:

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
        'remark': 'str',
        'invocation_type': 'str',
        'version': 'str',
        'timeout': 'int',
        'authorizer_id': 'str'
    }

    attribute_map = {
        'function_urn': 'function_urn',
        'remark': 'remark',
        'invocation_type': 'invocation_type',
        'version': 'version',
        'timeout': 'timeout',
        'authorizer_id': 'authorizer_id'
    }

    def __init__(self, function_urn=None, remark=None, invocation_type=None, version=None, timeout=None, authorizer_id=None):
        """ApiFuncCreate

        The model defined in huaweicloud sdk

        :param function_urn: 函数URN
        :type function_urn: str
        :param remark: 描述信息。 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type remark: str
        :param invocation_type: 调用类型 - async： 异步 - sync：同步
        :type invocation_type: str
        :param version: 版本。
        :type version: str
        :param timeout: ROMA Connect APIC请求后端服务的超时时间。最大超时时间可通过实例特性backend_timeout配置修改，可修改的上限为600000  单位：毫秒。
        :type timeout: int
        :param authorizer_id: 后端自定义认证ID
        :type authorizer_id: str
        """
        
        

        self._function_urn = None
        self._remark = None
        self._invocation_type = None
        self._version = None
        self._timeout = None
        self._authorizer_id = None
        self.discriminator = None

        self.function_urn = function_urn
        if remark is not None:
            self.remark = remark
        self.invocation_type = invocation_type
        if version is not None:
            self.version = version
        self.timeout = timeout
        if authorizer_id is not None:
            self.authorizer_id = authorizer_id

    @property
    def function_urn(self):
        """Gets the function_urn of this ApiFuncCreate.

        函数URN

        :return: The function_urn of this ApiFuncCreate.
        :rtype: str
        """
        return self._function_urn

    @function_urn.setter
    def function_urn(self, function_urn):
        """Sets the function_urn of this ApiFuncCreate.

        函数URN

        :param function_urn: The function_urn of this ApiFuncCreate.
        :type function_urn: str
        """
        self._function_urn = function_urn

    @property
    def remark(self):
        """Gets the remark of this ApiFuncCreate.

        描述信息。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The remark of this ApiFuncCreate.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this ApiFuncCreate.

        描述信息。 > 中文字符必须为UTF-8或者unicode编码。

        :param remark: The remark of this ApiFuncCreate.
        :type remark: str
        """
        self._remark = remark

    @property
    def invocation_type(self):
        """Gets the invocation_type of this ApiFuncCreate.

        调用类型 - async： 异步 - sync：同步

        :return: The invocation_type of this ApiFuncCreate.
        :rtype: str
        """
        return self._invocation_type

    @invocation_type.setter
    def invocation_type(self, invocation_type):
        """Sets the invocation_type of this ApiFuncCreate.

        调用类型 - async： 异步 - sync：同步

        :param invocation_type: The invocation_type of this ApiFuncCreate.
        :type invocation_type: str
        """
        self._invocation_type = invocation_type

    @property
    def version(self):
        """Gets the version of this ApiFuncCreate.

        版本。

        :return: The version of this ApiFuncCreate.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ApiFuncCreate.

        版本。

        :param version: The version of this ApiFuncCreate.
        :type version: str
        """
        self._version = version

    @property
    def timeout(self):
        """Gets the timeout of this ApiFuncCreate.

        ROMA Connect APIC请求后端服务的超时时间。最大超时时间可通过实例特性backend_timeout配置修改，可修改的上限为600000  单位：毫秒。

        :return: The timeout of this ApiFuncCreate.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this ApiFuncCreate.

        ROMA Connect APIC请求后端服务的超时时间。最大超时时间可通过实例特性backend_timeout配置修改，可修改的上限为600000  单位：毫秒。

        :param timeout: The timeout of this ApiFuncCreate.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def authorizer_id(self):
        """Gets the authorizer_id of this ApiFuncCreate.

        后端自定义认证ID

        :return: The authorizer_id of this ApiFuncCreate.
        :rtype: str
        """
        return self._authorizer_id

    @authorizer_id.setter
    def authorizer_id(self, authorizer_id):
        """Sets the authorizer_id of this ApiFuncCreate.

        后端自定义认证ID

        :param authorizer_id: The authorizer_id of this ApiFuncCreate.
        :type authorizer_id: str
        """
        self._authorizer_id = authorizer_id

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
        if not isinstance(other, ApiFuncCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
