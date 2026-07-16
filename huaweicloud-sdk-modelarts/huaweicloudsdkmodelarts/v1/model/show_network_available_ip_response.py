# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowNetworkAvailableIpResponse(SdkResponse):

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
        'network_id': 'str',
        'subnet_ip_availability': 'list[SubnetIpAvailability]'
    }

    attribute_map = {
        'name': 'name',
        'network_id': 'networkId',
        'subnet_ip_availability': 'subnetIpAvailability'
    }

    def __init__(self, name=None, network_id=None, subnet_ip_availability=None):
        r"""ShowNetworkAvailableIpResponse

        The model defined in huaweicloud sdk

        :param name: **参数解释**：子网的名称。 **取值范围**：不涉及。
        :type name: str
        :param network_id: **参数解释**：子网的ID。 **取值范围**：不涉及。
        :type network_id: str
        :param subnet_ip_availability: **参数解释**：子网可用的网络IP数量。
        :type subnet_ip_availability: list[:class:`huaweicloudsdkmodelarts.v1.SubnetIpAvailability`]
        """
        
        super().__init__()

        self._name = None
        self._network_id = None
        self._subnet_ip_availability = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if network_id is not None:
            self.network_id = network_id
        if subnet_ip_availability is not None:
            self.subnet_ip_availability = subnet_ip_availability

    @property
    def name(self):
        r"""Gets the name of this ShowNetworkAvailableIpResponse.

        **参数解释**：子网的名称。 **取值范围**：不涉及。

        :return: The name of this ShowNetworkAvailableIpResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowNetworkAvailableIpResponse.

        **参数解释**：子网的名称。 **取值范围**：不涉及。

        :param name: The name of this ShowNetworkAvailableIpResponse.
        :type name: str
        """
        self._name = name

    @property
    def network_id(self):
        r"""Gets the network_id of this ShowNetworkAvailableIpResponse.

        **参数解释**：子网的ID。 **取值范围**：不涉及。

        :return: The network_id of this ShowNetworkAvailableIpResponse.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        r"""Sets the network_id of this ShowNetworkAvailableIpResponse.

        **参数解释**：子网的ID。 **取值范围**：不涉及。

        :param network_id: The network_id of this ShowNetworkAvailableIpResponse.
        :type network_id: str
        """
        self._network_id = network_id

    @property
    def subnet_ip_availability(self):
        r"""Gets the subnet_ip_availability of this ShowNetworkAvailableIpResponse.

        **参数解释**：子网可用的网络IP数量。

        :return: The subnet_ip_availability of this ShowNetworkAvailableIpResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.SubnetIpAvailability`]
        """
        return self._subnet_ip_availability

    @subnet_ip_availability.setter
    def subnet_ip_availability(self, subnet_ip_availability):
        r"""Sets the subnet_ip_availability of this ShowNetworkAvailableIpResponse.

        **参数解释**：子网可用的网络IP数量。

        :param subnet_ip_availability: The subnet_ip_availability of this ShowNetworkAvailableIpResponse.
        :type subnet_ip_availability: list[:class:`huaweicloudsdkmodelarts.v1.SubnetIpAvailability`]
        """
        self._subnet_ip_availability = subnet_ip_availability

    def to_dict(self):
        import warnings
        warnings.warn("ShowNetworkAvailableIpResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowNetworkAvailableIpResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
