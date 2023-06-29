# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VirtualChannelOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'custom_virtual_channel_name': 'str',
        'virtual_channel_plugin_details': 'str',
        'third_party_plugin_name': 'str'
    }

    attribute_map = {
        'custom_virtual_channel_name': 'custom_virtual_channel_name',
        'virtual_channel_plugin_details': 'virtual_channel_plugin_details',
        'third_party_plugin_name': 'third_party_plugin_name'
    }

    def __init__(self, custom_virtual_channel_name=None, virtual_channel_plugin_details=None, third_party_plugin_name=None):
        """VirtualChannelOptions

        The model defined in huaweicloud sdk

        :param custom_virtual_channel_name: 自定义虚拟通道注册名。
        :type custom_virtual_channel_name: str
        :param virtual_channel_plugin_details: 虚拟通道下载配置信息，需Base64加密。
        :type virtual_channel_plugin_details: str
        :param third_party_plugin_name: 第三方插件名称。
        :type third_party_plugin_name: str
        """
        
        

        self._custom_virtual_channel_name = None
        self._virtual_channel_plugin_details = None
        self._third_party_plugin_name = None
        self.discriminator = None

        if custom_virtual_channel_name is not None:
            self.custom_virtual_channel_name = custom_virtual_channel_name
        if virtual_channel_plugin_details is not None:
            self.virtual_channel_plugin_details = virtual_channel_plugin_details
        if third_party_plugin_name is not None:
            self.third_party_plugin_name = third_party_plugin_name

    @property
    def custom_virtual_channel_name(self):
        """Gets the custom_virtual_channel_name of this VirtualChannelOptions.

        自定义虚拟通道注册名。

        :return: The custom_virtual_channel_name of this VirtualChannelOptions.
        :rtype: str
        """
        return self._custom_virtual_channel_name

    @custom_virtual_channel_name.setter
    def custom_virtual_channel_name(self, custom_virtual_channel_name):
        """Sets the custom_virtual_channel_name of this VirtualChannelOptions.

        自定义虚拟通道注册名。

        :param custom_virtual_channel_name: The custom_virtual_channel_name of this VirtualChannelOptions.
        :type custom_virtual_channel_name: str
        """
        self._custom_virtual_channel_name = custom_virtual_channel_name

    @property
    def virtual_channel_plugin_details(self):
        """Gets the virtual_channel_plugin_details of this VirtualChannelOptions.

        虚拟通道下载配置信息，需Base64加密。

        :return: The virtual_channel_plugin_details of this VirtualChannelOptions.
        :rtype: str
        """
        return self._virtual_channel_plugin_details

    @virtual_channel_plugin_details.setter
    def virtual_channel_plugin_details(self, virtual_channel_plugin_details):
        """Sets the virtual_channel_plugin_details of this VirtualChannelOptions.

        虚拟通道下载配置信息，需Base64加密。

        :param virtual_channel_plugin_details: The virtual_channel_plugin_details of this VirtualChannelOptions.
        :type virtual_channel_plugin_details: str
        """
        self._virtual_channel_plugin_details = virtual_channel_plugin_details

    @property
    def third_party_plugin_name(self):
        """Gets the third_party_plugin_name of this VirtualChannelOptions.

        第三方插件名称。

        :return: The third_party_plugin_name of this VirtualChannelOptions.
        :rtype: str
        """
        return self._third_party_plugin_name

    @third_party_plugin_name.setter
    def third_party_plugin_name(self, third_party_plugin_name):
        """Sets the third_party_plugin_name of this VirtualChannelOptions.

        第三方插件名称。

        :param third_party_plugin_name: The third_party_plugin_name of this VirtualChannelOptions.
        :type third_party_plugin_name: str
        """
        self._third_party_plugin_name = third_party_plugin_name

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
        if not isinstance(other, VirtualChannelOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
