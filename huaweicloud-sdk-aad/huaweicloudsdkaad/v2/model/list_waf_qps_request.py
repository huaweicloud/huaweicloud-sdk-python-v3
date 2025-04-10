# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWafQpsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domains': 'str',
        'value_type': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'recent': 'str',
        'overseas_type': 'int'
    }

    attribute_map = {
        'domains': 'domains',
        'value_type': 'value_type',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'recent': 'recent',
        'overseas_type': 'overseas_type'
    }

    def __init__(self, domains=None, value_type=None, start_time=None, end_time=None, recent=None, overseas_type=None):
        r"""ListWafQpsRequest

        The model defined in huaweicloud sdk

        :param domains: 不传时代表全部域名
        :type domains: str
        :param value_type: 用于 QPS、带宽: 平均值 mean、峰值 peak;用于 响应状态码: 源站返回值 source 、高防返回值 proxy
        :type value_type: str
        :param start_time: 开始时间（毫秒时间戳）
        :type start_time: str
        :param end_time: 结束时间（毫秒时间戳）
        :type end_time: str
        :param recent: 枚举值：yesterday,today,3days,1week,1month 与开始结束时间不同时为空
        :type recent: str
        :param overseas_type: 实例类型，0-大陆，1-海外
        :type overseas_type: int
        """
        
        

        self._domains = None
        self._value_type = None
        self._start_time = None
        self._end_time = None
        self._recent = None
        self._overseas_type = None
        self.discriminator = None

        if domains is not None:
            self.domains = domains
        self.value_type = value_type
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if recent is not None:
            self.recent = recent
        if overseas_type is not None:
            self.overseas_type = overseas_type

    @property
    def domains(self):
        r"""Gets the domains of this ListWafQpsRequest.

        不传时代表全部域名

        :return: The domains of this ListWafQpsRequest.
        :rtype: str
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        r"""Sets the domains of this ListWafQpsRequest.

        不传时代表全部域名

        :param domains: The domains of this ListWafQpsRequest.
        :type domains: str
        """
        self._domains = domains

    @property
    def value_type(self):
        r"""Gets the value_type of this ListWafQpsRequest.

        用于 QPS、带宽: 平均值 mean、峰值 peak;用于 响应状态码: 源站返回值 source 、高防返回值 proxy

        :return: The value_type of this ListWafQpsRequest.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        r"""Sets the value_type of this ListWafQpsRequest.

        用于 QPS、带宽: 平均值 mean、峰值 peak;用于 响应状态码: 源站返回值 source 、高防返回值 proxy

        :param value_type: The value_type of this ListWafQpsRequest.
        :type value_type: str
        """
        self._value_type = value_type

    @property
    def start_time(self):
        r"""Gets the start_time of this ListWafQpsRequest.

        开始时间（毫秒时间戳）

        :return: The start_time of this ListWafQpsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListWafQpsRequest.

        开始时间（毫秒时间戳）

        :param start_time: The start_time of this ListWafQpsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListWafQpsRequest.

        结束时间（毫秒时间戳）

        :return: The end_time of this ListWafQpsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListWafQpsRequest.

        结束时间（毫秒时间戳）

        :param end_time: The end_time of this ListWafQpsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def recent(self):
        r"""Gets the recent of this ListWafQpsRequest.

        枚举值：yesterday,today,3days,1week,1month 与开始结束时间不同时为空

        :return: The recent of this ListWafQpsRequest.
        :rtype: str
        """
        return self._recent

    @recent.setter
    def recent(self, recent):
        r"""Sets the recent of this ListWafQpsRequest.

        枚举值：yesterday,today,3days,1week,1month 与开始结束时间不同时为空

        :param recent: The recent of this ListWafQpsRequest.
        :type recent: str
        """
        self._recent = recent

    @property
    def overseas_type(self):
        r"""Gets the overseas_type of this ListWafQpsRequest.

        实例类型，0-大陆，1-海外

        :return: The overseas_type of this ListWafQpsRequest.
        :rtype: int
        """
        return self._overseas_type

    @overseas_type.setter
    def overseas_type(self, overseas_type):
        r"""Sets the overseas_type of this ListWafQpsRequest.

        实例类型，0-大陆，1-海外

        :param overseas_type: The overseas_type of this ListWafQpsRequest.
        :type overseas_type: int
        """
        self._overseas_type = overseas_type

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
        if not isinstance(other, ListWafQpsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
