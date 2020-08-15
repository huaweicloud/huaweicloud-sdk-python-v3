# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CreateRequestThrottlingPolicyV2Response(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bind_num': 'int',
        'is_include_special_throttle': 'int',
        'create_time': 'datetime',
        'remark': 'str',
        'type': 'int',
        'time_interval': 'int',
        'ip_call_limits': 'int',
        'app_call_limits': 'int',
        'name': 'str',
        'time_unit': 'str',
        'api_call_limits': 'int',
        'id': 'str',
        'user_call_limits': 'int',
        'enable_adaptive_control': 'str'
    }

    attribute_map = {
        'bind_num': 'bind_num',
        'is_include_special_throttle': 'is_include_special_throttle',
        'create_time': 'create_time',
        'remark': 'remark',
        'type': 'type',
        'time_interval': 'time_interval',
        'ip_call_limits': 'ip_call_limits',
        'app_call_limits': 'app_call_limits',
        'name': 'name',
        'time_unit': 'time_unit',
        'api_call_limits': 'api_call_limits',
        'id': 'id',
        'user_call_limits': 'user_call_limits',
        'enable_adaptive_control': 'enable_adaptive_control'
    }

    def __init__(self, bind_num=None, is_include_special_throttle=None, create_time=None, remark=None, type=None, time_interval=None, ip_call_limits=None, app_call_limits=None, name=None, time_unit=None, api_call_limits=None, id=None, user_call_limits=None, enable_adaptive_control=None):
        """CreateRequestThrottlingPolicyV2Response - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._bind_num = None
        self._is_include_special_throttle = None
        self._create_time = None
        self._remark = None
        self._type = None
        self._time_interval = None
        self._ip_call_limits = None
        self._app_call_limits = None
        self._name = None
        self._time_unit = None
        self._api_call_limits = None
        self._id = None
        self._user_call_limits = None
        self._enable_adaptive_control = None
        self.discriminator = None

        if bind_num is not None:
            self.bind_num = bind_num
        if is_include_special_throttle is not None:
            self.is_include_special_throttle = is_include_special_throttle
        if create_time is not None:
            self.create_time = create_time
        if remark is not None:
            self.remark = remark
        if type is not None:
            self.type = type
        if time_interval is not None:
            self.time_interval = time_interval
        if ip_call_limits is not None:
            self.ip_call_limits = ip_call_limits
        if app_call_limits is not None:
            self.app_call_limits = app_call_limits
        if name is not None:
            self.name = name
        if time_unit is not None:
            self.time_unit = time_unit
        if api_call_limits is not None:
            self.api_call_limits = api_call_limits
        if id is not None:
            self.id = id
        if user_call_limits is not None:
            self.user_call_limits = user_call_limits
        if enable_adaptive_control is not None:
            self.enable_adaptive_control = enable_adaptive_control

    @property
    def bind_num(self):
        """Gets the bind_num of this CreateRequestThrottlingPolicyV2Response.

        流控绑定的API数量

        :return: The bind_num of this CreateRequestThrottlingPolicyV2Response.
        :rtype: int
        """
        return self._bind_num

    @bind_num.setter
    def bind_num(self, bind_num):
        """Sets the bind_num of this CreateRequestThrottlingPolicyV2Response.

        流控绑定的API数量

        :param bind_num: The bind_num of this CreateRequestThrottlingPolicyV2Response.
        :type: int
        """
        self._bind_num = bind_num

    @property
    def is_include_special_throttle(self):
        """Gets the is_include_special_throttle of this CreateRequestThrottlingPolicyV2Response.

        是否包含特殊流控配置 - 1：包含 - 2：不包含

        :return: The is_include_special_throttle of this CreateRequestThrottlingPolicyV2Response.
        :rtype: int
        """
        return self._is_include_special_throttle

    @is_include_special_throttle.setter
    def is_include_special_throttle(self, is_include_special_throttle):
        """Sets the is_include_special_throttle of this CreateRequestThrottlingPolicyV2Response.

        是否包含特殊流控配置 - 1：包含 - 2：不包含

        :param is_include_special_throttle: The is_include_special_throttle of this CreateRequestThrottlingPolicyV2Response.
        :type: int
        """
        self._is_include_special_throttle = is_include_special_throttle

    @property
    def create_time(self):
        """Gets the create_time of this CreateRequestThrottlingPolicyV2Response.

        创建时间

        :return: The create_time of this CreateRequestThrottlingPolicyV2Response.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CreateRequestThrottlingPolicyV2Response.

        创建时间

        :param create_time: The create_time of this CreateRequestThrottlingPolicyV2Response.
        :type: datetime
        """
        self._create_time = create_time

    @property
    def remark(self):
        """Gets the remark of this CreateRequestThrottlingPolicyV2Response.

        描述

        :return: The remark of this CreateRequestThrottlingPolicyV2Response.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this CreateRequestThrottlingPolicyV2Response.

        描述

        :param remark: The remark of this CreateRequestThrottlingPolicyV2Response.
        :type: str
        """
        self._remark = remark

    @property
    def type(self):
        """Gets the type of this CreateRequestThrottlingPolicyV2Response.

        流控策略的类型 - 1：独享，表示绑定到流控策略的单个API流控时间内能够被调用多少次。 - 2：共享，表示绑定到流控策略的所有API流控时间内能够被调用多少次

        :return: The type of this CreateRequestThrottlingPolicyV2Response.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateRequestThrottlingPolicyV2Response.

        流控策略的类型 - 1：独享，表示绑定到流控策略的单个API流控时间内能够被调用多少次。 - 2：共享，表示绑定到流控策略的所有API流控时间内能够被调用多少次

        :param type: The type of this CreateRequestThrottlingPolicyV2Response.
        :type: int
        """
        self._type = type

    @property
    def time_interval(self):
        """Gets the time_interval of this CreateRequestThrottlingPolicyV2Response.

        流控的时长

        :return: The time_interval of this CreateRequestThrottlingPolicyV2Response.
        :rtype: int
        """
        return self._time_interval

    @time_interval.setter
    def time_interval(self, time_interval):
        """Sets the time_interval of this CreateRequestThrottlingPolicyV2Response.

        流控的时长

        :param time_interval: The time_interval of this CreateRequestThrottlingPolicyV2Response.
        :type: int
        """
        self._time_interval = time_interval

    @property
    def ip_call_limits(self):
        """Gets the ip_call_limits of this CreateRequestThrottlingPolicyV2Response.

        单个IP流控时间内能够访问API的次数限制

        :return: The ip_call_limits of this CreateRequestThrottlingPolicyV2Response.
        :rtype: int
        """
        return self._ip_call_limits

    @ip_call_limits.setter
    def ip_call_limits(self, ip_call_limits):
        """Sets the ip_call_limits of this CreateRequestThrottlingPolicyV2Response.

        单个IP流控时间内能够访问API的次数限制

        :param ip_call_limits: The ip_call_limits of this CreateRequestThrottlingPolicyV2Response.
        :type: int
        """
        self._ip_call_limits = ip_call_limits

    @property
    def app_call_limits(self):
        """Gets the app_call_limits of this CreateRequestThrottlingPolicyV2Response.

        单个APP流控时间内能够访问API的次数限制

        :return: The app_call_limits of this CreateRequestThrottlingPolicyV2Response.
        :rtype: int
        """
        return self._app_call_limits

    @app_call_limits.setter
    def app_call_limits(self, app_call_limits):
        """Sets the app_call_limits of this CreateRequestThrottlingPolicyV2Response.

        单个APP流控时间内能够访问API的次数限制

        :param app_call_limits: The app_call_limits of this CreateRequestThrottlingPolicyV2Response.
        :type: int
        """
        self._app_call_limits = app_call_limits

    @property
    def name(self):
        """Gets the name of this CreateRequestThrottlingPolicyV2Response.

        流控策略的名称

        :return: The name of this CreateRequestThrottlingPolicyV2Response.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateRequestThrottlingPolicyV2Response.

        流控策略的名称

        :param name: The name of this CreateRequestThrottlingPolicyV2Response.
        :type: str
        """
        self._name = name

    @property
    def time_unit(self):
        """Gets the time_unit of this CreateRequestThrottlingPolicyV2Response.

        流控的时间单位

        :return: The time_unit of this CreateRequestThrottlingPolicyV2Response.
        :rtype: str
        """
        return self._time_unit

    @time_unit.setter
    def time_unit(self, time_unit):
        """Sets the time_unit of this CreateRequestThrottlingPolicyV2Response.

        流控的时间单位

        :param time_unit: The time_unit of this CreateRequestThrottlingPolicyV2Response.
        :type: str
        """
        self._time_unit = time_unit

    @property
    def api_call_limits(self):
        """Gets the api_call_limits of this CreateRequestThrottlingPolicyV2Response.

        单个API流控时间内能够被访问的次数限制

        :return: The api_call_limits of this CreateRequestThrottlingPolicyV2Response.
        :rtype: int
        """
        return self._api_call_limits

    @api_call_limits.setter
    def api_call_limits(self, api_call_limits):
        """Sets the api_call_limits of this CreateRequestThrottlingPolicyV2Response.

        单个API流控时间内能够被访问的次数限制

        :param api_call_limits: The api_call_limits of this CreateRequestThrottlingPolicyV2Response.
        :type: int
        """
        self._api_call_limits = api_call_limits

    @property
    def id(self):
        """Gets the id of this CreateRequestThrottlingPolicyV2Response.

        流控策略的ID

        :return: The id of this CreateRequestThrottlingPolicyV2Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateRequestThrottlingPolicyV2Response.

        流控策略的ID

        :param id: The id of this CreateRequestThrottlingPolicyV2Response.
        :type: str
        """
        self._id = id

    @property
    def user_call_limits(self):
        """Gets the user_call_limits of this CreateRequestThrottlingPolicyV2Response.

        单个用户流控时间内能够访问API的次数限制

        :return: The user_call_limits of this CreateRequestThrottlingPolicyV2Response.
        :rtype: int
        """
        return self._user_call_limits

    @user_call_limits.setter
    def user_call_limits(self, user_call_limits):
        """Sets the user_call_limits of this CreateRequestThrottlingPolicyV2Response.

        单个用户流控时间内能够访问API的次数限制

        :param user_call_limits: The user_call_limits of this CreateRequestThrottlingPolicyV2Response.
        :type: int
        """
        self._user_call_limits = user_call_limits

    @property
    def enable_adaptive_control(self):
        """Gets the enable_adaptive_control of this CreateRequestThrottlingPolicyV2Response.

        是否开启动态流控  暂不支持

        :return: The enable_adaptive_control of this CreateRequestThrottlingPolicyV2Response.
        :rtype: str
        """
        return self._enable_adaptive_control

    @enable_adaptive_control.setter
    def enable_adaptive_control(self, enable_adaptive_control):
        """Sets the enable_adaptive_control of this CreateRequestThrottlingPolicyV2Response.

        是否开启动态流控  暂不支持

        :param enable_adaptive_control: The enable_adaptive_control of this CreateRequestThrottlingPolicyV2Response.
        :type: str
        """
        self._enable_adaptive_control = enable_adaptive_control

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateRequestThrottlingPolicyV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
