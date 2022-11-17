# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportFunctionRequest:

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
        'config': 'bool',
        'code': 'bool',
        'type': 'str'
    }

    attribute_map = {
        'function_urn': 'function_urn',
        'config': 'config',
        'code': 'code',
        'type': 'type'
    }

    def __init__(self, function_urn=None, config=None, code=None, type=None):
        """ExportFunctionRequest

        The model defined in huaweicloud sdk

        :param function_urn: 函数的URN，详细解释见FunctionGraph函数模型的描述。
        :type function_urn: str
        :param config: 是否导出函数配置
        :type config: bool
        :param code: 是否导出函数代码
        :type code: bool
        :param type: 兼容老的方式，type&#x3D;code代表导出代码,type&#x3D;config代码导出配置
        :type type: str
        """
        
        

        self._function_urn = None
        self._config = None
        self._code = None
        self._type = None
        self.discriminator = None

        self.function_urn = function_urn
        if config is not None:
            self.config = config
        if code is not None:
            self.code = code
        if type is not None:
            self.type = type

    @property
    def function_urn(self):
        """Gets the function_urn of this ExportFunctionRequest.

        函数的URN，详细解释见FunctionGraph函数模型的描述。

        :return: The function_urn of this ExportFunctionRequest.
        :rtype: str
        """
        return self._function_urn

    @function_urn.setter
    def function_urn(self, function_urn):
        """Sets the function_urn of this ExportFunctionRequest.

        函数的URN，详细解释见FunctionGraph函数模型的描述。

        :param function_urn: The function_urn of this ExportFunctionRequest.
        :type function_urn: str
        """
        self._function_urn = function_urn

    @property
    def config(self):
        """Gets the config of this ExportFunctionRequest.

        是否导出函数配置

        :return: The config of this ExportFunctionRequest.
        :rtype: bool
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this ExportFunctionRequest.

        是否导出函数配置

        :param config: The config of this ExportFunctionRequest.
        :type config: bool
        """
        self._config = config

    @property
    def code(self):
        """Gets the code of this ExportFunctionRequest.

        是否导出函数代码

        :return: The code of this ExportFunctionRequest.
        :rtype: bool
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ExportFunctionRequest.

        是否导出函数代码

        :param code: The code of this ExportFunctionRequest.
        :type code: bool
        """
        self._code = code

    @property
    def type(self):
        """Gets the type of this ExportFunctionRequest.

        兼容老的方式，type=code代表导出代码,type=config代码导出配置

        :return: The type of this ExportFunctionRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExportFunctionRequest.

        兼容老的方式，type=code代表导出代码,type=config代码导出配置

        :param type: The type of this ExportFunctionRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ExportFunctionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
