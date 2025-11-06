# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNetworkDevicesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'network_devices': 'list[NetworkDevice]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'network_devices': 'network_devices',
        'page_info': 'page_info'
    }

    def __init__(self, network_devices=None, page_info=None):
        r"""ListNetworkDevicesResponse

        The model defined in huaweicloud sdk

        :param network_devices: 网络设备列表
        :type network_devices: list[:class:`huaweicloudsdkcloudpond.v2.NetworkDevice`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkcloudpond.v2.PageInfo`
        """
        
        super().__init__()

        self._network_devices = None
        self._page_info = None
        self.discriminator = None

        if network_devices is not None:
            self.network_devices = network_devices
        if page_info is not None:
            self.page_info = page_info

    @property
    def network_devices(self):
        r"""Gets the network_devices of this ListNetworkDevicesResponse.

        网络设备列表

        :return: The network_devices of this ListNetworkDevicesResponse.
        :rtype: list[:class:`huaweicloudsdkcloudpond.v2.NetworkDevice`]
        """
        return self._network_devices

    @network_devices.setter
    def network_devices(self, network_devices):
        r"""Sets the network_devices of this ListNetworkDevicesResponse.

        网络设备列表

        :param network_devices: The network_devices of this ListNetworkDevicesResponse.
        :type network_devices: list[:class:`huaweicloudsdkcloudpond.v2.NetworkDevice`]
        """
        self._network_devices = network_devices

    @property
    def page_info(self):
        r"""Gets the page_info of this ListNetworkDevicesResponse.

        :return: The page_info of this ListNetworkDevicesResponse.
        :rtype: :class:`huaweicloudsdkcloudpond.v2.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListNetworkDevicesResponse.

        :param page_info: The page_info of this ListNetworkDevicesResponse.
        :type page_info: :class:`huaweicloudsdkcloudpond.v2.PageInfo`
        """
        self._page_info = page_info

    def to_dict(self):
        import warnings
        warnings.warn("ListNetworkDevicesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListNetworkDevicesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
