# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDeviceGroupsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'device_groups': 'list[DeviceGroupResponseDTO]',
        'page': 'Page'
    }

    attribute_map = {
        'device_groups': 'device_groups',
        'page': 'page'
    }

    def __init__(self, device_groups=None, page=None):
        """ListDeviceGroupsResponse

        The model defined in huaweicloud sdk

        :param device_groups: 设备组信息列表。
        :type device_groups: list[:class:`huaweicloudsdkiotda.v5.DeviceGroupResponseDTO`]
        :param page: 
        :type page: :class:`huaweicloudsdkiotda.v5.Page`
        """
        
        super(ListDeviceGroupsResponse, self).__init__()

        self._device_groups = None
        self._page = None
        self.discriminator = None

        if device_groups is not None:
            self.device_groups = device_groups
        if page is not None:
            self.page = page

    @property
    def device_groups(self):
        """Gets the device_groups of this ListDeviceGroupsResponse.

        设备组信息列表。

        :return: The device_groups of this ListDeviceGroupsResponse.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.DeviceGroupResponseDTO`]
        """
        return self._device_groups

    @device_groups.setter
    def device_groups(self, device_groups):
        """Sets the device_groups of this ListDeviceGroupsResponse.

        设备组信息列表。

        :param device_groups: The device_groups of this ListDeviceGroupsResponse.
        :type device_groups: list[:class:`huaweicloudsdkiotda.v5.DeviceGroupResponseDTO`]
        """
        self._device_groups = device_groups

    @property
    def page(self):
        """Gets the page of this ListDeviceGroupsResponse.

        :return: The page of this ListDeviceGroupsResponse.
        :rtype: :class:`huaweicloudsdkiotda.v5.Page`
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListDeviceGroupsResponse.

        :param page: The page of this ListDeviceGroupsResponse.
        :type page: :class:`huaweicloudsdkiotda.v5.Page`
        """
        self._page = page

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
        if not isinstance(other, ListDeviceGroupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
