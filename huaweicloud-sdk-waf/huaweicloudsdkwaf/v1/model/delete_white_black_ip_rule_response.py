# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteWhiteBlackIpRuleResponse(SdkResponse):

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
        'policyid': 'str',
        'name': 'str',
        'timestamp': 'int',
        'description': 'str',
        'status': 'int',
        'addr': 'str',
        'white': 'int',
        'time_mode': 'str',
        'start': 'int',
        'terminal': 'int',
        'ip_group': 'IpGroup'
    }

    attribute_map = {
        'id': 'id',
        'policyid': 'policyid',
        'name': 'name',
        'timestamp': 'timestamp',
        'description': 'description',
        'status': 'status',
        'addr': 'addr',
        'white': 'white',
        'time_mode': 'time_mode',
        'start': 'start',
        'terminal': 'terminal',
        'ip_group': 'ip_group'
    }

    def __init__(self, id=None, policyid=None, name=None, timestamp=None, description=None, status=None, addr=None, white=None, time_mode=None, start=None, terminal=None, ip_group=None):
        r"""DeleteWhiteBlackIpRuleResponse

        The model defined in huaweicloud sdk

        :param id: 黑白名单规则id
        :type id: str
        :param policyid: 策略id
        :type policyid: str
        :param name: 黑白名单规则名称
        :type name: str
        :param timestamp: 删除规则时间，13位毫秒时间戳
        :type timestamp: int
        :param description: 描述
        :type description: str
        :param status: 规则状态，0：关闭，1：开启
        :type status: int
        :param addr: 黑白名单ip地址，标准的ip地址或地址段，例如：42.123.120.66或42.123.120.0/16
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
        """
        
        super(DeleteWhiteBlackIpRuleResponse, self).__init__()

        self._id = None
        self._policyid = None
        self._name = None
        self._timestamp = None
        self._description = None
        self._status = None
        self._addr = None
        self._white = None
        self._time_mode = None
        self._start = None
        self._terminal = None
        self._ip_group = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if policyid is not None:
            self.policyid = policyid
        if name is not None:
            self.name = name
        if timestamp is not None:
            self.timestamp = timestamp
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
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

    @property
    def id(self):
        r"""Gets the id of this DeleteWhiteBlackIpRuleResponse.

        黑白名单规则id

        :return: The id of this DeleteWhiteBlackIpRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DeleteWhiteBlackIpRuleResponse.

        黑白名单规则id

        :param id: The id of this DeleteWhiteBlackIpRuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def policyid(self):
        r"""Gets the policyid of this DeleteWhiteBlackIpRuleResponse.

        策略id

        :return: The policyid of this DeleteWhiteBlackIpRuleResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        r"""Sets the policyid of this DeleteWhiteBlackIpRuleResponse.

        策略id

        :param policyid: The policyid of this DeleteWhiteBlackIpRuleResponse.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def name(self):
        r"""Gets the name of this DeleteWhiteBlackIpRuleResponse.

        黑白名单规则名称

        :return: The name of this DeleteWhiteBlackIpRuleResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DeleteWhiteBlackIpRuleResponse.

        黑白名单规则名称

        :param name: The name of this DeleteWhiteBlackIpRuleResponse.
        :type name: str
        """
        self._name = name

    @property
    def timestamp(self):
        r"""Gets the timestamp of this DeleteWhiteBlackIpRuleResponse.

        删除规则时间，13位毫秒时间戳

        :return: The timestamp of this DeleteWhiteBlackIpRuleResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this DeleteWhiteBlackIpRuleResponse.

        删除规则时间，13位毫秒时间戳

        :param timestamp: The timestamp of this DeleteWhiteBlackIpRuleResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def description(self):
        r"""Gets the description of this DeleteWhiteBlackIpRuleResponse.

        描述

        :return: The description of this DeleteWhiteBlackIpRuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DeleteWhiteBlackIpRuleResponse.

        描述

        :param description: The description of this DeleteWhiteBlackIpRuleResponse.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this DeleteWhiteBlackIpRuleResponse.

        规则状态，0：关闭，1：开启

        :return: The status of this DeleteWhiteBlackIpRuleResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DeleteWhiteBlackIpRuleResponse.

        规则状态，0：关闭，1：开启

        :param status: The status of this DeleteWhiteBlackIpRuleResponse.
        :type status: int
        """
        self._status = status

    @property
    def addr(self):
        r"""Gets the addr of this DeleteWhiteBlackIpRuleResponse.

        黑白名单ip地址，标准的ip地址或地址段，例如：42.123.120.66或42.123.120.0/16

        :return: The addr of this DeleteWhiteBlackIpRuleResponse.
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        r"""Sets the addr of this DeleteWhiteBlackIpRuleResponse.

        黑白名单ip地址，标准的ip地址或地址段，例如：42.123.120.66或42.123.120.0/16

        :param addr: The addr of this DeleteWhiteBlackIpRuleResponse.
        :type addr: str
        """
        self._addr = addr

    @property
    def white(self):
        r"""Gets the white of this DeleteWhiteBlackIpRuleResponse.

        防护动作：  - 0 拦截  - 1 放行  - 2 仅记录

        :return: The white of this DeleteWhiteBlackIpRuleResponse.
        :rtype: int
        """
        return self._white

    @white.setter
    def white(self, white):
        r"""Sets the white of this DeleteWhiteBlackIpRuleResponse.

        防护动作：  - 0 拦截  - 1 放行  - 2 仅记录

        :param white: The white of this DeleteWhiteBlackIpRuleResponse.
        :type white: int
        """
        self._white = white

    @property
    def time_mode(self):
        r"""Gets the time_mode of this DeleteWhiteBlackIpRuleResponse.

        生效模式，默认为permanent（立即生效）

        :return: The time_mode of this DeleteWhiteBlackIpRuleResponse.
        :rtype: str
        """
        return self._time_mode

    @time_mode.setter
    def time_mode(self, time_mode):
        r"""Sets the time_mode of this DeleteWhiteBlackIpRuleResponse.

        生效模式，默认为permanent（立即生效）

        :param time_mode: The time_mode of this DeleteWhiteBlackIpRuleResponse.
        :type time_mode: str
        """
        self._time_mode = time_mode

    @property
    def start(self):
        r"""Gets the start of this DeleteWhiteBlackIpRuleResponse.

        规则生效开始时间，生效模式为自定义时，此字段才有效

        :return: The start of this DeleteWhiteBlackIpRuleResponse.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this DeleteWhiteBlackIpRuleResponse.

        规则生效开始时间，生效模式为自定义时，此字段才有效

        :param start: The start of this DeleteWhiteBlackIpRuleResponse.
        :type start: int
        """
        self._start = start

    @property
    def terminal(self):
        r"""Gets the terminal of this DeleteWhiteBlackIpRuleResponse.

        规则生效结束时间，生效模式为自定义时，此字段才有效

        :return: The terminal of this DeleteWhiteBlackIpRuleResponse.
        :rtype: int
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        r"""Sets the terminal of this DeleteWhiteBlackIpRuleResponse.

        规则生效结束时间，生效模式为自定义时，此字段才有效

        :param terminal: The terminal of this DeleteWhiteBlackIpRuleResponse.
        :type terminal: int
        """
        self._terminal = terminal

    @property
    def ip_group(self):
        r"""Gets the ip_group of this DeleteWhiteBlackIpRuleResponse.

        :return: The ip_group of this DeleteWhiteBlackIpRuleResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.IpGroup`
        """
        return self._ip_group

    @ip_group.setter
    def ip_group(self, ip_group):
        r"""Sets the ip_group of this DeleteWhiteBlackIpRuleResponse.

        :param ip_group: The ip_group of this DeleteWhiteBlackIpRuleResponse.
        :type ip_group: :class:`huaweicloudsdkwaf.v1.IpGroup`
        """
        self._ip_group = ip_group

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
        if not isinstance(other, DeleteWhiteBlackIpRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
