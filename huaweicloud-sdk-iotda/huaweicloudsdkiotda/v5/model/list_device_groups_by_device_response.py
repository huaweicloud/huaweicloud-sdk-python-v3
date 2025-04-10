# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDeviceGroupsByDeviceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'device_groups': 'list[ListDeviceGroupSummary]'
    }

    attribute_map = {
        'device_groups': 'device_groups'
    }

    def __init__(self, device_groups=None):
        r"""ListDeviceGroupsByDeviceResponse

        The model defined in huaweicloud sdk

        :param device_groups: 设备组信息列表。
        :type device_groups: list[:class:`huaweicloudsdkiotda.v5.ListDeviceGroupSummary`]
        """
        
        super(ListDeviceGroupsByDeviceResponse, self).__init__()

        self._device_groups = None
        self.discriminator = None

        if device_groups is not None:
            self.device_groups = device_groups

    @property
    def device_groups(self):
        r"""Gets the device_groups of this ListDeviceGroupsByDeviceResponse.

        设备组信息列表。

        :return: The device_groups of this ListDeviceGroupsByDeviceResponse.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.ListDeviceGroupSummary`]
        """
        return self._device_groups

    @device_groups.setter
    def device_groups(self, device_groups):
        r"""Sets the device_groups of this ListDeviceGroupsByDeviceResponse.

        设备组信息列表。

        :param device_groups: The device_groups of this ListDeviceGroupsByDeviceResponse.
        :type device_groups: list[:class:`huaweicloudsdkiotda.v5.ListDeviceGroupSummary`]
        """
        self._device_groups = device_groups

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
        if not isinstance(other, ListDeviceGroupsByDeviceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
