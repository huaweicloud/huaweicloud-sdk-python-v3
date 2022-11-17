# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ThrottleForApi:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_call_limits': 'int',
        'name': 'str',
        'time_unit': 'str',
        'remark': 'str',
        'api_call_limits': 'int',
        'type': 'int',
        'enable_adaptive_control': 'str',
        'user_call_limits': 'int',
        'time_interval': 'int',
        'ip_call_limits': 'int',
        'id': 'str',
        'bind_num': 'int',
        'is_inclu_special_throttle': 'int',
        'create_time': 'datetime',
        'env_name': 'str',
        'bind_id': 'str',
        'bind_time': 'datetime'
    }

    attribute_map = {
        'app_call_limits': 'app_call_limits',
        'name': 'name',
        'time_unit': 'time_unit',
        'remark': 'remark',
        'api_call_limits': 'api_call_limits',
        'type': 'type',
        'enable_adaptive_control': 'enable_adaptive_control',
        'user_call_limits': 'user_call_limits',
        'time_interval': 'time_interval',
        'ip_call_limits': 'ip_call_limits',
        'id': 'id',
        'bind_num': 'bind_num',
        'is_inclu_special_throttle': 'is_inclu_special_throttle',
        'create_time': 'create_time',
        'env_name': 'env_name',
        'bind_id': 'bind_id',
        'bind_time': 'bind_time'
    }

    def __init__(self, app_call_limits=None, name=None, time_unit=None, remark=None, api_call_limits=None, type=None, enable_adaptive_control=None, user_call_limits=None, time_interval=None, ip_call_limits=None, id=None, bind_num=None, is_inclu_special_throttle=None, create_time=None, env_name=None, bind_id=None, bind_time=None):
        """ThrottleForApi

        The model defined in huaweicloud sdk

        :param app_call_limits: APP流量限制是指一个API在时长之内被每个APP访问的次数上限，该数值不超过用户流量限制值。输入的值不超过2147483647。正整数。 
        :type app_call_limits: int
        :param name: 流控策略名称。支持汉字，英文，数字，下划线，且只能以英文和汉字开头，3 ~ 64字符。 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type name: str
        :param time_unit: 流控的时间单位
        :type time_unit: str
        :param remark: 流控策略描述字符长度不超过255。 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type remark: str
        :param api_call_limits: API流量限制是指时长内一个API能够被访问的次数上限。该值不超过系统默认配额限制，系统默认配额为200tps，用户可根据实际情况修改该系统默认配额。输入的值不超过2147483647。正整数。 
        :type api_call_limits: int
        :param type: 流控策略的类型 - 1：基础，表示绑定到流控策略的单个API流控时间内能够被调用多少次。 - 2：共享，表示绑定到流控策略的所有API流控时间内能够被调用多少次。
        :type type: int
        :param enable_adaptive_control: 是否开启动态流控： - TRUE - FALSE  暂不支持
        :type enable_adaptive_control: str
        :param user_call_limits: 用户流量限制是指一个API在时长之内每一个用户能访问的次数上限，该数值不超过API流量限制值。输入的值不超过2147483647。正整数。
        :type user_call_limits: int
        :param time_interval: 流量控制的时长单位。与“流量限制次数”配合使用，表示单位时间内的API请求次数上限。输入的值不超过2147483647。正整数。
        :type time_interval: int
        :param ip_call_limits: 源IP流量限制是指一个API在时长之内被每个IP访问的次数上限，该数值不超过API流量限制值。输入的值不超过2147483647。正整数。
        :type ip_call_limits: int
        :param id: 流控策略的ID
        :type id: str
        :param bind_num: 流控绑定的API数量
        :type bind_num: int
        :param is_inclu_special_throttle: 是否包含特殊流控配置 - 1：包含 - 2：不包含
        :type is_inclu_special_throttle: int
        :param create_time: 创建时间
        :type create_time: datetime
        :param env_name: 流控策略生效的环境（即在哪个环境上有效）
        :type env_name: str
        :param bind_id: 流控策略与API绑定关系编号
        :type bind_id: str
        :param bind_time: 流控策略与API绑定时间
        :type bind_time: datetime
        """
        
        

        self._app_call_limits = None
        self._name = None
        self._time_unit = None
        self._remark = None
        self._api_call_limits = None
        self._type = None
        self._enable_adaptive_control = None
        self._user_call_limits = None
        self._time_interval = None
        self._ip_call_limits = None
        self._id = None
        self._bind_num = None
        self._is_inclu_special_throttle = None
        self._create_time = None
        self._env_name = None
        self._bind_id = None
        self._bind_time = None
        self.discriminator = None

        if app_call_limits is not None:
            self.app_call_limits = app_call_limits
        self.name = name
        self.time_unit = time_unit
        if remark is not None:
            self.remark = remark
        self.api_call_limits = api_call_limits
        if type is not None:
            self.type = type
        if enable_adaptive_control is not None:
            self.enable_adaptive_control = enable_adaptive_control
        if user_call_limits is not None:
            self.user_call_limits = user_call_limits
        self.time_interval = time_interval
        if ip_call_limits is not None:
            self.ip_call_limits = ip_call_limits
        if id is not None:
            self.id = id
        if bind_num is not None:
            self.bind_num = bind_num
        if is_inclu_special_throttle is not None:
            self.is_inclu_special_throttle = is_inclu_special_throttle
        if create_time is not None:
            self.create_time = create_time
        if env_name is not None:
            self.env_name = env_name
        if bind_id is not None:
            self.bind_id = bind_id
        if bind_time is not None:
            self.bind_time = bind_time

    @property
    def app_call_limits(self):
        """Gets the app_call_limits of this ThrottleForApi.

        APP流量限制是指一个API在时长之内被每个APP访问的次数上限，该数值不超过用户流量限制值。输入的值不超过2147483647。正整数。 

        :return: The app_call_limits of this ThrottleForApi.
        :rtype: int
        """
        return self._app_call_limits

    @app_call_limits.setter
    def app_call_limits(self, app_call_limits):
        """Sets the app_call_limits of this ThrottleForApi.

        APP流量限制是指一个API在时长之内被每个APP访问的次数上限，该数值不超过用户流量限制值。输入的值不超过2147483647。正整数。 

        :param app_call_limits: The app_call_limits of this ThrottleForApi.
        :type app_call_limits: int
        """
        self._app_call_limits = app_call_limits

    @property
    def name(self):
        """Gets the name of this ThrottleForApi.

        流控策略名称。支持汉字，英文，数字，下划线，且只能以英文和汉字开头，3 ~ 64字符。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The name of this ThrottleForApi.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ThrottleForApi.

        流控策略名称。支持汉字，英文，数字，下划线，且只能以英文和汉字开头，3 ~ 64字符。 > 中文字符必须为UTF-8或者unicode编码。

        :param name: The name of this ThrottleForApi.
        :type name: str
        """
        self._name = name

    @property
    def time_unit(self):
        """Gets the time_unit of this ThrottleForApi.

        流控的时间单位

        :return: The time_unit of this ThrottleForApi.
        :rtype: str
        """
        return self._time_unit

    @time_unit.setter
    def time_unit(self, time_unit):
        """Sets the time_unit of this ThrottleForApi.

        流控的时间单位

        :param time_unit: The time_unit of this ThrottleForApi.
        :type time_unit: str
        """
        self._time_unit = time_unit

    @property
    def remark(self):
        """Gets the remark of this ThrottleForApi.

        流控策略描述字符长度不超过255。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The remark of this ThrottleForApi.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this ThrottleForApi.

        流控策略描述字符长度不超过255。 > 中文字符必须为UTF-8或者unicode编码。

        :param remark: The remark of this ThrottleForApi.
        :type remark: str
        """
        self._remark = remark

    @property
    def api_call_limits(self):
        """Gets the api_call_limits of this ThrottleForApi.

        API流量限制是指时长内一个API能够被访问的次数上限。该值不超过系统默认配额限制，系统默认配额为200tps，用户可根据实际情况修改该系统默认配额。输入的值不超过2147483647。正整数。 

        :return: The api_call_limits of this ThrottleForApi.
        :rtype: int
        """
        return self._api_call_limits

    @api_call_limits.setter
    def api_call_limits(self, api_call_limits):
        """Sets the api_call_limits of this ThrottleForApi.

        API流量限制是指时长内一个API能够被访问的次数上限。该值不超过系统默认配额限制，系统默认配额为200tps，用户可根据实际情况修改该系统默认配额。输入的值不超过2147483647。正整数。 

        :param api_call_limits: The api_call_limits of this ThrottleForApi.
        :type api_call_limits: int
        """
        self._api_call_limits = api_call_limits

    @property
    def type(self):
        """Gets the type of this ThrottleForApi.

        流控策略的类型 - 1：基础，表示绑定到流控策略的单个API流控时间内能够被调用多少次。 - 2：共享，表示绑定到流控策略的所有API流控时间内能够被调用多少次。

        :return: The type of this ThrottleForApi.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ThrottleForApi.

        流控策略的类型 - 1：基础，表示绑定到流控策略的单个API流控时间内能够被调用多少次。 - 2：共享，表示绑定到流控策略的所有API流控时间内能够被调用多少次。

        :param type: The type of this ThrottleForApi.
        :type type: int
        """
        self._type = type

    @property
    def enable_adaptive_control(self):
        """Gets the enable_adaptive_control of this ThrottleForApi.

        是否开启动态流控： - TRUE - FALSE  暂不支持

        :return: The enable_adaptive_control of this ThrottleForApi.
        :rtype: str
        """
        return self._enable_adaptive_control

    @enable_adaptive_control.setter
    def enable_adaptive_control(self, enable_adaptive_control):
        """Sets the enable_adaptive_control of this ThrottleForApi.

        是否开启动态流控： - TRUE - FALSE  暂不支持

        :param enable_adaptive_control: The enable_adaptive_control of this ThrottleForApi.
        :type enable_adaptive_control: str
        """
        self._enable_adaptive_control = enable_adaptive_control

    @property
    def user_call_limits(self):
        """Gets the user_call_limits of this ThrottleForApi.

        用户流量限制是指一个API在时长之内每一个用户能访问的次数上限，该数值不超过API流量限制值。输入的值不超过2147483647。正整数。

        :return: The user_call_limits of this ThrottleForApi.
        :rtype: int
        """
        return self._user_call_limits

    @user_call_limits.setter
    def user_call_limits(self, user_call_limits):
        """Sets the user_call_limits of this ThrottleForApi.

        用户流量限制是指一个API在时长之内每一个用户能访问的次数上限，该数值不超过API流量限制值。输入的值不超过2147483647。正整数。

        :param user_call_limits: The user_call_limits of this ThrottleForApi.
        :type user_call_limits: int
        """
        self._user_call_limits = user_call_limits

    @property
    def time_interval(self):
        """Gets the time_interval of this ThrottleForApi.

        流量控制的时长单位。与“流量限制次数”配合使用，表示单位时间内的API请求次数上限。输入的值不超过2147483647。正整数。

        :return: The time_interval of this ThrottleForApi.
        :rtype: int
        """
        return self._time_interval

    @time_interval.setter
    def time_interval(self, time_interval):
        """Sets the time_interval of this ThrottleForApi.

        流量控制的时长单位。与“流量限制次数”配合使用，表示单位时间内的API请求次数上限。输入的值不超过2147483647。正整数。

        :param time_interval: The time_interval of this ThrottleForApi.
        :type time_interval: int
        """
        self._time_interval = time_interval

    @property
    def ip_call_limits(self):
        """Gets the ip_call_limits of this ThrottleForApi.

        源IP流量限制是指一个API在时长之内被每个IP访问的次数上限，该数值不超过API流量限制值。输入的值不超过2147483647。正整数。

        :return: The ip_call_limits of this ThrottleForApi.
        :rtype: int
        """
        return self._ip_call_limits

    @ip_call_limits.setter
    def ip_call_limits(self, ip_call_limits):
        """Sets the ip_call_limits of this ThrottleForApi.

        源IP流量限制是指一个API在时长之内被每个IP访问的次数上限，该数值不超过API流量限制值。输入的值不超过2147483647。正整数。

        :param ip_call_limits: The ip_call_limits of this ThrottleForApi.
        :type ip_call_limits: int
        """
        self._ip_call_limits = ip_call_limits

    @property
    def id(self):
        """Gets the id of this ThrottleForApi.

        流控策略的ID

        :return: The id of this ThrottleForApi.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ThrottleForApi.

        流控策略的ID

        :param id: The id of this ThrottleForApi.
        :type id: str
        """
        self._id = id

    @property
    def bind_num(self):
        """Gets the bind_num of this ThrottleForApi.

        流控绑定的API数量

        :return: The bind_num of this ThrottleForApi.
        :rtype: int
        """
        return self._bind_num

    @bind_num.setter
    def bind_num(self, bind_num):
        """Sets the bind_num of this ThrottleForApi.

        流控绑定的API数量

        :param bind_num: The bind_num of this ThrottleForApi.
        :type bind_num: int
        """
        self._bind_num = bind_num

    @property
    def is_inclu_special_throttle(self):
        """Gets the is_inclu_special_throttle of this ThrottleForApi.

        是否包含特殊流控配置 - 1：包含 - 2：不包含

        :return: The is_inclu_special_throttle of this ThrottleForApi.
        :rtype: int
        """
        return self._is_inclu_special_throttle

    @is_inclu_special_throttle.setter
    def is_inclu_special_throttle(self, is_inclu_special_throttle):
        """Sets the is_inclu_special_throttle of this ThrottleForApi.

        是否包含特殊流控配置 - 1：包含 - 2：不包含

        :param is_inclu_special_throttle: The is_inclu_special_throttle of this ThrottleForApi.
        :type is_inclu_special_throttle: int
        """
        self._is_inclu_special_throttle = is_inclu_special_throttle

    @property
    def create_time(self):
        """Gets the create_time of this ThrottleForApi.

        创建时间

        :return: The create_time of this ThrottleForApi.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ThrottleForApi.

        创建时间

        :param create_time: The create_time of this ThrottleForApi.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def env_name(self):
        """Gets the env_name of this ThrottleForApi.

        流控策略生效的环境（即在哪个环境上有效）

        :return: The env_name of this ThrottleForApi.
        :rtype: str
        """
        return self._env_name

    @env_name.setter
    def env_name(self, env_name):
        """Sets the env_name of this ThrottleForApi.

        流控策略生效的环境（即在哪个环境上有效）

        :param env_name: The env_name of this ThrottleForApi.
        :type env_name: str
        """
        self._env_name = env_name

    @property
    def bind_id(self):
        """Gets the bind_id of this ThrottleForApi.

        流控策略与API绑定关系编号

        :return: The bind_id of this ThrottleForApi.
        :rtype: str
        """
        return self._bind_id

    @bind_id.setter
    def bind_id(self, bind_id):
        """Sets the bind_id of this ThrottleForApi.

        流控策略与API绑定关系编号

        :param bind_id: The bind_id of this ThrottleForApi.
        :type bind_id: str
        """
        self._bind_id = bind_id

    @property
    def bind_time(self):
        """Gets the bind_time of this ThrottleForApi.

        流控策略与API绑定时间

        :return: The bind_time of this ThrottleForApi.
        :rtype: datetime
        """
        return self._bind_time

    @bind_time.setter
    def bind_time(self, bind_time):
        """Sets the bind_time of this ThrottleForApi.

        流控策略与API绑定时间

        :param bind_time: The bind_time of this ThrottleForApi.
        :type bind_time: datetime
        """
        self._bind_time = bind_time

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
        if not isinstance(other, ThrottleForApi):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
