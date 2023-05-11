# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHostRaspProtectHistoryInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'enterprise_project_id': 'str',
        'host_id': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'limit': 'int',
        'offset': 'int',
        'alarm_level': 'int',
        'severity': 'str',
        'protect_status': 'str'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'host_id': 'host_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset',
        'alarm_level': 'alarm_level',
        'severity': 'severity',
        'protect_status': 'protect_status'
    }

    def __init__(self, region=None, enterprise_project_id=None, host_id=None, start_time=None, end_time=None, limit=None, offset=None, alarm_level=None, severity=None, protect_status=None):
        """ListHostRaspProtectHistoryInfoRequest

        The model defined in huaweicloud sdk

        :param region: Region Id
        :type region: str
        :param enterprise_project_id: 企业项目
        :type enterprise_project_id: str
        :param host_id: Host Id
        :type host_id: str
        :param start_time: 起始时间
        :type start_time: int
        :param end_time: 终止时间
        :type end_time: int
        :param limit: limit
        :type limit: int
        :param offset: offset
        :type offset: int
        :param alarm_level: 告警级别
        :type alarm_level: int
        :param severity: 威胁等级   - Security : 安全   - Low : 低危   - Medium : 中危   - High : 高危   - Critical : 危急
        :type severity: str
        :param protect_status: 防护状态   - closed : 未开启   - opened : 防护中
        :type protect_status: str
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._host_id = None
        self._start_time = None
        self._end_time = None
        self._limit = None
        self._offset = None
        self._alarm_level = None
        self._severity = None
        self._protect_status = None
        self.discriminator = None

        self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.host_id = host_id
        self.start_time = start_time
        self.end_time = end_time
        self.limit = limit
        self.offset = offset
        if alarm_level is not None:
            self.alarm_level = alarm_level
        if severity is not None:
            self.severity = severity
        if protect_status is not None:
            self.protect_status = protect_status

    @property
    def region(self):
        """Gets the region of this ListHostRaspProtectHistoryInfoRequest.

        Region Id

        :return: The region of this ListHostRaspProtectHistoryInfoRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListHostRaspProtectHistoryInfoRequest.

        Region Id

        :param region: The region of this ListHostRaspProtectHistoryInfoRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListHostRaspProtectHistoryInfoRequest.

        企业项目

        :return: The enterprise_project_id of this ListHostRaspProtectHistoryInfoRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListHostRaspProtectHistoryInfoRequest.

        企业项目

        :param enterprise_project_id: The enterprise_project_id of this ListHostRaspProtectHistoryInfoRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def host_id(self):
        """Gets the host_id of this ListHostRaspProtectHistoryInfoRequest.

        Host Id

        :return: The host_id of this ListHostRaspProtectHistoryInfoRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ListHostRaspProtectHistoryInfoRequest.

        Host Id

        :param host_id: The host_id of this ListHostRaspProtectHistoryInfoRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def start_time(self):
        """Gets the start_time of this ListHostRaspProtectHistoryInfoRequest.

        起始时间

        :return: The start_time of this ListHostRaspProtectHistoryInfoRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListHostRaspProtectHistoryInfoRequest.

        起始时间

        :param start_time: The start_time of this ListHostRaspProtectHistoryInfoRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListHostRaspProtectHistoryInfoRequest.

        终止时间

        :return: The end_time of this ListHostRaspProtectHistoryInfoRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListHostRaspProtectHistoryInfoRequest.

        终止时间

        :param end_time: The end_time of this ListHostRaspProtectHistoryInfoRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def limit(self):
        """Gets the limit of this ListHostRaspProtectHistoryInfoRequest.

        limit

        :return: The limit of this ListHostRaspProtectHistoryInfoRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListHostRaspProtectHistoryInfoRequest.

        limit

        :param limit: The limit of this ListHostRaspProtectHistoryInfoRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListHostRaspProtectHistoryInfoRequest.

        offset

        :return: The offset of this ListHostRaspProtectHistoryInfoRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListHostRaspProtectHistoryInfoRequest.

        offset

        :param offset: The offset of this ListHostRaspProtectHistoryInfoRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def alarm_level(self):
        """Gets the alarm_level of this ListHostRaspProtectHistoryInfoRequest.

        告警级别

        :return: The alarm_level of this ListHostRaspProtectHistoryInfoRequest.
        :rtype: int
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        """Sets the alarm_level of this ListHostRaspProtectHistoryInfoRequest.

        告警级别

        :param alarm_level: The alarm_level of this ListHostRaspProtectHistoryInfoRequest.
        :type alarm_level: int
        """
        self._alarm_level = alarm_level

    @property
    def severity(self):
        """Gets the severity of this ListHostRaspProtectHistoryInfoRequest.

        威胁等级   - Security : 安全   - Low : 低危   - Medium : 中危   - High : 高危   - Critical : 危急

        :return: The severity of this ListHostRaspProtectHistoryInfoRequest.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this ListHostRaspProtectHistoryInfoRequest.

        威胁等级   - Security : 安全   - Low : 低危   - Medium : 中危   - High : 高危   - Critical : 危急

        :param severity: The severity of this ListHostRaspProtectHistoryInfoRequest.
        :type severity: str
        """
        self._severity = severity

    @property
    def protect_status(self):
        """Gets the protect_status of this ListHostRaspProtectHistoryInfoRequest.

        防护状态   - closed : 未开启   - opened : 防护中

        :return: The protect_status of this ListHostRaspProtectHistoryInfoRequest.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        """Sets the protect_status of this ListHostRaspProtectHistoryInfoRequest.

        防护状态   - closed : 未开启   - opened : 防护中

        :param protect_status: The protect_status of this ListHostRaspProtectHistoryInfoRequest.
        :type protect_status: str
        """
        self._protect_status = protect_status

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
        if not isinstance(other, ListHostRaspProtectHistoryInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
