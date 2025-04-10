# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmLogRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time': 'AlarmLogRequestTime',
        'risk': 'str',
        'type': 'str',
        'status': 'str',
        'page': 'int',
        'size': 'int'
    }

    attribute_map = {
        'time': 'time',
        'risk': 'risk',
        'type': 'type',
        'status': 'status',
        'page': 'page',
        'size': 'size'
    }

    def __init__(self, time=None, risk=None, type=None, status=None, page=None, size=None):
        r"""AlarmLogRequest

        The model defined in huaweicloud sdk

        :param time: 
        :type time: :class:`huaweicloudsdkdbss.v1.AlarmLogRequestTime`
        :param risk: 风险级别 - LOW - MEDIUM - HIGH
        :type risk: str
        :param type: 告警类型 - RISK_RULE: 风险规则 - RISK_CPU: CPU超限 - RISK_MEMORY: 内存超限 - RISK_DISK: 磁盘超限 - RISK_DISK_CAPACITY: 磁盘容量不足六个月 - RISK_BACKUP: 备份失败 - AUDIT_QPS_OVERFLOW: 流量超限入库延迟告警 - RISK_AGENT: Agent异常 - AUDIT_BACKUP_FAILED: 实例备份失败(运维侧)
        :type type: str
        :param status: 告警确认状态 - DONE: 已确认 - UNDO: 未确认
        :type status: str
        :param page: 页码
        :type page: int
        :param size: 每页条数
        :type size: int
        """
        
        

        self._time = None
        self._risk = None
        self._type = None
        self._status = None
        self._page = None
        self._size = None
        self.discriminator = None

        self.time = time
        if risk is not None:
            self.risk = risk
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if page is not None:
            self.page = page
        if size is not None:
            self.size = size

    @property
    def time(self):
        r"""Gets the time of this AlarmLogRequest.

        :return: The time of this AlarmLogRequest.
        :rtype: :class:`huaweicloudsdkdbss.v1.AlarmLogRequestTime`
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this AlarmLogRequest.

        :param time: The time of this AlarmLogRequest.
        :type time: :class:`huaweicloudsdkdbss.v1.AlarmLogRequestTime`
        """
        self._time = time

    @property
    def risk(self):
        r"""Gets the risk of this AlarmLogRequest.

        风险级别 - LOW - MEDIUM - HIGH

        :return: The risk of this AlarmLogRequest.
        :rtype: str
        """
        return self._risk

    @risk.setter
    def risk(self, risk):
        r"""Sets the risk of this AlarmLogRequest.

        风险级别 - LOW - MEDIUM - HIGH

        :param risk: The risk of this AlarmLogRequest.
        :type risk: str
        """
        self._risk = risk

    @property
    def type(self):
        r"""Gets the type of this AlarmLogRequest.

        告警类型 - RISK_RULE: 风险规则 - RISK_CPU: CPU超限 - RISK_MEMORY: 内存超限 - RISK_DISK: 磁盘超限 - RISK_DISK_CAPACITY: 磁盘容量不足六个月 - RISK_BACKUP: 备份失败 - AUDIT_QPS_OVERFLOW: 流量超限入库延迟告警 - RISK_AGENT: Agent异常 - AUDIT_BACKUP_FAILED: 实例备份失败(运维侧)

        :return: The type of this AlarmLogRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AlarmLogRequest.

        告警类型 - RISK_RULE: 风险规则 - RISK_CPU: CPU超限 - RISK_MEMORY: 内存超限 - RISK_DISK: 磁盘超限 - RISK_DISK_CAPACITY: 磁盘容量不足六个月 - RISK_BACKUP: 备份失败 - AUDIT_QPS_OVERFLOW: 流量超限入库延迟告警 - RISK_AGENT: Agent异常 - AUDIT_BACKUP_FAILED: 实例备份失败(运维侧)

        :param type: The type of this AlarmLogRequest.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this AlarmLogRequest.

        告警确认状态 - DONE: 已确认 - UNDO: 未确认

        :return: The status of this AlarmLogRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AlarmLogRequest.

        告警确认状态 - DONE: 已确认 - UNDO: 未确认

        :param status: The status of this AlarmLogRequest.
        :type status: str
        """
        self._status = status

    @property
    def page(self):
        r"""Gets the page of this AlarmLogRequest.

        页码

        :return: The page of this AlarmLogRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this AlarmLogRequest.

        页码

        :param page: The page of this AlarmLogRequest.
        :type page: int
        """
        self._page = page

    @property
    def size(self):
        r"""Gets the size of this AlarmLogRequest.

        每页条数

        :return: The size of this AlarmLogRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this AlarmLogRequest.

        每页条数

        :param size: The size of this AlarmLogRequest.
        :type size: int
        """
        self._size = size

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
        if not isinstance(other, AlarmLogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
