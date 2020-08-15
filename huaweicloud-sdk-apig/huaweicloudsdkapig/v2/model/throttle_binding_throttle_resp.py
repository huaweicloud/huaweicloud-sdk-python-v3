# coding: utf-8

import pprint
import re

import six





class ThrottleBindingThrottleResp:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'api_call_limits': 'int',
        'user_call_limits': 'int',
        'app_call_limits': 'int',
        'ip_call_limits': 'int',
        'time_interval': 'int',
        'time_unit': 'str',
        'remark': 'str',
        'create_time': 'datetime',
        'is_include_special_throttle': 'int',
        'env_name': 'str',
        'type': 'int',
        'bind_id': 'str',
        'bind_time': 'datetime',
        'bind_num': 'int',
        'enable_adaptive_control': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'api_call_limits': 'api_call_limits',
        'user_call_limits': 'user_call_limits',
        'app_call_limits': 'app_call_limits',
        'ip_call_limits': 'ip_call_limits',
        'time_interval': 'time_interval',
        'time_unit': 'time_unit',
        'remark': 'remark',
        'create_time': 'create_time',
        'is_include_special_throttle': 'is_include_special_throttle',
        'env_name': 'env_name',
        'type': 'type',
        'bind_id': 'bind_id',
        'bind_time': 'bind_time',
        'bind_num': 'bind_num',
        'enable_adaptive_control': 'enable_adaptive_control'
    }

    def __init__(self, id=None, name=None, api_call_limits=None, user_call_limits=None, app_call_limits=None, ip_call_limits=None, time_interval=None, time_unit=None, remark=None, create_time=None, is_include_special_throttle=None, env_name=None, type=None, bind_id=None, bind_time=None, bind_num=None, enable_adaptive_control=None):
        """ThrottleBindingThrottleResp - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._api_call_limits = None
        self._user_call_limits = None
        self._app_call_limits = None
        self._ip_call_limits = None
        self._time_interval = None
        self._time_unit = None
        self._remark = None
        self._create_time = None
        self._is_include_special_throttle = None
        self._env_name = None
        self._type = None
        self._bind_id = None
        self._bind_time = None
        self._bind_num = None
        self._enable_adaptive_control = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if api_call_limits is not None:
            self.api_call_limits = api_call_limits
        if user_call_limits is not None:
            self.user_call_limits = user_call_limits
        if app_call_limits is not None:
            self.app_call_limits = app_call_limits
        if ip_call_limits is not None:
            self.ip_call_limits = ip_call_limits
        if time_interval is not None:
            self.time_interval = time_interval
        if time_unit is not None:
            self.time_unit = time_unit
        if remark is not None:
            self.remark = remark
        if create_time is not None:
            self.create_time = create_time
        if is_include_special_throttle is not None:
            self.is_include_special_throttle = is_include_special_throttle
        if env_name is not None:
            self.env_name = env_name
        if type is not None:
            self.type = type
        if bind_id is not None:
            self.bind_id = bind_id
        if bind_time is not None:
            self.bind_time = bind_time
        if bind_num is not None:
            self.bind_num = bind_num
        if enable_adaptive_control is not None:
            self.enable_adaptive_control = enable_adaptive_control

    @property
    def id(self):
        """Gets the id of this ThrottleBindingThrottleResp.

        流控策略的ID

        :return: The id of this ThrottleBindingThrottleResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ThrottleBindingThrottleResp.

        流控策略的ID

        :param id: The id of this ThrottleBindingThrottleResp.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ThrottleBindingThrottleResp.

        流控策略的名称

        :return: The name of this ThrottleBindingThrottleResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ThrottleBindingThrottleResp.

        流控策略的名称

        :param name: The name of this ThrottleBindingThrottleResp.
        :type: str
        """
        self._name = name

    @property
    def api_call_limits(self):
        """Gets the api_call_limits of this ThrottleBindingThrottleResp.

        单个API流控时间内能够被访问的次数限制

        :return: The api_call_limits of this ThrottleBindingThrottleResp.
        :rtype: int
        """
        return self._api_call_limits

    @api_call_limits.setter
    def api_call_limits(self, api_call_limits):
        """Sets the api_call_limits of this ThrottleBindingThrottleResp.

        单个API流控时间内能够被访问的次数限制

        :param api_call_limits: The api_call_limits of this ThrottleBindingThrottleResp.
        :type: int
        """
        self._api_call_limits = api_call_limits

    @property
    def user_call_limits(self):
        """Gets the user_call_limits of this ThrottleBindingThrottleResp.

        单个用户流控时间内能够访问API的次数限制

        :return: The user_call_limits of this ThrottleBindingThrottleResp.
        :rtype: int
        """
        return self._user_call_limits

    @user_call_limits.setter
    def user_call_limits(self, user_call_limits):
        """Sets the user_call_limits of this ThrottleBindingThrottleResp.

        单个用户流控时间内能够访问API的次数限制

        :param user_call_limits: The user_call_limits of this ThrottleBindingThrottleResp.
        :type: int
        """
        self._user_call_limits = user_call_limits

    @property
    def app_call_limits(self):
        """Gets the app_call_limits of this ThrottleBindingThrottleResp.

        单个APP流控时间内能够访问API的次数限制

        :return: The app_call_limits of this ThrottleBindingThrottleResp.
        :rtype: int
        """
        return self._app_call_limits

    @app_call_limits.setter
    def app_call_limits(self, app_call_limits):
        """Sets the app_call_limits of this ThrottleBindingThrottleResp.

        单个APP流控时间内能够访问API的次数限制

        :param app_call_limits: The app_call_limits of this ThrottleBindingThrottleResp.
        :type: int
        """
        self._app_call_limits = app_call_limits

    @property
    def ip_call_limits(self):
        """Gets the ip_call_limits of this ThrottleBindingThrottleResp.

        单个源IP流控时间内能够访问API的次数限制

        :return: The ip_call_limits of this ThrottleBindingThrottleResp.
        :rtype: int
        """
        return self._ip_call_limits

    @ip_call_limits.setter
    def ip_call_limits(self, ip_call_limits):
        """Sets the ip_call_limits of this ThrottleBindingThrottleResp.

        单个源IP流控时间内能够访问API的次数限制

        :param ip_call_limits: The ip_call_limits of this ThrottleBindingThrottleResp.
        :type: int
        """
        self._ip_call_limits = ip_call_limits

    @property
    def time_interval(self):
        """Gets the time_interval of this ThrottleBindingThrottleResp.

        流控的时长

        :return: The time_interval of this ThrottleBindingThrottleResp.
        :rtype: int
        """
        return self._time_interval

    @time_interval.setter
    def time_interval(self, time_interval):
        """Sets the time_interval of this ThrottleBindingThrottleResp.

        流控的时长

        :param time_interval: The time_interval of this ThrottleBindingThrottleResp.
        :type: int
        """
        self._time_interval = time_interval

    @property
    def time_unit(self):
        """Gets the time_unit of this ThrottleBindingThrottleResp.

        流控的时间单位

        :return: The time_unit of this ThrottleBindingThrottleResp.
        :rtype: str
        """
        return self._time_unit

    @time_unit.setter
    def time_unit(self, time_unit):
        """Sets the time_unit of this ThrottleBindingThrottleResp.

        流控的时间单位

        :param time_unit: The time_unit of this ThrottleBindingThrottleResp.
        :type: str
        """
        self._time_unit = time_unit

    @property
    def remark(self):
        """Gets the remark of this ThrottleBindingThrottleResp.

        描述

        :return: The remark of this ThrottleBindingThrottleResp.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this ThrottleBindingThrottleResp.

        描述

        :param remark: The remark of this ThrottleBindingThrottleResp.
        :type: str
        """
        self._remark = remark

    @property
    def create_time(self):
        """Gets the create_time of this ThrottleBindingThrottleResp.

        创建时间

        :return: The create_time of this ThrottleBindingThrottleResp.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ThrottleBindingThrottleResp.

        创建时间

        :param create_time: The create_time of this ThrottleBindingThrottleResp.
        :type: datetime
        """
        self._create_time = create_time

    @property
    def is_include_special_throttle(self):
        """Gets the is_include_special_throttle of this ThrottleBindingThrottleResp.

        是否包含特殊流控 - 1：包含 - 2：不包含

        :return: The is_include_special_throttle of this ThrottleBindingThrottleResp.
        :rtype: int
        """
        return self._is_include_special_throttle

    @is_include_special_throttle.setter
    def is_include_special_throttle(self, is_include_special_throttle):
        """Sets the is_include_special_throttle of this ThrottleBindingThrottleResp.

        是否包含特殊流控 - 1：包含 - 2：不包含

        :param is_include_special_throttle: The is_include_special_throttle of this ThrottleBindingThrottleResp.
        :type: int
        """
        self._is_include_special_throttle = is_include_special_throttle

    @property
    def env_name(self):
        """Gets the env_name of this ThrottleBindingThrottleResp.

        流控策略生效的环境（即在哪个环境上有效）

        :return: The env_name of this ThrottleBindingThrottleResp.
        :rtype: str
        """
        return self._env_name

    @env_name.setter
    def env_name(self, env_name):
        """Sets the env_name of this ThrottleBindingThrottleResp.

        流控策略生效的环境（即在哪个环境上有效）

        :param env_name: The env_name of this ThrottleBindingThrottleResp.
        :type: str
        """
        self._env_name = env_name

    @property
    def type(self):
        """Gets the type of this ThrottleBindingThrottleResp.

        流控策略的类型

        :return: The type of this ThrottleBindingThrottleResp.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ThrottleBindingThrottleResp.

        流控策略的类型

        :param type: The type of this ThrottleBindingThrottleResp.
        :type: int
        """
        self._type = type

    @property
    def bind_id(self):
        """Gets the bind_id of this ThrottleBindingThrottleResp.

        流控策略与API绑定关系编号

        :return: The bind_id of this ThrottleBindingThrottleResp.
        :rtype: str
        """
        return self._bind_id

    @bind_id.setter
    def bind_id(self, bind_id):
        """Sets the bind_id of this ThrottleBindingThrottleResp.

        流控策略与API绑定关系编号

        :param bind_id: The bind_id of this ThrottleBindingThrottleResp.
        :type: str
        """
        self._bind_id = bind_id

    @property
    def bind_time(self):
        """Gets the bind_time of this ThrottleBindingThrottleResp.

        流控策略与API绑定时间

        :return: The bind_time of this ThrottleBindingThrottleResp.
        :rtype: datetime
        """
        return self._bind_time

    @bind_time.setter
    def bind_time(self, bind_time):
        """Sets the bind_time of this ThrottleBindingThrottleResp.

        流控策略与API绑定时间

        :param bind_time: The bind_time of this ThrottleBindingThrottleResp.
        :type: datetime
        """
        self._bind_time = bind_time

    @property
    def bind_num(self):
        """Gets the bind_num of this ThrottleBindingThrottleResp.

        流控策略绑定的API数量

        :return: The bind_num of this ThrottleBindingThrottleResp.
        :rtype: int
        """
        return self._bind_num

    @bind_num.setter
    def bind_num(self, bind_num):
        """Sets the bind_num of this ThrottleBindingThrottleResp.

        流控策略绑定的API数量

        :param bind_num: The bind_num of this ThrottleBindingThrottleResp.
        :type: int
        """
        self._bind_num = bind_num

    @property
    def enable_adaptive_control(self):
        """Gets the enable_adaptive_control of this ThrottleBindingThrottleResp.

        是否开启动态流控，暂不支持

        :return: The enable_adaptive_control of this ThrottleBindingThrottleResp.
        :rtype: str
        """
        return self._enable_adaptive_control

    @enable_adaptive_control.setter
    def enable_adaptive_control(self, enable_adaptive_control):
        """Sets the enable_adaptive_control of this ThrottleBindingThrottleResp.

        是否开启动态流控，暂不支持

        :param enable_adaptive_control: The enable_adaptive_control of this ThrottleBindingThrottleResp.
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
        if not isinstance(other, ThrottleBindingThrottleResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
