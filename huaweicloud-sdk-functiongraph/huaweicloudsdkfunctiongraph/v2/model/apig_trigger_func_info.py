# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApigTriggerFuncInfo:

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
        'timeout': 'int',
        'version': 'str'
    }

    attribute_map = {
        'function_urn': 'function_urn',
        'invocation_type': 'invocation_type',
        'timeout': 'timeout',
        'version': 'version'
    }

    def __init__(self, function_urn=None, invocation_type=None, timeout=None, version=None):
        r"""ApigTriggerFuncInfo

        The model defined in huaweicloud sdk

        :param function_urn: 函数的URN，详细解释见FunctionGraph函数模型的描述。
        :type function_urn: str
        :param invocation_type: 调用函数执行方式。 - sync：同步执行 - async：异步执行
        :type invocation_type: str
        :param timeout: API网关请求函数服务的超时时间（毫秒）。APIG触发器此参数必填。
        :type timeout: int
        :param version: 函数版本信息。
        :type version: str
        """
        
        

        self._function_urn = None
        self._invocation_type = None
        self._timeout = None
        self._version = None
        self.discriminator = None

        if function_urn is not None:
            self.function_urn = function_urn
        if invocation_type is not None:
            self.invocation_type = invocation_type
        self.timeout = timeout
        if version is not None:
            self.version = version

    @property
    def function_urn(self):
        r"""Gets the function_urn of this ApigTriggerFuncInfo.

        函数的URN，详细解释见FunctionGraph函数模型的描述。

        :return: The function_urn of this ApigTriggerFuncInfo.
        :rtype: str
        """
        return self._function_urn

    @function_urn.setter
    def function_urn(self, function_urn):
        r"""Sets the function_urn of this ApigTriggerFuncInfo.

        函数的URN，详细解释见FunctionGraph函数模型的描述。

        :param function_urn: The function_urn of this ApigTriggerFuncInfo.
        :type function_urn: str
        """
        self._function_urn = function_urn

    @property
    def invocation_type(self):
        r"""Gets the invocation_type of this ApigTriggerFuncInfo.

        调用函数执行方式。 - sync：同步执行 - async：异步执行

        :return: The invocation_type of this ApigTriggerFuncInfo.
        :rtype: str
        """
        return self._invocation_type

    @invocation_type.setter
    def invocation_type(self, invocation_type):
        r"""Sets the invocation_type of this ApigTriggerFuncInfo.

        调用函数执行方式。 - sync：同步执行 - async：异步执行

        :param invocation_type: The invocation_type of this ApigTriggerFuncInfo.
        :type invocation_type: str
        """
        self._invocation_type = invocation_type

    @property
    def timeout(self):
        r"""Gets the timeout of this ApigTriggerFuncInfo.

        API网关请求函数服务的超时时间（毫秒）。APIG触发器此参数必填。

        :return: The timeout of this ApigTriggerFuncInfo.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this ApigTriggerFuncInfo.

        API网关请求函数服务的超时时间（毫秒）。APIG触发器此参数必填。

        :param timeout: The timeout of this ApigTriggerFuncInfo.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def version(self):
        r"""Gets the version of this ApigTriggerFuncInfo.

        函数版本信息。

        :return: The version of this ApigTriggerFuncInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ApigTriggerFuncInfo.

        函数版本信息。

        :param version: The version of this ApigTriggerFuncInfo.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, ApigTriggerFuncInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
