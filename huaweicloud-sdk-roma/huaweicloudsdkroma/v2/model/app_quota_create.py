# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppQuotaCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'call_limits': 'int',
        'time_unit': 'str',
        'time_interval': 'int',
        'reset_time': 'str',
        'remark': 'str'
    }

    attribute_map = {
        'name': 'name',
        'call_limits': 'call_limits',
        'time_unit': 'time_unit',
        'time_interval': 'time_interval',
        'reset_time': 'reset_time',
        'remark': 'remark'
    }

    def __init__(self, name=None, call_limits=None, time_unit=None, time_interval=None, reset_time=None, remark=None):
        """AppQuotaCreate

        The model defined in huaweicloud sdk

        :param name: 配额名称。支持汉字，英文，数字，下划线，且只能以英文和汉字开头
        :type name: str
        :param call_limits: 客户端配额的访问次数限制
        :type call_limits: int
        :param time_unit: 限定时间单位：SECOND:秒、MINUTE:分、HOURE:时、DAY:天
        :type time_unit: str
        :param time_interval: 流控的限定时间值
        :type time_interval: int
        :param reset_time: 首次配额重置时间点，不配置默认为首次调用时间计算
        :type reset_time: str
        :param remark: 参数说明和描述。  不支持&lt;，&gt;字符
        :type remark: str
        """
        
        

        self._name = None
        self._call_limits = None
        self._time_unit = None
        self._time_interval = None
        self._reset_time = None
        self._remark = None
        self.discriminator = None

        self.name = name
        self.call_limits = call_limits
        self.time_unit = time_unit
        self.time_interval = time_interval
        if reset_time is not None:
            self.reset_time = reset_time
        if remark is not None:
            self.remark = remark

    @property
    def name(self):
        """Gets the name of this AppQuotaCreate.

        配额名称。支持汉字，英文，数字，下划线，且只能以英文和汉字开头

        :return: The name of this AppQuotaCreate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AppQuotaCreate.

        配额名称。支持汉字，英文，数字，下划线，且只能以英文和汉字开头

        :param name: The name of this AppQuotaCreate.
        :type name: str
        """
        self._name = name

    @property
    def call_limits(self):
        """Gets the call_limits of this AppQuotaCreate.

        客户端配额的访问次数限制

        :return: The call_limits of this AppQuotaCreate.
        :rtype: int
        """
        return self._call_limits

    @call_limits.setter
    def call_limits(self, call_limits):
        """Sets the call_limits of this AppQuotaCreate.

        客户端配额的访问次数限制

        :param call_limits: The call_limits of this AppQuotaCreate.
        :type call_limits: int
        """
        self._call_limits = call_limits

    @property
    def time_unit(self):
        """Gets the time_unit of this AppQuotaCreate.

        限定时间单位：SECOND:秒、MINUTE:分、HOURE:时、DAY:天

        :return: The time_unit of this AppQuotaCreate.
        :rtype: str
        """
        return self._time_unit

    @time_unit.setter
    def time_unit(self, time_unit):
        """Sets the time_unit of this AppQuotaCreate.

        限定时间单位：SECOND:秒、MINUTE:分、HOURE:时、DAY:天

        :param time_unit: The time_unit of this AppQuotaCreate.
        :type time_unit: str
        """
        self._time_unit = time_unit

    @property
    def time_interval(self):
        """Gets the time_interval of this AppQuotaCreate.

        流控的限定时间值

        :return: The time_interval of this AppQuotaCreate.
        :rtype: int
        """
        return self._time_interval

    @time_interval.setter
    def time_interval(self, time_interval):
        """Sets the time_interval of this AppQuotaCreate.

        流控的限定时间值

        :param time_interval: The time_interval of this AppQuotaCreate.
        :type time_interval: int
        """
        self._time_interval = time_interval

    @property
    def reset_time(self):
        """Gets the reset_time of this AppQuotaCreate.

        首次配额重置时间点，不配置默认为首次调用时间计算

        :return: The reset_time of this AppQuotaCreate.
        :rtype: str
        """
        return self._reset_time

    @reset_time.setter
    def reset_time(self, reset_time):
        """Sets the reset_time of this AppQuotaCreate.

        首次配额重置时间点，不配置默认为首次调用时间计算

        :param reset_time: The reset_time of this AppQuotaCreate.
        :type reset_time: str
        """
        self._reset_time = reset_time

    @property
    def remark(self):
        """Gets the remark of this AppQuotaCreate.

        参数说明和描述。  不支持<，>字符

        :return: The remark of this AppQuotaCreate.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this AppQuotaCreate.

        参数说明和描述。  不支持<，>字符

        :param remark: The remark of this AppQuotaCreate.
        :type remark: str
        """
        self._remark = remark

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
        if not isinstance(other, AppQuotaCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
