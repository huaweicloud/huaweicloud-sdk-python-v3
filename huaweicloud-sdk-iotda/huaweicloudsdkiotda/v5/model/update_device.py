# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        r"""UpdateDevice

        The model defined in huaweicloud sdk

        :param device_name: **参数说明**：设备名称。 **取值范围**：长度不超过256，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合，建议不少于4个字符。
        :type device_name: str
        :param description: **参数说明**：设备的描述信息。 **取值范围**：长度不超过2048，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合
        :type description: str
        :param extension_info: **参数说明**：设备扩展信息。用户可以自定义任何想要的扩展信息，修改子设备信息时不会下发给网关。
        :type extension_info: object
        :param auth_info: 
        :type auth_info: :class:`huaweicloudsdkiotda.v5.AuthInfoWithoutSecret`
        """
        
        

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
        r"""Gets the device_name of this UpdateDevice.

        **参数说明**：设备名称。 **取值范围**：长度不超过256，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合，建议不少于4个字符。

        :return: The device_name of this UpdateDevice.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        r"""Sets the device_name of this UpdateDevice.

        **参数说明**：设备名称。 **取值范围**：长度不超过256，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合，建议不少于4个字符。

        :param device_name: The device_name of this UpdateDevice.
        :type device_name: str
        """
        self._device_name = device_name

    @property
    def description(self):
        r"""Gets the description of this UpdateDevice.

        **参数说明**：设备的描述信息。 **取值范围**：长度不超过2048，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合

        :return: The description of this UpdateDevice.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateDevice.

        **参数说明**：设备的描述信息。 **取值范围**：长度不超过2048，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合

        :param description: The description of this UpdateDevice.
        :type description: str
        """
        self._description = description

    @property
    def extension_info(self):
        r"""Gets the extension_info of this UpdateDevice.

        **参数说明**：设备扩展信息。用户可以自定义任何想要的扩展信息，修改子设备信息时不会下发给网关。

        :return: The extension_info of this UpdateDevice.
        :rtype: object
        """
        return self._extension_info

    @extension_info.setter
    def extension_info(self, extension_info):
        r"""Sets the extension_info of this UpdateDevice.

        **参数说明**：设备扩展信息。用户可以自定义任何想要的扩展信息，修改子设备信息时不会下发给网关。

        :param extension_info: The extension_info of this UpdateDevice.
        :type extension_info: object
        """
        self._extension_info = extension_info

    @property
    def auth_info(self):
        r"""Gets the auth_info of this UpdateDevice.

        :return: The auth_info of this UpdateDevice.
        :rtype: :class:`huaweicloudsdkiotda.v5.AuthInfoWithoutSecret`
        """
        return self._auth_info

    @auth_info.setter
    def auth_info(self, auth_info):
        r"""Sets the auth_info of this UpdateDevice.

        :param auth_info: The auth_info of this UpdateDevice.
        :type auth_info: :class:`huaweicloudsdkiotda.v5.AuthInfoWithoutSecret`
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
        if not isinstance(other, UpdateDevice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
