# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLinkFlavorsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vm_flavor': 'FlavorInfo',
        'volume_flavor': 'FlavorInfo',
        'flow_flavor': 'FlavorInfo'
    }

    attribute_map = {
        'vm_flavor': 'vm_flavor',
        'volume_flavor': 'volume_flavor',
        'flow_flavor': 'flow_flavor'
    }

    def __init__(self, vm_flavor=None, volume_flavor=None, flow_flavor=None):
        r"""ShowLinkFlavorsResponse

        The model defined in huaweicloud sdk

        :param vm_flavor: 
        :type vm_flavor: :class:`huaweicloudsdkdrs.v5.FlavorInfo`
        :param volume_flavor: 
        :type volume_flavor: :class:`huaweicloudsdkdrs.v5.FlavorInfo`
        :param flow_flavor: 
        :type flow_flavor: :class:`huaweicloudsdkdrs.v5.FlavorInfo`
        """
        
        super().__init__()

        self._vm_flavor = None
        self._volume_flavor = None
        self._flow_flavor = None
        self.discriminator = None

        if vm_flavor is not None:
            self.vm_flavor = vm_flavor
        if volume_flavor is not None:
            self.volume_flavor = volume_flavor
        if flow_flavor is not None:
            self.flow_flavor = flow_flavor

    @property
    def vm_flavor(self):
        r"""Gets the vm_flavor of this ShowLinkFlavorsResponse.

        :return: The vm_flavor of this ShowLinkFlavorsResponse.
        :rtype: :class:`huaweicloudsdkdrs.v5.FlavorInfo`
        """
        return self._vm_flavor

    @vm_flavor.setter
    def vm_flavor(self, vm_flavor):
        r"""Sets the vm_flavor of this ShowLinkFlavorsResponse.

        :param vm_flavor: The vm_flavor of this ShowLinkFlavorsResponse.
        :type vm_flavor: :class:`huaweicloudsdkdrs.v5.FlavorInfo`
        """
        self._vm_flavor = vm_flavor

    @property
    def volume_flavor(self):
        r"""Gets the volume_flavor of this ShowLinkFlavorsResponse.

        :return: The volume_flavor of this ShowLinkFlavorsResponse.
        :rtype: :class:`huaweicloudsdkdrs.v5.FlavorInfo`
        """
        return self._volume_flavor

    @volume_flavor.setter
    def volume_flavor(self, volume_flavor):
        r"""Sets the volume_flavor of this ShowLinkFlavorsResponse.

        :param volume_flavor: The volume_flavor of this ShowLinkFlavorsResponse.
        :type volume_flavor: :class:`huaweicloudsdkdrs.v5.FlavorInfo`
        """
        self._volume_flavor = volume_flavor

    @property
    def flow_flavor(self):
        r"""Gets the flow_flavor of this ShowLinkFlavorsResponse.

        :return: The flow_flavor of this ShowLinkFlavorsResponse.
        :rtype: :class:`huaweicloudsdkdrs.v5.FlavorInfo`
        """
        return self._flow_flavor

    @flow_flavor.setter
    def flow_flavor(self, flow_flavor):
        r"""Sets the flow_flavor of this ShowLinkFlavorsResponse.

        :param flow_flavor: The flow_flavor of this ShowLinkFlavorsResponse.
        :type flow_flavor: :class:`huaweicloudsdkdrs.v5.FlavorInfo`
        """
        self._flow_flavor = flow_flavor

    def to_dict(self):
        import warnings
        warnings.warn("ShowLinkFlavorsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowLinkFlavorsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
