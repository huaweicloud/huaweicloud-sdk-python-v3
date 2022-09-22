# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublishDeviceResponseDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'device_user_id': 'str',
        'device_name': 'str'
    }

    attribute_map = {
        'device_user_id': 'deviceUserId',
        'device_name': 'deviceName'
    }

    def __init__(self, device_user_id=None, device_name=None):
        """PublishDeviceResponseDTO

        The model defined in huaweicloud sdk

        :param device_user_id: 设备用户ID。
        :type device_user_id: str
        :param device_name: 设备名称。
        :type device_name: str
        """
        
        

        self._device_user_id = None
        self._device_name = None
        self.discriminator = None

        if device_user_id is not None:
            self.device_user_id = device_user_id
        if device_name is not None:
            self.device_name = device_name

    @property
    def device_user_id(self):
        """Gets the device_user_id of this PublishDeviceResponseDTO.

        设备用户ID。

        :return: The device_user_id of this PublishDeviceResponseDTO.
        :rtype: str
        """
        return self._device_user_id

    @device_user_id.setter
    def device_user_id(self, device_user_id):
        """Sets the device_user_id of this PublishDeviceResponseDTO.

        设备用户ID。

        :param device_user_id: The device_user_id of this PublishDeviceResponseDTO.
        :type device_user_id: str
        """
        self._device_user_id = device_user_id

    @property
    def device_name(self):
        """Gets the device_name of this PublishDeviceResponseDTO.

        设备名称。

        :return: The device_name of this PublishDeviceResponseDTO.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this PublishDeviceResponseDTO.

        设备名称。

        :param device_name: The device_name of this PublishDeviceResponseDTO.
        :type device_name: str
        """
        self._device_name = device_name

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
        if not isinstance(other, PublishDeviceResponseDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
