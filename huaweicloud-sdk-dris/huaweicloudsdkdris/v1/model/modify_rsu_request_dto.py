# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyRsuRequestDTO:

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
        'ip': 'str',
        'position_description': 'str',
        'related_edge_num': 'int',
        'intersection_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'ip': 'ip',
        'position_description': 'position_description',
        'related_edge_num': 'related_edge_num',
        'intersection_id': 'intersection_id'
    }

    def __init__(self, name=None, description=None, ip=None, position_description=None, related_edge_num=None, intersection_id=None):
        """ModifyRsuRequestDTO

        The model defined in huaweicloud sdk

        :param name: **参数说明**：RSU的名字。  **取值范围**：长度不低于1不超过128，只允许中文、字母、数字、下划线（_）、连接符（-）的组合。
        :type name: str
        :param description: **参数说明**：RSU的描述。  **取值范围**：只允许中文、字母、数字、下划线（_）、中文分号（；）、中文冒号（：）、中文问号（？）、中文感叹号（！）中文逗号（，）、中文句号（。）、英文分号（;）、英文冒号（:）、英文逗号（,）、英文句号（.）、英文问号（?）、英文感叹号（!）、顿号（、）、连接符（-）的组合。
        :type description: str
        :param ip: **参数说明**：RSU的IP。满足IP的格式，例如127.0.0.1。
        :type ip: str
        :param position_description: **参数说明**：安装位置编码，由用户自定义。  **取值范围**：长度不低于1不超过128，只允许字母、数字、下划线（_）的组合。
        :type position_description: str
        :param related_edge_num: **参数说明**：RSU可关联的Edge的数量，修改值需大于等于当前已连接设备。
        :type related_edge_num: int
        :param intersection_id: **参数说明**：在地图中，rsu所在区域对应的路口ID，也即区域ID拼接路口ID，格式为：region-node_id。其中路网最基本的构成即节点和节点之间连接的路段。节点可以是路口，也可以是一条 路的端点。一个节点的ID在同一个区域内是唯一的。
        :type intersection_id: str
        """
        
        

        self._name = None
        self._description = None
        self._ip = None
        self._position_description = None
        self._related_edge_num = None
        self._intersection_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if ip is not None:
            self.ip = ip
        if position_description is not None:
            self.position_description = position_description
        if related_edge_num is not None:
            self.related_edge_num = related_edge_num
        if intersection_id is not None:
            self.intersection_id = intersection_id

    @property
    def name(self):
        """Gets the name of this ModifyRsuRequestDTO.

        **参数说明**：RSU的名字。  **取值范围**：长度不低于1不超过128，只允许中文、字母、数字、下划线（_）、连接符（-）的组合。

        :return: The name of this ModifyRsuRequestDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModifyRsuRequestDTO.

        **参数说明**：RSU的名字。  **取值范围**：长度不低于1不超过128，只允许中文、字母、数字、下划线（_）、连接符（-）的组合。

        :param name: The name of this ModifyRsuRequestDTO.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ModifyRsuRequestDTO.

        **参数说明**：RSU的描述。  **取值范围**：只允许中文、字母、数字、下划线（_）、中文分号（；）、中文冒号（：）、中文问号（？）、中文感叹号（！）中文逗号（，）、中文句号（。）、英文分号（;）、英文冒号（:）、英文逗号（,）、英文句号（.）、英文问号（?）、英文感叹号（!）、顿号（、）、连接符（-）的组合。

        :return: The description of this ModifyRsuRequestDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModifyRsuRequestDTO.

        **参数说明**：RSU的描述。  **取值范围**：只允许中文、字母、数字、下划线（_）、中文分号（；）、中文冒号（：）、中文问号（？）、中文感叹号（！）中文逗号（，）、中文句号（。）、英文分号（;）、英文冒号（:）、英文逗号（,）、英文句号（.）、英文问号（?）、英文感叹号（!）、顿号（、）、连接符（-）的组合。

        :param description: The description of this ModifyRsuRequestDTO.
        :type description: str
        """
        self._description = description

    @property
    def ip(self):
        """Gets the ip of this ModifyRsuRequestDTO.

        **参数说明**：RSU的IP。满足IP的格式，例如127.0.0.1。

        :return: The ip of this ModifyRsuRequestDTO.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ModifyRsuRequestDTO.

        **参数说明**：RSU的IP。满足IP的格式，例如127.0.0.1。

        :param ip: The ip of this ModifyRsuRequestDTO.
        :type ip: str
        """
        self._ip = ip

    @property
    def position_description(self):
        """Gets the position_description of this ModifyRsuRequestDTO.

        **参数说明**：安装位置编码，由用户自定义。  **取值范围**：长度不低于1不超过128，只允许字母、数字、下划线（_）的组合。

        :return: The position_description of this ModifyRsuRequestDTO.
        :rtype: str
        """
        return self._position_description

    @position_description.setter
    def position_description(self, position_description):
        """Sets the position_description of this ModifyRsuRequestDTO.

        **参数说明**：安装位置编码，由用户自定义。  **取值范围**：长度不低于1不超过128，只允许字母、数字、下划线（_）的组合。

        :param position_description: The position_description of this ModifyRsuRequestDTO.
        :type position_description: str
        """
        self._position_description = position_description

    @property
    def related_edge_num(self):
        """Gets the related_edge_num of this ModifyRsuRequestDTO.

        **参数说明**：RSU可关联的Edge的数量，修改值需大于等于当前已连接设备。

        :return: The related_edge_num of this ModifyRsuRequestDTO.
        :rtype: int
        """
        return self._related_edge_num

    @related_edge_num.setter
    def related_edge_num(self, related_edge_num):
        """Sets the related_edge_num of this ModifyRsuRequestDTO.

        **参数说明**：RSU可关联的Edge的数量，修改值需大于等于当前已连接设备。

        :param related_edge_num: The related_edge_num of this ModifyRsuRequestDTO.
        :type related_edge_num: int
        """
        self._related_edge_num = related_edge_num

    @property
    def intersection_id(self):
        """Gets the intersection_id of this ModifyRsuRequestDTO.

        **参数说明**：在地图中，rsu所在区域对应的路口ID，也即区域ID拼接路口ID，格式为：region-node_id。其中路网最基本的构成即节点和节点之间连接的路段。节点可以是路口，也可以是一条 路的端点。一个节点的ID在同一个区域内是唯一的。

        :return: The intersection_id of this ModifyRsuRequestDTO.
        :rtype: str
        """
        return self._intersection_id

    @intersection_id.setter
    def intersection_id(self, intersection_id):
        """Sets the intersection_id of this ModifyRsuRequestDTO.

        **参数说明**：在地图中，rsu所在区域对应的路口ID，也即区域ID拼接路口ID，格式为：region-node_id。其中路网最基本的构成即节点和节点之间连接的路段。节点可以是路口，也可以是一条 路的端点。一个节点的ID在同一个区域内是唯一的。

        :param intersection_id: The intersection_id of this ModifyRsuRequestDTO.
        :type intersection_id: str
        """
        self._intersection_id = intersection_id

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
        if not isinstance(other, ModifyRsuRequestDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
