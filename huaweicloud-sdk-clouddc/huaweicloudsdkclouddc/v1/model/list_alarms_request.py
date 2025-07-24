# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_record_id': 'str',
        'alarm_status': 'str',
        'alarm_type': 'str',
        'resource_id': 'str',
        'alarm_level': 'int',
        '_from': 'str',
        'to': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'alarm_record_id': 'alarm_record_id',
        'alarm_status': 'alarm_status',
        'alarm_type': 'alarm_type',
        'resource_id': 'resource_id',
        'alarm_level': 'alarm_level',
        '_from': 'from',
        'to': 'to',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, alarm_record_id=None, alarm_status=None, alarm_type=None, resource_id=None, alarm_level=None, _from=None, to=None, offset=None, limit=None):
        r"""ListAlarmsRequest

        The model defined in huaweicloud sdk

        :param alarm_record_id: 告警记录ID,以ah开头，后跟22位由字母或数字组成的字符串
        :type alarm_record_id: str
        :param alarm_status: 告警状态，ok为正常，alarm为告警，invalid为已失效
        :type alarm_status: str
        :param alarm_type: 告警类型
        :type alarm_type: str
        :param resource_id: 告警资源ID,多值可以以逗号分割,
        :type resource_id: str
        :param alarm_level: 告警级别，1为紧急，2为重要，3为次要，4为提示
        :type alarm_level: int
        :param _from: 产生告警开始时间
        :type _from: str
        :param to: 产生告警结束时间
        :type to: str
        :param offset: 分页游标
        :type offset: int
        :param limit: 分页大小
        :type limit: int
        """
        
        

        self._alarm_record_id = None
        self._alarm_status = None
        self._alarm_type = None
        self._resource_id = None
        self._alarm_level = None
        self.__from = None
        self._to = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if alarm_record_id is not None:
            self.alarm_record_id = alarm_record_id
        if alarm_status is not None:
            self.alarm_status = alarm_status
        if alarm_type is not None:
            self.alarm_type = alarm_type
        if resource_id is not None:
            self.resource_id = resource_id
        if alarm_level is not None:
            self.alarm_level = alarm_level
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def alarm_record_id(self):
        r"""Gets the alarm_record_id of this ListAlarmsRequest.

        告警记录ID,以ah开头，后跟22位由字母或数字组成的字符串

        :return: The alarm_record_id of this ListAlarmsRequest.
        :rtype: str
        """
        return self._alarm_record_id

    @alarm_record_id.setter
    def alarm_record_id(self, alarm_record_id):
        r"""Sets the alarm_record_id of this ListAlarmsRequest.

        告警记录ID,以ah开头，后跟22位由字母或数字组成的字符串

        :param alarm_record_id: The alarm_record_id of this ListAlarmsRequest.
        :type alarm_record_id: str
        """
        self._alarm_record_id = alarm_record_id

    @property
    def alarm_status(self):
        r"""Gets the alarm_status of this ListAlarmsRequest.

        告警状态，ok为正常，alarm为告警，invalid为已失效

        :return: The alarm_status of this ListAlarmsRequest.
        :rtype: str
        """
        return self._alarm_status

    @alarm_status.setter
    def alarm_status(self, alarm_status):
        r"""Sets the alarm_status of this ListAlarmsRequest.

        告警状态，ok为正常，alarm为告警，invalid为已失效

        :param alarm_status: The alarm_status of this ListAlarmsRequest.
        :type alarm_status: str
        """
        self._alarm_status = alarm_status

    @property
    def alarm_type(self):
        r"""Gets the alarm_type of this ListAlarmsRequest.

        告警类型

        :return: The alarm_type of this ListAlarmsRequest.
        :rtype: str
        """
        return self._alarm_type

    @alarm_type.setter
    def alarm_type(self, alarm_type):
        r"""Sets the alarm_type of this ListAlarmsRequest.

        告警类型

        :param alarm_type: The alarm_type of this ListAlarmsRequest.
        :type alarm_type: str
        """
        self._alarm_type = alarm_type

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ListAlarmsRequest.

        告警资源ID,多值可以以逗号分割,

        :return: The resource_id of this ListAlarmsRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ListAlarmsRequest.

        告警资源ID,多值可以以逗号分割,

        :param resource_id: The resource_id of this ListAlarmsRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def alarm_level(self):
        r"""Gets the alarm_level of this ListAlarmsRequest.

        告警级别，1为紧急，2为重要，3为次要，4为提示

        :return: The alarm_level of this ListAlarmsRequest.
        :rtype: int
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        r"""Sets the alarm_level of this ListAlarmsRequest.

        告警级别，1为紧急，2为重要，3为次要，4为提示

        :param alarm_level: The alarm_level of this ListAlarmsRequest.
        :type alarm_level: int
        """
        self._alarm_level = alarm_level

    @property
    def _from(self):
        r"""Gets the _from of this ListAlarmsRequest.

        产生告警开始时间

        :return: The _from of this ListAlarmsRequest.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ListAlarmsRequest.

        产生告警开始时间

        :param _from: The _from of this ListAlarmsRequest.
        :type _from: str
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this ListAlarmsRequest.

        产生告警结束时间

        :return: The to of this ListAlarmsRequest.
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this ListAlarmsRequest.

        产生告警结束时间

        :param to: The to of this ListAlarmsRequest.
        :type to: str
        """
        self._to = to

    @property
    def offset(self):
        r"""Gets the offset of this ListAlarmsRequest.

        分页游标

        :return: The offset of this ListAlarmsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAlarmsRequest.

        分页游标

        :param offset: The offset of this ListAlarmsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAlarmsRequest.

        分页大小

        :return: The limit of this ListAlarmsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAlarmsRequest.

        分页大小

        :param limit: The limit of this ListAlarmsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListAlarmsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
