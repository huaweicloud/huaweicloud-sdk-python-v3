# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class V2XEdgeListResponseDTO:

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
        'esn': 'str',
        'ip': 'str',
        'position_description': 'str',
        'location': 'Location',
        'status': 'str',
        'channel_status': 'str',
        'created_time': 'datetime'
    }

    attribute_map = {
        'v2x_edge_id': 'v2x_edge_id',
        'name': 'name',
        'esn': 'esn',
        'ip': 'ip',
        'position_description': 'position_description',
        'location': 'location',
        'status': 'status',
        'channel_status': 'channel_status',
        'created_time': 'created_time'
    }

    def __init__(self, v2x_edge_id=None, name=None, esn=None, ip=None, position_description=None, location=None, status=None, channel_status=None, created_time=None):
        r"""V2XEdgeListResponseDTO

        The model defined in huaweicloud sdk

        :param v2x_edge_id: **参数说明**：Edge ID，用于唯一标识一个Edge。
        :type v2x_edge_id: str
        :param name: **参数说明**：V2XEdge的名称  **取值范围**：长度不超过128，只允许中文、字母、数字、以及_.-等字符的组合。
        :type name: str
        :param esn: **参数说明**：设备编码。  **取值范围**：长度不超过64，只允许字母、数字、以及_等字符的组合。
        :type esn: str
        :param ip: **参数说明**：网络IP，例如127.0.0.1。 
        :type ip: str
        :param position_description: **参数说明**：安装位置编码，由用户自定义。  **取值范围**：长度不低于1不超过128，只允许字母、数字、下划线（_）的组合。
        :type position_description: str
        :param location: 
        :type location: :class:`huaweicloudsdkdris.v1.Location`
        :param status: **参数说明**：状态。  **取值范围**： - UNINSTALLED： 待部署 - INSTALLED：部署中 - OFFLINE：离线 - ONLINE：在线： - UPGRADING：升级中 - DELETING：删除中
        :type status: str
        :param channel_status: **参数说明**：业务通道状态。
        :type channel_status: str
        :param created_time: **参数说明**：创建时间。  格式：yyyy-MM-dd&#39;&#39;T&#39;&#39;HH:mm:ss&#39;&#39;Z&#39;&#39;。  例如 2020-09-01T01:37:01Z。
        :type created_time: datetime
        """
        
        

        self._v2x_edge_id = None
        self._name = None
        self._esn = None
        self._ip = None
        self._position_description = None
        self._location = None
        self._status = None
        self._channel_status = None
        self._created_time = None
        self.discriminator = None

        if v2x_edge_id is not None:
            self.v2x_edge_id = v2x_edge_id
        if name is not None:
            self.name = name
        if esn is not None:
            self.esn = esn
        if ip is not None:
            self.ip = ip
        if position_description is not None:
            self.position_description = position_description
        if location is not None:
            self.location = location
        if status is not None:
            self.status = status
        if channel_status is not None:
            self.channel_status = channel_status
        if created_time is not None:
            self.created_time = created_time

    @property
    def v2x_edge_id(self):
        r"""Gets the v2x_edge_id of this V2XEdgeListResponseDTO.

        **参数说明**：Edge ID，用于唯一标识一个Edge。

        :return: The v2x_edge_id of this V2XEdgeListResponseDTO.
        :rtype: str
        """
        return self._v2x_edge_id

    @v2x_edge_id.setter
    def v2x_edge_id(self, v2x_edge_id):
        r"""Sets the v2x_edge_id of this V2XEdgeListResponseDTO.

        **参数说明**：Edge ID，用于唯一标识一个Edge。

        :param v2x_edge_id: The v2x_edge_id of this V2XEdgeListResponseDTO.
        :type v2x_edge_id: str
        """
        self._v2x_edge_id = v2x_edge_id

    @property
    def name(self):
        r"""Gets the name of this V2XEdgeListResponseDTO.

        **参数说明**：V2XEdge的名称  **取值范围**：长度不超过128，只允许中文、字母、数字、以及_.-等字符的组合。

        :return: The name of this V2XEdgeListResponseDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this V2XEdgeListResponseDTO.

        **参数说明**：V2XEdge的名称  **取值范围**：长度不超过128，只允许中文、字母、数字、以及_.-等字符的组合。

        :param name: The name of this V2XEdgeListResponseDTO.
        :type name: str
        """
        self._name = name

    @property
    def esn(self):
        r"""Gets the esn of this V2XEdgeListResponseDTO.

        **参数说明**：设备编码。  **取值范围**：长度不超过64，只允许字母、数字、以及_等字符的组合。

        :return: The esn of this V2XEdgeListResponseDTO.
        :rtype: str
        """
        return self._esn

    @esn.setter
    def esn(self, esn):
        r"""Sets the esn of this V2XEdgeListResponseDTO.

        **参数说明**：设备编码。  **取值范围**：长度不超过64，只允许字母、数字、以及_等字符的组合。

        :param esn: The esn of this V2XEdgeListResponseDTO.
        :type esn: str
        """
        self._esn = esn

    @property
    def ip(self):
        r"""Gets the ip of this V2XEdgeListResponseDTO.

        **参数说明**：网络IP，例如127.0.0.1。 

        :return: The ip of this V2XEdgeListResponseDTO.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this V2XEdgeListResponseDTO.

        **参数说明**：网络IP，例如127.0.0.1。 

        :param ip: The ip of this V2XEdgeListResponseDTO.
        :type ip: str
        """
        self._ip = ip

    @property
    def position_description(self):
        r"""Gets the position_description of this V2XEdgeListResponseDTO.

        **参数说明**：安装位置编码，由用户自定义。  **取值范围**：长度不低于1不超过128，只允许字母、数字、下划线（_）的组合。

        :return: The position_description of this V2XEdgeListResponseDTO.
        :rtype: str
        """
        return self._position_description

    @position_description.setter
    def position_description(self, position_description):
        r"""Sets the position_description of this V2XEdgeListResponseDTO.

        **参数说明**：安装位置编码，由用户自定义。  **取值范围**：长度不低于1不超过128，只允许字母、数字、下划线（_）的组合。

        :param position_description: The position_description of this V2XEdgeListResponseDTO.
        :type position_description: str
        """
        self._position_description = position_description

    @property
    def location(self):
        r"""Gets the location of this V2XEdgeListResponseDTO.

        :return: The location of this V2XEdgeListResponseDTO.
        :rtype: :class:`huaweicloudsdkdris.v1.Location`
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this V2XEdgeListResponseDTO.

        :param location: The location of this V2XEdgeListResponseDTO.
        :type location: :class:`huaweicloudsdkdris.v1.Location`
        """
        self._location = location

    @property
    def status(self):
        r"""Gets the status of this V2XEdgeListResponseDTO.

        **参数说明**：状态。  **取值范围**： - UNINSTALLED： 待部署 - INSTALLED：部署中 - OFFLINE：离线 - ONLINE：在线： - UPGRADING：升级中 - DELETING：删除中

        :return: The status of this V2XEdgeListResponseDTO.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this V2XEdgeListResponseDTO.

        **参数说明**：状态。  **取值范围**： - UNINSTALLED： 待部署 - INSTALLED：部署中 - OFFLINE：离线 - ONLINE：在线： - UPGRADING：升级中 - DELETING：删除中

        :param status: The status of this V2XEdgeListResponseDTO.
        :type status: str
        """
        self._status = status

    @property
    def channel_status(self):
        r"""Gets the channel_status of this V2XEdgeListResponseDTO.

        **参数说明**：业务通道状态。

        :return: The channel_status of this V2XEdgeListResponseDTO.
        :rtype: str
        """
        return self._channel_status

    @channel_status.setter
    def channel_status(self, channel_status):
        r"""Sets the channel_status of this V2XEdgeListResponseDTO.

        **参数说明**：业务通道状态。

        :param channel_status: The channel_status of this V2XEdgeListResponseDTO.
        :type channel_status: str
        """
        self._channel_status = channel_status

    @property
    def created_time(self):
        r"""Gets the created_time of this V2XEdgeListResponseDTO.

        **参数说明**：创建时间。  格式：yyyy-MM-dd''T''HH:mm:ss''Z''。  例如 2020-09-01T01:37:01Z。

        :return: The created_time of this V2XEdgeListResponseDTO.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this V2XEdgeListResponseDTO.

        **参数说明**：创建时间。  格式：yyyy-MM-dd''T''HH:mm:ss''Z''。  例如 2020-09-01T01:37:01Z。

        :param created_time: The created_time of this V2XEdgeListResponseDTO.
        :type created_time: datetime
        """
        self._created_time = created_time

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
        if not isinstance(other, V2XEdgeListResponseDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
