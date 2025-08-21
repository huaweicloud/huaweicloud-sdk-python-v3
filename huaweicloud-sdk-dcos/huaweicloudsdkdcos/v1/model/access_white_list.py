# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessWhiteList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'end_time': 'str',
        'reason': 'str',
        'reason_supplement': 'str',
        'scope': 'str',
        'room_code': 'str',
        'whitelist': 'list[ContactInformation]'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'reason': 'reason',
        'reason_supplement': 'reason_supplement',
        'scope': 'scope',
        'room_code': 'room_code',
        'whitelist': 'whitelist'
    }

    def __init__(self, start_time=None, end_time=None, reason=None, reason_supplement=None, scope=None, room_code=None, whitelist=None):
        r"""AccessWhiteList

        The model defined in huaweicloud sdk

        :param start_time: 开始时间
        :type start_time: str
        :param end_time: 结束时间
        :type end_time: str
        :param reason: 原因
        :type reason: str
        :param reason_supplement: 原因补充
        :type reason_supplement: str
        :param scope: 作业范围
        :type scope: str
        :param room_code: 机房编码
        :type room_code: str
        :param whitelist: 人员名单
        :type whitelist: list[:class:`huaweicloudsdkdcos.v1.ContactInformation`]
        """
        
        

        self._start_time = None
        self._end_time = None
        self._reason = None
        self._reason_supplement = None
        self._scope = None
        self._room_code = None
        self._whitelist = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if reason is not None:
            self.reason = reason
        if reason_supplement is not None:
            self.reason_supplement = reason_supplement
        if scope is not None:
            self.scope = scope
        if room_code is not None:
            self.room_code = room_code
        if whitelist is not None:
            self.whitelist = whitelist

    @property
    def start_time(self):
        r"""Gets the start_time of this AccessWhiteList.

        开始时间

        :return: The start_time of this AccessWhiteList.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this AccessWhiteList.

        开始时间

        :param start_time: The start_time of this AccessWhiteList.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this AccessWhiteList.

        结束时间

        :return: The end_time of this AccessWhiteList.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this AccessWhiteList.

        结束时间

        :param end_time: The end_time of this AccessWhiteList.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def reason(self):
        r"""Gets the reason of this AccessWhiteList.

        原因

        :return: The reason of this AccessWhiteList.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this AccessWhiteList.

        原因

        :param reason: The reason of this AccessWhiteList.
        :type reason: str
        """
        self._reason = reason

    @property
    def reason_supplement(self):
        r"""Gets the reason_supplement of this AccessWhiteList.

        原因补充

        :return: The reason_supplement of this AccessWhiteList.
        :rtype: str
        """
        return self._reason_supplement

    @reason_supplement.setter
    def reason_supplement(self, reason_supplement):
        r"""Sets the reason_supplement of this AccessWhiteList.

        原因补充

        :param reason_supplement: The reason_supplement of this AccessWhiteList.
        :type reason_supplement: str
        """
        self._reason_supplement = reason_supplement

    @property
    def scope(self):
        r"""Gets the scope of this AccessWhiteList.

        作业范围

        :return: The scope of this AccessWhiteList.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this AccessWhiteList.

        作业范围

        :param scope: The scope of this AccessWhiteList.
        :type scope: str
        """
        self._scope = scope

    @property
    def room_code(self):
        r"""Gets the room_code of this AccessWhiteList.

        机房编码

        :return: The room_code of this AccessWhiteList.
        :rtype: str
        """
        return self._room_code

    @room_code.setter
    def room_code(self, room_code):
        r"""Sets the room_code of this AccessWhiteList.

        机房编码

        :param room_code: The room_code of this AccessWhiteList.
        :type room_code: str
        """
        self._room_code = room_code

    @property
    def whitelist(self):
        r"""Gets the whitelist of this AccessWhiteList.

        人员名单

        :return: The whitelist of this AccessWhiteList.
        :rtype: list[:class:`huaweicloudsdkdcos.v1.ContactInformation`]
        """
        return self._whitelist

    @whitelist.setter
    def whitelist(self, whitelist):
        r"""Sets the whitelist of this AccessWhiteList.

        人员名单

        :param whitelist: The whitelist of this AccessWhiteList.
        :type whitelist: list[:class:`huaweicloudsdkdcos.v1.ContactInformation`]
        """
        self._whitelist = whitelist

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
        if not isinstance(other, AccessWhiteList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
