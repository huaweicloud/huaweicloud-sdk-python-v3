# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEndpointOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'resource_type': 'str',
        'weight': 'int',
        'ip_address': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_type': 'resource_type',
        'weight': 'weight',
        'ip_address': 'ip_address'
    }

    def __init__(self, resource_id=None, resource_type=None, weight=None, ip_address=None):
        r"""CreateEndpointOption

        The model defined in huaweicloud sdk

        :param resource_id: 对应后端资源的ID，比如EIP的ID。
        :type resource_id: str
        :param resource_type: 终端节点类型，取值范围: - EIP：本账号中的弹性公网IP - ECS：本账号中私网ECS实例 - ELB：本账号中私网ELB实例 - CUSTOM_IP：云外公网IP - CUSTOM_DOMAIN_NAME：云外公网域名 - CUSTOM_EIP：本Region的弹性公网IP
        :type resource_type: str
        :param weight: 终端节点权重。
        :type weight: int
        :param ip_address: IP地址。
        :type ip_address: str
        """
        
        

        self._resource_id = None
        self._resource_type = None
        self._weight = None
        self._ip_address = None
        self.discriminator = None

        self.resource_id = resource_id
        self.resource_type = resource_type
        if weight is not None:
            self.weight = weight
        self.ip_address = ip_address

    @property
    def resource_id(self):
        r"""Gets the resource_id of this CreateEndpointOption.

        对应后端资源的ID，比如EIP的ID。

        :return: The resource_id of this CreateEndpointOption.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this CreateEndpointOption.

        对应后端资源的ID，比如EIP的ID。

        :param resource_id: The resource_id of this CreateEndpointOption.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this CreateEndpointOption.

        终端节点类型，取值范围: - EIP：本账号中的弹性公网IP - ECS：本账号中私网ECS实例 - ELB：本账号中私网ELB实例 - CUSTOM_IP：云外公网IP - CUSTOM_DOMAIN_NAME：云外公网域名 - CUSTOM_EIP：本Region的弹性公网IP

        :return: The resource_type of this CreateEndpointOption.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this CreateEndpointOption.

        终端节点类型，取值范围: - EIP：本账号中的弹性公网IP - ECS：本账号中私网ECS实例 - ELB：本账号中私网ELB实例 - CUSTOM_IP：云外公网IP - CUSTOM_DOMAIN_NAME：云外公网域名 - CUSTOM_EIP：本Region的弹性公网IP

        :param resource_type: The resource_type of this CreateEndpointOption.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def weight(self):
        r"""Gets the weight of this CreateEndpointOption.

        终端节点权重。

        :return: The weight of this CreateEndpointOption.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this CreateEndpointOption.

        终端节点权重。

        :param weight: The weight of this CreateEndpointOption.
        :type weight: int
        """
        self._weight = weight

    @property
    def ip_address(self):
        r"""Gets the ip_address of this CreateEndpointOption.

        IP地址。

        :return: The ip_address of this CreateEndpointOption.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this CreateEndpointOption.

        IP地址。

        :param ip_address: The ip_address of this CreateEndpointOption.
        :type ip_address: str
        """
        self._ip_address = ip_address

    def to_dict(self):
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
        if not isinstance(other, CreateEndpointOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
