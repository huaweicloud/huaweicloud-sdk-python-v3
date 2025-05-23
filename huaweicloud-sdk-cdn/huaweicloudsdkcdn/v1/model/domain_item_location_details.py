# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DomainItemLocationDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'int',
        'end_time': 'int',
        'stat_type': 'str',
        'domains': 'list[DomainRegion]'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'stat_type': 'stat_type',
        'domains': 'domains'
    }

    def __init__(self, start_time=None, end_time=None, stat_type=None, domains=None):
        r"""DomainItemLocationDetails

        The model defined in huaweicloud sdk

        :param start_time: 数据起始时间戳，可能与请求时间不一致
        :type start_time: int
        :param end_time: 数据结束时间戳，可能与请求时间不一致
        :type end_time: int
        :param stat_type: 指标类型
        :type stat_type: str
        :param domains: 域名详情数据列表
        :type domains: list[:class:`huaweicloudsdkcdn.v1.DomainRegion`]
        """
        
        

        self._start_time = None
        self._end_time = None
        self._stat_type = None
        self._domains = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if stat_type is not None:
            self.stat_type = stat_type
        if domains is not None:
            self.domains = domains

    @property
    def start_time(self):
        r"""Gets the start_time of this DomainItemLocationDetails.

        数据起始时间戳，可能与请求时间不一致

        :return: The start_time of this DomainItemLocationDetails.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this DomainItemLocationDetails.

        数据起始时间戳，可能与请求时间不一致

        :param start_time: The start_time of this DomainItemLocationDetails.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this DomainItemLocationDetails.

        数据结束时间戳，可能与请求时间不一致

        :return: The end_time of this DomainItemLocationDetails.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this DomainItemLocationDetails.

        数据结束时间戳，可能与请求时间不一致

        :param end_time: The end_time of this DomainItemLocationDetails.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def stat_type(self):
        r"""Gets the stat_type of this DomainItemLocationDetails.

        指标类型

        :return: The stat_type of this DomainItemLocationDetails.
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        r"""Sets the stat_type of this DomainItemLocationDetails.

        指标类型

        :param stat_type: The stat_type of this DomainItemLocationDetails.
        :type stat_type: str
        """
        self._stat_type = stat_type

    @property
    def domains(self):
        r"""Gets the domains of this DomainItemLocationDetails.

        域名详情数据列表

        :return: The domains of this DomainItemLocationDetails.
        :rtype: list[:class:`huaweicloudsdkcdn.v1.DomainRegion`]
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        r"""Sets the domains of this DomainItemLocationDetails.

        域名详情数据列表

        :param domains: The domains of this DomainItemLocationDetails.
        :type domains: list[:class:`huaweicloudsdkcdn.v1.DomainRegion`]
        """
        self._domains = domains

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
        if not isinstance(other, DomainItemLocationDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
