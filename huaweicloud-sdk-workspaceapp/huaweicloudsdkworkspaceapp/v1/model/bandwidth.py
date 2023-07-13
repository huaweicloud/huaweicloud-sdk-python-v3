# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Bandwidth:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'intelligent_data_transport_flag': 'str',
        'total_bandwidth_control_enable': 'bool',
        'options': 'TotalBandwidthControlOptions',
        'display_bandwidth_control_enable': 'bool',
        'display_bandwidth_control_options': 'DisplayBandwidthControlOptions',
        'multimedia_bandwidth_control_enable': 'bool',
        'multimedia_bandwidth_control_options': 'MultimediaBandwidthControlOptions',
        'usb_bandwidth_control_enable': 'bool',
        'usb_bandwidth_control_options': 'UsbBandwidthControlOptions',
        'pcsc_bandwidth_control_enable': 'bool',
        'pcsc_bandwidth_control_options': 'PcscBandwidthControlOptions',
        'twain_bandwidth_control_enable': 'bool',
        'twain_bandwidth_control_options': 'TwainBandwidthControlOptions',
        'printer_bandwidth_control_enable': 'bool',
        'printer_bandwidth_control_options': 'PrinterBandwidthControlOptions',
        'com_bandwidth_control_enable': 'bool',
        'com_bandwidth_control_options': 'ComBandwidthControlOptions',
        'file_redirection_bandwidth_control_enable': 'bool',
        'file_redirection_bandwidth_control_options': 'FileRedirectionBandwidthControlOptions',
        'clipboard_bandwidth_control_enable': 'bool',
        'clipboard_bandwidth_control_options': 'ClipboardBandwidthControlOptions',
        'secure_channel_bandwidth_control_enable': 'bool',
        'secure_channel_bandwidth_control_options': 'SecureChannelBandwidthControlOptions',
        'camera_bandwidth_control_enable': 'bool',
        'camera_bandwidth_control_options': 'CameraBandwidthControlOptions',
        'virtual_channel_bandwidth_control_enable': 'bool',
        'virtual_channel_bandwidth_control_options': 'VirtualChannelBandwidthControlOptions'
    }

    attribute_map = {
        'intelligent_data_transport_flag': 'intelligent_data_transport_flag',
        'total_bandwidth_control_enable': 'total_bandwidth_control_enable',
        'options': 'options',
        'display_bandwidth_control_enable': 'display_bandwidth_control_enable',
        'display_bandwidth_control_options': 'display_bandwidth_control_options',
        'multimedia_bandwidth_control_enable': 'multimedia_bandwidth_control_enable',
        'multimedia_bandwidth_control_options': 'multimedia_bandwidth_control_options',
        'usb_bandwidth_control_enable': 'usb_bandwidth_control_enable',
        'usb_bandwidth_control_options': 'usb_bandwidth_control_options',
        'pcsc_bandwidth_control_enable': 'pcsc_bandwidth_control_enable',
        'pcsc_bandwidth_control_options': 'pcsc_bandwidth_control_options',
        'twain_bandwidth_control_enable': 'twain_bandwidth_control_enable',
        'twain_bandwidth_control_options': 'twain_bandwidth_control_options',
        'printer_bandwidth_control_enable': 'printer_bandwidth_control_enable',
        'printer_bandwidth_control_options': 'printer_bandwidth_control_options',
        'com_bandwidth_control_enable': 'com_bandwidth_control_enable',
        'com_bandwidth_control_options': 'com_bandwidth_control_options',
        'file_redirection_bandwidth_control_enable': 'file_redirection_bandwidth_control_enable',
        'file_redirection_bandwidth_control_options': 'file_redirection_bandwidth_control_options',
        'clipboard_bandwidth_control_enable': 'clipboard_bandwidth_control_enable',
        'clipboard_bandwidth_control_options': 'clipboard_bandwidth_control_options',
        'secure_channel_bandwidth_control_enable': 'secure_channel_bandwidth_control_enable',
        'secure_channel_bandwidth_control_options': 'secure_channel_bandwidth_control_options',
        'camera_bandwidth_control_enable': 'camera_bandwidth_control_enable',
        'camera_bandwidth_control_options': 'camera_bandwidth_control_options',
        'virtual_channel_bandwidth_control_enable': 'virtual_channel_bandwidth_control_enable',
        'virtual_channel_bandwidth_control_options': 'virtual_channel_bandwidth_control_options'
    }

    def __init__(self, intelligent_data_transport_flag=None, total_bandwidth_control_enable=None, options=None, display_bandwidth_control_enable=None, display_bandwidth_control_options=None, multimedia_bandwidth_control_enable=None, multimedia_bandwidth_control_options=None, usb_bandwidth_control_enable=None, usb_bandwidth_control_options=None, pcsc_bandwidth_control_enable=None, pcsc_bandwidth_control_options=None, twain_bandwidth_control_enable=None, twain_bandwidth_control_options=None, printer_bandwidth_control_enable=None, printer_bandwidth_control_options=None, com_bandwidth_control_enable=None, com_bandwidth_control_options=None, file_redirection_bandwidth_control_enable=None, file_redirection_bandwidth_control_options=None, clipboard_bandwidth_control_enable=None, clipboard_bandwidth_control_options=None, secure_channel_bandwidth_control_enable=None, secure_channel_bandwidth_control_options=None, camera_bandwidth_control_enable=None, camera_bandwidth_control_options=None, virtual_channel_bandwidth_control_enable=None, virtual_channel_bandwidth_control_options=None):
        """Bandwidth

        The model defined in huaweicloud sdk

        :param intelligent_data_transport_flag: 智能显示传输。取值为：DISABLE：表示关闭。ENABLE：表示开启。DIAGNOSTIC：诊断模式
        :type intelligent_data_transport_flag: str
        :param total_bandwidth_control_enable: 是否开启总带宽控制。取值为：false：表示关闭。true：表示开启。
        :type total_bandwidth_control_enable: bool
        :param options: 
        :type options: :class:`huaweicloudsdkworkspaceapp.v1.TotalBandwidthControlOptions`
        :param display_bandwidth_control_enable: 是否开启显示带宽控制。取值为：false：表示关闭。true：表示开启。
        :type display_bandwidth_control_enable: bool
        :param display_bandwidth_control_options: 
        :type display_bandwidth_control_options: :class:`huaweicloudsdkworkspaceapp.v1.DisplayBandwidthControlOptions`
        :param multimedia_bandwidth_control_enable: 是否开启多媒体带宽控制。取值为：false：表示关闭。true：表示开启。
        :type multimedia_bandwidth_control_enable: bool
        :param multimedia_bandwidth_control_options: 
        :type multimedia_bandwidth_control_options: :class:`huaweicloudsdkworkspaceapp.v1.MultimediaBandwidthControlOptions`
        :param usb_bandwidth_control_enable: 是否开启USB带宽控制。取值为：false：表示关闭。true：表示开启。
        :type usb_bandwidth_control_enable: bool
        :param usb_bandwidth_control_options: 
        :type usb_bandwidth_control_options: :class:`huaweicloudsdkworkspaceapp.v1.UsbBandwidthControlOptions`
        :param pcsc_bandwidth_control_enable: 是否开启PCSC控制。取值为：false：表示关闭。true：表示开启。
        :type pcsc_bandwidth_control_enable: bool
        :param pcsc_bandwidth_control_options: 
        :type pcsc_bandwidth_control_options: :class:`huaweicloudsdkworkspaceapp.v1.PcscBandwidthControlOptions`
        :param twain_bandwidth_control_enable: 是否开启TWAIN带宽控制。取值为：false：表示关闭。true：表示开启。
        :type twain_bandwidth_control_enable: bool
        :param twain_bandwidth_control_options: 
        :type twain_bandwidth_control_options: :class:`huaweicloudsdkworkspaceapp.v1.TwainBandwidthControlOptions`
        :param printer_bandwidth_control_enable: 是否开启打印机带宽控制。取值为：false：表示关闭。true：表示开启。
        :type printer_bandwidth_control_enable: bool
        :param printer_bandwidth_control_options: 
        :type printer_bandwidth_control_options: :class:`huaweicloudsdkworkspaceapp.v1.PrinterBandwidthControlOptions`
        :param com_bandwidth_control_enable: 是否开启串口带宽控制。取值为：false：表示关闭。true：表示开启。
        :type com_bandwidth_control_enable: bool
        :param com_bandwidth_control_options: 
        :type com_bandwidth_control_options: :class:`huaweicloudsdkworkspaceapp.v1.ComBandwidthControlOptions`
        :param file_redirection_bandwidth_control_enable: 是否开启文件重定向带宽控制。取值为：false：表示关闭。true：表示开启
        :type file_redirection_bandwidth_control_enable: bool
        :param file_redirection_bandwidth_control_options: 
        :type file_redirection_bandwidth_control_options: :class:`huaweicloudsdkworkspaceapp.v1.FileRedirectionBandwidthControlOptions`
        :param clipboard_bandwidth_control_enable: 是否开启剪切板带宽控制。取值为：false：表示关闭。true：表示开启。
        :type clipboard_bandwidth_control_enable: bool
        :param clipboard_bandwidth_control_options: 
        :type clipboard_bandwidth_control_options: :class:`huaweicloudsdkworkspaceapp.v1.ClipboardBandwidthControlOptions`
        :param secure_channel_bandwidth_control_enable: 是否开启安全通道带宽控制。取值为：false：表示关闭。true：表示开启。
        :type secure_channel_bandwidth_control_enable: bool
        :param secure_channel_bandwidth_control_options: 
        :type secure_channel_bandwidth_control_options: :class:`huaweicloudsdkworkspaceapp.v1.SecureChannelBandwidthControlOptions`
        :param camera_bandwidth_control_enable: 是否开启摄像头带宽控制。取值为：false：表示关闭。true：表示开启。
        :type camera_bandwidth_control_enable: bool
        :param camera_bandwidth_control_options: 
        :type camera_bandwidth_control_options: :class:`huaweicloudsdkworkspaceapp.v1.CameraBandwidthControlOptions`
        :param virtual_channel_bandwidth_control_enable: 是否开启虚拟通道带宽控制。取值为：false：表示关闭。true：表示开启。
        :type virtual_channel_bandwidth_control_enable: bool
        :param virtual_channel_bandwidth_control_options: 
        :type virtual_channel_bandwidth_control_options: :class:`huaweicloudsdkworkspaceapp.v1.VirtualChannelBandwidthControlOptions`
        """
        
        

        self._intelligent_data_transport_flag = None
        self._total_bandwidth_control_enable = None
        self._options = None
        self._display_bandwidth_control_enable = None
        self._display_bandwidth_control_options = None
        self._multimedia_bandwidth_control_enable = None
        self._multimedia_bandwidth_control_options = None
        self._usb_bandwidth_control_enable = None
        self._usb_bandwidth_control_options = None
        self._pcsc_bandwidth_control_enable = None
        self._pcsc_bandwidth_control_options = None
        self._twain_bandwidth_control_enable = None
        self._twain_bandwidth_control_options = None
        self._printer_bandwidth_control_enable = None
        self._printer_bandwidth_control_options = None
        self._com_bandwidth_control_enable = None
        self._com_bandwidth_control_options = None
        self._file_redirection_bandwidth_control_enable = None
        self._file_redirection_bandwidth_control_options = None
        self._clipboard_bandwidth_control_enable = None
        self._clipboard_bandwidth_control_options = None
        self._secure_channel_bandwidth_control_enable = None
        self._secure_channel_bandwidth_control_options = None
        self._camera_bandwidth_control_enable = None
        self._camera_bandwidth_control_options = None
        self._virtual_channel_bandwidth_control_enable = None
        self._virtual_channel_bandwidth_control_options = None
        self.discriminator = None

        if intelligent_data_transport_flag is not None:
            self.intelligent_data_transport_flag = intelligent_data_transport_flag
        if total_bandwidth_control_enable is not None:
            self.total_bandwidth_control_enable = total_bandwidth_control_enable
        if options is not None:
            self.options = options
        if display_bandwidth_control_enable is not None:
            self.display_bandwidth_control_enable = display_bandwidth_control_enable
        if display_bandwidth_control_options is not None:
            self.display_bandwidth_control_options = display_bandwidth_control_options
        if multimedia_bandwidth_control_enable is not None:
            self.multimedia_bandwidth_control_enable = multimedia_bandwidth_control_enable
        if multimedia_bandwidth_control_options is not None:
            self.multimedia_bandwidth_control_options = multimedia_bandwidth_control_options
        if usb_bandwidth_control_enable is not None:
            self.usb_bandwidth_control_enable = usb_bandwidth_control_enable
        if usb_bandwidth_control_options is not None:
            self.usb_bandwidth_control_options = usb_bandwidth_control_options
        if pcsc_bandwidth_control_enable is not None:
            self.pcsc_bandwidth_control_enable = pcsc_bandwidth_control_enable
        if pcsc_bandwidth_control_options is not None:
            self.pcsc_bandwidth_control_options = pcsc_bandwidth_control_options
        if twain_bandwidth_control_enable is not None:
            self.twain_bandwidth_control_enable = twain_bandwidth_control_enable
        if twain_bandwidth_control_options is not None:
            self.twain_bandwidth_control_options = twain_bandwidth_control_options
        if printer_bandwidth_control_enable is not None:
            self.printer_bandwidth_control_enable = printer_bandwidth_control_enable
        if printer_bandwidth_control_options is not None:
            self.printer_bandwidth_control_options = printer_bandwidth_control_options
        if com_bandwidth_control_enable is not None:
            self.com_bandwidth_control_enable = com_bandwidth_control_enable
        if com_bandwidth_control_options is not None:
            self.com_bandwidth_control_options = com_bandwidth_control_options
        if file_redirection_bandwidth_control_enable is not None:
            self.file_redirection_bandwidth_control_enable = file_redirection_bandwidth_control_enable
        if file_redirection_bandwidth_control_options is not None:
            self.file_redirection_bandwidth_control_options = file_redirection_bandwidth_control_options
        if clipboard_bandwidth_control_enable is not None:
            self.clipboard_bandwidth_control_enable = clipboard_bandwidth_control_enable
        if clipboard_bandwidth_control_options is not None:
            self.clipboard_bandwidth_control_options = clipboard_bandwidth_control_options
        if secure_channel_bandwidth_control_enable is not None:
            self.secure_channel_bandwidth_control_enable = secure_channel_bandwidth_control_enable
        if secure_channel_bandwidth_control_options is not None:
            self.secure_channel_bandwidth_control_options = secure_channel_bandwidth_control_options
        if camera_bandwidth_control_enable is not None:
            self.camera_bandwidth_control_enable = camera_bandwidth_control_enable
        if camera_bandwidth_control_options is not None:
            self.camera_bandwidth_control_options = camera_bandwidth_control_options
        if virtual_channel_bandwidth_control_enable is not None:
            self.virtual_channel_bandwidth_control_enable = virtual_channel_bandwidth_control_enable
        if virtual_channel_bandwidth_control_options is not None:
            self.virtual_channel_bandwidth_control_options = virtual_channel_bandwidth_control_options

    @property
    def intelligent_data_transport_flag(self):
        """Gets the intelligent_data_transport_flag of this Bandwidth.

        智能显示传输。取值为：DISABLE：表示关闭。ENABLE：表示开启。DIAGNOSTIC：诊断模式

        :return: The intelligent_data_transport_flag of this Bandwidth.
        :rtype: str
        """
        return self._intelligent_data_transport_flag

    @intelligent_data_transport_flag.setter
    def intelligent_data_transport_flag(self, intelligent_data_transport_flag):
        """Sets the intelligent_data_transport_flag of this Bandwidth.

        智能显示传输。取值为：DISABLE：表示关闭。ENABLE：表示开启。DIAGNOSTIC：诊断模式

        :param intelligent_data_transport_flag: The intelligent_data_transport_flag of this Bandwidth.
        :type intelligent_data_transport_flag: str
        """
        self._intelligent_data_transport_flag = intelligent_data_transport_flag

    @property
    def total_bandwidth_control_enable(self):
        """Gets the total_bandwidth_control_enable of this Bandwidth.

        是否开启总带宽控制。取值为：false：表示关闭。true：表示开启。

        :return: The total_bandwidth_control_enable of this Bandwidth.
        :rtype: bool
        """
        return self._total_bandwidth_control_enable

    @total_bandwidth_control_enable.setter
    def total_bandwidth_control_enable(self, total_bandwidth_control_enable):
        """Sets the total_bandwidth_control_enable of this Bandwidth.

        是否开启总带宽控制。取值为：false：表示关闭。true：表示开启。

        :param total_bandwidth_control_enable: The total_bandwidth_control_enable of this Bandwidth.
        :type total_bandwidth_control_enable: bool
        """
        self._total_bandwidth_control_enable = total_bandwidth_control_enable

    @property
    def options(self):
        """Gets the options of this Bandwidth.

        :return: The options of this Bandwidth.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.TotalBandwidthControlOptions`
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this Bandwidth.

        :param options: The options of this Bandwidth.
        :type options: :class:`huaweicloudsdkworkspaceapp.v1.TotalBandwidthControlOptions`
        """
        self._options = options

    @property
    def display_bandwidth_control_enable(self):
        """Gets the display_bandwidth_control_enable of this Bandwidth.

        是否开启显示带宽控制。取值为：false：表示关闭。true：表示开启。

        :return: The display_bandwidth_control_enable of this Bandwidth.
        :rtype: bool
        """
        return self._display_bandwidth_control_enable

    @display_bandwidth_control_enable.setter
    def display_bandwidth_control_enable(self, display_bandwidth_control_enable):
        """Sets the display_bandwidth_control_enable of this Bandwidth.

        是否开启显示带宽控制。取值为：false：表示关闭。true：表示开启。

        :param display_bandwidth_control_enable: The display_bandwidth_control_enable of this Bandwidth.
        :type display_bandwidth_control_enable: bool
        """
        self._display_bandwidth_control_enable = display_bandwidth_control_enable

    @property
    def display_bandwidth_control_options(self):
        """Gets the display_bandwidth_control_options of this Bandwidth.

        :return: The display_bandwidth_control_options of this Bandwidth.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.DisplayBandwidthControlOptions`
        """
        return self._display_bandwidth_control_options

    @display_bandwidth_control_options.setter
    def display_bandwidth_control_options(self, display_bandwidth_control_options):
        """Sets the display_bandwidth_control_options of this Bandwidth.

        :param display_bandwidth_control_options: The display_bandwidth_control_options of this Bandwidth.
        :type display_bandwidth_control_options: :class:`huaweicloudsdkworkspaceapp.v1.DisplayBandwidthControlOptions`
        """
        self._display_bandwidth_control_options = display_bandwidth_control_options

    @property
    def multimedia_bandwidth_control_enable(self):
        """Gets the multimedia_bandwidth_control_enable of this Bandwidth.

        是否开启多媒体带宽控制。取值为：false：表示关闭。true：表示开启。

        :return: The multimedia_bandwidth_control_enable of this Bandwidth.
        :rtype: bool
        """
        return self._multimedia_bandwidth_control_enable

    @multimedia_bandwidth_control_enable.setter
    def multimedia_bandwidth_control_enable(self, multimedia_bandwidth_control_enable):
        """Sets the multimedia_bandwidth_control_enable of this Bandwidth.

        是否开启多媒体带宽控制。取值为：false：表示关闭。true：表示开启。

        :param multimedia_bandwidth_control_enable: The multimedia_bandwidth_control_enable of this Bandwidth.
        :type multimedia_bandwidth_control_enable: bool
        """
        self._multimedia_bandwidth_control_enable = multimedia_bandwidth_control_enable

    @property
    def multimedia_bandwidth_control_options(self):
        """Gets the multimedia_bandwidth_control_options of this Bandwidth.

        :return: The multimedia_bandwidth_control_options of this Bandwidth.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.MultimediaBandwidthControlOptions`
        """
        return self._multimedia_bandwidth_control_options

    @multimedia_bandwidth_control_options.setter
    def multimedia_bandwidth_control_options(self, multimedia_bandwidth_control_options):
        """Sets the multimedia_bandwidth_control_options of this Bandwidth.

        :param multimedia_bandwidth_control_options: The multimedia_bandwidth_control_options of this Bandwidth.
        :type multimedia_bandwidth_control_options: :class:`huaweicloudsdkworkspaceapp.v1.MultimediaBandwidthControlOptions`
        """
        self._multimedia_bandwidth_control_options = multimedia_bandwidth_control_options

    @property
    def usb_bandwidth_control_enable(self):
        """Gets the usb_bandwidth_control_enable of this Bandwidth.

        是否开启USB带宽控制。取值为：false：表示关闭。true：表示开启。

        :return: The usb_bandwidth_control_enable of this Bandwidth.
        :rtype: bool
        """
        return self._usb_bandwidth_control_enable

    @usb_bandwidth_control_enable.setter
    def usb_bandwidth_control_enable(self, usb_bandwidth_control_enable):
        """Sets the usb_bandwidth_control_enable of this Bandwidth.

        是否开启USB带宽控制。取值为：false：表示关闭。true：表示开启。

        :param usb_bandwidth_control_enable: The usb_bandwidth_control_enable of this Bandwidth.
        :type usb_bandwidth_control_enable: bool
        """
        self._usb_bandwidth_control_enable = usb_bandwidth_control_enable

    @property
    def usb_bandwidth_control_options(self):
        """Gets the usb_bandwidth_control_options of this Bandwidth.

        :return: The usb_bandwidth_control_options of this Bandwidth.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UsbBandwidthControlOptions`
        """
        return self._usb_bandwidth_control_options

    @usb_bandwidth_control_options.setter
    def usb_bandwidth_control_options(self, usb_bandwidth_control_options):
        """Sets the usb_bandwidth_control_options of this Bandwidth.

        :param usb_bandwidth_control_options: The usb_bandwidth_control_options of this Bandwidth.
        :type usb_bandwidth_control_options: :class:`huaweicloudsdkworkspaceapp.v1.UsbBandwidthControlOptions`
        """
        self._usb_bandwidth_control_options = usb_bandwidth_control_options

    @property
    def pcsc_bandwidth_control_enable(self):
        """Gets the pcsc_bandwidth_control_enable of this Bandwidth.

        是否开启PCSC控制。取值为：false：表示关闭。true：表示开启。

        :return: The pcsc_bandwidth_control_enable of this Bandwidth.
        :rtype: bool
        """
        return self._pcsc_bandwidth_control_enable

    @pcsc_bandwidth_control_enable.setter
    def pcsc_bandwidth_control_enable(self, pcsc_bandwidth_control_enable):
        """Sets the pcsc_bandwidth_control_enable of this Bandwidth.

        是否开启PCSC控制。取值为：false：表示关闭。true：表示开启。

        :param pcsc_bandwidth_control_enable: The pcsc_bandwidth_control_enable of this Bandwidth.
        :type pcsc_bandwidth_control_enable: bool
        """
        self._pcsc_bandwidth_control_enable = pcsc_bandwidth_control_enable

    @property
    def pcsc_bandwidth_control_options(self):
        """Gets the pcsc_bandwidth_control_options of this Bandwidth.

        :return: The pcsc_bandwidth_control_options of this Bandwidth.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PcscBandwidthControlOptions`
        """
        return self._pcsc_bandwidth_control_options

    @pcsc_bandwidth_control_options.setter
    def pcsc_bandwidth_control_options(self, pcsc_bandwidth_control_options):
        """Sets the pcsc_bandwidth_control_options of this Bandwidth.

        :param pcsc_bandwidth_control_options: The pcsc_bandwidth_control_options of this Bandwidth.
        :type pcsc_bandwidth_control_options: :class:`huaweicloudsdkworkspaceapp.v1.PcscBandwidthControlOptions`
        """
        self._pcsc_bandwidth_control_options = pcsc_bandwidth_control_options

    @property
    def twain_bandwidth_control_enable(self):
        """Gets the twain_bandwidth_control_enable of this Bandwidth.

        是否开启TWAIN带宽控制。取值为：false：表示关闭。true：表示开启。

        :return: The twain_bandwidth_control_enable of this Bandwidth.
        :rtype: bool
        """
        return self._twain_bandwidth_control_enable

    @twain_bandwidth_control_enable.setter
    def twain_bandwidth_control_enable(self, twain_bandwidth_control_enable):
        """Sets the twain_bandwidth_control_enable of this Bandwidth.

        是否开启TWAIN带宽控制。取值为：false：表示关闭。true：表示开启。

        :param twain_bandwidth_control_enable: The twain_bandwidth_control_enable of this Bandwidth.
        :type twain_bandwidth_control_enable: bool
        """
        self._twain_bandwidth_control_enable = twain_bandwidth_control_enable

    @property
    def twain_bandwidth_control_options(self):
        """Gets the twain_bandwidth_control_options of this Bandwidth.

        :return: The twain_bandwidth_control_options of this Bandwidth.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.TwainBandwidthControlOptions`
        """
        return self._twain_bandwidth_control_options

    @twain_bandwidth_control_options.setter
    def twain_bandwidth_control_options(self, twain_bandwidth_control_options):
        """Sets the twain_bandwidth_control_options of this Bandwidth.

        :param twain_bandwidth_control_options: The twain_bandwidth_control_options of this Bandwidth.
        :type twain_bandwidth_control_options: :class:`huaweicloudsdkworkspaceapp.v1.TwainBandwidthControlOptions`
        """
        self._twain_bandwidth_control_options = twain_bandwidth_control_options

    @property
    def printer_bandwidth_control_enable(self):
        """Gets the printer_bandwidth_control_enable of this Bandwidth.

        是否开启打印机带宽控制。取值为：false：表示关闭。true：表示开启。

        :return: The printer_bandwidth_control_enable of this Bandwidth.
        :rtype: bool
        """
        return self._printer_bandwidth_control_enable

    @printer_bandwidth_control_enable.setter
    def printer_bandwidth_control_enable(self, printer_bandwidth_control_enable):
        """Sets the printer_bandwidth_control_enable of this Bandwidth.

        是否开启打印机带宽控制。取值为：false：表示关闭。true：表示开启。

        :param printer_bandwidth_control_enable: The printer_bandwidth_control_enable of this Bandwidth.
        :type printer_bandwidth_control_enable: bool
        """
        self._printer_bandwidth_control_enable = printer_bandwidth_control_enable

    @property
    def printer_bandwidth_control_options(self):
        """Gets the printer_bandwidth_control_options of this Bandwidth.

        :return: The printer_bandwidth_control_options of this Bandwidth.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PrinterBandwidthControlOptions`
        """
        return self._printer_bandwidth_control_options

    @printer_bandwidth_control_options.setter
    def printer_bandwidth_control_options(self, printer_bandwidth_control_options):
        """Sets the printer_bandwidth_control_options of this Bandwidth.

        :param printer_bandwidth_control_options: The printer_bandwidth_control_options of this Bandwidth.
        :type printer_bandwidth_control_options: :class:`huaweicloudsdkworkspaceapp.v1.PrinterBandwidthControlOptions`
        """
        self._printer_bandwidth_control_options = printer_bandwidth_control_options

    @property
    def com_bandwidth_control_enable(self):
        """Gets the com_bandwidth_control_enable of this Bandwidth.

        是否开启串口带宽控制。取值为：false：表示关闭。true：表示开启。

        :return: The com_bandwidth_control_enable of this Bandwidth.
        :rtype: bool
        """
        return self._com_bandwidth_control_enable

    @com_bandwidth_control_enable.setter
    def com_bandwidth_control_enable(self, com_bandwidth_control_enable):
        """Sets the com_bandwidth_control_enable of this Bandwidth.

        是否开启串口带宽控制。取值为：false：表示关闭。true：表示开启。

        :param com_bandwidth_control_enable: The com_bandwidth_control_enable of this Bandwidth.
        :type com_bandwidth_control_enable: bool
        """
        self._com_bandwidth_control_enable = com_bandwidth_control_enable

    @property
    def com_bandwidth_control_options(self):
        """Gets the com_bandwidth_control_options of this Bandwidth.

        :return: The com_bandwidth_control_options of this Bandwidth.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ComBandwidthControlOptions`
        """
        return self._com_bandwidth_control_options

    @com_bandwidth_control_options.setter
    def com_bandwidth_control_options(self, com_bandwidth_control_options):
        """Sets the com_bandwidth_control_options of this Bandwidth.

        :param com_bandwidth_control_options: The com_bandwidth_control_options of this Bandwidth.
        :type com_bandwidth_control_options: :class:`huaweicloudsdkworkspaceapp.v1.ComBandwidthControlOptions`
        """
        self._com_bandwidth_control_options = com_bandwidth_control_options

    @property
    def file_redirection_bandwidth_control_enable(self):
        """Gets the file_redirection_bandwidth_control_enable of this Bandwidth.

        是否开启文件重定向带宽控制。取值为：false：表示关闭。true：表示开启

        :return: The file_redirection_bandwidth_control_enable of this Bandwidth.
        :rtype: bool
        """
        return self._file_redirection_bandwidth_control_enable

    @file_redirection_bandwidth_control_enable.setter
    def file_redirection_bandwidth_control_enable(self, file_redirection_bandwidth_control_enable):
        """Sets the file_redirection_bandwidth_control_enable of this Bandwidth.

        是否开启文件重定向带宽控制。取值为：false：表示关闭。true：表示开启

        :param file_redirection_bandwidth_control_enable: The file_redirection_bandwidth_control_enable of this Bandwidth.
        :type file_redirection_bandwidth_control_enable: bool
        """
        self._file_redirection_bandwidth_control_enable = file_redirection_bandwidth_control_enable

    @property
    def file_redirection_bandwidth_control_options(self):
        """Gets the file_redirection_bandwidth_control_options of this Bandwidth.

        :return: The file_redirection_bandwidth_control_options of this Bandwidth.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.FileRedirectionBandwidthControlOptions`
        """
        return self._file_redirection_bandwidth_control_options

    @file_redirection_bandwidth_control_options.setter
    def file_redirection_bandwidth_control_options(self, file_redirection_bandwidth_control_options):
        """Sets the file_redirection_bandwidth_control_options of this Bandwidth.

        :param file_redirection_bandwidth_control_options: The file_redirection_bandwidth_control_options of this Bandwidth.
        :type file_redirection_bandwidth_control_options: :class:`huaweicloudsdkworkspaceapp.v1.FileRedirectionBandwidthControlOptions`
        """
        self._file_redirection_bandwidth_control_options = file_redirection_bandwidth_control_options

    @property
    def clipboard_bandwidth_control_enable(self):
        """Gets the clipboard_bandwidth_control_enable of this Bandwidth.

        是否开启剪切板带宽控制。取值为：false：表示关闭。true：表示开启。

        :return: The clipboard_bandwidth_control_enable of this Bandwidth.
        :rtype: bool
        """
        return self._clipboard_bandwidth_control_enable

    @clipboard_bandwidth_control_enable.setter
    def clipboard_bandwidth_control_enable(self, clipboard_bandwidth_control_enable):
        """Sets the clipboard_bandwidth_control_enable of this Bandwidth.

        是否开启剪切板带宽控制。取值为：false：表示关闭。true：表示开启。

        :param clipboard_bandwidth_control_enable: The clipboard_bandwidth_control_enable of this Bandwidth.
        :type clipboard_bandwidth_control_enable: bool
        """
        self._clipboard_bandwidth_control_enable = clipboard_bandwidth_control_enable

    @property
    def clipboard_bandwidth_control_options(self):
        """Gets the clipboard_bandwidth_control_options of this Bandwidth.

        :return: The clipboard_bandwidth_control_options of this Bandwidth.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ClipboardBandwidthControlOptions`
        """
        return self._clipboard_bandwidth_control_options

    @clipboard_bandwidth_control_options.setter
    def clipboard_bandwidth_control_options(self, clipboard_bandwidth_control_options):
        """Sets the clipboard_bandwidth_control_options of this Bandwidth.

        :param clipboard_bandwidth_control_options: The clipboard_bandwidth_control_options of this Bandwidth.
        :type clipboard_bandwidth_control_options: :class:`huaweicloudsdkworkspaceapp.v1.ClipboardBandwidthControlOptions`
        """
        self._clipboard_bandwidth_control_options = clipboard_bandwidth_control_options

    @property
    def secure_channel_bandwidth_control_enable(self):
        """Gets the secure_channel_bandwidth_control_enable of this Bandwidth.

        是否开启安全通道带宽控制。取值为：false：表示关闭。true：表示开启。

        :return: The secure_channel_bandwidth_control_enable of this Bandwidth.
        :rtype: bool
        """
        return self._secure_channel_bandwidth_control_enable

    @secure_channel_bandwidth_control_enable.setter
    def secure_channel_bandwidth_control_enable(self, secure_channel_bandwidth_control_enable):
        """Sets the secure_channel_bandwidth_control_enable of this Bandwidth.

        是否开启安全通道带宽控制。取值为：false：表示关闭。true：表示开启。

        :param secure_channel_bandwidth_control_enable: The secure_channel_bandwidth_control_enable of this Bandwidth.
        :type secure_channel_bandwidth_control_enable: bool
        """
        self._secure_channel_bandwidth_control_enable = secure_channel_bandwidth_control_enable

    @property
    def secure_channel_bandwidth_control_options(self):
        """Gets the secure_channel_bandwidth_control_options of this Bandwidth.

        :return: The secure_channel_bandwidth_control_options of this Bandwidth.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.SecureChannelBandwidthControlOptions`
        """
        return self._secure_channel_bandwidth_control_options

    @secure_channel_bandwidth_control_options.setter
    def secure_channel_bandwidth_control_options(self, secure_channel_bandwidth_control_options):
        """Sets the secure_channel_bandwidth_control_options of this Bandwidth.

        :param secure_channel_bandwidth_control_options: The secure_channel_bandwidth_control_options of this Bandwidth.
        :type secure_channel_bandwidth_control_options: :class:`huaweicloudsdkworkspaceapp.v1.SecureChannelBandwidthControlOptions`
        """
        self._secure_channel_bandwidth_control_options = secure_channel_bandwidth_control_options

    @property
    def camera_bandwidth_control_enable(self):
        """Gets the camera_bandwidth_control_enable of this Bandwidth.

        是否开启摄像头带宽控制。取值为：false：表示关闭。true：表示开启。

        :return: The camera_bandwidth_control_enable of this Bandwidth.
        :rtype: bool
        """
        return self._camera_bandwidth_control_enable

    @camera_bandwidth_control_enable.setter
    def camera_bandwidth_control_enable(self, camera_bandwidth_control_enable):
        """Sets the camera_bandwidth_control_enable of this Bandwidth.

        是否开启摄像头带宽控制。取值为：false：表示关闭。true：表示开启。

        :param camera_bandwidth_control_enable: The camera_bandwidth_control_enable of this Bandwidth.
        :type camera_bandwidth_control_enable: bool
        """
        self._camera_bandwidth_control_enable = camera_bandwidth_control_enable

    @property
    def camera_bandwidth_control_options(self):
        """Gets the camera_bandwidth_control_options of this Bandwidth.

        :return: The camera_bandwidth_control_options of this Bandwidth.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CameraBandwidthControlOptions`
        """
        return self._camera_bandwidth_control_options

    @camera_bandwidth_control_options.setter
    def camera_bandwidth_control_options(self, camera_bandwidth_control_options):
        """Sets the camera_bandwidth_control_options of this Bandwidth.

        :param camera_bandwidth_control_options: The camera_bandwidth_control_options of this Bandwidth.
        :type camera_bandwidth_control_options: :class:`huaweicloudsdkworkspaceapp.v1.CameraBandwidthControlOptions`
        """
        self._camera_bandwidth_control_options = camera_bandwidth_control_options

    @property
    def virtual_channel_bandwidth_control_enable(self):
        """Gets the virtual_channel_bandwidth_control_enable of this Bandwidth.

        是否开启虚拟通道带宽控制。取值为：false：表示关闭。true：表示开启。

        :return: The virtual_channel_bandwidth_control_enable of this Bandwidth.
        :rtype: bool
        """
        return self._virtual_channel_bandwidth_control_enable

    @virtual_channel_bandwidth_control_enable.setter
    def virtual_channel_bandwidth_control_enable(self, virtual_channel_bandwidth_control_enable):
        """Sets the virtual_channel_bandwidth_control_enable of this Bandwidth.

        是否开启虚拟通道带宽控制。取值为：false：表示关闭。true：表示开启。

        :param virtual_channel_bandwidth_control_enable: The virtual_channel_bandwidth_control_enable of this Bandwidth.
        :type virtual_channel_bandwidth_control_enable: bool
        """
        self._virtual_channel_bandwidth_control_enable = virtual_channel_bandwidth_control_enable

    @property
    def virtual_channel_bandwidth_control_options(self):
        """Gets the virtual_channel_bandwidth_control_options of this Bandwidth.

        :return: The virtual_channel_bandwidth_control_options of this Bandwidth.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.VirtualChannelBandwidthControlOptions`
        """
        return self._virtual_channel_bandwidth_control_options

    @virtual_channel_bandwidth_control_options.setter
    def virtual_channel_bandwidth_control_options(self, virtual_channel_bandwidth_control_options):
        """Sets the virtual_channel_bandwidth_control_options of this Bandwidth.

        :param virtual_channel_bandwidth_control_options: The virtual_channel_bandwidth_control_options of this Bandwidth.
        :type virtual_channel_bandwidth_control_options: :class:`huaweicloudsdkworkspaceapp.v1.VirtualChannelBandwidthControlOptions`
        """
        self._virtual_channel_bandwidth_control_options = virtual_channel_bandwidth_control_options

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
        if not isinstance(other, Bandwidth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
