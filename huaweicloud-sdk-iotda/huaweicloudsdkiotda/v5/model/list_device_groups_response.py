# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


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
        """ListDeviceGroupsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

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
        :rtype: list[DeviceGroupResponseDTO]
        """
        return self._device_groups

    @device_groups.setter
    def device_groups(self, device_groups):
        """Sets the device_groups of this ListDeviceGroupsResponse.

        设备组信息列表。

        :param device_groups: The device_groups of this ListDeviceGroupsResponse.
        :type: list[DeviceGroupResponseDTO]
        """
        self._device_groups = device_groups

    @property
    def page(self):
        """Gets the page of this ListDeviceGroupsResponse.


        :return: The page of this ListDeviceGroupsResponse.
        :rtype: Page
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListDeviceGroupsResponse.


        :param page: The page of this ListDeviceGroupsResponse.
        :type: Page
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListDeviceGroupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
