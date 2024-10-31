# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHttpBlockTrustIpRuleResponseBody:

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
        'policy_id': 'str',
        'policy_name': 'str',
        'timestamp': 'int',
        'description': 'str',
        'status': 'int',
        'addr': 'str',
        'white': 'int',
        'followed_action_id': 'str',
        'ip_group': 'HttpIpGroup'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'policy_id': 'policy_id',
        'policy_name': 'policy_name',
        'timestamp': 'timestamp',
        'description': 'description',
        'status': 'status',
        'addr': 'addr',
        'white': 'white',
        'followed_action_id': 'followed_action_id',
        'ip_group': 'ip_group'
    }

    def __init__(self, id=None, name=None, policy_id=None, policy_name=None, timestamp=None, description=None, status=None, addr=None, white=None, followed_action_id=None, ip_group=None):
        """ShowHttpBlockTrustIpRuleResponseBody

        The model defined in huaweicloud sdk

        :param id: 规则id
        :type id: str
        :param name: 规则名称
        :type name: str
        :param policy_id: 规则所在策略id
        :type policy_id: str
        :param policy_name: 规则所在策略名称
        :type policy_name: str
        :param timestamp: 创建规则时间戳
        :type timestamp: int
        :param description: 规则描述
        :type description: str
        :param status: 规则开关： - 0：关闭 - 1：开启 
        :type status: int
        :param addr: ip地址/地址段
        :type addr: str
        :param white: - 0：拦截 - 1：放行 - 2：仅记录 
        :type white: int
        :param followed_action_id: 攻击惩罚规则id
        :type followed_action_id: str
        :param ip_group: 
        :type ip_group: :class:`huaweicloudsdkedgesec.v2.HttpIpGroup`
        """
        
        

        self._id = None
        self._name = None
        self._policy_id = None
        self._policy_name = None
        self._timestamp = None
        self._description = None
        self._status = None
        self._addr = None
        self._white = None
        self._followed_action_id = None
        self._ip_group = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if policy_id is not None:
            self.policy_id = policy_id
        if policy_name is not None:
            self.policy_name = policy_name
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
        if followed_action_id is not None:
            self.followed_action_id = followed_action_id
        if ip_group is not None:
            self.ip_group = ip_group

    @property
    def id(self):
        """Gets the id of this ShowHttpBlockTrustIpRuleResponseBody.

        规则id

        :return: The id of this ShowHttpBlockTrustIpRuleResponseBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowHttpBlockTrustIpRuleResponseBody.

        规则id

        :param id: The id of this ShowHttpBlockTrustIpRuleResponseBody.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowHttpBlockTrustIpRuleResponseBody.

        规则名称

        :return: The name of this ShowHttpBlockTrustIpRuleResponseBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowHttpBlockTrustIpRuleResponseBody.

        规则名称

        :param name: The name of this ShowHttpBlockTrustIpRuleResponseBody.
        :type name: str
        """
        self._name = name

    @property
    def policy_id(self):
        """Gets the policy_id of this ShowHttpBlockTrustIpRuleResponseBody.

        规则所在策略id

        :return: The policy_id of this ShowHttpBlockTrustIpRuleResponseBody.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this ShowHttpBlockTrustIpRuleResponseBody.

        规则所在策略id

        :param policy_id: The policy_id of this ShowHttpBlockTrustIpRuleResponseBody.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def policy_name(self):
        """Gets the policy_name of this ShowHttpBlockTrustIpRuleResponseBody.

        规则所在策略名称

        :return: The policy_name of this ShowHttpBlockTrustIpRuleResponseBody.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this ShowHttpBlockTrustIpRuleResponseBody.

        规则所在策略名称

        :param policy_name: The policy_name of this ShowHttpBlockTrustIpRuleResponseBody.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def timestamp(self):
        """Gets the timestamp of this ShowHttpBlockTrustIpRuleResponseBody.

        创建规则时间戳

        :return: The timestamp of this ShowHttpBlockTrustIpRuleResponseBody.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ShowHttpBlockTrustIpRuleResponseBody.

        创建规则时间戳

        :param timestamp: The timestamp of this ShowHttpBlockTrustIpRuleResponseBody.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def description(self):
        """Gets the description of this ShowHttpBlockTrustIpRuleResponseBody.

        规则描述

        :return: The description of this ShowHttpBlockTrustIpRuleResponseBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowHttpBlockTrustIpRuleResponseBody.

        规则描述

        :param description: The description of this ShowHttpBlockTrustIpRuleResponseBody.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this ShowHttpBlockTrustIpRuleResponseBody.

        规则开关： - 0：关闭 - 1：开启 

        :return: The status of this ShowHttpBlockTrustIpRuleResponseBody.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowHttpBlockTrustIpRuleResponseBody.

        规则开关： - 0：关闭 - 1：开启 

        :param status: The status of this ShowHttpBlockTrustIpRuleResponseBody.
        :type status: int
        """
        self._status = status

    @property
    def addr(self):
        """Gets the addr of this ShowHttpBlockTrustIpRuleResponseBody.

        ip地址/地址段

        :return: The addr of this ShowHttpBlockTrustIpRuleResponseBody.
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        """Sets the addr of this ShowHttpBlockTrustIpRuleResponseBody.

        ip地址/地址段

        :param addr: The addr of this ShowHttpBlockTrustIpRuleResponseBody.
        :type addr: str
        """
        self._addr = addr

    @property
    def white(self):
        """Gets the white of this ShowHttpBlockTrustIpRuleResponseBody.

        - 0：拦截 - 1：放行 - 2：仅记录 

        :return: The white of this ShowHttpBlockTrustIpRuleResponseBody.
        :rtype: int
        """
        return self._white

    @white.setter
    def white(self, white):
        """Sets the white of this ShowHttpBlockTrustIpRuleResponseBody.

        - 0：拦截 - 1：放行 - 2：仅记录 

        :param white: The white of this ShowHttpBlockTrustIpRuleResponseBody.
        :type white: int
        """
        self._white = white

    @property
    def followed_action_id(self):
        """Gets the followed_action_id of this ShowHttpBlockTrustIpRuleResponseBody.

        攻击惩罚规则id

        :return: The followed_action_id of this ShowHttpBlockTrustIpRuleResponseBody.
        :rtype: str
        """
        return self._followed_action_id

    @followed_action_id.setter
    def followed_action_id(self, followed_action_id):
        """Sets the followed_action_id of this ShowHttpBlockTrustIpRuleResponseBody.

        攻击惩罚规则id

        :param followed_action_id: The followed_action_id of this ShowHttpBlockTrustIpRuleResponseBody.
        :type followed_action_id: str
        """
        self._followed_action_id = followed_action_id

    @property
    def ip_group(self):
        """Gets the ip_group of this ShowHttpBlockTrustIpRuleResponseBody.

        :return: The ip_group of this ShowHttpBlockTrustIpRuleResponseBody.
        :rtype: :class:`huaweicloudsdkedgesec.v2.HttpIpGroup`
        """
        return self._ip_group

    @ip_group.setter
    def ip_group(self, ip_group):
        """Sets the ip_group of this ShowHttpBlockTrustIpRuleResponseBody.

        :param ip_group: The ip_group of this ShowHttpBlockTrustIpRuleResponseBody.
        :type ip_group: :class:`huaweicloudsdkedgesec.v2.HttpIpGroup`
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
        if not isinstance(other, ShowHttpBlockTrustIpRuleResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
