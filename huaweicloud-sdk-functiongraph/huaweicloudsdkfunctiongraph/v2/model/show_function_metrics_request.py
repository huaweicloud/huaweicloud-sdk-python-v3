# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFunctionMetricsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'func_urn': 'str',
        'period': 'str'
    }

    attribute_map = {
        'func_urn': 'func_urn',
        'period': 'period'
    }

    def __init__(self, func_urn=None, period=None):
        r"""ShowFunctionMetricsRequest

        The model defined in huaweicloud sdk

        :param func_urn: 函数的URN，详细解释见FunctionGraph函数模型的描述。
        :type func_urn: str
        :param period: 时间间隔（单位：min）
        :type period: str
        """
        
        

        self._func_urn = None
        self._period = None
        self.discriminator = None

        self.func_urn = func_urn
        self.period = period

    @property
    def func_urn(self):
        r"""Gets the func_urn of this ShowFunctionMetricsRequest.

        函数的URN，详细解释见FunctionGraph函数模型的描述。

        :return: The func_urn of this ShowFunctionMetricsRequest.
        :rtype: str
        """
        return self._func_urn

    @func_urn.setter
    def func_urn(self, func_urn):
        r"""Sets the func_urn of this ShowFunctionMetricsRequest.

        函数的URN，详细解释见FunctionGraph函数模型的描述。

        :param func_urn: The func_urn of this ShowFunctionMetricsRequest.
        :type func_urn: str
        """
        self._func_urn = func_urn

    @property
    def period(self):
        r"""Gets the period of this ShowFunctionMetricsRequest.

        时间间隔（单位：min）

        :return: The period of this ShowFunctionMetricsRequest.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this ShowFunctionMetricsRequest.

        时间间隔（单位：min）

        :param period: The period of this ShowFunctionMetricsRequest.
        :type period: str
        """
        self._period = period

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
        if not isinstance(other, ShowFunctionMetricsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
