# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OcaIpExtendProperties:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'device': 'OcaIpDevice',
        'system': 'OcaIpSystem',
        'services': 'list[OcaIpService]'
    }

    attribute_map = {
        'device': 'device',
        'system': 'system',
        'services': 'services'
    }

    def __init__(self, device=None, system=None, services=None):
        r"""OcaIpExtendProperties

        The model defined in huaweicloud sdk

        :param device: 
        :type device: :class:`huaweicloudsdksecmaster.v1.OcaIpDevice`
        :param system: 
        :type system: :class:`huaweicloudsdksecmaster.v1.OcaIpSystem`
        :param services: 应用信息
        :type services: list[:class:`huaweicloudsdksecmaster.v1.OcaIpService`]
        """
        
        

        self._device = None
        self._system = None
        self._services = None
        self.discriminator = None

        if device is not None:
            self.device = device
        if system is not None:
            self.system = system
        if services is not None:
            self.services = services

    @property
    def device(self):
        r"""Gets the device of this OcaIpExtendProperties.

        :return: The device of this OcaIpExtendProperties.
        :rtype: :class:`huaweicloudsdksecmaster.v1.OcaIpDevice`
        """
        return self._device

    @device.setter
    def device(self, device):
        r"""Sets the device of this OcaIpExtendProperties.

        :param device: The device of this OcaIpExtendProperties.
        :type device: :class:`huaweicloudsdksecmaster.v1.OcaIpDevice`
        """
        self._device = device

    @property
    def system(self):
        r"""Gets the system of this OcaIpExtendProperties.

        :return: The system of this OcaIpExtendProperties.
        :rtype: :class:`huaweicloudsdksecmaster.v1.OcaIpSystem`
        """
        return self._system

    @system.setter
    def system(self, system):
        r"""Sets the system of this OcaIpExtendProperties.

        :param system: The system of this OcaIpExtendProperties.
        :type system: :class:`huaweicloudsdksecmaster.v1.OcaIpSystem`
        """
        self._system = system

    @property
    def services(self):
        r"""Gets the services of this OcaIpExtendProperties.

        应用信息

        :return: The services of this OcaIpExtendProperties.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.OcaIpService`]
        """
        return self._services

    @services.setter
    def services(self, services):
        r"""Sets the services of this OcaIpExtendProperties.

        应用信息

        :param services: The services of this OcaIpExtendProperties.
        :type services: list[:class:`huaweicloudsdksecmaster.v1.OcaIpService`]
        """
        self._services = services

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
        if not isinstance(other, OcaIpExtendProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
