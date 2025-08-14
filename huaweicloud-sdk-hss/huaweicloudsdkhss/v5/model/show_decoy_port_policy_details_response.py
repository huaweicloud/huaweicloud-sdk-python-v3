# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDecoyPortPolicyDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_name': 'str',
        'port_list': 'list[PolicyDetailsPortList]',
        'os_type': 'str',
        'white_ip': 'list[str]',
        'host_list': 'list[str]'
    }

    attribute_map = {
        'policy_name': 'policy_name',
        'port_list': 'port_list',
        'os_type': 'os_type',
        'white_ip': 'white_ip',
        'host_list': 'host_list'
    }

    def __init__(self, policy_name=None, port_list=None, os_type=None, white_ip=None, host_list=None):
        r"""ShowDecoyPortPolicyDetailsResponse

        The model defined in huaweicloud sdk

        :param policy_name: 策略名称
        :type policy_name: str
        :param port_list: 端口与协议
        :type port_list: list[:class:`huaweicloudsdkhss.v5.PolicyDetailsPortList`]
        :param os_type: **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 
        :type os_type: str
        :param white_ip: ip白名单
        :type white_ip: list[str]
        :param host_list: 主机列表
        :type host_list: list[str]
        """
        
        super(ShowDecoyPortPolicyDetailsResponse, self).__init__()

        self._policy_name = None
        self._port_list = None
        self._os_type = None
        self._white_ip = None
        self._host_list = None
        self.discriminator = None

        if policy_name is not None:
            self.policy_name = policy_name
        if port_list is not None:
            self.port_list = port_list
        if os_type is not None:
            self.os_type = os_type
        if white_ip is not None:
            self.white_ip = white_ip
        if host_list is not None:
            self.host_list = host_list

    @property
    def policy_name(self):
        r"""Gets the policy_name of this ShowDecoyPortPolicyDetailsResponse.

        策略名称

        :return: The policy_name of this ShowDecoyPortPolicyDetailsResponse.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this ShowDecoyPortPolicyDetailsResponse.

        策略名称

        :param policy_name: The policy_name of this ShowDecoyPortPolicyDetailsResponse.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def port_list(self):
        r"""Gets the port_list of this ShowDecoyPortPolicyDetailsResponse.

        端口与协议

        :return: The port_list of this ShowDecoyPortPolicyDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.PolicyDetailsPortList`]
        """
        return self._port_list

    @port_list.setter
    def port_list(self, port_list):
        r"""Sets the port_list of this ShowDecoyPortPolicyDetailsResponse.

        端口与协议

        :param port_list: The port_list of this ShowDecoyPortPolicyDetailsResponse.
        :type port_list: list[:class:`huaweicloudsdkhss.v5.PolicyDetailsPortList`]
        """
        self._port_list = port_list

    @property
    def os_type(self):
        r"""Gets the os_type of this ShowDecoyPortPolicyDetailsResponse.

        **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 

        :return: The os_type of this ShowDecoyPortPolicyDetailsResponse.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ShowDecoyPortPolicyDetailsResponse.

        **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 

        :param os_type: The os_type of this ShowDecoyPortPolicyDetailsResponse.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def white_ip(self):
        r"""Gets the white_ip of this ShowDecoyPortPolicyDetailsResponse.

        ip白名单

        :return: The white_ip of this ShowDecoyPortPolicyDetailsResponse.
        :rtype: list[str]
        """
        return self._white_ip

    @white_ip.setter
    def white_ip(self, white_ip):
        r"""Sets the white_ip of this ShowDecoyPortPolicyDetailsResponse.

        ip白名单

        :param white_ip: The white_ip of this ShowDecoyPortPolicyDetailsResponse.
        :type white_ip: list[str]
        """
        self._white_ip = white_ip

    @property
    def host_list(self):
        r"""Gets the host_list of this ShowDecoyPortPolicyDetailsResponse.

        主机列表

        :return: The host_list of this ShowDecoyPortPolicyDetailsResponse.
        :rtype: list[str]
        """
        return self._host_list

    @host_list.setter
    def host_list(self, host_list):
        r"""Sets the host_list of this ShowDecoyPortPolicyDetailsResponse.

        主机列表

        :param host_list: The host_list of this ShowDecoyPortPolicyDetailsResponse.
        :type host_list: list[str]
        """
        self._host_list = host_list

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
        if not isinstance(other, ShowDecoyPortPolicyDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
