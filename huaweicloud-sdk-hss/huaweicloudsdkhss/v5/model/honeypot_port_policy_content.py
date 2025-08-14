# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HoneypotPortPolicyContent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'os_type': 'str',
        'policy_name': 'str',
        'ports_list': 'list[HoneypotPortPolicyContentPortsList]',
        'white_ip': 'list[str]',
        'host_id': 'list[str]',
        'group_list': 'list[str]'
    }

    attribute_map = {
        'os_type': 'os_type',
        'policy_name': 'policy_name',
        'ports_list': 'ports_list',
        'white_ip': 'white_ip',
        'host_id': 'host_id',
        'group_list': 'group_list'
    }

    def __init__(self, os_type=None, policy_name=None, ports_list=None, white_ip=None, host_id=None, group_list=None):
        r"""HoneypotPortPolicyContent

        The model defined in huaweicloud sdk

        :param os_type: **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 
        :type os_type: str
        :param policy_name: 策略名称
        :type policy_name: str
        :param ports_list: 端口与协议
        :type ports_list: list[:class:`huaweicloudsdkhss.v5.HoneypotPortPolicyContentPortsList`]
        :param white_ip: ip白名单
        :type white_ip: list[str]
        :param host_id: 主机列表
        :type host_id: list[str]
        :param group_list: 分组列表
        :type group_list: list[str]
        """
        
        

        self._os_type = None
        self._policy_name = None
        self._ports_list = None
        self._white_ip = None
        self._host_id = None
        self._group_list = None
        self.discriminator = None

        self.os_type = os_type
        self.policy_name = policy_name
        self.ports_list = ports_list
        self.white_ip = white_ip
        self.host_id = host_id
        if group_list is not None:
            self.group_list = group_list

    @property
    def os_type(self):
        r"""Gets the os_type of this HoneypotPortPolicyContent.

        **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 

        :return: The os_type of this HoneypotPortPolicyContent.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this HoneypotPortPolicyContent.

        **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 

        :param os_type: The os_type of this HoneypotPortPolicyContent.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def policy_name(self):
        r"""Gets the policy_name of this HoneypotPortPolicyContent.

        策略名称

        :return: The policy_name of this HoneypotPortPolicyContent.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this HoneypotPortPolicyContent.

        策略名称

        :param policy_name: The policy_name of this HoneypotPortPolicyContent.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def ports_list(self):
        r"""Gets the ports_list of this HoneypotPortPolicyContent.

        端口与协议

        :return: The ports_list of this HoneypotPortPolicyContent.
        :rtype: list[:class:`huaweicloudsdkhss.v5.HoneypotPortPolicyContentPortsList`]
        """
        return self._ports_list

    @ports_list.setter
    def ports_list(self, ports_list):
        r"""Sets the ports_list of this HoneypotPortPolicyContent.

        端口与协议

        :param ports_list: The ports_list of this HoneypotPortPolicyContent.
        :type ports_list: list[:class:`huaweicloudsdkhss.v5.HoneypotPortPolicyContentPortsList`]
        """
        self._ports_list = ports_list

    @property
    def white_ip(self):
        r"""Gets the white_ip of this HoneypotPortPolicyContent.

        ip白名单

        :return: The white_ip of this HoneypotPortPolicyContent.
        :rtype: list[str]
        """
        return self._white_ip

    @white_ip.setter
    def white_ip(self, white_ip):
        r"""Sets the white_ip of this HoneypotPortPolicyContent.

        ip白名单

        :param white_ip: The white_ip of this HoneypotPortPolicyContent.
        :type white_ip: list[str]
        """
        self._white_ip = white_ip

    @property
    def host_id(self):
        r"""Gets the host_id of this HoneypotPortPolicyContent.

        主机列表

        :return: The host_id of this HoneypotPortPolicyContent.
        :rtype: list[str]
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this HoneypotPortPolicyContent.

        主机列表

        :param host_id: The host_id of this HoneypotPortPolicyContent.
        :type host_id: list[str]
        """
        self._host_id = host_id

    @property
    def group_list(self):
        r"""Gets the group_list of this HoneypotPortPolicyContent.

        分组列表

        :return: The group_list of this HoneypotPortPolicyContent.
        :rtype: list[str]
        """
        return self._group_list

    @group_list.setter
    def group_list(self, group_list):
        r"""Sets the group_list of this HoneypotPortPolicyContent.

        分组列表

        :param group_list: The group_list of this HoneypotPortPolicyContent.
        :type group_list: list[str]
        """
        self._group_list = group_list

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
        if not isinstance(other, HoneypotPortPolicyContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
