# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAppQuotaResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_quota_id': 'str',
        'name': 'str',
        'call_limits': 'int',
        'time_unit': 'str',
        'time_interval': 'int',
        'remark': 'str',
        'reset_time': 'str',
        'create_time': 'datetime',
        'bound_app_num': 'int'
    }

    attribute_map = {
        'app_quota_id': 'app_quota_id',
        'name': 'name',
        'call_limits': 'call_limits',
        'time_unit': 'time_unit',
        'time_interval': 'time_interval',
        'remark': 'remark',
        'reset_time': 'reset_time',
        'create_time': 'create_time',
        'bound_app_num': 'bound_app_num'
    }

    def __init__(self, app_quota_id=None, name=None, call_limits=None, time_unit=None, time_interval=None, remark=None, reset_time=None, create_time=None, bound_app_num=None):
        """UpdateAppQuotaResponse

        The model defined in huaweicloud sdk

        :param app_quota_id: 客户端配额编号
        :type app_quota_id: str
        :param name: 配额名称。支持汉字，英文，数字，下划线，且只能以英文和汉字开头，3-255字符
        :type name: str
        :param call_limits: 客户端配额的访问次数限制
        :type call_limits: int
        :param time_unit: 限定时间单位：SECOND:秒、MINUTE:分、HOURE:时、DAY:天
        :type time_unit: str
        :param time_interval: 配额的限定时间值
        :type time_interval: int
        :param remark: 参数说明和描述
        :type remark: str
        :param reset_time: 首次配额重置时间点，不配置默认为首次调用时间计算
        :type reset_time: str
        :param create_time: 创建时间
        :type create_time: datetime
        :param bound_app_num: 配额策略已绑定应用数量
        :type bound_app_num: int
        """
        
        super(UpdateAppQuotaResponse, self).__init__()

        self._app_quota_id = None
        self._name = None
        self._call_limits = None
        self._time_unit = None
        self._time_interval = None
        self._remark = None
        self._reset_time = None
        self._create_time = None
        self._bound_app_num = None
        self.discriminator = None

        if app_quota_id is not None:
            self.app_quota_id = app_quota_id
        if name is not None:
            self.name = name
        if call_limits is not None:
            self.call_limits = call_limits
        if time_unit is not None:
            self.time_unit = time_unit
        if time_interval is not None:
            self.time_interval = time_interval
        if remark is not None:
            self.remark = remark
        if reset_time is not None:
            self.reset_time = reset_time
        if create_time is not None:
            self.create_time = create_time
        if bound_app_num is not None:
            self.bound_app_num = bound_app_num

    @property
    def app_quota_id(self):
        """Gets the app_quota_id of this UpdateAppQuotaResponse.

        客户端配额编号

        :return: The app_quota_id of this UpdateAppQuotaResponse.
        :rtype: str
        """
        return self._app_quota_id

    @app_quota_id.setter
    def app_quota_id(self, app_quota_id):
        """Sets the app_quota_id of this UpdateAppQuotaResponse.

        客户端配额编号

        :param app_quota_id: The app_quota_id of this UpdateAppQuotaResponse.
        :type app_quota_id: str
        """
        self._app_quota_id = app_quota_id

    @property
    def name(self):
        """Gets the name of this UpdateAppQuotaResponse.

        配额名称。支持汉字，英文，数字，下划线，且只能以英文和汉字开头，3-255字符

        :return: The name of this UpdateAppQuotaResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateAppQuotaResponse.

        配额名称。支持汉字，英文，数字，下划线，且只能以英文和汉字开头，3-255字符

        :param name: The name of this UpdateAppQuotaResponse.
        :type name: str
        """
        self._name = name

    @property
    def call_limits(self):
        """Gets the call_limits of this UpdateAppQuotaResponse.

        客户端配额的访问次数限制

        :return: The call_limits of this UpdateAppQuotaResponse.
        :rtype: int
        """
        return self._call_limits

    @call_limits.setter
    def call_limits(self, call_limits):
        """Sets the call_limits of this UpdateAppQuotaResponse.

        客户端配额的访问次数限制

        :param call_limits: The call_limits of this UpdateAppQuotaResponse.
        :type call_limits: int
        """
        self._call_limits = call_limits

    @property
    def time_unit(self):
        """Gets the time_unit of this UpdateAppQuotaResponse.

        限定时间单位：SECOND:秒、MINUTE:分、HOURE:时、DAY:天

        :return: The time_unit of this UpdateAppQuotaResponse.
        :rtype: str
        """
        return self._time_unit

    @time_unit.setter
    def time_unit(self, time_unit):
        """Sets the time_unit of this UpdateAppQuotaResponse.

        限定时间单位：SECOND:秒、MINUTE:分、HOURE:时、DAY:天

        :param time_unit: The time_unit of this UpdateAppQuotaResponse.
        :type time_unit: str
        """
        self._time_unit = time_unit

    @property
    def time_interval(self):
        """Gets the time_interval of this UpdateAppQuotaResponse.

        配额的限定时间值

        :return: The time_interval of this UpdateAppQuotaResponse.
        :rtype: int
        """
        return self._time_interval

    @time_interval.setter
    def time_interval(self, time_interval):
        """Sets the time_interval of this UpdateAppQuotaResponse.

        配额的限定时间值

        :param time_interval: The time_interval of this UpdateAppQuotaResponse.
        :type time_interval: int
        """
        self._time_interval = time_interval

    @property
    def remark(self):
        """Gets the remark of this UpdateAppQuotaResponse.

        参数说明和描述

        :return: The remark of this UpdateAppQuotaResponse.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this UpdateAppQuotaResponse.

        参数说明和描述

        :param remark: The remark of this UpdateAppQuotaResponse.
        :type remark: str
        """
        self._remark = remark

    @property
    def reset_time(self):
        """Gets the reset_time of this UpdateAppQuotaResponse.

        首次配额重置时间点，不配置默认为首次调用时间计算

        :return: The reset_time of this UpdateAppQuotaResponse.
        :rtype: str
        """
        return self._reset_time

    @reset_time.setter
    def reset_time(self, reset_time):
        """Sets the reset_time of this UpdateAppQuotaResponse.

        首次配额重置时间点，不配置默认为首次调用时间计算

        :param reset_time: The reset_time of this UpdateAppQuotaResponse.
        :type reset_time: str
        """
        self._reset_time = reset_time

    @property
    def create_time(self):
        """Gets the create_time of this UpdateAppQuotaResponse.

        创建时间

        :return: The create_time of this UpdateAppQuotaResponse.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this UpdateAppQuotaResponse.

        创建时间

        :param create_time: The create_time of this UpdateAppQuotaResponse.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def bound_app_num(self):
        """Gets the bound_app_num of this UpdateAppQuotaResponse.

        配额策略已绑定应用数量

        :return: The bound_app_num of this UpdateAppQuotaResponse.
        :rtype: int
        """
        return self._bound_app_num

    @bound_app_num.setter
    def bound_app_num(self, bound_app_num):
        """Sets the bound_app_num of this UpdateAppQuotaResponse.

        配额策略已绑定应用数量

        :param bound_app_num: The bound_app_num of this UpdateAppQuotaResponse.
        :type bound_app_num: int
        """
        self._bound_app_num = bound_app_num

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
        if not isinstance(other, UpdateAppQuotaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
