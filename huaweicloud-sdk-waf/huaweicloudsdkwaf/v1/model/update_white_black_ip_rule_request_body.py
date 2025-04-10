# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateWhiteBlackIpRuleRequestBody:

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
        'addr': 'str',
        'description': 'str',
        'white': 'int',
        'ip_group_id': 'str',
        'time_mode': 'str',
        'start': 'int',
        'terminal': 'int'
    }

    attribute_map = {
        'name': 'name',
        'addr': 'addr',
        'description': 'description',
        'white': 'white',
        'ip_group_id': 'ip_group_id',
        'time_mode': 'time_mode',
        'start': 'start',
        'terminal': 'terminal'
    }

    def __init__(self, name=None, addr=None, description=None, white=None, ip_group_id=None, time_mode=None, start=None, terminal=None):
        r"""UpdateWhiteBlackIpRuleRequestBody

        The model defined in huaweicloud sdk

        :param name: 黑白名单规则名称
        :type name: str
        :param addr: 黑白名单ip地址，需要输入标准的ip地址或地址段，例如：42.123.120.66或42.123.120.0/16
        :type addr: str
        :param description: 黑白名单规则描述
        :type description: str
        :param white: 防护动作：  - 0 拦截  - 1 放行  - 2 仅记录
        :type white: int
        :param ip_group_id: 创建的Ip地址组id，该参数与addr参数使用一个即可；Ip地址组可在控制台中对象管理-&gt;地址组管理中添加。
        :type ip_group_id: str
        :param time_mode: 生效模式，默认为permanent（立即生效）,创建自定义生效规则时请输入：customize
        :type time_mode: str
        :param start: 规则生效开始时间，生效模式为自定义时，此字段才有效，请输入时间戳
        :type start: int
        :param terminal: 规则生效结束时间，生效模式为自定义时，此字段才有效，请输入时间戳
        :type terminal: int
        """
        
        

        self._name = None
        self._addr = None
        self._description = None
        self._white = None
        self._ip_group_id = None
        self._time_mode = None
        self._start = None
        self._terminal = None
        self.discriminator = None

        self.name = name
        if addr is not None:
            self.addr = addr
        if description is not None:
            self.description = description
        self.white = white
        if ip_group_id is not None:
            self.ip_group_id = ip_group_id
        if time_mode is not None:
            self.time_mode = time_mode
        if start is not None:
            self.start = start
        if terminal is not None:
            self.terminal = terminal

    @property
    def name(self):
        r"""Gets the name of this UpdateWhiteBlackIpRuleRequestBody.

        黑白名单规则名称

        :return: The name of this UpdateWhiteBlackIpRuleRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateWhiteBlackIpRuleRequestBody.

        黑白名单规则名称

        :param name: The name of this UpdateWhiteBlackIpRuleRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def addr(self):
        r"""Gets the addr of this UpdateWhiteBlackIpRuleRequestBody.

        黑白名单ip地址，需要输入标准的ip地址或地址段，例如：42.123.120.66或42.123.120.0/16

        :return: The addr of this UpdateWhiteBlackIpRuleRequestBody.
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        r"""Sets the addr of this UpdateWhiteBlackIpRuleRequestBody.

        黑白名单ip地址，需要输入标准的ip地址或地址段，例如：42.123.120.66或42.123.120.0/16

        :param addr: The addr of this UpdateWhiteBlackIpRuleRequestBody.
        :type addr: str
        """
        self._addr = addr

    @property
    def description(self):
        r"""Gets the description of this UpdateWhiteBlackIpRuleRequestBody.

        黑白名单规则描述

        :return: The description of this UpdateWhiteBlackIpRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateWhiteBlackIpRuleRequestBody.

        黑白名单规则描述

        :param description: The description of this UpdateWhiteBlackIpRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def white(self):
        r"""Gets the white of this UpdateWhiteBlackIpRuleRequestBody.

        防护动作：  - 0 拦截  - 1 放行  - 2 仅记录

        :return: The white of this UpdateWhiteBlackIpRuleRequestBody.
        :rtype: int
        """
        return self._white

    @white.setter
    def white(self, white):
        r"""Sets the white of this UpdateWhiteBlackIpRuleRequestBody.

        防护动作：  - 0 拦截  - 1 放行  - 2 仅记录

        :param white: The white of this UpdateWhiteBlackIpRuleRequestBody.
        :type white: int
        """
        self._white = white

    @property
    def ip_group_id(self):
        r"""Gets the ip_group_id of this UpdateWhiteBlackIpRuleRequestBody.

        创建的Ip地址组id，该参数与addr参数使用一个即可；Ip地址组可在控制台中对象管理->地址组管理中添加。

        :return: The ip_group_id of this UpdateWhiteBlackIpRuleRequestBody.
        :rtype: str
        """
        return self._ip_group_id

    @ip_group_id.setter
    def ip_group_id(self, ip_group_id):
        r"""Sets the ip_group_id of this UpdateWhiteBlackIpRuleRequestBody.

        创建的Ip地址组id，该参数与addr参数使用一个即可；Ip地址组可在控制台中对象管理->地址组管理中添加。

        :param ip_group_id: The ip_group_id of this UpdateWhiteBlackIpRuleRequestBody.
        :type ip_group_id: str
        """
        self._ip_group_id = ip_group_id

    @property
    def time_mode(self):
        r"""Gets the time_mode of this UpdateWhiteBlackIpRuleRequestBody.

        生效模式，默认为permanent（立即生效）,创建自定义生效规则时请输入：customize

        :return: The time_mode of this UpdateWhiteBlackIpRuleRequestBody.
        :rtype: str
        """
        return self._time_mode

    @time_mode.setter
    def time_mode(self, time_mode):
        r"""Sets the time_mode of this UpdateWhiteBlackIpRuleRequestBody.

        生效模式，默认为permanent（立即生效）,创建自定义生效规则时请输入：customize

        :param time_mode: The time_mode of this UpdateWhiteBlackIpRuleRequestBody.
        :type time_mode: str
        """
        self._time_mode = time_mode

    @property
    def start(self):
        r"""Gets the start of this UpdateWhiteBlackIpRuleRequestBody.

        规则生效开始时间，生效模式为自定义时，此字段才有效，请输入时间戳

        :return: The start of this UpdateWhiteBlackIpRuleRequestBody.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this UpdateWhiteBlackIpRuleRequestBody.

        规则生效开始时间，生效模式为自定义时，此字段才有效，请输入时间戳

        :param start: The start of this UpdateWhiteBlackIpRuleRequestBody.
        :type start: int
        """
        self._start = start

    @property
    def terminal(self):
        r"""Gets the terminal of this UpdateWhiteBlackIpRuleRequestBody.

        规则生效结束时间，生效模式为自定义时，此字段才有效，请输入时间戳

        :return: The terminal of this UpdateWhiteBlackIpRuleRequestBody.
        :rtype: int
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        r"""Sets the terminal of this UpdateWhiteBlackIpRuleRequestBody.

        规则生效结束时间，生效模式为自定义时，此字段才有效，请输入时间戳

        :param terminal: The terminal of this UpdateWhiteBlackIpRuleRequestBody.
        :type terminal: int
        """
        self._terminal = terminal

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
        if not isinstance(other, UpdateWhiteBlackIpRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
