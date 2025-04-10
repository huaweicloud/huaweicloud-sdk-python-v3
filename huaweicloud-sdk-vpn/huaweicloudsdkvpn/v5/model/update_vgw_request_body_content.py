# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVgwRequestBodyContent:

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
        'local_subnets': 'list[str]',
        'local_subnets_v6': 'list[str]',
        'eip_id_1': 'str',
        'eip_id_2': 'str',
        'policy_template': 'UpdateRequestPolicyTemplate'
    }

    attribute_map = {
        'name': 'name',
        'local_subnets': 'local_subnets',
        'local_subnets_v6': 'local_subnets_v6',
        'eip_id_1': 'eip_id_1',
        'eip_id_2': 'eip_id_2',
        'policy_template': 'policy_template'
    }

    def __init__(self, name=None, local_subnets=None, local_subnets_v6=None, eip_id_1=None, eip_id_2=None, policy_template=None):
        r"""UpdateVgwRequestBodyContent

        The model defined in huaweicloud sdk

        :param name: 网关名称
        :type name: str
        :param local_subnets: 本端子网
        :type local_subnets: list[str]
        :param local_subnets_v6: 使能ipv6的本端子网
        :type local_subnets_v6: list[str]
        :param eip_id_1: 有效的EIP的ID，表示绑定新的EIP作为双活VPN网关使用的第一个EIP或主备VPN网关的主EIP。
        :type eip_id_1: str
        :param eip_id_2: 有效的EIP的ID，表示绑定新的EIP作为双活VPN网关使用的第二个EIP或主备VPN网关的备EIP。
        :type eip_id_2: str
        :param policy_template: 
        :type policy_template: :class:`huaweicloudsdkvpn.v5.UpdateRequestPolicyTemplate`
        """
        
        

        self._name = None
        self._local_subnets = None
        self._local_subnets_v6 = None
        self._eip_id_1 = None
        self._eip_id_2 = None
        self._policy_template = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if local_subnets is not None:
            self.local_subnets = local_subnets
        if local_subnets_v6 is not None:
            self.local_subnets_v6 = local_subnets_v6
        if eip_id_1 is not None:
            self.eip_id_1 = eip_id_1
        if eip_id_2 is not None:
            self.eip_id_2 = eip_id_2
        if policy_template is not None:
            self.policy_template = policy_template

    @property
    def name(self):
        r"""Gets the name of this UpdateVgwRequestBodyContent.

        网关名称

        :return: The name of this UpdateVgwRequestBodyContent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateVgwRequestBodyContent.

        网关名称

        :param name: The name of this UpdateVgwRequestBodyContent.
        :type name: str
        """
        self._name = name

    @property
    def local_subnets(self):
        r"""Gets the local_subnets of this UpdateVgwRequestBodyContent.

        本端子网

        :return: The local_subnets of this UpdateVgwRequestBodyContent.
        :rtype: list[str]
        """
        return self._local_subnets

    @local_subnets.setter
    def local_subnets(self, local_subnets):
        r"""Sets the local_subnets of this UpdateVgwRequestBodyContent.

        本端子网

        :param local_subnets: The local_subnets of this UpdateVgwRequestBodyContent.
        :type local_subnets: list[str]
        """
        self._local_subnets = local_subnets

    @property
    def local_subnets_v6(self):
        r"""Gets the local_subnets_v6 of this UpdateVgwRequestBodyContent.

        使能ipv6的本端子网

        :return: The local_subnets_v6 of this UpdateVgwRequestBodyContent.
        :rtype: list[str]
        """
        return self._local_subnets_v6

    @local_subnets_v6.setter
    def local_subnets_v6(self, local_subnets_v6):
        r"""Sets the local_subnets_v6 of this UpdateVgwRequestBodyContent.

        使能ipv6的本端子网

        :param local_subnets_v6: The local_subnets_v6 of this UpdateVgwRequestBodyContent.
        :type local_subnets_v6: list[str]
        """
        self._local_subnets_v6 = local_subnets_v6

    @property
    def eip_id_1(self):
        r"""Gets the eip_id_1 of this UpdateVgwRequestBodyContent.

        有效的EIP的ID，表示绑定新的EIP作为双活VPN网关使用的第一个EIP或主备VPN网关的主EIP。

        :return: The eip_id_1 of this UpdateVgwRequestBodyContent.
        :rtype: str
        """
        return self._eip_id_1

    @eip_id_1.setter
    def eip_id_1(self, eip_id_1):
        r"""Sets the eip_id_1 of this UpdateVgwRequestBodyContent.

        有效的EIP的ID，表示绑定新的EIP作为双活VPN网关使用的第一个EIP或主备VPN网关的主EIP。

        :param eip_id_1: The eip_id_1 of this UpdateVgwRequestBodyContent.
        :type eip_id_1: str
        """
        self._eip_id_1 = eip_id_1

    @property
    def eip_id_2(self):
        r"""Gets the eip_id_2 of this UpdateVgwRequestBodyContent.

        有效的EIP的ID，表示绑定新的EIP作为双活VPN网关使用的第二个EIP或主备VPN网关的备EIP。

        :return: The eip_id_2 of this UpdateVgwRequestBodyContent.
        :rtype: str
        """
        return self._eip_id_2

    @eip_id_2.setter
    def eip_id_2(self, eip_id_2):
        r"""Sets the eip_id_2 of this UpdateVgwRequestBodyContent.

        有效的EIP的ID，表示绑定新的EIP作为双活VPN网关使用的第二个EIP或主备VPN网关的备EIP。

        :param eip_id_2: The eip_id_2 of this UpdateVgwRequestBodyContent.
        :type eip_id_2: str
        """
        self._eip_id_2 = eip_id_2

    @property
    def policy_template(self):
        r"""Gets the policy_template of this UpdateVgwRequestBodyContent.

        :return: The policy_template of this UpdateVgwRequestBodyContent.
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateRequestPolicyTemplate`
        """
        return self._policy_template

    @policy_template.setter
    def policy_template(self, policy_template):
        r"""Sets the policy_template of this UpdateVgwRequestBodyContent.

        :param policy_template: The policy_template of this UpdateVgwRequestBodyContent.
        :type policy_template: :class:`huaweicloudsdkvpn.v5.UpdateRequestPolicyTemplate`
        """
        self._policy_template = policy_template

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
        if not isinstance(other, UpdateVgwRequestBodyContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
