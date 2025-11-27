# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownlinkVpcOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'virsubnet_id': 'str',
        'ngport_ip_address': 'str'
    }

    attribute_map = {
        'virsubnet_id': 'virsubnet_id',
        'ngport_ip_address': 'ngport_ip_address'
    }

    def __init__(self, virsubnet_id=None, ngport_ip_address=None):
        r"""DownlinkVpcOption

        The model defined in huaweicloud sdk

        :param virsubnet_id: 私网NAT网关实例所属的子网的ID。
        :type virsubnet_id: str
        :param ngport_ip_address: 私网NAT网关的ngport_ip_addrss。
        :type ngport_ip_address: str
        """
        
        

        self._virsubnet_id = None
        self._ngport_ip_address = None
        self.discriminator = None

        self.virsubnet_id = virsubnet_id
        if ngport_ip_address is not None:
            self.ngport_ip_address = ngport_ip_address

    @property
    def virsubnet_id(self):
        r"""Gets the virsubnet_id of this DownlinkVpcOption.

        私网NAT网关实例所属的子网的ID。

        :return: The virsubnet_id of this DownlinkVpcOption.
        :rtype: str
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        r"""Sets the virsubnet_id of this DownlinkVpcOption.

        私网NAT网关实例所属的子网的ID。

        :param virsubnet_id: The virsubnet_id of this DownlinkVpcOption.
        :type virsubnet_id: str
        """
        self._virsubnet_id = virsubnet_id

    @property
    def ngport_ip_address(self):
        r"""Gets the ngport_ip_address of this DownlinkVpcOption.

        私网NAT网关的ngport_ip_addrss。

        :return: The ngport_ip_address of this DownlinkVpcOption.
        :rtype: str
        """
        return self._ngport_ip_address

    @ngport_ip_address.setter
    def ngport_ip_address(self, ngport_ip_address):
        r"""Sets the ngport_ip_address of this DownlinkVpcOption.

        私网NAT网关的ngport_ip_addrss。

        :param ngport_ip_address: The ngport_ip_address of this DownlinkVpcOption.
        :type ngport_ip_address: str
        """
        self._ngport_ip_address = ngport_ip_address

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
        if not isinstance(other, DownlinkVpcOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
