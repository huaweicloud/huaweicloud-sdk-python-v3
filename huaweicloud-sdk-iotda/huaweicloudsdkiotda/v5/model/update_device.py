# coding: utf-8

import pprint
import re

import six





class UpdateDevice:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'device_name': 'str',
        'description': 'str',
        'extension_info': 'object',
        'auth_info': 'AuthInfoWithoutSecret'
    }

    attribute_map = {
        'device_name': 'device_name',
        'description': 'description',
        'extension_info': 'extension_info',
        'auth_info': 'auth_info'
    }

    def __init__(self, device_name=None, description=None, extension_info=None, auth_info=None):
        """UpdateDevice - a model defined in huaweicloud sdk"""
        
        

        self._device_name = None
        self._description = None
        self._extension_info = None
        self._auth_info = None
        self.discriminator = None

        if device_name is not None:
            self.device_name = device_name
        if description is not None:
            self.description = description
        if extension_info is not None:
            self.extension_info = extension_info
        if auth_info is not None:
            self.auth_info = auth_info

    @property
    def device_name(self):
        """Gets the device_name of this UpdateDevice.

        设备名称。

        :return: The device_name of this UpdateDevice.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this UpdateDevice.

        设备名称。

        :param device_name: The device_name of this UpdateDevice.
        :type: str
        """
        self._device_name = device_name

    @property
    def description(self):
        """Gets the description of this UpdateDevice.

        设备的描述信息。

        :return: The description of this UpdateDevice.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateDevice.

        设备的描述信息。

        :param description: The description of this UpdateDevice.
        :type: str
        """
        self._description = description

    @property
    def extension_info(self):
        """Gets the extension_info of this UpdateDevice.

        设备扩展信息。用户可以自定义任何想要的扩展信息，修改子设备信息时不会下发给网关。

        :return: The extension_info of this UpdateDevice.
        :rtype: object
        """
        return self._extension_info

    @extension_info.setter
    def extension_info(self, extension_info):
        """Sets the extension_info of this UpdateDevice.

        设备扩展信息。用户可以自定义任何想要的扩展信息，修改子设备信息时不会下发给网关。

        :param extension_info: The extension_info of this UpdateDevice.
        :type: object
        """
        self._extension_info = extension_info

    @property
    def auth_info(self):
        """Gets the auth_info of this UpdateDevice.


        :return: The auth_info of this UpdateDevice.
        :rtype: AuthInfoWithoutSecret
        """
        return self._auth_info

    @auth_info.setter
    def auth_info(self, auth_info):
        """Sets the auth_info of this UpdateDevice.


        :param auth_info: The auth_info of this UpdateDevice.
        :type: AuthInfoWithoutSecret
        """
        self._auth_info = auth_info

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
        if not isinstance(other, UpdateDevice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
