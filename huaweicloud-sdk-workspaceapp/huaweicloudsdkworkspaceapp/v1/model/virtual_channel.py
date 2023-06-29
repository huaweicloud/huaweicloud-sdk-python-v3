# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VirtualChannel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'virtual_channel_control_enable': 'bool',
        'options': 'VirtualChannelOptions'
    }

    attribute_map = {
        'virtual_channel_control_enable': 'virtual_channel_control_enable',
        'options': 'options'
    }

    def __init__(self, virtual_channel_control_enable=None, options=None):
        """VirtualChannel

        The model defined in huaweicloud sdk

        :param virtual_channel_control_enable: 是否开启虚拟通道策略设置。取值为：false：表示关闭。true：表示开启。
        :type virtual_channel_control_enable: bool
        :param options: 
        :type options: :class:`huaweicloudsdkworkspaceapp.v1.VirtualChannelOptions`
        """
        
        

        self._virtual_channel_control_enable = None
        self._options = None
        self.discriminator = None

        if virtual_channel_control_enable is not None:
            self.virtual_channel_control_enable = virtual_channel_control_enable
        if options is not None:
            self.options = options

    @property
    def virtual_channel_control_enable(self):
        """Gets the virtual_channel_control_enable of this VirtualChannel.

        是否开启虚拟通道策略设置。取值为：false：表示关闭。true：表示开启。

        :return: The virtual_channel_control_enable of this VirtualChannel.
        :rtype: bool
        """
        return self._virtual_channel_control_enable

    @virtual_channel_control_enable.setter
    def virtual_channel_control_enable(self, virtual_channel_control_enable):
        """Sets the virtual_channel_control_enable of this VirtualChannel.

        是否开启虚拟通道策略设置。取值为：false：表示关闭。true：表示开启。

        :param virtual_channel_control_enable: The virtual_channel_control_enable of this VirtualChannel.
        :type virtual_channel_control_enable: bool
        """
        self._virtual_channel_control_enable = virtual_channel_control_enable

    @property
    def options(self):
        """Gets the options of this VirtualChannel.

        :return: The options of this VirtualChannel.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.VirtualChannelOptions`
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this VirtualChannel.

        :param options: The options of this VirtualChannel.
        :type options: :class:`huaweicloudsdkworkspaceapp.v1.VirtualChannelOptions`
        """
        self._options = options

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
        if not isinstance(other, VirtualChannel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
