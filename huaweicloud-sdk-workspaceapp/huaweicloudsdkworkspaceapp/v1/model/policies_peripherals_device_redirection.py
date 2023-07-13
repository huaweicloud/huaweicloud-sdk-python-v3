# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesPeripheralsDeviceRedirection:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'printer_redirection': 'PoliciesPeripheralsDeviceRedirectionPrinterRedirection',
        'session_printer': 'PoliciesPeripheralsDeviceRedirectionSessionPrinter',
        'camera_redirection': 'PoliciesPeripheralsDeviceRedirectionCameraRedirection',
        'twain_redirection_enable': 'bool',
        'image_compression_level': 'str'
    }

    attribute_map = {
        'printer_redirection': 'printer_redirection',
        'session_printer': 'session_printer',
        'camera_redirection': 'camera_redirection',
        'twain_redirection_enable': 'twain_redirection_enable',
        'image_compression_level': 'image_compression_level'
    }

    def __init__(self, printer_redirection=None, session_printer=None, camera_redirection=None, twain_redirection_enable=None, image_compression_level=None):
        """PoliciesPeripheralsDeviceRedirection

        The model defined in huaweicloud sdk

        :param printer_redirection: 
        :type printer_redirection: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesPeripheralsDeviceRedirectionPrinterRedirection`
        :param session_printer: 
        :type session_printer: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesPeripheralsDeviceRedirectionSessionPrinter`
        :param camera_redirection: 
        :type camera_redirection: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesPeripheralsDeviceRedirectionCameraRedirection`
        :param twain_redirection_enable: 是否开启TWAIN设备重定向。取值为： false：表示关闭。 true：表示开启。
        :type twain_redirection_enable: bool
        :param image_compression_level: 图形压缩级别。取值为： - 不压缩：none。 - 低（速度最快）：low。 - 中（速度适中）：medium。 - 高（速度最慢）：high。 - 无损（无损压缩）：lossless。 - 低损（低损压缩）：low-loss。 - 中损（中损压缩）：medium-loss。 - 高损（高损压缩）：high-loss。
        :type image_compression_level: str
        """
        
        

        self._printer_redirection = None
        self._session_printer = None
        self._camera_redirection = None
        self._twain_redirection_enable = None
        self._image_compression_level = None
        self.discriminator = None

        if printer_redirection is not None:
            self.printer_redirection = printer_redirection
        if session_printer is not None:
            self.session_printer = session_printer
        if camera_redirection is not None:
            self.camera_redirection = camera_redirection
        if twain_redirection_enable is not None:
            self.twain_redirection_enable = twain_redirection_enable
        if image_compression_level is not None:
            self.image_compression_level = image_compression_level

    @property
    def printer_redirection(self):
        """Gets the printer_redirection of this PoliciesPeripheralsDeviceRedirection.

        :return: The printer_redirection of this PoliciesPeripheralsDeviceRedirection.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesPeripheralsDeviceRedirectionPrinterRedirection`
        """
        return self._printer_redirection

    @printer_redirection.setter
    def printer_redirection(self, printer_redirection):
        """Sets the printer_redirection of this PoliciesPeripheralsDeviceRedirection.

        :param printer_redirection: The printer_redirection of this PoliciesPeripheralsDeviceRedirection.
        :type printer_redirection: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesPeripheralsDeviceRedirectionPrinterRedirection`
        """
        self._printer_redirection = printer_redirection

    @property
    def session_printer(self):
        """Gets the session_printer of this PoliciesPeripheralsDeviceRedirection.

        :return: The session_printer of this PoliciesPeripheralsDeviceRedirection.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesPeripheralsDeviceRedirectionSessionPrinter`
        """
        return self._session_printer

    @session_printer.setter
    def session_printer(self, session_printer):
        """Sets the session_printer of this PoliciesPeripheralsDeviceRedirection.

        :param session_printer: The session_printer of this PoliciesPeripheralsDeviceRedirection.
        :type session_printer: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesPeripheralsDeviceRedirectionSessionPrinter`
        """
        self._session_printer = session_printer

    @property
    def camera_redirection(self):
        """Gets the camera_redirection of this PoliciesPeripheralsDeviceRedirection.

        :return: The camera_redirection of this PoliciesPeripheralsDeviceRedirection.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesPeripheralsDeviceRedirectionCameraRedirection`
        """
        return self._camera_redirection

    @camera_redirection.setter
    def camera_redirection(self, camera_redirection):
        """Sets the camera_redirection of this PoliciesPeripheralsDeviceRedirection.

        :param camera_redirection: The camera_redirection of this PoliciesPeripheralsDeviceRedirection.
        :type camera_redirection: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesPeripheralsDeviceRedirectionCameraRedirection`
        """
        self._camera_redirection = camera_redirection

    @property
    def twain_redirection_enable(self):
        """Gets the twain_redirection_enable of this PoliciesPeripheralsDeviceRedirection.

        是否开启TWAIN设备重定向。取值为： false：表示关闭。 true：表示开启。

        :return: The twain_redirection_enable of this PoliciesPeripheralsDeviceRedirection.
        :rtype: bool
        """
        return self._twain_redirection_enable

    @twain_redirection_enable.setter
    def twain_redirection_enable(self, twain_redirection_enable):
        """Sets the twain_redirection_enable of this PoliciesPeripheralsDeviceRedirection.

        是否开启TWAIN设备重定向。取值为： false：表示关闭。 true：表示开启。

        :param twain_redirection_enable: The twain_redirection_enable of this PoliciesPeripheralsDeviceRedirection.
        :type twain_redirection_enable: bool
        """
        self._twain_redirection_enable = twain_redirection_enable

    @property
    def image_compression_level(self):
        """Gets the image_compression_level of this PoliciesPeripheralsDeviceRedirection.

        图形压缩级别。取值为： - 不压缩：none。 - 低（速度最快）：low。 - 中（速度适中）：medium。 - 高（速度最慢）：high。 - 无损（无损压缩）：lossless。 - 低损（低损压缩）：low-loss。 - 中损（中损压缩）：medium-loss。 - 高损（高损压缩）：high-loss。

        :return: The image_compression_level of this PoliciesPeripheralsDeviceRedirection.
        :rtype: str
        """
        return self._image_compression_level

    @image_compression_level.setter
    def image_compression_level(self, image_compression_level):
        """Sets the image_compression_level of this PoliciesPeripheralsDeviceRedirection.

        图形压缩级别。取值为： - 不压缩：none。 - 低（速度最快）：low。 - 中（速度适中）：medium。 - 高（速度最慢）：high。 - 无损（无损压缩）：lossless。 - 低损（低损压缩）：low-loss。 - 中损（中损压缩）：medium-loss。 - 高损（高损压缩）：high-loss。

        :param image_compression_level: The image_compression_level of this PoliciesPeripheralsDeviceRedirection.
        :type image_compression_level: str
        """
        self._image_compression_level = image_compression_level

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
        if not isinstance(other, PoliciesPeripheralsDeviceRedirection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
