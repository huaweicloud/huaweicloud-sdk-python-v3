# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnvironmentCheck:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'params': 'list[str]',
        'name': 'str',
        'result': 'str',
        'error_code': 'str',
        'error_or_warn': 'str',
        'error_params': 'str'
    }

    attribute_map = {
        'id': 'id',
        'params': 'params',
        'name': 'name',
        'result': 'result',
        'error_code': 'error_code',
        'error_or_warn': 'error_or_warn',
        'error_params': 'error_params'
    }

    def __init__(self, id=None, params=None, name=None, result=None, error_code=None, error_or_warn=None, error_params=None):
        r"""EnvironmentCheck

        The model defined in huaweicloud sdk

        :param id: 该检查项的ID
        :type id: int
        :param params: 参数
        :type params: list[str]
        :param name: 检查项名称
        :type name: str
        :param result: 检查结果 OK：检查通过 WARN：警告 ERROR:检查不通过
        :type result: str
        :param error_code: 检查不通过的错误码
        :type error_code: str
        :param error_or_warn: 检查的错误或者警告
        :type error_or_warn: str
        :param error_params: 检查不通过的错误参数
        :type error_params: str
        """
        
        

        self._id = None
        self._params = None
        self._name = None
        self._result = None
        self._error_code = None
        self._error_or_warn = None
        self._error_params = None
        self.discriminator = None

        self.id = id
        if params is not None:
            self.params = params
        self.name = name
        self.result = result
        if error_code is not None:
            self.error_code = error_code
        if error_or_warn is not None:
            self.error_or_warn = error_or_warn
        if error_params is not None:
            self.error_params = error_params

    @property
    def id(self):
        r"""Gets the id of this EnvironmentCheck.

        该检查项的ID

        :return: The id of this EnvironmentCheck.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this EnvironmentCheck.

        该检查项的ID

        :param id: The id of this EnvironmentCheck.
        :type id: int
        """
        self._id = id

    @property
    def params(self):
        r"""Gets the params of this EnvironmentCheck.

        参数

        :return: The params of this EnvironmentCheck.
        :rtype: list[str]
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this EnvironmentCheck.

        参数

        :param params: The params of this EnvironmentCheck.
        :type params: list[str]
        """
        self._params = params

    @property
    def name(self):
        r"""Gets the name of this EnvironmentCheck.

        检查项名称

        :return: The name of this EnvironmentCheck.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EnvironmentCheck.

        检查项名称

        :param name: The name of this EnvironmentCheck.
        :type name: str
        """
        self._name = name

    @property
    def result(self):
        r"""Gets the result of this EnvironmentCheck.

        检查结果 OK：检查通过 WARN：警告 ERROR:检查不通过

        :return: The result of this EnvironmentCheck.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this EnvironmentCheck.

        检查结果 OK：检查通过 WARN：警告 ERROR:检查不通过

        :param result: The result of this EnvironmentCheck.
        :type result: str
        """
        self._result = result

    @property
    def error_code(self):
        r"""Gets the error_code of this EnvironmentCheck.

        检查不通过的错误码

        :return: The error_code of this EnvironmentCheck.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this EnvironmentCheck.

        检查不通过的错误码

        :param error_code: The error_code of this EnvironmentCheck.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_or_warn(self):
        r"""Gets the error_or_warn of this EnvironmentCheck.

        检查的错误或者警告

        :return: The error_or_warn of this EnvironmentCheck.
        :rtype: str
        """
        return self._error_or_warn

    @error_or_warn.setter
    def error_or_warn(self, error_or_warn):
        r"""Sets the error_or_warn of this EnvironmentCheck.

        检查的错误或者警告

        :param error_or_warn: The error_or_warn of this EnvironmentCheck.
        :type error_or_warn: str
        """
        self._error_or_warn = error_or_warn

    @property
    def error_params(self):
        r"""Gets the error_params of this EnvironmentCheck.

        检查不通过的错误参数

        :return: The error_params of this EnvironmentCheck.
        :rtype: str
        """
        return self._error_params

    @error_params.setter
    def error_params(self, error_params):
        r"""Sets the error_params of this EnvironmentCheck.

        检查不通过的错误参数

        :param error_params: The error_params of this EnvironmentCheck.
        :type error_params: str
        """
        self._error_params = error_params

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
        if not isinstance(other, EnvironmentCheck):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
