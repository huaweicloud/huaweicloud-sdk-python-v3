# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWafAttackEventRequest:

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
        'start_time': 'str',
        'end_time': 'str',
        'recent': 'str',
        'overseas_type': 'int',
        'sip': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'domains': 'domains',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'recent': 'recent',
        'overseas_type': 'overseas_type',
        'sip': 'sip',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, domains=None, start_time=None, end_time=None, recent=None, overseas_type=None, sip=None, limit=None, offset=None):
        r"""ListWafAttackEventRequest

        The model defined in huaweicloud sdk

        :param domains: 不传时代表全部域名
        :type domains: str
        :param start_time: 开始时间（毫秒时间戳）
        :type start_time: str
        :param end_time: 结束时间（毫秒时间戳）
        :type end_time: str
        :param recent: 枚举值：yesterday,today,3days,1week,1month 与开始结束时间不同时为空
        :type recent: str
        :param overseas_type: 实例类型，0-大陆，1-海外
        :type overseas_type: int
        :param sip: 攻击源IP
        :type sip: str
        :param limit: limit
        :type limit: int
        :param offset: offset
        :type offset: int
        """
        
        

        self._domains = None
        self._start_time = None
        self._end_time = None
        self._recent = None
        self._overseas_type = None
        self._sip = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if domains is not None:
            self.domains = domains
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if recent is not None:
            self.recent = recent
        if overseas_type is not None:
            self.overseas_type = overseas_type
        if sip is not None:
            self.sip = sip
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def domains(self):
        r"""Gets the domains of this ListWafAttackEventRequest.

        不传时代表全部域名

        :return: The domains of this ListWafAttackEventRequest.
        :rtype: str
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        r"""Sets the domains of this ListWafAttackEventRequest.

        不传时代表全部域名

        :param domains: The domains of this ListWafAttackEventRequest.
        :type domains: str
        """
        self._domains = domains

    @property
    def start_time(self):
        r"""Gets the start_time of this ListWafAttackEventRequest.

        开始时间（毫秒时间戳）

        :return: The start_time of this ListWafAttackEventRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListWafAttackEventRequest.

        开始时间（毫秒时间戳）

        :param start_time: The start_time of this ListWafAttackEventRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListWafAttackEventRequest.

        结束时间（毫秒时间戳）

        :return: The end_time of this ListWafAttackEventRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListWafAttackEventRequest.

        结束时间（毫秒时间戳）

        :param end_time: The end_time of this ListWafAttackEventRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def recent(self):
        r"""Gets the recent of this ListWafAttackEventRequest.

        枚举值：yesterday,today,3days,1week,1month 与开始结束时间不同时为空

        :return: The recent of this ListWafAttackEventRequest.
        :rtype: str
        """
        return self._recent

    @recent.setter
    def recent(self, recent):
        r"""Sets the recent of this ListWafAttackEventRequest.

        枚举值：yesterday,today,3days,1week,1month 与开始结束时间不同时为空

        :param recent: The recent of this ListWafAttackEventRequest.
        :type recent: str
        """
        self._recent = recent

    @property
    def overseas_type(self):
        r"""Gets the overseas_type of this ListWafAttackEventRequest.

        实例类型，0-大陆，1-海外

        :return: The overseas_type of this ListWafAttackEventRequest.
        :rtype: int
        """
        return self._overseas_type

    @overseas_type.setter
    def overseas_type(self, overseas_type):
        r"""Sets the overseas_type of this ListWafAttackEventRequest.

        实例类型，0-大陆，1-海外

        :param overseas_type: The overseas_type of this ListWafAttackEventRequest.
        :type overseas_type: int
        """
        self._overseas_type = overseas_type

    @property
    def sip(self):
        r"""Gets the sip of this ListWafAttackEventRequest.

        攻击源IP

        :return: The sip of this ListWafAttackEventRequest.
        :rtype: str
        """
        return self._sip

    @sip.setter
    def sip(self, sip):
        r"""Sets the sip of this ListWafAttackEventRequest.

        攻击源IP

        :param sip: The sip of this ListWafAttackEventRequest.
        :type sip: str
        """
        self._sip = sip

    @property
    def limit(self):
        r"""Gets the limit of this ListWafAttackEventRequest.

        limit

        :return: The limit of this ListWafAttackEventRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListWafAttackEventRequest.

        limit

        :param limit: The limit of this ListWafAttackEventRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListWafAttackEventRequest.

        offset

        :return: The offset of this ListWafAttackEventRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListWafAttackEventRequest.

        offset

        :param offset: The offset of this ListWafAttackEventRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListWafAttackEventRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
