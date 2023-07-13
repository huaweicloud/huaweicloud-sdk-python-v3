# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowV2xEdgeDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'v2x_edge_id': 'str',
        'name': 'str',
        'description': 'str',
        'esn': 'str',
        'ip': 'str',
        'port': 'int',
        'hardware_type': 'str',
        'position_description': 'str',
        'location': 'Location',
        'cameras': 'list[IdAndStatus]',
        'radars': 'list[IdAndStatus]',
        'local_rsus': 'list[IdAndStatus]',
        'edge_general_config': 'EdgeGeneralConfigInResponse',
        'edge_advance_config': 'object',
        'status': 'str',
        'channel_status': 'str',
        'node_id': 'str',
        'created_time': 'datetime',
        'last_modified_time': 'datetime'
    }

    attribute_map = {
        'v2x_edge_id': 'v2x_edge_id',
        'name': 'name',
        'description': 'description',
        'esn': 'esn',
        'ip': 'ip',
        'port': 'port',
        'hardware_type': 'hardware_type',
        'position_description': 'position_description',
        'location': 'location',
        'cameras': 'cameras',
        'radars': 'radars',
        'local_rsus': 'local_rsus',
        'edge_general_config': 'edge_general_config',
        'edge_advance_config': 'edge_advance_config',
        'status': 'status',
        'channel_status': 'channel_status',
        'node_id': 'node_id',
        'created_time': 'created_time',
        'last_modified_time': 'last_modified_time'
    }

    def __init__(self, v2x_edge_id=None, name=None, description=None, esn=None, ip=None, port=None, hardware_type=None, position_description=None, location=None, cameras=None, radars=None, local_rsus=None, edge_general_config=None, edge_advance_config=None, status=None, channel_status=None, node_id=None, created_time=None, last_modified_time=None):
        """ShowV2xEdgeDetailResponse

        The model defined in huaweicloud sdk

        :param v2x_edge_id: **参数说明**：Edge ID，用于唯一标识一个Edge。
        :type v2x_edge_id: str
        :param name: **参数说明**：名称。  **取值范围**：长度不超过128，只允许中文、字母、数字、以及_.-等字符的组合。
        :type name: str
        :param description: **参数说明**：Edge描述。
        :type description: str
        :param esn: **参数说明**：序列号。  **取值范围**：长度不超过64，只允许字母、数字、以及_等字符的组合。
        :type esn: str
        :param ip: **参数说明**：网络I，例如127.0.0.1。
        :type ip: str
        :param port: ITS800,ATLAS 端口号
        :type port: int
        :param hardware_type: **参数说明**：硬件类型。  **取值范围**：ITS800 或者 ATLAS。
        :type hardware_type: str
        :param position_description: **参数说明**：安装位置编码，由用户自定义。  **取值范围**：长度不低于1不超过128，只允许字母、数字、下划线（_）的组合。
        :type position_description: str
        :param location: 
        :type location: :class:`huaweicloudsdkdris.v1.Location`
        :param cameras: **参数说明**：Edge关联的摄像头列表。
        :type cameras: list[:class:`huaweicloudsdkdris.v1.IdAndStatus`]
        :param radars: **参数说明**：Edge关联的雷达列表。
        :type radars: list[:class:`huaweicloudsdkdris.v1.IdAndStatus`]
        :param local_rsus: **参数说明**：Edge关联的本地RSU列表。
        :type local_rsus: list[:class:`huaweicloudsdkdris.v1.IdAndStatus`]
        :param edge_general_config: 
        :type edge_general_config: :class:`huaweicloudsdkdris.v1.EdgeGeneralConfigInResponse`
        :param edge_advance_config: **参数说明**：Edge高级配置，Json格式
        :type edge_advance_config: object
        :param status: **参数说明**：状态。  **取值范围**： - UNINSTALLED： 待部署 - INSTALLED：部署中 - OFFLINE：离线 - ONLINE：在线： - UPGRADING：升级中 - DELETING：删除中
        :type status: str
        :param channel_status: **参数说明**：业务通道状态。  **取值范围**： - ONLINE：在线 - OFFLINE：离线 - INITIAL：初始化
        :type channel_status: str
        :param node_id: **参数说明**：边缘管理服务返回的node_id，用于关联EdgeManager的资源。
        :type node_id: str
        :param created_time: **参数说明**：创建时间。  格式：yyyy-MM-dd&#39;&#39;T&#39;&#39;HH:mm:ss&#39;&#39;Z&#39;&#39;。  例如 2020-09-01T01:37:01Z。
        :type created_time: datetime
        :param last_modified_time: **参数说明**：创建时间。  格式：yyyy-MM-dd&#39;&#39;T&#39;&#39;HH:mm:ss&#39;&#39;Z&#39;&#39;。  例如 2020-09-01T01:37:01Z。
        :type last_modified_time: datetime
        """
        
        super(ShowV2xEdgeDetailResponse, self).__init__()

        self._v2x_edge_id = None
        self._name = None
        self._description = None
        self._esn = None
        self._ip = None
        self._port = None
        self._hardware_type = None
        self._position_description = None
        self._location = None
        self._cameras = None
        self._radars = None
        self._local_rsus = None
        self._edge_general_config = None
        self._edge_advance_config = None
        self._status = None
        self._channel_status = None
        self._node_id = None
        self._created_time = None
        self._last_modified_time = None
        self.discriminator = None

        if v2x_edge_id is not None:
            self.v2x_edge_id = v2x_edge_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if esn is not None:
            self.esn = esn
        if ip is not None:
            self.ip = ip
        if port is not None:
            self.port = port
        if hardware_type is not None:
            self.hardware_type = hardware_type
        if position_description is not None:
            self.position_description = position_description
        if location is not None:
            self.location = location
        if cameras is not None:
            self.cameras = cameras
        if radars is not None:
            self.radars = radars
        if local_rsus is not None:
            self.local_rsus = local_rsus
        if edge_general_config is not None:
            self.edge_general_config = edge_general_config
        if edge_advance_config is not None:
            self.edge_advance_config = edge_advance_config
        if status is not None:
            self.status = status
        if channel_status is not None:
            self.channel_status = channel_status
        if node_id is not None:
            self.node_id = node_id
        if created_time is not None:
            self.created_time = created_time
        if last_modified_time is not None:
            self.last_modified_time = last_modified_time

    @property
    def v2x_edge_id(self):
        """Gets the v2x_edge_id of this ShowV2xEdgeDetailResponse.

        **参数说明**：Edge ID，用于唯一标识一个Edge。

        :return: The v2x_edge_id of this ShowV2xEdgeDetailResponse.
        :rtype: str
        """
        return self._v2x_edge_id

    @v2x_edge_id.setter
    def v2x_edge_id(self, v2x_edge_id):
        """Sets the v2x_edge_id of this ShowV2xEdgeDetailResponse.

        **参数说明**：Edge ID，用于唯一标识一个Edge。

        :param v2x_edge_id: The v2x_edge_id of this ShowV2xEdgeDetailResponse.
        :type v2x_edge_id: str
        """
        self._v2x_edge_id = v2x_edge_id

    @property
    def name(self):
        """Gets the name of this ShowV2xEdgeDetailResponse.

        **参数说明**：名称。  **取值范围**：长度不超过128，只允许中文、字母、数字、以及_.-等字符的组合。

        :return: The name of this ShowV2xEdgeDetailResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowV2xEdgeDetailResponse.

        **参数说明**：名称。  **取值范围**：长度不超过128，只允许中文、字母、数字、以及_.-等字符的组合。

        :param name: The name of this ShowV2xEdgeDetailResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ShowV2xEdgeDetailResponse.

        **参数说明**：Edge描述。

        :return: The description of this ShowV2xEdgeDetailResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowV2xEdgeDetailResponse.

        **参数说明**：Edge描述。

        :param description: The description of this ShowV2xEdgeDetailResponse.
        :type description: str
        """
        self._description = description

    @property
    def esn(self):
        """Gets the esn of this ShowV2xEdgeDetailResponse.

        **参数说明**：序列号。  **取值范围**：长度不超过64，只允许字母、数字、以及_等字符的组合。

        :return: The esn of this ShowV2xEdgeDetailResponse.
        :rtype: str
        """
        return self._esn

    @esn.setter
    def esn(self, esn):
        """Sets the esn of this ShowV2xEdgeDetailResponse.

        **参数说明**：序列号。  **取值范围**：长度不超过64，只允许字母、数字、以及_等字符的组合。

        :param esn: The esn of this ShowV2xEdgeDetailResponse.
        :type esn: str
        """
        self._esn = esn

    @property
    def ip(self):
        """Gets the ip of this ShowV2xEdgeDetailResponse.

        **参数说明**：网络I，例如127.0.0.1。

        :return: The ip of this ShowV2xEdgeDetailResponse.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ShowV2xEdgeDetailResponse.

        **参数说明**：网络I，例如127.0.0.1。

        :param ip: The ip of this ShowV2xEdgeDetailResponse.
        :type ip: str
        """
        self._ip = ip

    @property
    def port(self):
        """Gets the port of this ShowV2xEdgeDetailResponse.

        ITS800,ATLAS 端口号

        :return: The port of this ShowV2xEdgeDetailResponse.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ShowV2xEdgeDetailResponse.

        ITS800,ATLAS 端口号

        :param port: The port of this ShowV2xEdgeDetailResponse.
        :type port: int
        """
        self._port = port

    @property
    def hardware_type(self):
        """Gets the hardware_type of this ShowV2xEdgeDetailResponse.

        **参数说明**：硬件类型。  **取值范围**：ITS800 或者 ATLAS。

        :return: The hardware_type of this ShowV2xEdgeDetailResponse.
        :rtype: str
        """
        return self._hardware_type

    @hardware_type.setter
    def hardware_type(self, hardware_type):
        """Sets the hardware_type of this ShowV2xEdgeDetailResponse.

        **参数说明**：硬件类型。  **取值范围**：ITS800 或者 ATLAS。

        :param hardware_type: The hardware_type of this ShowV2xEdgeDetailResponse.
        :type hardware_type: str
        """
        self._hardware_type = hardware_type

    @property
    def position_description(self):
        """Gets the position_description of this ShowV2xEdgeDetailResponse.

        **参数说明**：安装位置编码，由用户自定义。  **取值范围**：长度不低于1不超过128，只允许字母、数字、下划线（_）的组合。

        :return: The position_description of this ShowV2xEdgeDetailResponse.
        :rtype: str
        """
        return self._position_description

    @position_description.setter
    def position_description(self, position_description):
        """Sets the position_description of this ShowV2xEdgeDetailResponse.

        **参数说明**：安装位置编码，由用户自定义。  **取值范围**：长度不低于1不超过128，只允许字母、数字、下划线（_）的组合。

        :param position_description: The position_description of this ShowV2xEdgeDetailResponse.
        :type position_description: str
        """
        self._position_description = position_description

    @property
    def location(self):
        """Gets the location of this ShowV2xEdgeDetailResponse.

        :return: The location of this ShowV2xEdgeDetailResponse.
        :rtype: :class:`huaweicloudsdkdris.v1.Location`
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this ShowV2xEdgeDetailResponse.

        :param location: The location of this ShowV2xEdgeDetailResponse.
        :type location: :class:`huaweicloudsdkdris.v1.Location`
        """
        self._location = location

    @property
    def cameras(self):
        """Gets the cameras of this ShowV2xEdgeDetailResponse.

        **参数说明**：Edge关联的摄像头列表。

        :return: The cameras of this ShowV2xEdgeDetailResponse.
        :rtype: list[:class:`huaweicloudsdkdris.v1.IdAndStatus`]
        """
        return self._cameras

    @cameras.setter
    def cameras(self, cameras):
        """Sets the cameras of this ShowV2xEdgeDetailResponse.

        **参数说明**：Edge关联的摄像头列表。

        :param cameras: The cameras of this ShowV2xEdgeDetailResponse.
        :type cameras: list[:class:`huaweicloudsdkdris.v1.IdAndStatus`]
        """
        self._cameras = cameras

    @property
    def radars(self):
        """Gets the radars of this ShowV2xEdgeDetailResponse.

        **参数说明**：Edge关联的雷达列表。

        :return: The radars of this ShowV2xEdgeDetailResponse.
        :rtype: list[:class:`huaweicloudsdkdris.v1.IdAndStatus`]
        """
        return self._radars

    @radars.setter
    def radars(self, radars):
        """Sets the radars of this ShowV2xEdgeDetailResponse.

        **参数说明**：Edge关联的雷达列表。

        :param radars: The radars of this ShowV2xEdgeDetailResponse.
        :type radars: list[:class:`huaweicloudsdkdris.v1.IdAndStatus`]
        """
        self._radars = radars

    @property
    def local_rsus(self):
        """Gets the local_rsus of this ShowV2xEdgeDetailResponse.

        **参数说明**：Edge关联的本地RSU列表。

        :return: The local_rsus of this ShowV2xEdgeDetailResponse.
        :rtype: list[:class:`huaweicloudsdkdris.v1.IdAndStatus`]
        """
        return self._local_rsus

    @local_rsus.setter
    def local_rsus(self, local_rsus):
        """Sets the local_rsus of this ShowV2xEdgeDetailResponse.

        **参数说明**：Edge关联的本地RSU列表。

        :param local_rsus: The local_rsus of this ShowV2xEdgeDetailResponse.
        :type local_rsus: list[:class:`huaweicloudsdkdris.v1.IdAndStatus`]
        """
        self._local_rsus = local_rsus

    @property
    def edge_general_config(self):
        """Gets the edge_general_config of this ShowV2xEdgeDetailResponse.

        :return: The edge_general_config of this ShowV2xEdgeDetailResponse.
        :rtype: :class:`huaweicloudsdkdris.v1.EdgeGeneralConfigInResponse`
        """
        return self._edge_general_config

    @edge_general_config.setter
    def edge_general_config(self, edge_general_config):
        """Sets the edge_general_config of this ShowV2xEdgeDetailResponse.

        :param edge_general_config: The edge_general_config of this ShowV2xEdgeDetailResponse.
        :type edge_general_config: :class:`huaweicloudsdkdris.v1.EdgeGeneralConfigInResponse`
        """
        self._edge_general_config = edge_general_config

    @property
    def edge_advance_config(self):
        """Gets the edge_advance_config of this ShowV2xEdgeDetailResponse.

        **参数说明**：Edge高级配置，Json格式

        :return: The edge_advance_config of this ShowV2xEdgeDetailResponse.
        :rtype: object
        """
        return self._edge_advance_config

    @edge_advance_config.setter
    def edge_advance_config(self, edge_advance_config):
        """Sets the edge_advance_config of this ShowV2xEdgeDetailResponse.

        **参数说明**：Edge高级配置，Json格式

        :param edge_advance_config: The edge_advance_config of this ShowV2xEdgeDetailResponse.
        :type edge_advance_config: object
        """
        self._edge_advance_config = edge_advance_config

    @property
    def status(self):
        """Gets the status of this ShowV2xEdgeDetailResponse.

        **参数说明**：状态。  **取值范围**： - UNINSTALLED： 待部署 - INSTALLED：部署中 - OFFLINE：离线 - ONLINE：在线： - UPGRADING：升级中 - DELETING：删除中

        :return: The status of this ShowV2xEdgeDetailResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowV2xEdgeDetailResponse.

        **参数说明**：状态。  **取值范围**： - UNINSTALLED： 待部署 - INSTALLED：部署中 - OFFLINE：离线 - ONLINE：在线： - UPGRADING：升级中 - DELETING：删除中

        :param status: The status of this ShowV2xEdgeDetailResponse.
        :type status: str
        """
        self._status = status

    @property
    def channel_status(self):
        """Gets the channel_status of this ShowV2xEdgeDetailResponse.

        **参数说明**：业务通道状态。  **取值范围**： - ONLINE：在线 - OFFLINE：离线 - INITIAL：初始化

        :return: The channel_status of this ShowV2xEdgeDetailResponse.
        :rtype: str
        """
        return self._channel_status

    @channel_status.setter
    def channel_status(self, channel_status):
        """Sets the channel_status of this ShowV2xEdgeDetailResponse.

        **参数说明**：业务通道状态。  **取值范围**： - ONLINE：在线 - OFFLINE：离线 - INITIAL：初始化

        :param channel_status: The channel_status of this ShowV2xEdgeDetailResponse.
        :type channel_status: str
        """
        self._channel_status = channel_status

    @property
    def node_id(self):
        """Gets the node_id of this ShowV2xEdgeDetailResponse.

        **参数说明**：边缘管理服务返回的node_id，用于关联EdgeManager的资源。

        :return: The node_id of this ShowV2xEdgeDetailResponse.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this ShowV2xEdgeDetailResponse.

        **参数说明**：边缘管理服务返回的node_id，用于关联EdgeManager的资源。

        :param node_id: The node_id of this ShowV2xEdgeDetailResponse.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def created_time(self):
        """Gets the created_time of this ShowV2xEdgeDetailResponse.

        **参数说明**：创建时间。  格式：yyyy-MM-dd''T''HH:mm:ss''Z''。  例如 2020-09-01T01:37:01Z。

        :return: The created_time of this ShowV2xEdgeDetailResponse.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ShowV2xEdgeDetailResponse.

        **参数说明**：创建时间。  格式：yyyy-MM-dd''T''HH:mm:ss''Z''。  例如 2020-09-01T01:37:01Z。

        :param created_time: The created_time of this ShowV2xEdgeDetailResponse.
        :type created_time: datetime
        """
        self._created_time = created_time

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this ShowV2xEdgeDetailResponse.

        **参数说明**：创建时间。  格式：yyyy-MM-dd''T''HH:mm:ss''Z''。  例如 2020-09-01T01:37:01Z。

        :return: The last_modified_time of this ShowV2xEdgeDetailResponse.
        :rtype: datetime
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this ShowV2xEdgeDetailResponse.

        **参数说明**：创建时间。  格式：yyyy-MM-dd''T''HH:mm:ss''Z''。  例如 2020-09-01T01:37:01Z。

        :param last_modified_time: The last_modified_time of this ShowV2xEdgeDetailResponse.
        :type last_modified_time: datetime
        """
        self._last_modified_time = last_modified_time

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
        if not isinstance(other, ShowV2xEdgeDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
