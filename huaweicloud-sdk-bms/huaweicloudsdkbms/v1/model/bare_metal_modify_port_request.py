# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BareMetalModifyPortRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subnet_id': 'str',
        'device_owner': 'str',
        'ip_addresses': 'list[str]',
        'reverse_binding': 'list[bool]'
    }

    attribute_map = {
        'subnet_id': 'subnet_id',
        'device_owner': 'device_owner',
        'ip_addresses': 'ip_addresses',
        'reverse_binding': 'reverse_binding'
    }

    def __init__(self, subnet_id=None, device_owner=None, ip_addresses=None, reverse_binding=None):
        r"""BareMetalModifyPortRequest

        The model defined in huaweicloud sdk

        :param subnet_id: 
        :type subnet_id: str
        :param device_owner: 
        :type device_owner: str
        :param ip_addresses: 
        :type ip_addresses: list[str]
        :param reverse_binding: 
        :type reverse_binding: list[bool]
        """
        
        

        self._subnet_id = None
        self._device_owner = None
        self._ip_addresses = None
        self._reverse_binding = None
        self.discriminator = None

        if subnet_id is not None:
            self.subnet_id = subnet_id
        if device_owner is not None:
            self.device_owner = device_owner
        if ip_addresses is not None:
            self.ip_addresses = ip_addresses
        if reverse_binding is not None:
            self.reverse_binding = reverse_binding

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this BareMetalModifyPortRequest.

        :return: The subnet_id of this BareMetalModifyPortRequest.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this BareMetalModifyPortRequest.

        :param subnet_id: The subnet_id of this BareMetalModifyPortRequest.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def device_owner(self):
        r"""Gets the device_owner of this BareMetalModifyPortRequest.

        :return: The device_owner of this BareMetalModifyPortRequest.
        :rtype: str
        """
        return self._device_owner

    @device_owner.setter
    def device_owner(self, device_owner):
        r"""Sets the device_owner of this BareMetalModifyPortRequest.

        :param device_owner: The device_owner of this BareMetalModifyPortRequest.
        :type device_owner: str
        """
        self._device_owner = device_owner

    @property
    def ip_addresses(self):
        r"""Gets the ip_addresses of this BareMetalModifyPortRequest.

        :return: The ip_addresses of this BareMetalModifyPortRequest.
        :rtype: list[str]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        r"""Sets the ip_addresses of this BareMetalModifyPortRequest.

        :param ip_addresses: The ip_addresses of this BareMetalModifyPortRequest.
        :type ip_addresses: list[str]
        """
        self._ip_addresses = ip_addresses

    @property
    def reverse_binding(self):
        r"""Gets the reverse_binding of this BareMetalModifyPortRequest.

        :return: The reverse_binding of this BareMetalModifyPortRequest.
        :rtype: list[bool]
        """
        return self._reverse_binding

    @reverse_binding.setter
    def reverse_binding(self, reverse_binding):
        r"""Sets the reverse_binding of this BareMetalModifyPortRequest.

        :param reverse_binding: The reverse_binding of this BareMetalModifyPortRequest.
        :type reverse_binding: list[bool]
        """
        self._reverse_binding = reverse_binding

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
        if not isinstance(other, BareMetalModifyPortRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
