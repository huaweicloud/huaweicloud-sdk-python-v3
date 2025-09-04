# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopIpSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ip': 'str',
        'value': 'int',
        'ratio': 'float'
    }

    attribute_map = {
        'ip': 'ip',
        'value': 'value',
        'ratio': 'ratio'
    }

    def __init__(self, ip=None, value=None, ratio=None):
        r"""TopIpSummary

        The model defined in huaweicloud sdk

        :param ip: IP值。
        :type ip: str
        :param value: 对应查询类型的值。（流量单位：Byte）
        :type value: int
        :param ratio: 该IP的流量(或请求数)占当前查询条件下总流量(或请求数)的比例。保留4位小数
        :type ratio: float
        """
        
        

        self._ip = None
        self._value = None
        self._ratio = None
        self.discriminator = None

        if ip is not None:
            self.ip = ip
        if value is not None:
            self.value = value
        if ratio is not None:
            self.ratio = ratio

    @property
    def ip(self):
        r"""Gets the ip of this TopIpSummary.

        IP值。

        :return: The ip of this TopIpSummary.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this TopIpSummary.

        IP值。

        :param ip: The ip of this TopIpSummary.
        :type ip: str
        """
        self._ip = ip

    @property
    def value(self):
        r"""Gets the value of this TopIpSummary.

        对应查询类型的值。（流量单位：Byte）

        :return: The value of this TopIpSummary.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this TopIpSummary.

        对应查询类型的值。（流量单位：Byte）

        :param value: The value of this TopIpSummary.
        :type value: int
        """
        self._value = value

    @property
    def ratio(self):
        r"""Gets the ratio of this TopIpSummary.

        该IP的流量(或请求数)占当前查询条件下总流量(或请求数)的比例。保留4位小数

        :return: The ratio of this TopIpSummary.
        :rtype: float
        """
        return self._ratio

    @ratio.setter
    def ratio(self, ratio):
        r"""Sets the ratio of this TopIpSummary.

        该IP的流量(或请求数)占当前查询条件下总流量(或请求数)的比例。保留4位小数

        :param ratio: The ratio of this TopIpSummary.
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
        if not isinstance(other, TopIpSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
