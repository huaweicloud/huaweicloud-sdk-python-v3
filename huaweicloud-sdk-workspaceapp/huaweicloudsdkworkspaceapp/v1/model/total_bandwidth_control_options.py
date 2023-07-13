# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TotalBandwidthControlOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_bandwidth_control_value': 'int',
        'display_bandwidth_percentage_enable': 'bool',
        'display_bandwidth_percentage_options': 'DisplayBandwidthPercentageOptions',
        'multimedia_bandwidth_percentage_enable': 'bool',
        'multimedia_bandwidth_percentage_options': 'MultimediaBandwidthPercentageOptions',
        'usb_bandwidth_percentage_enable': 'bool',
        'usb_bandwidth_percentage_options': 'UsbBandwidthPercentageOptions',
        'pcsc_bandwidth_percentage_enable': 'bool',
        'pcsc_bandwidth_percentage_options': 'PcscBandwidthPercentageOptions',
        'twain_bandwidth_percentage_enable': 'bool',
        'twain_bandwidth_percentage_options': 'TwainBandwidthPercentageOptions',
        'printer_bandwidth_percentage_enable': 'bool',
        'printer_bandwidth_percentage_options': 'PrinterBandwidthPercentageOptions',
        'com_bandwidth_percentage_enable': 'bool',
        'com_bandwidth_percentage_options': 'ComBandwidthPercentageOptions',
        'file_redirection_bandwidth_percentage_enable': 'bool',
        'file_redirection_bandwidth_percentage_options': 'FileRedirectionBandwidthPercentageOptions',
        'clipboard_bandwidth_percentage_enable': 'bool',
        'clipboard_bandwidth_percentage_options': 'ClipboardBandwidthPercentageOptions',
        'secure_channel_bandwidth_percentage_enable': 'bool',
        'secure_channel_bandwidth_percentage_options': 'SecureChannelBandwidthPercentageOptions',
        'camera_bandwidth_percentage_enable': 'bool',
        'camera_bandwidth_percentage_options': 'CameraBandwidthPercentageOptions',
        'virtual_channel_bandwidth_percentage_enable': 'bool',
        'virtual_channel_bandwidth_percentage_options': 'VirtualChannelBandwidthPercentageOptions'
    }

    attribute_map = {
        'total_bandwidth_control_value': 'total_bandwidth_control_value',
        'display_bandwidth_percentage_enable': 'display_bandwidth_percentage_enable',
        'display_bandwidth_percentage_options': 'display_bandwidth_percentage_options',
        'multimedia_bandwidth_percentage_enable': 'multimedia_bandwidth_percentage_enable',
        'multimedia_bandwidth_percentage_options': 'multimedia_bandwidth_percentage_options',
        'usb_bandwidth_percentage_enable': 'usb_bandwidth_percentage_enable',
        'usb_bandwidth_percentage_options': 'usb_bandwidth_percentage_options',
        'pcsc_bandwidth_percentage_enable': 'pcsc_bandwidth_percentage_enable',
        'pcsc_bandwidth_percentage_options': 'pcsc_bandwidth_percentage_options',
        'twain_bandwidth_percentage_enable': 'twain_bandwidth_percentage_enable',
        'twain_bandwidth_percentage_options': 'twain_bandwidth_percentage_options',
        'printer_bandwidth_percentage_enable': 'printer_bandwidth_percentage_enable',
        'printer_bandwidth_percentage_options': 'printer_bandwidth_percentage_options',
        'com_bandwidth_percentage_enable': 'com_bandwidth_percentage_enable',
        'com_bandwidth_percentage_options': 'com_bandwidth_percentage_options',
        'file_redirection_bandwidth_percentage_enable': 'file_redirection_bandwidth_percentage_enable',
        'file_redirection_bandwidth_percentage_options': 'file_redirection_bandwidth_percentage_options',
        'clipboard_bandwidth_percentage_enable': 'clipboard_bandwidth_percentage_enable',
        'clipboard_bandwidth_percentage_options': 'clipboard_bandwidth_percentage_options',
        'secure_channel_bandwidth_percentage_enable': 'secure_channel_bandwidth_percentage_enable',
        'secure_channel_bandwidth_percentage_options': 'secure_channel_bandwidth_percentage_options',
        'camera_bandwidth_percentage_enable': 'camera_bandwidth_percentage_enable',
        'camera_bandwidth_percentage_options': 'camera_bandwidth_percentage_options',
        'virtual_channel_bandwidth_percentage_enable': 'virtual_channel_bandwidth_percentage_enable',
        'virtual_channel_bandwidth_percentage_options': 'virtual_channel_bandwidth_percentage_options'
    }

    def __init__(self, total_bandwidth_control_value=None, display_bandwidth_percentage_enable=None, display_bandwidth_percentage_options=None, multimedia_bandwidth_percentage_enable=None, multimedia_bandwidth_percentage_options=None, usb_bandwidth_percentage_enable=None, usb_bandwidth_percentage_options=None, pcsc_bandwidth_percentage_enable=None, pcsc_bandwidth_percentage_options=None, twain_bandwidth_percentage_enable=None, twain_bandwidth_percentage_options=None, printer_bandwidth_percentage_enable=None, printer_bandwidth_percentage_options=None, com_bandwidth_percentage_enable=None, com_bandwidth_percentage_options=None, file_redirection_bandwidth_percentage_enable=None, file_redirection_bandwidth_percentage_options=None, clipboard_bandwidth_percentage_enable=None, clipboard_bandwidth_percentage_options=None, secure_channel_bandwidth_percentage_enable=None, secure_channel_bandwidth_percentage_options=None, camera_bandwidth_percentage_enable=None, camera_bandwidth_percentage_options=None, virtual_channel_bandwidth_percentage_enable=None, virtual_channel_bandwidth_percentage_options=None):
        """TotalBandwidthControlOptions

        The model defined in huaweicloud sdk

        :param total_bandwidth_control_value: 总带宽控制量（Kbps）。取值范围为[10000-1000000]。默认：30000。
        :type total_bandwidth_control_value: int
        :param display_bandwidth_percentage_enable: 显示带宽百分比控制。取值为：false：表示关闭。true：表示开启。
        :type display_bandwidth_percentage_enable: bool
        :param display_bandwidth_percentage_options: 
        :type display_bandwidth_percentage_options: :class:`huaweicloudsdkworkspaceapp.v1.DisplayBandwidthPercentageOptions`
        :param multimedia_bandwidth_percentage_enable: 多媒体带宽百分比控制。取值为：false：表示关闭。true：表示开启。
        :type multimedia_bandwidth_percentage_enable: bool
        :param multimedia_bandwidth_percentage_options: 
        :type multimedia_bandwidth_percentage_options: :class:`huaweicloudsdkworkspaceapp.v1.MultimediaBandwidthPercentageOptions`
        :param usb_bandwidth_percentage_enable: USB带宽百分比控制。取值为：false：表示关闭。true：表示开启。
        :type usb_bandwidth_percentage_enable: bool
        :param usb_bandwidth_percentage_options: 
        :type usb_bandwidth_percentage_options: :class:`huaweicloudsdkworkspaceapp.v1.UsbBandwidthPercentageOptions`
        :param pcsc_bandwidth_percentage_enable: PCSC带宽百分比控制。取值为：false：表示关闭。true：表示开启。
        :type pcsc_bandwidth_percentage_enable: bool
        :param pcsc_bandwidth_percentage_options: 
        :type pcsc_bandwidth_percentage_options: :class:`huaweicloudsdkworkspaceapp.v1.PcscBandwidthPercentageOptions`
        :param twain_bandwidth_percentage_enable: TWAIN带宽百分比控制。取值为：false：表示关闭。true：表示开启。
        :type twain_bandwidth_percentage_enable: bool
        :param twain_bandwidth_percentage_options: 
        :type twain_bandwidth_percentage_options: :class:`huaweicloudsdkworkspaceapp.v1.TwainBandwidthPercentageOptions`
        :param printer_bandwidth_percentage_enable: 打印机带宽百分比控制。取值为：false：表示关闭。true：表示开启。
        :type printer_bandwidth_percentage_enable: bool
        :param printer_bandwidth_percentage_options: 
        :type printer_bandwidth_percentage_options: :class:`huaweicloudsdkworkspaceapp.v1.PrinterBandwidthPercentageOptions`
        :param com_bandwidth_percentage_enable: 串口带宽百分比控制。取值为：false：表示关闭。true：表示开启。
        :type com_bandwidth_percentage_enable: bool
        :param com_bandwidth_percentage_options: 
        :type com_bandwidth_percentage_options: :class:`huaweicloudsdkworkspaceapp.v1.ComBandwidthPercentageOptions`
        :param file_redirection_bandwidth_percentage_enable: 文件重定向带宽百分比控制。取值为：false：表示关闭。true：表示开启。
        :type file_redirection_bandwidth_percentage_enable: bool
        :param file_redirection_bandwidth_percentage_options: 
        :type file_redirection_bandwidth_percentage_options: :class:`huaweicloudsdkworkspaceapp.v1.FileRedirectionBandwidthPercentageOptions`
        :param clipboard_bandwidth_percentage_enable: 剪切板带宽百分比控制。取值为：false：表示关闭。true：表示开启。
        :type clipboard_bandwidth_percentage_enable: bool
        :param clipboard_bandwidth_percentage_options: 
        :type clipboard_bandwidth_percentage_options: :class:`huaweicloudsdkworkspaceapp.v1.ClipboardBandwidthPercentageOptions`
        :param secure_channel_bandwidth_percentage_enable: 安全通道带宽百分比控制。取值为：false：表示关闭。true：表示开启。
        :type secure_channel_bandwidth_percentage_enable: bool
        :param secure_channel_bandwidth_percentage_options: 
        :type secure_channel_bandwidth_percentage_options: :class:`huaweicloudsdkworkspaceapp.v1.SecureChannelBandwidthPercentageOptions`
        :param camera_bandwidth_percentage_enable: 摄像头带宽百分比控制。取值为：false：表示关闭。true：表示开启。
        :type camera_bandwidth_percentage_enable: bool
        :param camera_bandwidth_percentage_options: 
        :type camera_bandwidth_percentage_options: :class:`huaweicloudsdkworkspaceapp.v1.CameraBandwidthPercentageOptions`
        :param virtual_channel_bandwidth_percentage_enable: 虚拟通道带宽百分比控制。取值为：false：表示关闭。true：表示开启。
        :type virtual_channel_bandwidth_percentage_enable: bool
        :param virtual_channel_bandwidth_percentage_options: 
        :type virtual_channel_bandwidth_percentage_options: :class:`huaweicloudsdkworkspaceapp.v1.VirtualChannelBandwidthPercentageOptions`
        """
        
        

        self._total_bandwidth_control_value = None
        self._display_bandwidth_percentage_enable = None
        self._display_bandwidth_percentage_options = None
        self._multimedia_bandwidth_percentage_enable = None
        self._multimedia_bandwidth_percentage_options = None
        self._usb_bandwidth_percentage_enable = None
        self._usb_bandwidth_percentage_options = None
        self._pcsc_bandwidth_percentage_enable = None
        self._pcsc_bandwidth_percentage_options = None
        self._twain_bandwidth_percentage_enable = None
        self._twain_bandwidth_percentage_options = None
        self._printer_bandwidth_percentage_enable = None
        self._printer_bandwidth_percentage_options = None
        self._com_bandwidth_percentage_enable = None
        self._com_bandwidth_percentage_options = None
        self._file_redirection_bandwidth_percentage_enable = None
        self._file_redirection_bandwidth_percentage_options = None
        self._clipboard_bandwidth_percentage_enable = None
        self._clipboard_bandwidth_percentage_options = None
        self._secure_channel_bandwidth_percentage_enable = None
        self._secure_channel_bandwidth_percentage_options = None
        self._camera_bandwidth_percentage_enable = None
        self._camera_bandwidth_percentage_options = None
        self._virtual_channel_bandwidth_percentage_enable = None
        self._virtual_channel_bandwidth_percentage_options = None
        self.discriminator = None

        if total_bandwidth_control_value is not None:
            self.total_bandwidth_control_value = total_bandwidth_control_value
        if display_bandwidth_percentage_enable is not None:
            self.display_bandwidth_percentage_enable = display_bandwidth_percentage_enable
        if display_bandwidth_percentage_options is not None:
            self.display_bandwidth_percentage_options = display_bandwidth_percentage_options
        if multimedia_bandwidth_percentage_enable is not None:
            self.multimedia_bandwidth_percentage_enable = multimedia_bandwidth_percentage_enable
        if multimedia_bandwidth_percentage_options is not None:
            self.multimedia_bandwidth_percentage_options = multimedia_bandwidth_percentage_options
        if usb_bandwidth_percentage_enable is not None:
            self.usb_bandwidth_percentage_enable = usb_bandwidth_percentage_enable
        if usb_bandwidth_percentage_options is not None:
            self.usb_bandwidth_percentage_options = usb_bandwidth_percentage_options
        if pcsc_bandwidth_percentage_enable is not None:
            self.pcsc_bandwidth_percentage_enable = pcsc_bandwidth_percentage_enable
        if pcsc_bandwidth_percentage_options is not None:
            self.pcsc_bandwidth_percentage_options = pcsc_bandwidth_percentage_options
        if twain_bandwidth_percentage_enable is not None:
            self.twain_bandwidth_percentage_enable = twain_bandwidth_percentage_enable
        if twain_bandwidth_percentage_options is not None:
            self.twain_bandwidth_percentage_options = twain_bandwidth_percentage_options
        if printer_bandwidth_percentage_enable is not None:
            self.printer_bandwidth_percentage_enable = printer_bandwidth_percentage_enable
        if printer_bandwidth_percentage_options is not None:
            self.printer_bandwidth_percentage_options = printer_bandwidth_percentage_options
        if com_bandwidth_percentage_enable is not None:
            self.com_bandwidth_percentage_enable = com_bandwidth_percentage_enable
        if com_bandwidth_percentage_options is not None:
            self.com_bandwidth_percentage_options = com_bandwidth_percentage_options
        if file_redirection_bandwidth_percentage_enable is not None:
            self.file_redirection_bandwidth_percentage_enable = file_redirection_bandwidth_percentage_enable
        if file_redirection_bandwidth_percentage_options is not None:
            self.file_redirection_bandwidth_percentage_options = file_redirection_bandwidth_percentage_options
        if clipboard_bandwidth_percentage_enable is not None:
            self.clipboard_bandwidth_percentage_enable = clipboard_bandwidth_percentage_enable
        if clipboard_bandwidth_percentage_options is not None:
            self.clipboard_bandwidth_percentage_options = clipboard_bandwidth_percentage_options
        if secure_channel_bandwidth_percentage_enable is not None:
            self.secure_channel_bandwidth_percentage_enable = secure_channel_bandwidth_percentage_enable
        if secure_channel_bandwidth_percentage_options is not None:
            self.secure_channel_bandwidth_percentage_options = secure_channel_bandwidth_percentage_options
        if camera_bandwidth_percentage_enable is not None:
            self.camera_bandwidth_percentage_enable = camera_bandwidth_percentage_enable
        if camera_bandwidth_percentage_options is not None:
            self.camera_bandwidth_percentage_options = camera_bandwidth_percentage_options
        if virtual_channel_bandwidth_percentage_enable is not None:
            self.virtual_channel_bandwidth_percentage_enable = virtual_channel_bandwidth_percentage_enable
        if virtual_channel_bandwidth_percentage_options is not None:
            self.virtual_channel_bandwidth_percentage_options = virtual_channel_bandwidth_percentage_options

    @property
    def total_bandwidth_control_value(self):
        """Gets the total_bandwidth_control_value of this TotalBandwidthControlOptions.

        总带宽控制量（Kbps）。取值范围为[10000-1000000]。默认：30000。

        :return: The total_bandwidth_control_value of this TotalBandwidthControlOptions.
        :rtype: int
        """
        return self._total_bandwidth_control_value

    @total_bandwidth_control_value.setter
    def total_bandwidth_control_value(self, total_bandwidth_control_value):
        """Sets the total_bandwidth_control_value of this TotalBandwidthControlOptions.

        总带宽控制量（Kbps）。取值范围为[10000-1000000]。默认：30000。

        :param total_bandwidth_control_value: The total_bandwidth_control_value of this TotalBandwidthControlOptions.
        :type total_bandwidth_control_value: int
        """
        self._total_bandwidth_control_value = total_bandwidth_control_value

    @property
    def display_bandwidth_percentage_enable(self):
        """Gets the display_bandwidth_percentage_enable of this TotalBandwidthControlOptions.

        显示带宽百分比控制。取值为：false：表示关闭。true：表示开启。

        :return: The display_bandwidth_percentage_enable of this TotalBandwidthControlOptions.
        :rtype: bool
        """
        return self._display_bandwidth_percentage_enable

    @display_bandwidth_percentage_enable.setter
    def display_bandwidth_percentage_enable(self, display_bandwidth_percentage_enable):
        """Sets the display_bandwidth_percentage_enable of this TotalBandwidthControlOptions.

        显示带宽百分比控制。取值为：false：表示关闭。true：表示开启。

        :param display_bandwidth_percentage_enable: The display_bandwidth_percentage_enable of this TotalBandwidthControlOptions.
        :type display_bandwidth_percentage_enable: bool
        """
        self._display_bandwidth_percentage_enable = display_bandwidth_percentage_enable

    @property
    def display_bandwidth_percentage_options(self):
        """Gets the display_bandwidth_percentage_options of this TotalBandwidthControlOptions.

        :return: The display_bandwidth_percentage_options of this TotalBandwidthControlOptions.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.DisplayBandwidthPercentageOptions`
        """
        return self._display_bandwidth_percentage_options

    @display_bandwidth_percentage_options.setter
    def display_bandwidth_percentage_options(self, display_bandwidth_percentage_options):
        """Sets the display_bandwidth_percentage_options of this TotalBandwidthControlOptions.

        :param display_bandwidth_percentage_options: The display_bandwidth_percentage_options of this TotalBandwidthControlOptions.
        :type display_bandwidth_percentage_options: :class:`huaweicloudsdkworkspaceapp.v1.DisplayBandwidthPercentageOptions`
        """
        self._display_bandwidth_percentage_options = display_bandwidth_percentage_options

    @property
    def multimedia_bandwidth_percentage_enable(self):
        """Gets the multimedia_bandwidth_percentage_enable of this TotalBandwidthControlOptions.

        多媒体带宽百分比控制。取值为：false：表示关闭。true：表示开启。

        :return: The multimedia_bandwidth_percentage_enable of this TotalBandwidthControlOptions.
        :rtype: bool
        """
        return self._multimedia_bandwidth_percentage_enable

    @multimedia_bandwidth_percentage_enable.setter
    def multimedia_bandwidth_percentage_enable(self, multimedia_bandwidth_percentage_enable):
        """Sets the multimedia_bandwidth_percentage_enable of this TotalBandwidthControlOptions.

        多媒体带宽百分比控制。取值为：false：表示关闭。true：表示开启。

        :param multimedia_bandwidth_percentage_enable: The multimedia_bandwidth_percentage_enable of this TotalBandwidthControlOptions.
        :type multimedia_bandwidth_percentage_enable: bool
        """
        self._multimedia_bandwidth_percentage_enable = multimedia_bandwidth_percentage_enable

    @property
    def multimedia_bandwidth_percentage_options(self):
        """Gets the multimedia_bandwidth_percentage_options of this TotalBandwidthControlOptions.

        :return: The multimedia_bandwidth_percentage_options of this TotalBandwidthControlOptions.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.MultimediaBandwidthPercentageOptions`
        """
        return self._multimedia_bandwidth_percentage_options

    @multimedia_bandwidth_percentage_options.setter
    def multimedia_bandwidth_percentage_options(self, multimedia_bandwidth_percentage_options):
        """Sets the multimedia_bandwidth_percentage_options of this TotalBandwidthControlOptions.

        :param multimedia_bandwidth_percentage_options: The multimedia_bandwidth_percentage_options of this TotalBandwidthControlOptions.
        :type multimedia_bandwidth_percentage_options: :class:`huaweicloudsdkworkspaceapp.v1.MultimediaBandwidthPercentageOptions`
        """
        self._multimedia_bandwidth_percentage_options = multimedia_bandwidth_percentage_options

    @property
    def usb_bandwidth_percentage_enable(self):
        """Gets the usb_bandwidth_percentage_enable of this TotalBandwidthControlOptions.

        USB带宽百分比控制。取值为：false：表示关闭。true：表示开启。

        :return: The usb_bandwidth_percentage_enable of this TotalBandwidthControlOptions.
        :rtype: bool
        """
        return self._usb_bandwidth_percentage_enable

    @usb_bandwidth_percentage_enable.setter
    def usb_bandwidth_percentage_enable(self, usb_bandwidth_percentage_enable):
        """Sets the usb_bandwidth_percentage_enable of this TotalBandwidthControlOptions.

        USB带宽百分比控制。取值为：false：表示关闭。true：表示开启。

        :param usb_bandwidth_percentage_enable: The usb_bandwidth_percentage_enable of this TotalBandwidthControlOptions.
        :type usb_bandwidth_percentage_enable: bool
        """
        self._usb_bandwidth_percentage_enable = usb_bandwidth_percentage_enable

    @property
    def usb_bandwidth_percentage_options(self):
        """Gets the usb_bandwidth_percentage_options of this TotalBandwidthControlOptions.

        :return: The usb_bandwidth_percentage_options of this TotalBandwidthControlOptions.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UsbBandwidthPercentageOptions`
        """
        return self._usb_bandwidth_percentage_options

    @usb_bandwidth_percentage_options.setter
    def usb_bandwidth_percentage_options(self, usb_bandwidth_percentage_options):
        """Sets the usb_bandwidth_percentage_options of this TotalBandwidthControlOptions.

        :param usb_bandwidth_percentage_options: The usb_bandwidth_percentage_options of this TotalBandwidthControlOptions.
        :type usb_bandwidth_percentage_options: :class:`huaweicloudsdkworkspaceapp.v1.UsbBandwidthPercentageOptions`
        """
        self._usb_bandwidth_percentage_options = usb_bandwidth_percentage_options

    @property
    def pcsc_bandwidth_percentage_enable(self):
        """Gets the pcsc_bandwidth_percentage_enable of this TotalBandwidthControlOptions.

        PCSC带宽百分比控制。取值为：false：表示关闭。true：表示开启。

        :return: The pcsc_bandwidth_percentage_enable of this TotalBandwidthControlOptions.
        :rtype: bool
        """
        return self._pcsc_bandwidth_percentage_enable

    @pcsc_bandwidth_percentage_enable.setter
    def pcsc_bandwidth_percentage_enable(self, pcsc_bandwidth_percentage_enable):
        """Sets the pcsc_bandwidth_percentage_enable of this TotalBandwidthControlOptions.

        PCSC带宽百分比控制。取值为：false：表示关闭。true：表示开启。

        :param pcsc_bandwidth_percentage_enable: The pcsc_bandwidth_percentage_enable of this TotalBandwidthControlOptions.
        :type pcsc_bandwidth_percentage_enable: bool
        """
        self._pcsc_bandwidth_percentage_enable = pcsc_bandwidth_percentage_enable

    @property
    def pcsc_bandwidth_percentage_options(self):
        """Gets the pcsc_bandwidth_percentage_options of this TotalBandwidthControlOptions.

        :return: The pcsc_bandwidth_percentage_options of this TotalBandwidthControlOptions.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PcscBandwidthPercentageOptions`
        """
        return self._pcsc_bandwidth_percentage_options

    @pcsc_bandwidth_percentage_options.setter
    def pcsc_bandwidth_percentage_options(self, pcsc_bandwidth_percentage_options):
        """Sets the pcsc_bandwidth_percentage_options of this TotalBandwidthControlOptions.

        :param pcsc_bandwidth_percentage_options: The pcsc_bandwidth_percentage_options of this TotalBandwidthControlOptions.
        :type pcsc_bandwidth_percentage_options: :class:`huaweicloudsdkworkspaceapp.v1.PcscBandwidthPercentageOptions`
        """
        self._pcsc_bandwidth_percentage_options = pcsc_bandwidth_percentage_options

    @property
    def twain_bandwidth_percentage_enable(self):
        """Gets the twain_bandwidth_percentage_enable of this TotalBandwidthControlOptions.

        TWAIN带宽百分比控制。取值为：false：表示关闭。true：表示开启。

        :return: The twain_bandwidth_percentage_enable of this TotalBandwidthControlOptions.
        :rtype: bool
        """
        return self._twain_bandwidth_percentage_enable

    @twain_bandwidth_percentage_enable.setter
    def twain_bandwidth_percentage_enable(self, twain_bandwidth_percentage_enable):
        """Sets the twain_bandwidth_percentage_enable of this TotalBandwidthControlOptions.

        TWAIN带宽百分比控制。取值为：false：表示关闭。true：表示开启。

        :param twain_bandwidth_percentage_enable: The twain_bandwidth_percentage_enable of this TotalBandwidthControlOptions.
        :type twain_bandwidth_percentage_enable: bool
        """
        self._twain_bandwidth_percentage_enable = twain_bandwidth_percentage_enable

    @property
    def twain_bandwidth_percentage_options(self):
        """Gets the twain_bandwidth_percentage_options of this TotalBandwidthControlOptions.

        :return: The twain_bandwidth_percentage_options of this TotalBandwidthControlOptions.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.TwainBandwidthPercentageOptions`
        """
        return self._twain_bandwidth_percentage_options

    @twain_bandwidth_percentage_options.setter
    def twain_bandwidth_percentage_options(self, twain_bandwidth_percentage_options):
        """Sets the twain_bandwidth_percentage_options of this TotalBandwidthControlOptions.

        :param twain_bandwidth_percentage_options: The twain_bandwidth_percentage_options of this TotalBandwidthControlOptions.
        :type twain_bandwidth_percentage_options: :class:`huaweicloudsdkworkspaceapp.v1.TwainBandwidthPercentageOptions`
        """
        self._twain_bandwidth_percentage_options = twain_bandwidth_percentage_options

    @property
    def printer_bandwidth_percentage_enable(self):
        """Gets the printer_bandwidth_percentage_enable of this TotalBandwidthControlOptions.

        打印机带宽百分比控制。取值为：false：表示关闭。true：表示开启。

        :return: The printer_bandwidth_percentage_enable of this TotalBandwidthControlOptions.
        :rtype: bool
        """
        return self._printer_bandwidth_percentage_enable

    @printer_bandwidth_percentage_enable.setter
    def printer_bandwidth_percentage_enable(self, printer_bandwidth_percentage_enable):
        """Sets the printer_bandwidth_percentage_enable of this TotalBandwidthControlOptions.

        打印机带宽百分比控制。取值为：false：表示关闭。true：表示开启。

        :param printer_bandwidth_percentage_enable: The printer_bandwidth_percentage_enable of this TotalBandwidthControlOptions.
        :type printer_bandwidth_percentage_enable: bool
        """
        self._printer_bandwidth_percentage_enable = printer_bandwidth_percentage_enable

    @property
    def printer_bandwidth_percentage_options(self):
        """Gets the printer_bandwidth_percentage_options of this TotalBandwidthControlOptions.

        :return: The printer_bandwidth_percentage_options of this TotalBandwidthControlOptions.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PrinterBandwidthPercentageOptions`
        """
        return self._printer_bandwidth_percentage_options

    @printer_bandwidth_percentage_options.setter
    def printer_bandwidth_percentage_options(self, printer_bandwidth_percentage_options):
        """Sets the printer_bandwidth_percentage_options of this TotalBandwidthControlOptions.

        :param printer_bandwidth_percentage_options: The printer_bandwidth_percentage_options of this TotalBandwidthControlOptions.
        :type printer_bandwidth_percentage_options: :class:`huaweicloudsdkworkspaceapp.v1.PrinterBandwidthPercentageOptions`
        """
        self._printer_bandwidth_percentage_options = printer_bandwidth_percentage_options

    @property
    def com_bandwidth_percentage_enable(self):
        """Gets the com_bandwidth_percentage_enable of this TotalBandwidthControlOptions.

        串口带宽百分比控制。取值为：false：表示关闭。true：表示开启。

        :return: The com_bandwidth_percentage_enable of this TotalBandwidthControlOptions.
        :rtype: bool
        """
        return self._com_bandwidth_percentage_enable

    @com_bandwidth_percentage_enable.setter
    def com_bandwidth_percentage_enable(self, com_bandwidth_percentage_enable):
        """Sets the com_bandwidth_percentage_enable of this TotalBandwidthControlOptions.

        串口带宽百分比控制。取值为：false：表示关闭。true：表示开启。

        :param com_bandwidth_percentage_enable: The com_bandwidth_percentage_enable of this TotalBandwidthControlOptions.
        :type com_bandwidth_percentage_enable: bool
        """
        self._com_bandwidth_percentage_enable = com_bandwidth_percentage_enable

    @property
    def com_bandwidth_percentage_options(self):
        """Gets the com_bandwidth_percentage_options of this TotalBandwidthControlOptions.

        :return: The com_bandwidth_percentage_options of this TotalBandwidthControlOptions.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ComBandwidthPercentageOptions`
        """
        return self._com_bandwidth_percentage_options

    @com_bandwidth_percentage_options.setter
    def com_bandwidth_percentage_options(self, com_bandwidth_percentage_options):
        """Sets the com_bandwidth_percentage_options of this TotalBandwidthControlOptions.

        :param com_bandwidth_percentage_options: The com_bandwidth_percentage_options of this TotalBandwidthControlOptions.
        :type com_bandwidth_percentage_options: :class:`huaweicloudsdkworkspaceapp.v1.ComBandwidthPercentageOptions`
        """
        self._com_bandwidth_percentage_options = com_bandwidth_percentage_options

    @property
    def file_redirection_bandwidth_percentage_enable(self):
        """Gets the file_redirection_bandwidth_percentage_enable of this TotalBandwidthControlOptions.

        文件重定向带宽百分比控制。取值为：false：表示关闭。true：表示开启。

        :return: The file_redirection_bandwidth_percentage_enable of this TotalBandwidthControlOptions.
        :rtype: bool
        """
        return self._file_redirection_bandwidth_percentage_enable

    @file_redirection_bandwidth_percentage_enable.setter
    def file_redirection_bandwidth_percentage_enable(self, file_redirection_bandwidth_percentage_enable):
        """Sets the file_redirection_bandwidth_percentage_enable of this TotalBandwidthControlOptions.

        文件重定向带宽百分比控制。取值为：false：表示关闭。true：表示开启。

        :param file_redirection_bandwidth_percentage_enable: The file_redirection_bandwidth_percentage_enable of this TotalBandwidthControlOptions.
        :type file_redirection_bandwidth_percentage_enable: bool
        """
        self._file_redirection_bandwidth_percentage_enable = file_redirection_bandwidth_percentage_enable

    @property
    def file_redirection_bandwidth_percentage_options(self):
        """Gets the file_redirection_bandwidth_percentage_options of this TotalBandwidthControlOptions.

        :return: The file_redirection_bandwidth_percentage_options of this TotalBandwidthControlOptions.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.FileRedirectionBandwidthPercentageOptions`
        """
        return self._file_redirection_bandwidth_percentage_options

    @file_redirection_bandwidth_percentage_options.setter
    def file_redirection_bandwidth_percentage_options(self, file_redirection_bandwidth_percentage_options):
        """Sets the file_redirection_bandwidth_percentage_options of this TotalBandwidthControlOptions.

        :param file_redirection_bandwidth_percentage_options: The file_redirection_bandwidth_percentage_options of this TotalBandwidthControlOptions.
        :type file_redirection_bandwidth_percentage_options: :class:`huaweicloudsdkworkspaceapp.v1.FileRedirectionBandwidthPercentageOptions`
        """
        self._file_redirection_bandwidth_percentage_options = file_redirection_bandwidth_percentage_options

    @property
    def clipboard_bandwidth_percentage_enable(self):
        """Gets the clipboard_bandwidth_percentage_enable of this TotalBandwidthControlOptions.

        剪切板带宽百分比控制。取值为：false：表示关闭。true：表示开启。

        :return: The clipboard_bandwidth_percentage_enable of this TotalBandwidthControlOptions.
        :rtype: bool
        """
        return self._clipboard_bandwidth_percentage_enable

    @clipboard_bandwidth_percentage_enable.setter
    def clipboard_bandwidth_percentage_enable(self, clipboard_bandwidth_percentage_enable):
        """Sets the clipboard_bandwidth_percentage_enable of this TotalBandwidthControlOptions.

        剪切板带宽百分比控制。取值为：false：表示关闭。true：表示开启。

        :param clipboard_bandwidth_percentage_enable: The clipboard_bandwidth_percentage_enable of this TotalBandwidthControlOptions.
        :type clipboard_bandwidth_percentage_enable: bool
        """
        self._clipboard_bandwidth_percentage_enable = clipboard_bandwidth_percentage_enable

    @property
    def clipboard_bandwidth_percentage_options(self):
        """Gets the clipboard_bandwidth_percentage_options of this TotalBandwidthControlOptions.

        :return: The clipboard_bandwidth_percentage_options of this TotalBandwidthControlOptions.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ClipboardBandwidthPercentageOptions`
        """
        return self._clipboard_bandwidth_percentage_options

    @clipboard_bandwidth_percentage_options.setter
    def clipboard_bandwidth_percentage_options(self, clipboard_bandwidth_percentage_options):
        """Sets the clipboard_bandwidth_percentage_options of this TotalBandwidthControlOptions.

        :param clipboard_bandwidth_percentage_options: The clipboard_bandwidth_percentage_options of this TotalBandwidthControlOptions.
        :type clipboard_bandwidth_percentage_options: :class:`huaweicloudsdkworkspaceapp.v1.ClipboardBandwidthPercentageOptions`
        """
        self._clipboard_bandwidth_percentage_options = clipboard_bandwidth_percentage_options

    @property
    def secure_channel_bandwidth_percentage_enable(self):
        """Gets the secure_channel_bandwidth_percentage_enable of this TotalBandwidthControlOptions.

        安全通道带宽百分比控制。取值为：false：表示关闭。true：表示开启。

        :return: The secure_channel_bandwidth_percentage_enable of this TotalBandwidthControlOptions.
        :rtype: bool
        """
        return self._secure_channel_bandwidth_percentage_enable

    @secure_channel_bandwidth_percentage_enable.setter
    def secure_channel_bandwidth_percentage_enable(self, secure_channel_bandwidth_percentage_enable):
        """Sets the secure_channel_bandwidth_percentage_enable of this TotalBandwidthControlOptions.

        安全通道带宽百分比控制。取值为：false：表示关闭。true：表示开启。

        :param secure_channel_bandwidth_percentage_enable: The secure_channel_bandwidth_percentage_enable of this TotalBandwidthControlOptions.
        :type secure_channel_bandwidth_percentage_enable: bool
        """
        self._secure_channel_bandwidth_percentage_enable = secure_channel_bandwidth_percentage_enable

    @property
    def secure_channel_bandwidth_percentage_options(self):
        """Gets the secure_channel_bandwidth_percentage_options of this TotalBandwidthControlOptions.

        :return: The secure_channel_bandwidth_percentage_options of this TotalBandwidthControlOptions.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.SecureChannelBandwidthPercentageOptions`
        """
        return self._secure_channel_bandwidth_percentage_options

    @secure_channel_bandwidth_percentage_options.setter
    def secure_channel_bandwidth_percentage_options(self, secure_channel_bandwidth_percentage_options):
        """Sets the secure_channel_bandwidth_percentage_options of this TotalBandwidthControlOptions.

        :param secure_channel_bandwidth_percentage_options: The secure_channel_bandwidth_percentage_options of this TotalBandwidthControlOptions.
        :type secure_channel_bandwidth_percentage_options: :class:`huaweicloudsdkworkspaceapp.v1.SecureChannelBandwidthPercentageOptions`
        """
        self._secure_channel_bandwidth_percentage_options = secure_channel_bandwidth_percentage_options

    @property
    def camera_bandwidth_percentage_enable(self):
        """Gets the camera_bandwidth_percentage_enable of this TotalBandwidthControlOptions.

        摄像头带宽百分比控制。取值为：false：表示关闭。true：表示开启。

        :return: The camera_bandwidth_percentage_enable of this TotalBandwidthControlOptions.
        :rtype: bool
        """
        return self._camera_bandwidth_percentage_enable

    @camera_bandwidth_percentage_enable.setter
    def camera_bandwidth_percentage_enable(self, camera_bandwidth_percentage_enable):
        """Sets the camera_bandwidth_percentage_enable of this TotalBandwidthControlOptions.

        摄像头带宽百分比控制。取值为：false：表示关闭。true：表示开启。

        :param camera_bandwidth_percentage_enable: The camera_bandwidth_percentage_enable of this TotalBandwidthControlOptions.
        :type camera_bandwidth_percentage_enable: bool
        """
        self._camera_bandwidth_percentage_enable = camera_bandwidth_percentage_enable

    @property
    def camera_bandwidth_percentage_options(self):
        """Gets the camera_bandwidth_percentage_options of this TotalBandwidthControlOptions.

        :return: The camera_bandwidth_percentage_options of this TotalBandwidthControlOptions.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CameraBandwidthPercentageOptions`
        """
        return self._camera_bandwidth_percentage_options

    @camera_bandwidth_percentage_options.setter
    def camera_bandwidth_percentage_options(self, camera_bandwidth_percentage_options):
        """Sets the camera_bandwidth_percentage_options of this TotalBandwidthControlOptions.

        :param camera_bandwidth_percentage_options: The camera_bandwidth_percentage_options of this TotalBandwidthControlOptions.
        :type camera_bandwidth_percentage_options: :class:`huaweicloudsdkworkspaceapp.v1.CameraBandwidthPercentageOptions`
        """
        self._camera_bandwidth_percentage_options = camera_bandwidth_percentage_options

    @property
    def virtual_channel_bandwidth_percentage_enable(self):
        """Gets the virtual_channel_bandwidth_percentage_enable of this TotalBandwidthControlOptions.

        虚拟通道带宽百分比控制。取值为：false：表示关闭。true：表示开启。

        :return: The virtual_channel_bandwidth_percentage_enable of this TotalBandwidthControlOptions.
        :rtype: bool
        """
        return self._virtual_channel_bandwidth_percentage_enable

    @virtual_channel_bandwidth_percentage_enable.setter
    def virtual_channel_bandwidth_percentage_enable(self, virtual_channel_bandwidth_percentage_enable):
        """Sets the virtual_channel_bandwidth_percentage_enable of this TotalBandwidthControlOptions.

        虚拟通道带宽百分比控制。取值为：false：表示关闭。true：表示开启。

        :param virtual_channel_bandwidth_percentage_enable: The virtual_channel_bandwidth_percentage_enable of this TotalBandwidthControlOptions.
        :type virtual_channel_bandwidth_percentage_enable: bool
        """
        self._virtual_channel_bandwidth_percentage_enable = virtual_channel_bandwidth_percentage_enable

    @property
    def virtual_channel_bandwidth_percentage_options(self):
        """Gets the virtual_channel_bandwidth_percentage_options of this TotalBandwidthControlOptions.

        :return: The virtual_channel_bandwidth_percentage_options of this TotalBandwidthControlOptions.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.VirtualChannelBandwidthPercentageOptions`
        """
        return self._virtual_channel_bandwidth_percentage_options

    @virtual_channel_bandwidth_percentage_options.setter
    def virtual_channel_bandwidth_percentage_options(self, virtual_channel_bandwidth_percentage_options):
        """Sets the virtual_channel_bandwidth_percentage_options of this TotalBandwidthControlOptions.

        :param virtual_channel_bandwidth_percentage_options: The virtual_channel_bandwidth_percentage_options of this TotalBandwidthControlOptions.
        :type virtual_channel_bandwidth_percentage_options: :class:`huaweicloudsdkworkspaceapp.v1.VirtualChannelBandwidthPercentageOptions`
        """
        self._virtual_channel_bandwidth_percentage_options = virtual_channel_bandwidth_percentage_options

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
        if not isinstance(other, TotalBandwidthControlOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
