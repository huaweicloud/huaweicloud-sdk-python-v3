# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopUaSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ua': 'str',
        'value': 'int',
        'ratio': 'float'
    }

    attribute_map = {
        'ua': 'ua',
        'value': 'value',
        'ratio': 'ratio'
    }

    def __init__(self, ua=None, value=None, ratio=None):
        r"""TopUaSummary

        The model defined in huaweicloud sdk

        :param ua: UA值。
        :type ua: str
        :param value: 对应查询类型的值。（流量单位：Byte）
        :type value: int
        :param ratio: 该ua的流量(或请求数)占当前查询条件下总流量(或请求数)的比例。保留4位小数
        :type ratio: float
        """
        
        

        self._ua = None
        self._value = None
        self._ratio = None
        self.discriminator = None

        if ua is not None:
            self.ua = ua
        if value is not None:
            self.value = value
        if ratio is not None:
            self.ratio = ratio

    @property
    def ua(self):
        r"""Gets the ua of this TopUaSummary.

        UA值。

        :return: The ua of this TopUaSummary.
        :rtype: str
        """
        return self._ua

    @ua.setter
    def ua(self, ua):
        r"""Sets the ua of this TopUaSummary.

        UA值。

        :param ua: The ua of this TopUaSummary.
        :type ua: str
        """
        self._ua = ua

    @property
    def value(self):
        r"""Gets the value of this TopUaSummary.

        对应查询类型的值。（流量单位：Byte）

        :return: The value of this TopUaSummary.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this TopUaSummary.

        对应查询类型的值。（流量单位：Byte）

        :param value: The value of this TopUaSummary.
        :type value: int
        """
        self._value = value

    @property
    def ratio(self):
        r"""Gets the ratio of this TopUaSummary.

        该ua的流量(或请求数)占当前查询条件下总流量(或请求数)的比例。保留4位小数

        :return: The ratio of this TopUaSummary.
        :rtype: float
        """
        return self._ratio

    @ratio.setter
    def ratio(self, ratio):
        r"""Sets the ratio of this TopUaSummary.

        该ua的流量(或请求数)占当前查询条件下总流量(或请求数)的比例。保留4位小数

        :param ratio: The ratio of this TopUaSummary.
        :type ratio: float
        """
        self._ratio = ratio

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
        if not isinstance(other, TopUaSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
