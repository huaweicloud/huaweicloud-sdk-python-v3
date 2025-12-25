# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChannelInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'channel_name': 'str',
        'config_status': 'str',
        'create_by': 'str',
        'mini_on_online': 'bool',
        'monitor': 'Monitor',
        'node_name': 'str',
        'private_ip_address': 'str',
        'public_ip_address': 'str',
        'read_write': 'ReadWrite',
        'region': 'str'
    }

    attribute_map = {
        'channel_name': 'channel_name',
        'config_status': 'config_status',
        'create_by': 'create_by',
        'mini_on_online': 'mini_on_online',
        'monitor': 'monitor',
        'node_name': 'node_name',
        'private_ip_address': 'private_ip_address',
        'public_ip_address': 'public_ip_address',
        'read_write': 'read_write',
        'region': 'region'
    }

    def __init__(self, channel_name=None, config_status=None, create_by=None, mini_on_online=None, monitor=None, node_name=None, private_ip_address=None, public_ip_address=None, read_write=None, region=None):
        r"""ChannelInstance

        The model defined in huaweicloud sdk

        :param channel_name: 分组名称
        :type channel_name: str
        :param config_status: **参数解释**: 采集通道配置状态 - OK 完成 - CHANGE 修改  **约束限制** 不涉及 **取值范围**: - OK - CHANGE  **默认值** 不涉及
        :type config_status: str
        :param create_by: Iam用户ID
        :type create_by: str
        :param mini_on_online: 是否在线
        :type mini_on_online: bool
        :param monitor: 
        :type monitor: :class:`huaweicloudsdksecmaster.v1.Monitor`
        :param node_name: 分组名称
        :type node_name: str
        :param private_ip_address: IP地址
        :type private_ip_address: str
        :param public_ip_address: IP地址
        :type public_ip_address: str
        :param read_write: 
        :type read_write: :class:`huaweicloudsdksecmaster.v1.ReadWrite`
        :param region: 地区
        :type region: str
        """
        
        

        self._channel_name = None
        self._config_status = None
        self._create_by = None
        self._mini_on_online = None
        self._monitor = None
        self._node_name = None
        self._private_ip_address = None
        self._public_ip_address = None
        self._read_write = None
        self._region = None
        self.discriminator = None

        if channel_name is not None:
            self.channel_name = channel_name
        if config_status is not None:
            self.config_status = config_status
        if create_by is not None:
            self.create_by = create_by
        if mini_on_online is not None:
            self.mini_on_online = mini_on_online
        if monitor is not None:
            self.monitor = monitor
        if node_name is not None:
            self.node_name = node_name
        if private_ip_address is not None:
            self.private_ip_address = private_ip_address
        if public_ip_address is not None:
            self.public_ip_address = public_ip_address
        if read_write is not None:
            self.read_write = read_write
        if region is not None:
            self.region = region

    @property
    def channel_name(self):
        r"""Gets the channel_name of this ChannelInstance.

        分组名称

        :return: The channel_name of this ChannelInstance.
        :rtype: str
        """
        return self._channel_name

    @channel_name.setter
    def channel_name(self, channel_name):
        r"""Sets the channel_name of this ChannelInstance.

        分组名称

        :param channel_name: The channel_name of this ChannelInstance.
        :type channel_name: str
        """
        self._channel_name = channel_name

    @property
    def config_status(self):
        r"""Gets the config_status of this ChannelInstance.

        **参数解释**: 采集通道配置状态 - OK 完成 - CHANGE 修改  **约束限制** 不涉及 **取值范围**: - OK - CHANGE  **默认值** 不涉及

        :return: The config_status of this ChannelInstance.
        :rtype: str
        """
        return self._config_status

    @config_status.setter
    def config_status(self, config_status):
        r"""Sets the config_status of this ChannelInstance.

        **参数解释**: 采集通道配置状态 - OK 完成 - CHANGE 修改  **约束限制** 不涉及 **取值范围**: - OK - CHANGE  **默认值** 不涉及

        :param config_status: The config_status of this ChannelInstance.
        :type config_status: str
        """
        self._config_status = config_status

    @property
    def create_by(self):
        r"""Gets the create_by of this ChannelInstance.

        Iam用户ID

        :return: The create_by of this ChannelInstance.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this ChannelInstance.

        Iam用户ID

        :param create_by: The create_by of this ChannelInstance.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def mini_on_online(self):
        r"""Gets the mini_on_online of this ChannelInstance.

        是否在线

        :return: The mini_on_online of this ChannelInstance.
        :rtype: bool
        """
        return self._mini_on_online

    @mini_on_online.setter
    def mini_on_online(self, mini_on_online):
        r"""Sets the mini_on_online of this ChannelInstance.

        是否在线

        :param mini_on_online: The mini_on_online of this ChannelInstance.
        :type mini_on_online: bool
        """
        self._mini_on_online = mini_on_online

    @property
    def monitor(self):
        r"""Gets the monitor of this ChannelInstance.

        :return: The monitor of this ChannelInstance.
        :rtype: :class:`huaweicloudsdksecmaster.v1.Monitor`
        """
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        r"""Sets the monitor of this ChannelInstance.

        :param monitor: The monitor of this ChannelInstance.
        :type monitor: :class:`huaweicloudsdksecmaster.v1.Monitor`
        """
        self._monitor = monitor

    @property
    def node_name(self):
        r"""Gets the node_name of this ChannelInstance.

        分组名称

        :return: The node_name of this ChannelInstance.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this ChannelInstance.

        分组名称

        :param node_name: The node_name of this ChannelInstance.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def private_ip_address(self):
        r"""Gets the private_ip_address of this ChannelInstance.

        IP地址

        :return: The private_ip_address of this ChannelInstance.
        :rtype: str
        """
        return self._private_ip_address

    @private_ip_address.setter
    def private_ip_address(self, private_ip_address):
        r"""Sets the private_ip_address of this ChannelInstance.

        IP地址

        :param private_ip_address: The private_ip_address of this ChannelInstance.
        :type private_ip_address: str
        """
        self._private_ip_address = private_ip_address

    @property
    def public_ip_address(self):
        r"""Gets the public_ip_address of this ChannelInstance.

        IP地址

        :return: The public_ip_address of this ChannelInstance.
        :rtype: str
        """
        return self._public_ip_address

    @public_ip_address.setter
    def public_ip_address(self, public_ip_address):
        r"""Sets the public_ip_address of this ChannelInstance.

        IP地址

        :param public_ip_address: The public_ip_address of this ChannelInstance.
        :type public_ip_address: str
        """
        self._public_ip_address = public_ip_address

    @property
    def read_write(self):
        r"""Gets the read_write of this ChannelInstance.

        :return: The read_write of this ChannelInstance.
        :rtype: :class:`huaweicloudsdksecmaster.v1.ReadWrite`
        """
        return self._read_write

    @read_write.setter
    def read_write(self, read_write):
        r"""Sets the read_write of this ChannelInstance.

        :param read_write: The read_write of this ChannelInstance.
        :type read_write: :class:`huaweicloudsdksecmaster.v1.ReadWrite`
        """
        self._read_write = read_write

    @property
    def region(self):
        r"""Gets the region of this ChannelInstance.

        地区

        :return: The region of this ChannelInstance.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ChannelInstance.

        地区

        :param region: The region of this ChannelInstance.
        :type region: str
        """
        self._region = region

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ChannelInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
