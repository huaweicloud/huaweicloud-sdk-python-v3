# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPlayDomainStreamInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'play_domains': 'list[str]',
        'time': 'str'
    }

    attribute_map = {
        'play_domains': 'play_domains',
        'time': 'time'
    }

    def __init__(self, play_domains=None, time=None):
        r"""ListPlayDomainStreamInfoRequest

        The model defined in huaweicloud sdk

        :param play_domains: 播放域名列表，最多支持查询10个域名，多个域名以逗号分隔。  如果不传入域名，则查询租户下所有播放域名的流数据。 
        :type play_domains: list[str]
        :param time: 查询数据的时间点，精确到分钟。  日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ，最大查询周期七天。  时间必须为时间粒度整时刻点，如：2024-02-02T08:01:00Z。 
        :type time: str
        """
        
        

        self._play_domains = None
        self._time = None
        self.discriminator = None

        if play_domains is not None:
            self.play_domains = play_domains
        self.time = time

    @property
    def play_domains(self):
        r"""Gets the play_domains of this ListPlayDomainStreamInfoRequest.

        播放域名列表，最多支持查询10个域名，多个域名以逗号分隔。  如果不传入域名，则查询租户下所有播放域名的流数据。 

        :return: The play_domains of this ListPlayDomainStreamInfoRequest.
        :rtype: list[str]
        """
        return self._play_domains

    @play_domains.setter
    def play_domains(self, play_domains):
        r"""Sets the play_domains of this ListPlayDomainStreamInfoRequest.

        播放域名列表，最多支持查询10个域名，多个域名以逗号分隔。  如果不传入域名，则查询租户下所有播放域名的流数据。 

        :param play_domains: The play_domains of this ListPlayDomainStreamInfoRequest.
        :type play_domains: list[str]
        """
        self._play_domains = play_domains

    @property
    def time(self):
        r"""Gets the time of this ListPlayDomainStreamInfoRequest.

        查询数据的时间点，精确到分钟。  日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ，最大查询周期七天。  时间必须为时间粒度整时刻点，如：2024-02-02T08:01:00Z。 

        :return: The time of this ListPlayDomainStreamInfoRequest.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this ListPlayDomainStreamInfoRequest.

        查询数据的时间点，精确到分钟。  日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ，最大查询周期七天。  时间必须为时间粒度整时刻点，如：2024-02-02T08:01:00Z。 

        :param time: The time of this ListPlayDomainStreamInfoRequest.
        :type time: str
        """
        self._time = time

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
        if not isinstance(other, ListPlayDomainStreamInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
