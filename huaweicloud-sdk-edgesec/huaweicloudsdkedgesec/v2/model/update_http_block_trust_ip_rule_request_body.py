# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHttpBlockTrustIpRuleRequestBody:

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
        'description': 'str',
        'status': 'int',
        'addr': 'str',
        'white': 'int',
        'followed_action_id': 'str',
        'ip_group_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'addr': 'addr',
        'white': 'white',
        'followed_action_id': 'followed_action_id',
        'ip_group_id': 'ip_group_id'
    }

    def __init__(self, name=None, description=None, status=None, addr=None, white=None, followed_action_id=None, ip_group_id=None):
        r"""UpdateHttpBlockTrustIpRuleRequestBody

        The model defined in huaweicloud sdk

        :param name: 规则名称
        :type name: str
        :param description: 规则描述，最长512字符
        :type description: str
        :param status: 规则开关： - 0：关闭 - 1：开启 
        :type status: int
        :param addr: ip地址/地址段；ip地址/地址段或者ip地址组id至少有一个
        :type addr: str
        :param white: - 0：拦截 - 1：放行 - 2：仅记录 
        :type white: int
        :param followed_action_id: 攻击惩罚规则id
        :type followed_action_id: str
        :param ip_group_id: ip地址组id；ip地址/地址段或者ip地址组id至少有一个
        :type ip_group_id: str
        """
        
        

        self._name = None
        self._description = None
        self._status = None
        self._addr = None
        self._white = None
        self._followed_action_id = None
        self._ip_group_id = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if addr is not None:
            self.addr = addr
        self.white = white
        if followed_action_id is not None:
            self.followed_action_id = followed_action_id
        if ip_group_id is not None:
            self.ip_group_id = ip_group_id

    @property
    def name(self):
        r"""Gets the name of this UpdateHttpBlockTrustIpRuleRequestBody.

        规则名称

        :return: The name of this UpdateHttpBlockTrustIpRuleRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateHttpBlockTrustIpRuleRequestBody.

        规则名称

        :param name: The name of this UpdateHttpBlockTrustIpRuleRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateHttpBlockTrustIpRuleRequestBody.

        规则描述，最长512字符

        :return: The description of this UpdateHttpBlockTrustIpRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateHttpBlockTrustIpRuleRequestBody.

        规则描述，最长512字符

        :param description: The description of this UpdateHttpBlockTrustIpRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this UpdateHttpBlockTrustIpRuleRequestBody.

        规则开关： - 0：关闭 - 1：开启 

        :return: The status of this UpdateHttpBlockTrustIpRuleRequestBody.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateHttpBlockTrustIpRuleRequestBody.

        规则开关： - 0：关闭 - 1：开启 

        :param status: The status of this UpdateHttpBlockTrustIpRuleRequestBody.
        :type status: int
        """
        self._status = status

    @property
    def addr(self):
        r"""Gets the addr of this UpdateHttpBlockTrustIpRuleRequestBody.

        ip地址/地址段；ip地址/地址段或者ip地址组id至少有一个

        :return: The addr of this UpdateHttpBlockTrustIpRuleRequestBody.
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        r"""Sets the addr of this UpdateHttpBlockTrustIpRuleRequestBody.

        ip地址/地址段；ip地址/地址段或者ip地址组id至少有一个

        :param addr: The addr of this UpdateHttpBlockTrustIpRuleRequestBody.
        :type addr: str
        """
        self._addr = addr

    @property
    def white(self):
        r"""Gets the white of this UpdateHttpBlockTrustIpRuleRequestBody.

        - 0：拦截 - 1：放行 - 2：仅记录 

        :return: The white of this UpdateHttpBlockTrustIpRuleRequestBody.
        :rtype: int
        """
        return self._white

    @white.setter
    def white(self, white):
        r"""Sets the white of this UpdateHttpBlockTrustIpRuleRequestBody.

        - 0：拦截 - 1：放行 - 2：仅记录 

        :param white: The white of this UpdateHttpBlockTrustIpRuleRequestBody.
        :type white: int
        """
        self._white = white

    @property
    def followed_action_id(self):
        r"""Gets the followed_action_id of this UpdateHttpBlockTrustIpRuleRequestBody.

        攻击惩罚规则id

        :return: The followed_action_id of this UpdateHttpBlockTrustIpRuleRequestBody.
        :rtype: str
        """
        return self._followed_action_id

    @followed_action_id.setter
    def followed_action_id(self, followed_action_id):
        r"""Sets the followed_action_id of this UpdateHttpBlockTrustIpRuleRequestBody.

        攻击惩罚规则id

        :param followed_action_id: The followed_action_id of this UpdateHttpBlockTrustIpRuleRequestBody.
        :type followed_action_id: str
        """
        self._followed_action_id = followed_action_id

    @property
    def ip_group_id(self):
        r"""Gets the ip_group_id of this UpdateHttpBlockTrustIpRuleRequestBody.

        ip地址组id；ip地址/地址段或者ip地址组id至少有一个

        :return: The ip_group_id of this UpdateHttpBlockTrustIpRuleRequestBody.
        :rtype: str
        """
        return self._ip_group_id

    @ip_group_id.setter
    def ip_group_id(self, ip_group_id):
        r"""Sets the ip_group_id of this UpdateHttpBlockTrustIpRuleRequestBody.

        ip地址组id；ip地址/地址段或者ip地址组id至少有一个

        :param ip_group_id: The ip_group_id of this UpdateHttpBlockTrustIpRuleRequestBody.
        :type ip_group_id: str
        """
        self._ip_group_id = ip_group_id

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
        if not isinstance(other, UpdateHttpBlockTrustIpRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
