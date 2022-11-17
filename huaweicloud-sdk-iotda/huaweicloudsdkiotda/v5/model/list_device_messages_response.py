# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDeviceMessagesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'device_id': 'str',
        'messages': 'list[DeviceMessage]'
    }

    attribute_map = {
        'device_id': 'device_id',
        'messages': 'messages'
    }

    def __init__(self, device_id=None, messages=None):
        """ListDeviceMessagesResponse

        The model defined in huaweicloud sdk

        :param device_id: 设备ID，用于唯一标识一个设备，在注册设备时由物联网平台分配获得。
        :type device_id: str
        :param messages: 设备消息列表。
        :type messages: list[:class:`huaweicloudsdkiotda.v5.DeviceMessage`]
        """
        
        super(ListDeviceMessagesResponse, self).__init__()

        self._device_id = None
        self._messages = None
        self.discriminator = None

        if device_id is not None:
            self.device_id = device_id
        if messages is not None:
            self.messages = messages

    @property
    def device_id(self):
        """Gets the device_id of this ListDeviceMessagesResponse.

        设备ID，用于唯一标识一个设备，在注册设备时由物联网平台分配获得。

        :return: The device_id of this ListDeviceMessagesResponse.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this ListDeviceMessagesResponse.

        设备ID，用于唯一标识一个设备，在注册设备时由物联网平台分配获得。

        :param device_id: The device_id of this ListDeviceMessagesResponse.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def messages(self):
        """Gets the messages of this ListDeviceMessagesResponse.

        设备消息列表。

        :return: The messages of this ListDeviceMessagesResponse.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.DeviceMessage`]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this ListDeviceMessagesResponse.

        设备消息列表。

        :param messages: The messages of this ListDeviceMessagesResponse.
        :type messages: list[:class:`huaweicloudsdkiotda.v5.DeviceMessage`]
        """
        self._messages = messages

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
        if not isinstance(other, ListDeviceMessagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
