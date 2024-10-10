# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWafQpsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'recent': 'str',
        'domains': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'overseas_type': 'int'
    }

    attribute_map = {
        'recent': 'recent',
        'domains': 'domains',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'overseas_type': 'overseas_type'
    }

    def __init__(self, recent=None, domains=None, start_time=None, end_time=None, overseas_type=None):
        """ShowWafQpsRequest

        The model defined in huaweicloud sdk

        :param recent: 枚举值：yesterday,today,3days,1week,1month 与开始结束时间不同时为空
        :type recent: str
        :param domains: 查询域名
        :type domains: str
        :param start_time: 开始时间（毫秒时间戳）
        :type start_time: str
        :param end_time: 结束时间（毫秒时间戳）
        :type end_time: str
        :param overseas_type: 防护区域，0-大陆，1-海外
        :type overseas_type: int
        """
        
        

        self._recent = None
        self._domains = None
        self._start_time = None
        self._end_time = None
        self._overseas_type = None
        self.discriminator = None

        if recent is not None:
            self.recent = recent
        if domains is not None:
            self.domains = domains
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if overseas_type is not None:
            self.overseas_type = overseas_type

    @property
    def recent(self):
        """Gets the recent of this ShowWafQpsRequest.

        枚举值：yesterday,today,3days,1week,1month 与开始结束时间不同时为空

        :return: The recent of this ShowWafQpsRequest.
        :rtype: str
        """
        return self._recent

    @recent.setter
    def recent(self, recent):
        """Sets the recent of this ShowWafQpsRequest.

        枚举值：yesterday,today,3days,1week,1month 与开始结束时间不同时为空

        :param recent: The recent of this ShowWafQpsRequest.
        :type recent: str
        """
        self._recent = recent

    @property
    def domains(self):
        """Gets the domains of this ShowWafQpsRequest.

        查询域名

        :return: The domains of this ShowWafQpsRequest.
        :rtype: str
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        """Sets the domains of this ShowWafQpsRequest.

        查询域名

        :param domains: The domains of this ShowWafQpsRequest.
        :type domains: str
        """
        self._domains = domains

    @property
    def start_time(self):
        """Gets the start_time of this ShowWafQpsRequest.

        开始时间（毫秒时间戳）

        :return: The start_time of this ShowWafQpsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowWafQpsRequest.

        开始时间（毫秒时间戳）

        :param start_time: The start_time of this ShowWafQpsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowWafQpsRequest.

        结束时间（毫秒时间戳）

        :return: The end_time of this ShowWafQpsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowWafQpsRequest.

        结束时间（毫秒时间戳）

        :param end_time: The end_time of this ShowWafQpsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def overseas_type(self):
        """Gets the overseas_type of this ShowWafQpsRequest.

        防护区域，0-大陆，1-海外

        :return: The overseas_type of this ShowWafQpsRequest.
        :rtype: int
        """
        return self._overseas_type

    @overseas_type.setter
    def overseas_type(self, overseas_type):
        """Sets the overseas_type of this ShowWafQpsRequest.

        防护区域，0-大陆，1-海外

        :param overseas_type: The overseas_type of this ShowWafQpsRequest.
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
        if not isinstance(other, ShowWafQpsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
