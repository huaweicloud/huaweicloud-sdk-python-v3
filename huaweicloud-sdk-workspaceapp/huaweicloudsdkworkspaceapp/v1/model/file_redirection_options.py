# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FileRedirectionOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fluid_control_switch_enable': 'bool',
        'fluid_control_options': 'FileRedirectionOptionsFluidControlOptions',
        'compression_switch_enable': 'bool',
        'compression_switch_options': 'FileRedirectionOptionsCompressionSwitchOptions',
        'linux_file_size_supported_enable': 'bool',
        'linux_file_size_supported_options': 'FileRedirectionOptionsLinuxFileSizeSupportedOptions',
        'linux_root_mount_switch_enable': 'bool',
        'linux_root_dir_list': 'str',
        'linux_file_mount_path': 'str',
        'linux_fixed_drive_file_system_format': 'str',
        'linux_removable_drive_file_system_format': 'str',
        'linux_cdrom_drive_file_system_format': 'str',
        'linux_network_drive_file_system_format': 'str',
        'path_separator': 'str',
        'fixed_drive_enable': 'bool',
        'removable_drive_enable': 'bool',
        'cd_rom_drive_enable': 'bool',
        'network_drive_enable': 'bool'
    }

    attribute_map = {
        'fluid_control_switch_enable': 'fluid_control_switch_enable',
        'fluid_control_options': 'fluid_control_options',
        'compression_switch_enable': 'compression_switch_enable',
        'compression_switch_options': 'compression_switch_options',
        'linux_file_size_supported_enable': 'linux_file_size_supported_enable',
        'linux_file_size_supported_options': 'linux_file_size_supported_options',
        'linux_root_mount_switch_enable': 'linux_root_mount_switch_enable',
        'linux_root_dir_list': 'linux_root_dir_list',
        'linux_file_mount_path': 'linux_file_mount_path',
        'linux_fixed_drive_file_system_format': 'linux_fixed_drive_file_system_format',
        'linux_removable_drive_file_system_format': 'linux_removable_drive_file_system_format',
        'linux_cdrom_drive_file_system_format': 'linux_cdrom_drive_file_system_format',
        'linux_network_drive_file_system_format': 'linux_network_drive_file_system_format',
        'path_separator': 'path_separator',
        'fixed_drive_enable': 'fixed_drive_enable',
        'removable_drive_enable': 'removable_drive_enable',
        'cd_rom_drive_enable': 'cd_rom_drive_enable',
        'network_drive_enable': 'network_drive_enable'
    }

    def __init__(self, fluid_control_switch_enable=None, fluid_control_options=None, compression_switch_enable=None, compression_switch_options=None, linux_file_size_supported_enable=None, linux_file_size_supported_options=None, linux_root_mount_switch_enable=None, linux_root_dir_list=None, linux_file_mount_path=None, linux_fixed_drive_file_system_format=None, linux_removable_drive_file_system_format=None, linux_cdrom_drive_file_system_format=None, linux_network_drive_file_system_format=None, path_separator=None, fixed_drive_enable=None, removable_drive_enable=None, cd_rom_drive_enable=None, network_drive_enable=None):
        """FileRedirectionOptions

        The model defined in huaweicloud sdk

        :param fluid_control_switch_enable: 是否开启流控开关。取值为： false：表示关闭。 true：表示开启。
        :type fluid_control_switch_enable: bool
        :param fluid_control_options: 
        :type fluid_control_options: :class:`huaweicloudsdkworkspaceapp.v1.FileRedirectionOptionsFluidControlOptions`
        :param compression_switch_enable: 是否开启压缩开关。取值为： false：表示关闭。 true：表示开启。
        :type compression_switch_enable: bool
        :param compression_switch_options: 
        :type compression_switch_options: :class:`huaweicloudsdkworkspaceapp.v1.FileRedirectionOptionsCompressionSwitchOptions`
        :param linux_file_size_supported_enable: 是否开启Linux支持设置文件大小。取值为： false：表示关闭。 true：表示开启。
        :type linux_file_size_supported_enable: bool
        :param linux_file_size_supported_options: 
        :type linux_file_size_supported_options: :class:`huaweicloudsdkworkspaceapp.v1.FileRedirectionOptionsLinuxFileSizeSupportedOptions`
        :param linux_root_mount_switch_enable: 是否开启Linux根目录挂载开关。取值为： false：表示关闭。 true：表示开启。
        :type linux_root_mount_switch_enable: bool
        :param linux_root_dir_list: Linux根目录挂载路径。默认：\&quot;\\home\&quot;。
        :type linux_root_dir_list: str
        :param linux_file_mount_path: Linux文件系统挂载路径。默认：\&quot;\\media|\\Volumes|\\swdb\\mnt|\\home|\\storage|\\tmp|\\run\\media\&quot;。
        :type linux_file_mount_path: str
        :param linux_fixed_drive_file_system_format: Linux固定驱动器文件系统格式。
        :type linux_fixed_drive_file_system_format: str
        :param linux_removable_drive_file_system_format: Linux可移动驱动器文件系统格式。默认：\&quot;vfat|ntfs|msdos|fuseblk|sdcardfs|exfat|fuse.fdredir\&quot;。
        :type linux_removable_drive_file_system_format: str
        :param linux_cdrom_drive_file_system_format: Linux光盘驱动器文件系统格式。默认：\&quot;cd9660|iso9660|udf\&quot;。
        :type linux_cdrom_drive_file_system_format: str
        :param linux_network_drive_file_system_format: Linux网络驱动器文件系统格式。默认：\&quot;smbfs|afpfs|cifs\&quot;。
        :type linux_network_drive_file_system_format: str
        :param path_separator: 路径分隔符。默认：\&quot;|\&quot;。
        :type path_separator: str
        :param fixed_drive_enable: 是否开启固定驱动器（如: 本地磁盘）。取值为： false：表示关闭。 true：表示开启。
        :type fixed_drive_enable: bool
        :param removable_drive_enable: 是否开启可移除驱动器（如: U盘）。取值为： false：表示关闭。 true：表示开启。
        :type removable_drive_enable: bool
        :param cd_rom_drive_enable: 是否开启光盘驱动器。取值为： false：表示关闭。 true：表示开启。
        :type cd_rom_drive_enable: bool
        :param network_drive_enable: 是否开启网络驱动器。取值为： false：表示关闭。 true：表示开启。
        :type network_drive_enable: bool
        """
        
        

        self._fluid_control_switch_enable = None
        self._fluid_control_options = None
        self._compression_switch_enable = None
        self._compression_switch_options = None
        self._linux_file_size_supported_enable = None
        self._linux_file_size_supported_options = None
        self._linux_root_mount_switch_enable = None
        self._linux_root_dir_list = None
        self._linux_file_mount_path = None
        self._linux_fixed_drive_file_system_format = None
        self._linux_removable_drive_file_system_format = None
        self._linux_cdrom_drive_file_system_format = None
        self._linux_network_drive_file_system_format = None
        self._path_separator = None
        self._fixed_drive_enable = None
        self._removable_drive_enable = None
        self._cd_rom_drive_enable = None
        self._network_drive_enable = None
        self.discriminator = None

        if fluid_control_switch_enable is not None:
            self.fluid_control_switch_enable = fluid_control_switch_enable
        if fluid_control_options is not None:
            self.fluid_control_options = fluid_control_options
        if compression_switch_enable is not None:
            self.compression_switch_enable = compression_switch_enable
        if compression_switch_options is not None:
            self.compression_switch_options = compression_switch_options
        if linux_file_size_supported_enable is not None:
            self.linux_file_size_supported_enable = linux_file_size_supported_enable
        if linux_file_size_supported_options is not None:
            self.linux_file_size_supported_options = linux_file_size_supported_options
        if linux_root_mount_switch_enable is not None:
            self.linux_root_mount_switch_enable = linux_root_mount_switch_enable
        if linux_root_dir_list is not None:
            self.linux_root_dir_list = linux_root_dir_list
        if linux_file_mount_path is not None:
            self.linux_file_mount_path = linux_file_mount_path
        if linux_fixed_drive_file_system_format is not None:
            self.linux_fixed_drive_file_system_format = linux_fixed_drive_file_system_format
        if linux_removable_drive_file_system_format is not None:
            self.linux_removable_drive_file_system_format = linux_removable_drive_file_system_format
        if linux_cdrom_drive_file_system_format is not None:
            self.linux_cdrom_drive_file_system_format = linux_cdrom_drive_file_system_format
        if linux_network_drive_file_system_format is not None:
            self.linux_network_drive_file_system_format = linux_network_drive_file_system_format
        if path_separator is not None:
            self.path_separator = path_separator
        if fixed_drive_enable is not None:
            self.fixed_drive_enable = fixed_drive_enable
        if removable_drive_enable is not None:
            self.removable_drive_enable = removable_drive_enable
        if cd_rom_drive_enable is not None:
            self.cd_rom_drive_enable = cd_rom_drive_enable
        if network_drive_enable is not None:
            self.network_drive_enable = network_drive_enable

    @property
    def fluid_control_switch_enable(self):
        """Gets the fluid_control_switch_enable of this FileRedirectionOptions.

        是否开启流控开关。取值为： false：表示关闭。 true：表示开启。

        :return: The fluid_control_switch_enable of this FileRedirectionOptions.
        :rtype: bool
        """
        return self._fluid_control_switch_enable

    @fluid_control_switch_enable.setter
    def fluid_control_switch_enable(self, fluid_control_switch_enable):
        """Sets the fluid_control_switch_enable of this FileRedirectionOptions.

        是否开启流控开关。取值为： false：表示关闭。 true：表示开启。

        :param fluid_control_switch_enable: The fluid_control_switch_enable of this FileRedirectionOptions.
        :type fluid_control_switch_enable: bool
        """
        self._fluid_control_switch_enable = fluid_control_switch_enable

    @property
    def fluid_control_options(self):
        """Gets the fluid_control_options of this FileRedirectionOptions.

        :return: The fluid_control_options of this FileRedirectionOptions.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.FileRedirectionOptionsFluidControlOptions`
        """
        return self._fluid_control_options

    @fluid_control_options.setter
    def fluid_control_options(self, fluid_control_options):
        """Sets the fluid_control_options of this FileRedirectionOptions.

        :param fluid_control_options: The fluid_control_options of this FileRedirectionOptions.
        :type fluid_control_options: :class:`huaweicloudsdkworkspaceapp.v1.FileRedirectionOptionsFluidControlOptions`
        """
        self._fluid_control_options = fluid_control_options

    @property
    def compression_switch_enable(self):
        """Gets the compression_switch_enable of this FileRedirectionOptions.

        是否开启压缩开关。取值为： false：表示关闭。 true：表示开启。

        :return: The compression_switch_enable of this FileRedirectionOptions.
        :rtype: bool
        """
        return self._compression_switch_enable

    @compression_switch_enable.setter
    def compression_switch_enable(self, compression_switch_enable):
        """Sets the compression_switch_enable of this FileRedirectionOptions.

        是否开启压缩开关。取值为： false：表示关闭。 true：表示开启。

        :param compression_switch_enable: The compression_switch_enable of this FileRedirectionOptions.
        :type compression_switch_enable: bool
        """
        self._compression_switch_enable = compression_switch_enable

    @property
    def compression_switch_options(self):
        """Gets the compression_switch_options of this FileRedirectionOptions.

        :return: The compression_switch_options of this FileRedirectionOptions.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.FileRedirectionOptionsCompressionSwitchOptions`
        """
        return self._compression_switch_options

    @compression_switch_options.setter
    def compression_switch_options(self, compression_switch_options):
        """Sets the compression_switch_options of this FileRedirectionOptions.

        :param compression_switch_options: The compression_switch_options of this FileRedirectionOptions.
        :type compression_switch_options: :class:`huaweicloudsdkworkspaceapp.v1.FileRedirectionOptionsCompressionSwitchOptions`
        """
        self._compression_switch_options = compression_switch_options

    @property
    def linux_file_size_supported_enable(self):
        """Gets the linux_file_size_supported_enable of this FileRedirectionOptions.

        是否开启Linux支持设置文件大小。取值为： false：表示关闭。 true：表示开启。

        :return: The linux_file_size_supported_enable of this FileRedirectionOptions.
        :rtype: bool
        """
        return self._linux_file_size_supported_enable

    @linux_file_size_supported_enable.setter
    def linux_file_size_supported_enable(self, linux_file_size_supported_enable):
        """Sets the linux_file_size_supported_enable of this FileRedirectionOptions.

        是否开启Linux支持设置文件大小。取值为： false：表示关闭。 true：表示开启。

        :param linux_file_size_supported_enable: The linux_file_size_supported_enable of this FileRedirectionOptions.
        :type linux_file_size_supported_enable: bool
        """
        self._linux_file_size_supported_enable = linux_file_size_supported_enable

    @property
    def linux_file_size_supported_options(self):
        """Gets the linux_file_size_supported_options of this FileRedirectionOptions.

        :return: The linux_file_size_supported_options of this FileRedirectionOptions.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.FileRedirectionOptionsLinuxFileSizeSupportedOptions`
        """
        return self._linux_file_size_supported_options

    @linux_file_size_supported_options.setter
    def linux_file_size_supported_options(self, linux_file_size_supported_options):
        """Sets the linux_file_size_supported_options of this FileRedirectionOptions.

        :param linux_file_size_supported_options: The linux_file_size_supported_options of this FileRedirectionOptions.
        :type linux_file_size_supported_options: :class:`huaweicloudsdkworkspaceapp.v1.FileRedirectionOptionsLinuxFileSizeSupportedOptions`
        """
        self._linux_file_size_supported_options = linux_file_size_supported_options

    @property
    def linux_root_mount_switch_enable(self):
        """Gets the linux_root_mount_switch_enable of this FileRedirectionOptions.

        是否开启Linux根目录挂载开关。取值为： false：表示关闭。 true：表示开启。

        :return: The linux_root_mount_switch_enable of this FileRedirectionOptions.
        :rtype: bool
        """
        return self._linux_root_mount_switch_enable

    @linux_root_mount_switch_enable.setter
    def linux_root_mount_switch_enable(self, linux_root_mount_switch_enable):
        """Sets the linux_root_mount_switch_enable of this FileRedirectionOptions.

        是否开启Linux根目录挂载开关。取值为： false：表示关闭。 true：表示开启。

        :param linux_root_mount_switch_enable: The linux_root_mount_switch_enable of this FileRedirectionOptions.
        :type linux_root_mount_switch_enable: bool
        """
        self._linux_root_mount_switch_enable = linux_root_mount_switch_enable

    @property
    def linux_root_dir_list(self):
        """Gets the linux_root_dir_list of this FileRedirectionOptions.

        Linux根目录挂载路径。默认：\"\\home\"。

        :return: The linux_root_dir_list of this FileRedirectionOptions.
        :rtype: str
        """
        return self._linux_root_dir_list

    @linux_root_dir_list.setter
    def linux_root_dir_list(self, linux_root_dir_list):
        """Sets the linux_root_dir_list of this FileRedirectionOptions.

        Linux根目录挂载路径。默认：\"\\home\"。

        :param linux_root_dir_list: The linux_root_dir_list of this FileRedirectionOptions.
        :type linux_root_dir_list: str
        """
        self._linux_root_dir_list = linux_root_dir_list

    @property
    def linux_file_mount_path(self):
        """Gets the linux_file_mount_path of this FileRedirectionOptions.

        Linux文件系统挂载路径。默认：\"\\media|\\Volumes|\\swdb\\mnt|\\home|\\storage|\\tmp|\\run\\media\"。

        :return: The linux_file_mount_path of this FileRedirectionOptions.
        :rtype: str
        """
        return self._linux_file_mount_path

    @linux_file_mount_path.setter
    def linux_file_mount_path(self, linux_file_mount_path):
        """Sets the linux_file_mount_path of this FileRedirectionOptions.

        Linux文件系统挂载路径。默认：\"\\media|\\Volumes|\\swdb\\mnt|\\home|\\storage|\\tmp|\\run\\media\"。

        :param linux_file_mount_path: The linux_file_mount_path of this FileRedirectionOptions.
        :type linux_file_mount_path: str
        """
        self._linux_file_mount_path = linux_file_mount_path

    @property
    def linux_fixed_drive_file_system_format(self):
        """Gets the linux_fixed_drive_file_system_format of this FileRedirectionOptions.

        Linux固定驱动器文件系统格式。

        :return: The linux_fixed_drive_file_system_format of this FileRedirectionOptions.
        :rtype: str
        """
        return self._linux_fixed_drive_file_system_format

    @linux_fixed_drive_file_system_format.setter
    def linux_fixed_drive_file_system_format(self, linux_fixed_drive_file_system_format):
        """Sets the linux_fixed_drive_file_system_format of this FileRedirectionOptions.

        Linux固定驱动器文件系统格式。

        :param linux_fixed_drive_file_system_format: The linux_fixed_drive_file_system_format of this FileRedirectionOptions.
        :type linux_fixed_drive_file_system_format: str
        """
        self._linux_fixed_drive_file_system_format = linux_fixed_drive_file_system_format

    @property
    def linux_removable_drive_file_system_format(self):
        """Gets the linux_removable_drive_file_system_format of this FileRedirectionOptions.

        Linux可移动驱动器文件系统格式。默认：\"vfat|ntfs|msdos|fuseblk|sdcardfs|exfat|fuse.fdredir\"。

        :return: The linux_removable_drive_file_system_format of this FileRedirectionOptions.
        :rtype: str
        """
        return self._linux_removable_drive_file_system_format

    @linux_removable_drive_file_system_format.setter
    def linux_removable_drive_file_system_format(self, linux_removable_drive_file_system_format):
        """Sets the linux_removable_drive_file_system_format of this FileRedirectionOptions.

        Linux可移动驱动器文件系统格式。默认：\"vfat|ntfs|msdos|fuseblk|sdcardfs|exfat|fuse.fdredir\"。

        :param linux_removable_drive_file_system_format: The linux_removable_drive_file_system_format of this FileRedirectionOptions.
        :type linux_removable_drive_file_system_format: str
        """
        self._linux_removable_drive_file_system_format = linux_removable_drive_file_system_format

    @property
    def linux_cdrom_drive_file_system_format(self):
        """Gets the linux_cdrom_drive_file_system_format of this FileRedirectionOptions.

        Linux光盘驱动器文件系统格式。默认：\"cd9660|iso9660|udf\"。

        :return: The linux_cdrom_drive_file_system_format of this FileRedirectionOptions.
        :rtype: str
        """
        return self._linux_cdrom_drive_file_system_format

    @linux_cdrom_drive_file_system_format.setter
    def linux_cdrom_drive_file_system_format(self, linux_cdrom_drive_file_system_format):
        """Sets the linux_cdrom_drive_file_system_format of this FileRedirectionOptions.

        Linux光盘驱动器文件系统格式。默认：\"cd9660|iso9660|udf\"。

        :param linux_cdrom_drive_file_system_format: The linux_cdrom_drive_file_system_format of this FileRedirectionOptions.
        :type linux_cdrom_drive_file_system_format: str
        """
        self._linux_cdrom_drive_file_system_format = linux_cdrom_drive_file_system_format

    @property
    def linux_network_drive_file_system_format(self):
        """Gets the linux_network_drive_file_system_format of this FileRedirectionOptions.

        Linux网络驱动器文件系统格式。默认：\"smbfs|afpfs|cifs\"。

        :return: The linux_network_drive_file_system_format of this FileRedirectionOptions.
        :rtype: str
        """
        return self._linux_network_drive_file_system_format

    @linux_network_drive_file_system_format.setter
    def linux_network_drive_file_system_format(self, linux_network_drive_file_system_format):
        """Sets the linux_network_drive_file_system_format of this FileRedirectionOptions.

        Linux网络驱动器文件系统格式。默认：\"smbfs|afpfs|cifs\"。

        :param linux_network_drive_file_system_format: The linux_network_drive_file_system_format of this FileRedirectionOptions.
        :type linux_network_drive_file_system_format: str
        """
        self._linux_network_drive_file_system_format = linux_network_drive_file_system_format

    @property
    def path_separator(self):
        """Gets the path_separator of this FileRedirectionOptions.

        路径分隔符。默认：\"|\"。

        :return: The path_separator of this FileRedirectionOptions.
        :rtype: str
        """
        return self._path_separator

    @path_separator.setter
    def path_separator(self, path_separator):
        """Sets the path_separator of this FileRedirectionOptions.

        路径分隔符。默认：\"|\"。

        :param path_separator: The path_separator of this FileRedirectionOptions.
        :type path_separator: str
        """
        self._path_separator = path_separator

    @property
    def fixed_drive_enable(self):
        """Gets the fixed_drive_enable of this FileRedirectionOptions.

        是否开启固定驱动器（如: 本地磁盘）。取值为： false：表示关闭。 true：表示开启。

        :return: The fixed_drive_enable of this FileRedirectionOptions.
        :rtype: bool
        """
        return self._fixed_drive_enable

    @fixed_drive_enable.setter
    def fixed_drive_enable(self, fixed_drive_enable):
        """Sets the fixed_drive_enable of this FileRedirectionOptions.

        是否开启固定驱动器（如: 本地磁盘）。取值为： false：表示关闭。 true：表示开启。

        :param fixed_drive_enable: The fixed_drive_enable of this FileRedirectionOptions.
        :type fixed_drive_enable: bool
        """
        self._fixed_drive_enable = fixed_drive_enable

    @property
    def removable_drive_enable(self):
        """Gets the removable_drive_enable of this FileRedirectionOptions.

        是否开启可移除驱动器（如: U盘）。取值为： false：表示关闭。 true：表示开启。

        :return: The removable_drive_enable of this FileRedirectionOptions.
        :rtype: bool
        """
        return self._removable_drive_enable

    @removable_drive_enable.setter
    def removable_drive_enable(self, removable_drive_enable):
        """Sets the removable_drive_enable of this FileRedirectionOptions.

        是否开启可移除驱动器（如: U盘）。取值为： false：表示关闭。 true：表示开启。

        :param removable_drive_enable: The removable_drive_enable of this FileRedirectionOptions.
        :type removable_drive_enable: bool
        """
        self._removable_drive_enable = removable_drive_enable

    @property
    def cd_rom_drive_enable(self):
        """Gets the cd_rom_drive_enable of this FileRedirectionOptions.

        是否开启光盘驱动器。取值为： false：表示关闭。 true：表示开启。

        :return: The cd_rom_drive_enable of this FileRedirectionOptions.
        :rtype: bool
        """
        return self._cd_rom_drive_enable

    @cd_rom_drive_enable.setter
    def cd_rom_drive_enable(self, cd_rom_drive_enable):
        """Sets the cd_rom_drive_enable of this FileRedirectionOptions.

        是否开启光盘驱动器。取值为： false：表示关闭。 true：表示开启。

        :param cd_rom_drive_enable: The cd_rom_drive_enable of this FileRedirectionOptions.
        :type cd_rom_drive_enable: bool
        """
        self._cd_rom_drive_enable = cd_rom_drive_enable

    @property
    def network_drive_enable(self):
        """Gets the network_drive_enable of this FileRedirectionOptions.

        是否开启网络驱动器。取值为： false：表示关闭。 true：表示开启。

        :return: The network_drive_enable of this FileRedirectionOptions.
        :rtype: bool
        """
        return self._network_drive_enable

    @network_drive_enable.setter
    def network_drive_enable(self, network_drive_enable):
        """Sets the network_drive_enable of this FileRedirectionOptions.

        是否开启网络驱动器。取值为： false：表示关闭。 true：表示开启。

        :param network_drive_enable: The network_drive_enable of this FileRedirectionOptions.
        :type network_drive_enable: bool
        """
        self._network_drive_enable = network_drive_enable

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
        if not isinstance(other, FileRedirectionOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
