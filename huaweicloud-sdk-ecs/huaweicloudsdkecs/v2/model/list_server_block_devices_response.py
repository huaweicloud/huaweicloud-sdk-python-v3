# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServerBlockDevicesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attachable_quantity': 'BlockDeviceAttachableQuantity',
        'volume_attachments': 'list[ServerBlockDevice]'
    }

    attribute_map = {
        'attachable_quantity': 'attachableQuantity',
        'volume_attachments': 'volumeAttachments'
    }

    def __init__(self, attachable_quantity=None, volume_attachments=None):
        """ListServerBlockDevicesResponse

        The model defined in huaweicloud sdk

        :param attachable_quantity: 
        :type attachable_quantity: :class:`huaweicloudsdkecs.v2.BlockDeviceAttachableQuantity`
        :param volume_attachments: 云服务器挂载信息列表。
        :type volume_attachments: list[:class:`huaweicloudsdkecs.v2.ServerBlockDevice`]
        """
        
        super(ListServerBlockDevicesResponse, self).__init__()

        self._attachable_quantity = None
        self._volume_attachments = None
        self.discriminator = None

        if attachable_quantity is not None:
            self.attachable_quantity = attachable_quantity
        if volume_attachments is not None:
            self.volume_attachments = volume_attachments

    @property
    def attachable_quantity(self):
        """Gets the attachable_quantity of this ListServerBlockDevicesResponse.

        :return: The attachable_quantity of this ListServerBlockDevicesResponse.
        :rtype: :class:`huaweicloudsdkecs.v2.BlockDeviceAttachableQuantity`
        """
        return self._attachable_quantity

    @attachable_quantity.setter
    def attachable_quantity(self, attachable_quantity):
        """Sets the attachable_quantity of this ListServerBlockDevicesResponse.

        :param attachable_quantity: The attachable_quantity of this ListServerBlockDevicesResponse.
        :type attachable_quantity: :class:`huaweicloudsdkecs.v2.BlockDeviceAttachableQuantity`
        """
        self._attachable_quantity = attachable_quantity

    @property
    def volume_attachments(self):
        """Gets the volume_attachments of this ListServerBlockDevicesResponse.

        云服务器挂载信息列表。

        :return: The volume_attachments of this ListServerBlockDevicesResponse.
        :rtype: list[:class:`huaweicloudsdkecs.v2.ServerBlockDevice`]
        """
        return self._volume_attachments

    @volume_attachments.setter
    def volume_attachments(self, volume_attachments):
        """Sets the volume_attachments of this ListServerBlockDevicesResponse.

        云服务器挂载信息列表。

        :param volume_attachments: The volume_attachments of this ListServerBlockDevicesResponse.
        :type volume_attachments: list[:class:`huaweicloudsdkecs.v2.ServerBlockDevice`]
        """
        self._volume_attachments = volume_attachments

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
        if not isinstance(other, ListServerBlockDevicesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
