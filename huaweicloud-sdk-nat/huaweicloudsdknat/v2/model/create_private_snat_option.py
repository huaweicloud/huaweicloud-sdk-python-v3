# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePrivateSnatOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'gateway_id': 'str',
        'cidr': 'str',
        'virsubnet_id': 'str',
        'description': 'str',
        'transit_ip_ids': 'list[str]'
    }

    attribute_map = {
        'gateway_id': 'gateway_id',
        'cidr': 'cidr',
        'virsubnet_id': 'virsubnet_id',
        'description': 'description',
        'transit_ip_ids': 'transit_ip_ids'
    }

    def __init__(self, gateway_id=None, cidr=None, virsubnet_id=None, description=None, transit_ip_ids=None):
        """CreatePrivateSnatOption

        The model defined in huaweicloud sdk

        :param gateway_id: 私网NAT网关实例的ID。
        :type gateway_id: str
        :param cidr: 功能说明：规则匹配的CIDR。取值约束：与virsubnet_id参数二选一。
        :type cidr: str
        :param virsubnet_id: 功能说明：规则匹配的子网的ID。 取值约束：与cidr参数二选一。
        :type virsubnet_id: str
        :param description: SNAT规则的描述。长度范围小于等于255个字符，不能包含“&lt;”和“&gt;”。
        :type description: str
        :param transit_ip_ids: 功能说明：中转IP的ID的列表。 取值约束：中转IP的ID个数不能超过1个。
        :type transit_ip_ids: list[str]
        """
        
        

        self._gateway_id = None
        self._cidr = None
        self._virsubnet_id = None
        self._description = None
        self._transit_ip_ids = None
        self.discriminator = None

        self.gateway_id = gateway_id
        if cidr is not None:
            self.cidr = cidr
        if virsubnet_id is not None:
            self.virsubnet_id = virsubnet_id
        if description is not None:
            self.description = description
        self.transit_ip_ids = transit_ip_ids

    @property
    def gateway_id(self):
        """Gets the gateway_id of this CreatePrivateSnatOption.

        私网NAT网关实例的ID。

        :return: The gateway_id of this CreatePrivateSnatOption.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """Sets the gateway_id of this CreatePrivateSnatOption.

        私网NAT网关实例的ID。

        :param gateway_id: The gateway_id of this CreatePrivateSnatOption.
        :type gateway_id: str
        """
        self._gateway_id = gateway_id

    @property
    def cidr(self):
        """Gets the cidr of this CreatePrivateSnatOption.

        功能说明：规则匹配的CIDR。取值约束：与virsubnet_id参数二选一。

        :return: The cidr of this CreatePrivateSnatOption.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this CreatePrivateSnatOption.

        功能说明：规则匹配的CIDR。取值约束：与virsubnet_id参数二选一。

        :param cidr: The cidr of this CreatePrivateSnatOption.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def virsubnet_id(self):
        """Gets the virsubnet_id of this CreatePrivateSnatOption.

        功能说明：规则匹配的子网的ID。 取值约束：与cidr参数二选一。

        :return: The virsubnet_id of this CreatePrivateSnatOption.
        :rtype: str
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        """Sets the virsubnet_id of this CreatePrivateSnatOption.

        功能说明：规则匹配的子网的ID。 取值约束：与cidr参数二选一。

        :param virsubnet_id: The virsubnet_id of this CreatePrivateSnatOption.
        :type virsubnet_id: str
        """
        self._virsubnet_id = virsubnet_id

    @property
    def description(self):
        """Gets the description of this CreatePrivateSnatOption.

        SNAT规则的描述。长度范围小于等于255个字符，不能包含“<”和“>”。

        :return: The description of this CreatePrivateSnatOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreatePrivateSnatOption.

        SNAT规则的描述。长度范围小于等于255个字符，不能包含“<”和“>”。

        :param description: The description of this CreatePrivateSnatOption.
        :type description: str
        """
        self._description = description

    @property
    def transit_ip_ids(self):
        """Gets the transit_ip_ids of this CreatePrivateSnatOption.

        功能说明：中转IP的ID的列表。 取值约束：中转IP的ID个数不能超过1个。

        :return: The transit_ip_ids of this CreatePrivateSnatOption.
        :rtype: list[str]
        """
        return self._transit_ip_ids

    @transit_ip_ids.setter
    def transit_ip_ids(self, transit_ip_ids):
        """Sets the transit_ip_ids of this CreatePrivateSnatOption.

        功能说明：中转IP的ID的列表。 取值约束：中转IP的ID个数不能超过1个。

        :param transit_ip_ids: The transit_ip_ids of this CreatePrivateSnatOption.
        :type transit_ip_ids: list[str]
        """
        self._transit_ip_ids = transit_ip_ids

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
        if not isinstance(other, CreatePrivateSnatOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
