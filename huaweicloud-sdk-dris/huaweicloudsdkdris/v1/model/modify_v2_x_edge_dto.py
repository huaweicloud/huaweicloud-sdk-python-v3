# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyV2XEdgeDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'esn': 'str',
        'ip': 'str',
        'port': 'int',
        'position_description': 'str',
        'location': 'Location',
        'camera_ids': 'list[str]',
        'radar_ids': 'list[str]',
        'local_rsus': 'list[str]',
        'edge_general_config': 'EdgeGeneralConfig',
        'edge_advance_config': 'object'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'esn': 'esn',
        'ip': 'ip',
        'port': 'port',
        'position_description': 'position_description',
        'location': 'location',
        'camera_ids': 'camera_ids',
        'radar_ids': 'radar_ids',
        'local_rsus': 'local_rsus',
        'edge_general_config': 'edge_general_config',
        'edge_advance_config': 'edge_advance_config'
    }

    def __init__(self, name=None, description=None, esn=None, ip=None, port=None, position_description=None, location=None, camera_ids=None, radar_ids=None, local_rsus=None, edge_general_config=None, edge_advance_config=None):
        """ModifyV2XEdgeDTO

        The model defined in huaweicloud sdk

        :param name: **参数说明**：名称。  **取值范围**：长度不超过128，只允许中文、字母、数字、以及_.-等字符的组合。
        :type name: str
        :param description: **参数说明**：Edge描述。  **取值范围**：长度不超过255，只允许中文、字母、数字、以及_.-等字符的组合。
        :type description: str
        :param esn: **参数说明**：设备编码。仅用于一致性检查，不可修改。  **取值范围**：长度不超过64，只允许中文、字母、数字、以及_等字符的组合。
        :type esn: str
        :param ip: **参数说明**：网络IP，例如：127.0.0.1。
        :type ip: str
        :param port: **参数说明**：ITS800,ATLAS 端口号。
        :type port: int
        :param position_description: **参数说明**：安装位置编码，由用户自定义。  **取值范围**：长度不低于1不超过128，只允许字母、数字、下划线（_）的组合。
        :type position_description: str
        :param location: 
        :type location: :class:`huaweicloudsdkdris.v1.Location`
        :param camera_ids: **参数说明**：摄像头ID列表。
        :type camera_ids: list[str]
        :param radar_ids: **参数说明**：雷达ID列表。
        :type radar_ids: list[str]
        :param local_rsus: **参数说明**：Edge关联的本地RSU列表。
        :type local_rsus: list[str]
        :param edge_general_config: 
        :type edge_general_config: :class:`huaweicloudsdkdris.v1.EdgeGeneralConfig`
        :param edge_advance_config: **参数说明**：Edge高级配置（请谨慎修改，错误的配置将导致edge不可用），Json格式；如果想要删除整个edge_advance_config可以填写空Object（例如:{}）。如果想移除某个配置项，直接从配置数据中移除相应的属性即可。
        :type edge_advance_config: object
        """
        
        

        self._name = None
        self._description = None
        self._esn = None
        self._ip = None
        self._port = None
        self._position_description = None
        self._location = None
        self._camera_ids = None
        self._radar_ids = None
        self._local_rsus = None
        self._edge_general_config = None
        self._edge_advance_config = None
        self.discriminator = None

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
        if position_description is not None:
            self.position_description = position_description
        if location is not None:
            self.location = location
        if camera_ids is not None:
            self.camera_ids = camera_ids
        if radar_ids is not None:
            self.radar_ids = radar_ids
        if local_rsus is not None:
            self.local_rsus = local_rsus
        if edge_general_config is not None:
            self.edge_general_config = edge_general_config
        if edge_advance_config is not None:
            self.edge_advance_config = edge_advance_config

    @property
    def name(self):
        """Gets the name of this ModifyV2XEdgeDTO.

        **参数说明**：名称。  **取值范围**：长度不超过128，只允许中文、字母、数字、以及_.-等字符的组合。

        :return: The name of this ModifyV2XEdgeDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModifyV2XEdgeDTO.

        **参数说明**：名称。  **取值范围**：长度不超过128，只允许中文、字母、数字、以及_.-等字符的组合。

        :param name: The name of this ModifyV2XEdgeDTO.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ModifyV2XEdgeDTO.

        **参数说明**：Edge描述。  **取值范围**：长度不超过255，只允许中文、字母、数字、以及_.-等字符的组合。

        :return: The description of this ModifyV2XEdgeDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModifyV2XEdgeDTO.

        **参数说明**：Edge描述。  **取值范围**：长度不超过255，只允许中文、字母、数字、以及_.-等字符的组合。

        :param description: The description of this ModifyV2XEdgeDTO.
        :type description: str
        """
        self._description = description

    @property
    def esn(self):
        """Gets the esn of this ModifyV2XEdgeDTO.

        **参数说明**：设备编码。仅用于一致性检查，不可修改。  **取值范围**：长度不超过64，只允许中文、字母、数字、以及_等字符的组合。

        :return: The esn of this ModifyV2XEdgeDTO.
        :rtype: str
        """
        return self._esn

    @esn.setter
    def esn(self, esn):
        """Sets the esn of this ModifyV2XEdgeDTO.

        **参数说明**：设备编码。仅用于一致性检查，不可修改。  **取值范围**：长度不超过64，只允许中文、字母、数字、以及_等字符的组合。

        :param esn: The esn of this ModifyV2XEdgeDTO.
        :type esn: str
        """
        self._esn = esn

    @property
    def ip(self):
        """Gets the ip of this ModifyV2XEdgeDTO.

        **参数说明**：网络IP，例如：127.0.0.1。

        :return: The ip of this ModifyV2XEdgeDTO.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ModifyV2XEdgeDTO.

        **参数说明**：网络IP，例如：127.0.0.1。

        :param ip: The ip of this ModifyV2XEdgeDTO.
        :type ip: str
        """
        self._ip = ip

    @property
    def port(self):
        """Gets the port of this ModifyV2XEdgeDTO.

        **参数说明**：ITS800,ATLAS 端口号。

        :return: The port of this ModifyV2XEdgeDTO.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ModifyV2XEdgeDTO.

        **参数说明**：ITS800,ATLAS 端口号。

        :param port: The port of this ModifyV2XEdgeDTO.
        :type port: int
        """
        self._port = port

    @property
    def position_description(self):
        """Gets the position_description of this ModifyV2XEdgeDTO.

        **参数说明**：安装位置编码，由用户自定义。  **取值范围**：长度不低于1不超过128，只允许字母、数字、下划线（_）的组合。

        :return: The position_description of this ModifyV2XEdgeDTO.
        :rtype: str
        """
        return self._position_description

    @position_description.setter
    def position_description(self, position_description):
        """Sets the position_description of this ModifyV2XEdgeDTO.

        **参数说明**：安装位置编码，由用户自定义。  **取值范围**：长度不低于1不超过128，只允许字母、数字、下划线（_）的组合。

        :param position_description: The position_description of this ModifyV2XEdgeDTO.
        :type position_description: str
        """
        self._position_description = position_description

    @property
    def location(self):
        """Gets the location of this ModifyV2XEdgeDTO.

        :return: The location of this ModifyV2XEdgeDTO.
        :rtype: :class:`huaweicloudsdkdris.v1.Location`
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this ModifyV2XEdgeDTO.

        :param location: The location of this ModifyV2XEdgeDTO.
        :type location: :class:`huaweicloudsdkdris.v1.Location`
        """
        self._location = location

    @property
    def camera_ids(self):
        """Gets the camera_ids of this ModifyV2XEdgeDTO.

        **参数说明**：摄像头ID列表。

        :return: The camera_ids of this ModifyV2XEdgeDTO.
        :rtype: list[str]
        """
        return self._camera_ids

    @camera_ids.setter
    def camera_ids(self, camera_ids):
        """Sets the camera_ids of this ModifyV2XEdgeDTO.

        **参数说明**：摄像头ID列表。

        :param camera_ids: The camera_ids of this ModifyV2XEdgeDTO.
        :type camera_ids: list[str]
        """
        self._camera_ids = camera_ids

    @property
    def radar_ids(self):
        """Gets the radar_ids of this ModifyV2XEdgeDTO.

        **参数说明**：雷达ID列表。

        :return: The radar_ids of this ModifyV2XEdgeDTO.
        :rtype: list[str]
        """
        return self._radar_ids

    @radar_ids.setter
    def radar_ids(self, radar_ids):
        """Sets the radar_ids of this ModifyV2XEdgeDTO.

        **参数说明**：雷达ID列表。

        :param radar_ids: The radar_ids of this ModifyV2XEdgeDTO.
        :type radar_ids: list[str]
        """
        self._radar_ids = radar_ids

    @property
    def local_rsus(self):
        """Gets the local_rsus of this ModifyV2XEdgeDTO.

        **参数说明**：Edge关联的本地RSU列表。

        :return: The local_rsus of this ModifyV2XEdgeDTO.
        :rtype: list[str]
        """
        return self._local_rsus

    @local_rsus.setter
    def local_rsus(self, local_rsus):
        """Sets the local_rsus of this ModifyV2XEdgeDTO.

        **参数说明**：Edge关联的本地RSU列表。

        :param local_rsus: The local_rsus of this ModifyV2XEdgeDTO.
        :type local_rsus: list[str]
        """
        self._local_rsus = local_rsus

    @property
    def edge_general_config(self):
        """Gets the edge_general_config of this ModifyV2XEdgeDTO.

        :return: The edge_general_config of this ModifyV2XEdgeDTO.
        :rtype: :class:`huaweicloudsdkdris.v1.EdgeGeneralConfig`
        """
        return self._edge_general_config

    @edge_general_config.setter
    def edge_general_config(self, edge_general_config):
        """Sets the edge_general_config of this ModifyV2XEdgeDTO.

        :param edge_general_config: The edge_general_config of this ModifyV2XEdgeDTO.
        :type edge_general_config: :class:`huaweicloudsdkdris.v1.EdgeGeneralConfig`
        """
        self._edge_general_config = edge_general_config

    @property
    def edge_advance_config(self):
        """Gets the edge_advance_config of this ModifyV2XEdgeDTO.

        **参数说明**：Edge高级配置（请谨慎修改，错误的配置将导致edge不可用），Json格式；如果想要删除整个edge_advance_config可以填写空Object（例如:{}）。如果想移除某个配置项，直接从配置数据中移除相应的属性即可。

        :return: The edge_advance_config of this ModifyV2XEdgeDTO.
        :rtype: object
        """
        return self._edge_advance_config

    @edge_advance_config.setter
    def edge_advance_config(self, edge_advance_config):
        """Sets the edge_advance_config of this ModifyV2XEdgeDTO.

        **参数说明**：Edge高级配置（请谨慎修改，错误的配置将导致edge不可用），Json格式；如果想要删除整个edge_advance_config可以填写空Object（例如:{}）。如果想移除某个配置项，直接从配置数据中移除相应的属性即可。

        :param edge_advance_config: The edge_advance_config of this ModifyV2XEdgeDTO.
        :type edge_advance_config: object
        """
        self._edge_advance_config = edge_advance_config

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
        if not isinstance(other, ModifyV2XEdgeDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
