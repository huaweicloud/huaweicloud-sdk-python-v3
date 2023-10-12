# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UsbPortRedirectionOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'usb_image_enable': 'bool',
        'usb_video_enable': 'bool',
        'usb_printer_enable': 'bool',
        'usb_storage_enable': 'bool',
        'wireless_devices_enable': 'bool',
        'network_devices_enable': 'bool',
        'usb_smart_card_enable': 'bool',
        'other_usb_devices_enable': 'bool',
        'usb_redirection_customization_policy': 'str',
        'usb_redirection_mode': 'str'
    }

    attribute_map = {
        'usb_image_enable': 'usb_image_enable',
        'usb_video_enable': 'usb_video_enable',
        'usb_printer_enable': 'usb_printer_enable',
        'usb_storage_enable': 'usb_storage_enable',
        'wireless_devices_enable': 'wireless_devices_enable',
        'network_devices_enable': 'network_devices_enable',
        'usb_smart_card_enable': 'usb_smart_card_enable',
        'other_usb_devices_enable': 'other_usb_devices_enable',
        'usb_redirection_customization_policy': 'usb_redirection_customization_policy',
        'usb_redirection_mode': 'usb_redirection_mode'
    }

    def __init__(self, usb_image_enable=None, usb_video_enable=None, usb_printer_enable=None, usb_storage_enable=None, wireless_devices_enable=None, network_devices_enable=None, usb_smart_card_enable=None, other_usb_devices_enable=None, usb_redirection_customization_policy=None, usb_redirection_mode=None):
        """UsbPortRedirectionOptions

        The model defined in huaweicloud sdk

        :param usb_image_enable: 是否开启图像设备（如: 扫描仪）。取值为： - false：表示关闭。 - true：表示开启。
        :type usb_image_enable: bool
        :param usb_video_enable: 是否开启视频设备（如: 摄像头）。取值为： - false：表示关闭。 - true：表示开启。
        :type usb_video_enable: bool
        :param usb_printer_enable: 是否开启打印设备（如: 打印机）。取值为： - false：表示关闭。 - true：表示开启。
        :type usb_printer_enable: bool
        :param usb_storage_enable: 是否开启存储设备（如: U盘）。取值为： - false：表示关闭。 - true：表示开启。
        :type usb_storage_enable: bool
        :param wireless_devices_enable: 是否开启无线设备（如：蓝牙）。取值为： - false：表示关闭。 - true：表示开启。
        :type wireless_devices_enable: bool
        :param network_devices_enable: 是否开启网路设备（如：无线网卡）。取值为： - false：表示关闭。 - true：表示开启。
        :type network_devices_enable: bool
        :param usb_smart_card_enable: 是否开启智能卡设备（如：Ukey）。取值为： - false：表示关闭。 - true：表示开启。
        :type usb_smart_card_enable: bool
        :param other_usb_devices_enable: 是否开启其他USB设备重定向。取值为： - false：表示关闭。 - true：表示开启。
        :type other_usb_devices_enable: bool
        :param usb_redirection_customization_policy: USB端口重定向自定义策略。
        :type usb_redirection_customization_policy: str
        :param usb_redirection_mode: USB 重定向模式。取值为： - Classical mode：经典模式。 - Common mode：通用模式。
        :type usb_redirection_mode: str
        """
        
        

        self._usb_image_enable = None
        self._usb_video_enable = None
        self._usb_printer_enable = None
        self._usb_storage_enable = None
        self._wireless_devices_enable = None
        self._network_devices_enable = None
        self._usb_smart_card_enable = None
        self._other_usb_devices_enable = None
        self._usb_redirection_customization_policy = None
        self._usb_redirection_mode = None
        self.discriminator = None

        if usb_image_enable is not None:
            self.usb_image_enable = usb_image_enable
        if usb_video_enable is not None:
            self.usb_video_enable = usb_video_enable
        if usb_printer_enable is not None:
            self.usb_printer_enable = usb_printer_enable
        if usb_storage_enable is not None:
            self.usb_storage_enable = usb_storage_enable
        if wireless_devices_enable is not None:
            self.wireless_devices_enable = wireless_devices_enable
        if network_devices_enable is not None:
            self.network_devices_enable = network_devices_enable
        if usb_smart_card_enable is not None:
            self.usb_smart_card_enable = usb_smart_card_enable
        if other_usb_devices_enable is not None:
            self.other_usb_devices_enable = other_usb_devices_enable
        if usb_redirection_customization_policy is not None:
            self.usb_redirection_customization_policy = usb_redirection_customization_policy
        if usb_redirection_mode is not None:
            self.usb_redirection_mode = usb_redirection_mode

    @property
    def usb_image_enable(self):
        """Gets the usb_image_enable of this UsbPortRedirectionOptions.

        是否开启图像设备（如: 扫描仪）。取值为： - false：表示关闭。 - true：表示开启。

        :return: The usb_image_enable of this UsbPortRedirectionOptions.
        :rtype: bool
        """
        return self._usb_image_enable

    @usb_image_enable.setter
    def usb_image_enable(self, usb_image_enable):
        """Sets the usb_image_enable of this UsbPortRedirectionOptions.

        是否开启图像设备（如: 扫描仪）。取值为： - false：表示关闭。 - true：表示开启。

        :param usb_image_enable: The usb_image_enable of this UsbPortRedirectionOptions.
        :type usb_image_enable: bool
        """
        self._usb_image_enable = usb_image_enable

    @property
    def usb_video_enable(self):
        """Gets the usb_video_enable of this UsbPortRedirectionOptions.

        是否开启视频设备（如: 摄像头）。取值为： - false：表示关闭。 - true：表示开启。

        :return: The usb_video_enable of this UsbPortRedirectionOptions.
        :rtype: bool
        """
        return self._usb_video_enable

    @usb_video_enable.setter
    def usb_video_enable(self, usb_video_enable):
        """Sets the usb_video_enable of this UsbPortRedirectionOptions.

        是否开启视频设备（如: 摄像头）。取值为： - false：表示关闭。 - true：表示开启。

        :param usb_video_enable: The usb_video_enable of this UsbPortRedirectionOptions.
        :type usb_video_enable: bool
        """
        self._usb_video_enable = usb_video_enable

    @property
    def usb_printer_enable(self):
        """Gets the usb_printer_enable of this UsbPortRedirectionOptions.

        是否开启打印设备（如: 打印机）。取值为： - false：表示关闭。 - true：表示开启。

        :return: The usb_printer_enable of this UsbPortRedirectionOptions.
        :rtype: bool
        """
        return self._usb_printer_enable

    @usb_printer_enable.setter
    def usb_printer_enable(self, usb_printer_enable):
        """Sets the usb_printer_enable of this UsbPortRedirectionOptions.

        是否开启打印设备（如: 打印机）。取值为： - false：表示关闭。 - true：表示开启。

        :param usb_printer_enable: The usb_printer_enable of this UsbPortRedirectionOptions.
        :type usb_printer_enable: bool
        """
        self._usb_printer_enable = usb_printer_enable

    @property
    def usb_storage_enable(self):
        """Gets the usb_storage_enable of this UsbPortRedirectionOptions.

        是否开启存储设备（如: U盘）。取值为： - false：表示关闭。 - true：表示开启。

        :return: The usb_storage_enable of this UsbPortRedirectionOptions.
        :rtype: bool
        """
        return self._usb_storage_enable

    @usb_storage_enable.setter
    def usb_storage_enable(self, usb_storage_enable):
        """Sets the usb_storage_enable of this UsbPortRedirectionOptions.

        是否开启存储设备（如: U盘）。取值为： - false：表示关闭。 - true：表示开启。

        :param usb_storage_enable: The usb_storage_enable of this UsbPortRedirectionOptions.
        :type usb_storage_enable: bool
        """
        self._usb_storage_enable = usb_storage_enable

    @property
    def wireless_devices_enable(self):
        """Gets the wireless_devices_enable of this UsbPortRedirectionOptions.

        是否开启无线设备（如：蓝牙）。取值为： - false：表示关闭。 - true：表示开启。

        :return: The wireless_devices_enable of this UsbPortRedirectionOptions.
        :rtype: bool
        """
        return self._wireless_devices_enable

    @wireless_devices_enable.setter
    def wireless_devices_enable(self, wireless_devices_enable):
        """Sets the wireless_devices_enable of this UsbPortRedirectionOptions.

        是否开启无线设备（如：蓝牙）。取值为： - false：表示关闭。 - true：表示开启。

        :param wireless_devices_enable: The wireless_devices_enable of this UsbPortRedirectionOptions.
        :type wireless_devices_enable: bool
        """
        self._wireless_devices_enable = wireless_devices_enable

    @property
    def network_devices_enable(self):
        """Gets the network_devices_enable of this UsbPortRedirectionOptions.

        是否开启网路设备（如：无线网卡）。取值为： - false：表示关闭。 - true：表示开启。

        :return: The network_devices_enable of this UsbPortRedirectionOptions.
        :rtype: bool
        """
        return self._network_devices_enable

    @network_devices_enable.setter
    def network_devices_enable(self, network_devices_enable):
        """Sets the network_devices_enable of this UsbPortRedirectionOptions.

        是否开启网路设备（如：无线网卡）。取值为： - false：表示关闭。 - true：表示开启。

        :param network_devices_enable: The network_devices_enable of this UsbPortRedirectionOptions.
        :type network_devices_enable: bool
        """
        self._network_devices_enable = network_devices_enable

    @property
    def usb_smart_card_enable(self):
        """Gets the usb_smart_card_enable of this UsbPortRedirectionOptions.

        是否开启智能卡设备（如：Ukey）。取值为： - false：表示关闭。 - true：表示开启。

        :return: The usb_smart_card_enable of this UsbPortRedirectionOptions.
        :rtype: bool
        """
        return self._usb_smart_card_enable

    @usb_smart_card_enable.setter
    def usb_smart_card_enable(self, usb_smart_card_enable):
        """Sets the usb_smart_card_enable of this UsbPortRedirectionOptions.

        是否开启智能卡设备（如：Ukey）。取值为： - false：表示关闭。 - true：表示开启。

        :param usb_smart_card_enable: The usb_smart_card_enable of this UsbPortRedirectionOptions.
        :type usb_smart_card_enable: bool
        """
        self._usb_smart_card_enable = usb_smart_card_enable

    @property
    def other_usb_devices_enable(self):
        """Gets the other_usb_devices_enable of this UsbPortRedirectionOptions.

        是否开启其他USB设备重定向。取值为： - false：表示关闭。 - true：表示开启。

        :return: The other_usb_devices_enable of this UsbPortRedirectionOptions.
        :rtype: bool
        """
        return self._other_usb_devices_enable

    @other_usb_devices_enable.setter
    def other_usb_devices_enable(self, other_usb_devices_enable):
        """Sets the other_usb_devices_enable of this UsbPortRedirectionOptions.

        是否开启其他USB设备重定向。取值为： - false：表示关闭。 - true：表示开启。

        :param other_usb_devices_enable: The other_usb_devices_enable of this UsbPortRedirectionOptions.
        :type other_usb_devices_enable: bool
        """
        self._other_usb_devices_enable = other_usb_devices_enable

    @property
    def usb_redirection_customization_policy(self):
        """Gets the usb_redirection_customization_policy of this UsbPortRedirectionOptions.

        USB端口重定向自定义策略。

        :return: The usb_redirection_customization_policy of this UsbPortRedirectionOptions.
        :rtype: str
        """
        return self._usb_redirection_customization_policy

    @usb_redirection_customization_policy.setter
    def usb_redirection_customization_policy(self, usb_redirection_customization_policy):
        """Sets the usb_redirection_customization_policy of this UsbPortRedirectionOptions.

        USB端口重定向自定义策略。

        :param usb_redirection_customization_policy: The usb_redirection_customization_policy of this UsbPortRedirectionOptions.
        :type usb_redirection_customization_policy: str
        """
        self._usb_redirection_customization_policy = usb_redirection_customization_policy

    @property
    def usb_redirection_mode(self):
        """Gets the usb_redirection_mode of this UsbPortRedirectionOptions.

        USB 重定向模式。取值为： - Classical mode：经典模式。 - Common mode：通用模式。

        :return: The usb_redirection_mode of this UsbPortRedirectionOptions.
        :rtype: str
        """
        return self._usb_redirection_mode

    @usb_redirection_mode.setter
    def usb_redirection_mode(self, usb_redirection_mode):
        """Sets the usb_redirection_mode of this UsbPortRedirectionOptions.

        USB 重定向模式。取值为： - Classical mode：经典模式。 - Common mode：通用模式。

        :param usb_redirection_mode: The usb_redirection_mode of this UsbPortRedirectionOptions.
        :type usb_redirection_mode: str
        """
        self._usb_redirection_mode = usb_redirection_mode

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
        if not isinstance(other, UsbPortRedirectionOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
