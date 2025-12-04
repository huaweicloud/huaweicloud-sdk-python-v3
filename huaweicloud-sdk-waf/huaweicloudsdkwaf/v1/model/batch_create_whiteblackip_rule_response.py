# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateWhiteblackipRuleResponse(SdkResponse):

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
        'policyid': 'str',
        'addr': 'str',
        'white': 'int',
        'time_mode': 'str',
        'start': 'int',
        'terminal': 'int',
        'ip_group': 'IpGroup',
        'status': 'int',
        'description': 'str',
        'timestamp': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'policyid': 'policyid',
        'addr': 'addr',
        'white': 'white',
        'time_mode': 'time_mode',
        'start': 'start',
        'terminal': 'terminal',
        'ip_group': 'ip_group',
        'status': 'status',
        'description': 'description',
        'timestamp': 'timestamp'
    }

    def __init__(self, id=None, name=None, policyid=None, addr=None, white=None, time_mode=None, start=None, terminal=None, ip_group=None, status=None, description=None, timestamp=None):
        r"""BatchCreateWhiteblackipRuleResponse

        The model defined in huaweicloud sdk

        :param id: 规则id
        :type id: str
        :param name: 黑白名单规则名称
        :type name: str
        :param policyid: 策略id
        :type policyid: str
        :param addr: 黑白名单ip地址，需要输入标准的ip地址或地址段，例如：42.123.120.66或42.123.120.0/16
        :type addr: str
        :param white: 防护动作：  - 0 拦截  - 1 放行  - 2 仅记录
        :type white: int
        :param time_mode: 生效模式，默认为permanent（立即生效）
        :type time_mode: str
        :param start: 规则生效开始时间，生效模式为自定义时，此字段才有效
        :type start: int
        :param terminal: 规则生效结束时间，生效模式为自定义时，此字段才有效
        :type terminal: int
        :param ip_group: 
        :type ip_group: :class:`huaweicloudsdkwaf.v1.IpGroup`
        :param status: **参数解释：** 规则状态标识，用于指定规则的启用或关闭状态 **约束限制：** 不涉及 **取值范围：**  - 0：关闭  - 1：开启 **默认取值：** 不涉及
        :type status: int
        :param description: 规则描述
        :type description: str
        :param timestamp: 创建规则的时间戳,13位毫秒时间戳
        :type timestamp: int
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._policyid = None
        self._addr = None
        self._white = None
        self._time_mode = None
        self._start = None
        self._terminal = None
        self._ip_group = None
        self._status = None
        self._description = None
        self._timestamp = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if policyid is not None:
            self.policyid = policyid
        if addr is not None:
            self.addr = addr
        if white is not None:
            self.white = white
        if time_mode is not None:
            self.time_mode = time_mode
        if start is not None:
            self.start = start
        if terminal is not None:
            self.terminal = terminal
        if ip_group is not None:
            self.ip_group = ip_group
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def id(self):
        r"""Gets the id of this BatchCreateWhiteblackipRuleResponse.

        规则id

        :return: The id of this BatchCreateWhiteblackipRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BatchCreateWhiteblackipRuleResponse.

        规则id

        :param id: The id of this BatchCreateWhiteblackipRuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this BatchCreateWhiteblackipRuleResponse.

        黑白名单规则名称

        :return: The name of this BatchCreateWhiteblackipRuleResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BatchCreateWhiteblackipRuleResponse.

        黑白名单规则名称

        :param name: The name of this BatchCreateWhiteblackipRuleResponse.
        :type name: str
        """
        self._name = name

    @property
    def policyid(self):
        r"""Gets the policyid of this BatchCreateWhiteblackipRuleResponse.

        策略id

        :return: The policyid of this BatchCreateWhiteblackipRuleResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        r"""Sets the policyid of this BatchCreateWhiteblackipRuleResponse.

        策略id

        :param policyid: The policyid of this BatchCreateWhiteblackipRuleResponse.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def addr(self):
        r"""Gets the addr of this BatchCreateWhiteblackipRuleResponse.

        黑白名单ip地址，需要输入标准的ip地址或地址段，例如：42.123.120.66或42.123.120.0/16

        :return: The addr of this BatchCreateWhiteblackipRuleResponse.
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        r"""Sets the addr of this BatchCreateWhiteblackipRuleResponse.

        黑白名单ip地址，需要输入标准的ip地址或地址段，例如：42.123.120.66或42.123.120.0/16

        :param addr: The addr of this BatchCreateWhiteblackipRuleResponse.
        :type addr: str
        """
        self._addr = addr

    @property
    def white(self):
        r"""Gets the white of this BatchCreateWhiteblackipRuleResponse.

        防护动作：  - 0 拦截  - 1 放行  - 2 仅记录

        :return: The white of this BatchCreateWhiteblackipRuleResponse.
        :rtype: int
        """
        return self._white

    @white.setter
    def white(self, white):
        r"""Sets the white of this BatchCreateWhiteblackipRuleResponse.

        防护动作：  - 0 拦截  - 1 放行  - 2 仅记录

        :param white: The white of this BatchCreateWhiteblackipRuleResponse.
        :type white: int
        """
        self._white = white

    @property
    def time_mode(self):
        r"""Gets the time_mode of this BatchCreateWhiteblackipRuleResponse.

        生效模式，默认为permanent（立即生效）

        :return: The time_mode of this BatchCreateWhiteblackipRuleResponse.
        :rtype: str
        """
        return self._time_mode

    @time_mode.setter
    def time_mode(self, time_mode):
        r"""Sets the time_mode of this BatchCreateWhiteblackipRuleResponse.

        生效模式，默认为permanent（立即生效）

        :param time_mode: The time_mode of this BatchCreateWhiteblackipRuleResponse.
        :type time_mode: str
        """
        self._time_mode = time_mode

    @property
    def start(self):
        r"""Gets the start of this BatchCreateWhiteblackipRuleResponse.

        规则生效开始时间，生效模式为自定义时，此字段才有效

        :return: The start of this BatchCreateWhiteblackipRuleResponse.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this BatchCreateWhiteblackipRuleResponse.

        规则生效开始时间，生效模式为自定义时，此字段才有效

        :param start: The start of this BatchCreateWhiteblackipRuleResponse.
        :type start: int
        """
        self._start = start

    @property
    def terminal(self):
        r"""Gets the terminal of this BatchCreateWhiteblackipRuleResponse.

        规则生效结束时间，生效模式为自定义时，此字段才有效

        :return: The terminal of this BatchCreateWhiteblackipRuleResponse.
        :rtype: int
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        r"""Sets the terminal of this BatchCreateWhiteblackipRuleResponse.

        规则生效结束时间，生效模式为自定义时，此字段才有效

        :param terminal: The terminal of this BatchCreateWhiteblackipRuleResponse.
        :type terminal: int
        """
        self._terminal = terminal

    @property
    def ip_group(self):
        r"""Gets the ip_group of this BatchCreateWhiteblackipRuleResponse.

        :return: The ip_group of this BatchCreateWhiteblackipRuleResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.IpGroup`
        """
        return self._ip_group

    @ip_group.setter
    def ip_group(self, ip_group):
        r"""Sets the ip_group of this BatchCreateWhiteblackipRuleResponse.

        :param ip_group: The ip_group of this BatchCreateWhiteblackipRuleResponse.
        :type ip_group: :class:`huaweicloudsdkwaf.v1.IpGroup`
        """
        self._ip_group = ip_group

    @property
    def status(self):
        r"""Gets the status of this BatchCreateWhiteblackipRuleResponse.

        **参数解释：** 规则状态标识，用于指定规则的启用或关闭状态 **约束限制：** 不涉及 **取值范围：**  - 0：关闭  - 1：开启 **默认取值：** 不涉及

        :return: The status of this BatchCreateWhiteblackipRuleResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BatchCreateWhiteblackipRuleResponse.

        **参数解释：** 规则状态标识，用于指定规则的启用或关闭状态 **约束限制：** 不涉及 **取值范围：**  - 0：关闭  - 1：开启 **默认取值：** 不涉及

        :param status: The status of this BatchCreateWhiteblackipRuleResponse.
        :type status: int
        """
        self._status = status

    @property
    def description(self):
        r"""Gets the description of this BatchCreateWhiteblackipRuleResponse.

        规则描述

        :return: The description of this BatchCreateWhiteblackipRuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BatchCreateWhiteblackipRuleResponse.

        规则描述

        :param description: The description of this BatchCreateWhiteblackipRuleResponse.
        :type description: str
        """
        self._description = description

    @property
    def timestamp(self):
        r"""Gets the timestamp of this BatchCreateWhiteblackipRuleResponse.

        创建规则的时间戳,13位毫秒时间戳

        :return: The timestamp of this BatchCreateWhiteblackipRuleResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this BatchCreateWhiteblackipRuleResponse.

        创建规则的时间戳,13位毫秒时间戳

        :param timestamp: The timestamp of this BatchCreateWhiteblackipRuleResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

    def to_dict(self):
        import warnings
        warnings.warn("BatchCreateWhiteblackipRuleResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchCreateWhiteblackipRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
