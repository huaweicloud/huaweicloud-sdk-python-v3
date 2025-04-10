# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DbConfigCheckResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'param_name': 'str',
        'value': 'str',
        'check_result': 'str'
    }

    attribute_map = {
        'param_name': 'param_name',
        'value': 'value',
        'check_result': 'check_result'
    }

    def __init__(self, param_name=None, value=None, check_result=None):
        r"""DbConfigCheckResult

        The model defined in huaweicloud sdk

        :param param_name: 参数名。
        :type param_name: str
        :param value: 参数值。
        :type value: str
        :param check_result: 校验结果。
        :type check_result: str
        """
        
        

        self._param_name = None
        self._value = None
        self._check_result = None
        self.discriminator = None

        if param_name is not None:
            self.param_name = param_name
        if value is not None:
            self.value = value
        if check_result is not None:
            self.check_result = check_result

    @property
    def param_name(self):
        r"""Gets the param_name of this DbConfigCheckResult.

        参数名。

        :return: The param_name of this DbConfigCheckResult.
        :rtype: str
        """
        return self._param_name

    @param_name.setter
    def param_name(self, param_name):
        r"""Sets the param_name of this DbConfigCheckResult.

        参数名。

        :param param_name: The param_name of this DbConfigCheckResult.
        :type param_name: str
        """
        self._param_name = param_name

    @property
    def value(self):
        r"""Gets the value of this DbConfigCheckResult.

        参数值。

        :return: The value of this DbConfigCheckResult.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this DbConfigCheckResult.

        参数值。

        :param value: The value of this DbConfigCheckResult.
        :type value: str
        """
        self._value = value

    @property
    def check_result(self):
        r"""Gets the check_result of this DbConfigCheckResult.

        校验结果。

        :return: The check_result of this DbConfigCheckResult.
        :rtype: str
        """
        return self._check_result

    @check_result.setter
    def check_result(self, check_result):
        r"""Sets the check_result of this DbConfigCheckResult.

        校验结果。

        :param check_result: The check_result of this DbConfigCheckResult.
        :type check_result: str
        """
        self._check_result = check_result

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
        if not isinstance(other, DbConfigCheckResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
