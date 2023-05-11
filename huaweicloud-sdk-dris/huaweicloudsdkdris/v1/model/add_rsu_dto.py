# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddRsuDTO:

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
        'position_description': 'str',
        'related_edge_num': 'int',
        'rsu_model_id': 'str',
        'intersection_id': 'str',
        'secret': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'esn': 'esn',
        'ip': 'ip',
        'position_description': 'position_description',
        'related_edge_num': 'related_edge_num',
        'rsu_model_id': 'rsu_model_id',
        'intersection_id': 'intersection_id',
        'secret': 'secret'
    }

    def __init__(self, name=None, description=None, esn=None, ip=None, position_description=None, related_edge_num=None, rsu_model_id=None, intersection_id=None, secret=None):
        """AddRsuDTO

        The model defined in huaweicloud sdk

        :param name: **参数说明**：RSU的名字。  **取值范围**：长度不低于1不超过128，只允许中文、字母、数字、下划线（_）、连接符（-）的组合。
        :type name: str
        :param description: **参数说明**：RSU的描述。  **取值范围**：只允许中文、字母、数字、下划线（_）、中文分号（；）、中文冒号（：）、中文问号（？）、中文感叹号（！）中文逗号（，）、中文句号（。）、英文分号（;）、英文冒号（:）、英文逗号（,）、英文句号（.）、英文问号（?）、英文感叹号（!）、顿号（、）、连接符（-）的组合。
        :type description: str
        :param esn: **参数说明**：RSU的设备序列号。  **取值范围**：只允许字母、数字、下划线（_）的组合。
        :type esn: str
        :param ip: **参数说明**：RSU的IP。满足IP的格式，例如127.0.0.1。
        :type ip: str
        :param position_description: **参数说明**：安装位置编码，由用户自定义。  **取值范围**：长度不低于1不超过128，只允许字母、数字、下划线（_）的组合。
        :type position_description: str
        :param related_edge_num: **参数说明**：RSU可关联的Edge的数量。
        :type related_edge_num: int
        :param rsu_model_id: **参数说明**：RSU型号ID，用于唯一标识一个RSU型号，在平台创建RSU型号后由平台分配获得，获取方法可参见 [创建RSU型号](https://support.huaweicloud.com/api-v2x/v2x_04_0020.html)。  **取值范围**：长度不低于1不超过36，只允许字母、数字、连接符（-）的组合。  **该字段仅供使用MQTT协议RSU设备的用户输入。使用websocket协议RSU设备的用户需忽略此字段。**
        :type rsu_model_id: str
        :param intersection_id: **参数说明**：在地图中，rsu所在区域对应的路口ID，也即区域ID拼接路口ID，格式为：region-node_id。其中路网最基本的构成即节点和节点之间连接的路段。节点可以是路口，也可以是一条 路的端点。一个节点的ID在同一个区域内是唯一的。
        :type intersection_id: str
        :param secret: **参数说明**：MQTT协议RSU密钥，若携带了rsu_model_id参数，则该字段必填。RSU创建后该字段无法修改，查询RSU及查询RSU列表时该字段均不返回。  **取值范围**：只允许数字、小写字母a-f、大写字母A-F的组合。
        :type secret: str
        """
        
        

        self._name = None
        self._description = None
        self._esn = None
        self._ip = None
        self._position_description = None
        self._related_edge_num = None
        self._rsu_model_id = None
        self._intersection_id = None
        self._secret = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.esn = esn
        if ip is not None:
            self.ip = ip
        if position_description is not None:
            self.position_description = position_description
        self.related_edge_num = related_edge_num
        if rsu_model_id is not None:
            self.rsu_model_id = rsu_model_id
        if intersection_id is not None:
            self.intersection_id = intersection_id
        if secret is not None:
            self.secret = secret

    @property
    def name(self):
        """Gets the name of this AddRsuDTO.

        **参数说明**：RSU的名字。  **取值范围**：长度不低于1不超过128，只允许中文、字母、数字、下划线（_）、连接符（-）的组合。

        :return: The name of this AddRsuDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddRsuDTO.

        **参数说明**：RSU的名字。  **取值范围**：长度不低于1不超过128，只允许中文、字母、数字、下划线（_）、连接符（-）的组合。

        :param name: The name of this AddRsuDTO.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this AddRsuDTO.

        **参数说明**：RSU的描述。  **取值范围**：只允许中文、字母、数字、下划线（_）、中文分号（；）、中文冒号（：）、中文问号（？）、中文感叹号（！）中文逗号（，）、中文句号（。）、英文分号（;）、英文冒号（:）、英文逗号（,）、英文句号（.）、英文问号（?）、英文感叹号（!）、顿号（、）、连接符（-）的组合。

        :return: The description of this AddRsuDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AddRsuDTO.

        **参数说明**：RSU的描述。  **取值范围**：只允许中文、字母、数字、下划线（_）、中文分号（；）、中文冒号（：）、中文问号（？）、中文感叹号（！）中文逗号（，）、中文句号（。）、英文分号（;）、英文冒号（:）、英文逗号（,）、英文句号（.）、英文问号（?）、英文感叹号（!）、顿号（、）、连接符（-）的组合。

        :param description: The description of this AddRsuDTO.
        :type description: str
        """
        self._description = description

    @property
    def esn(self):
        """Gets the esn of this AddRsuDTO.

        **参数说明**：RSU的设备序列号。  **取值范围**：只允许字母、数字、下划线（_）的组合。

        :return: The esn of this AddRsuDTO.
        :rtype: str
        """
        return self._esn

    @esn.setter
    def esn(self, esn):
        """Sets the esn of this AddRsuDTO.

        **参数说明**：RSU的设备序列号。  **取值范围**：只允许字母、数字、下划线（_）的组合。

        :param esn: The esn of this AddRsuDTO.
        :type esn: str
        """
        self._esn = esn

    @property
    def ip(self):
        """Gets the ip of this AddRsuDTO.

        **参数说明**：RSU的IP。满足IP的格式，例如127.0.0.1。

        :return: The ip of this AddRsuDTO.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this AddRsuDTO.

        **参数说明**：RSU的IP。满足IP的格式，例如127.0.0.1。

        :param ip: The ip of this AddRsuDTO.
        :type ip: str
        """
        self._ip = ip

    @property
    def position_description(self):
        """Gets the position_description of this AddRsuDTO.

        **参数说明**：安装位置编码，由用户自定义。  **取值范围**：长度不低于1不超过128，只允许字母、数字、下划线（_）的组合。

        :return: The position_description of this AddRsuDTO.
        :rtype: str
        """
        return self._position_description

    @position_description.setter
    def position_description(self, position_description):
        """Sets the position_description of this AddRsuDTO.

        **参数说明**：安装位置编码，由用户自定义。  **取值范围**：长度不低于1不超过128，只允许字母、数字、下划线（_）的组合。

        :param position_description: The position_description of this AddRsuDTO.
        :type position_description: str
        """
        self._position_description = position_description

    @property
    def related_edge_num(self):
        """Gets the related_edge_num of this AddRsuDTO.

        **参数说明**：RSU可关联的Edge的数量。

        :return: The related_edge_num of this AddRsuDTO.
        :rtype: int
        """
        return self._related_edge_num

    @related_edge_num.setter
    def related_edge_num(self, related_edge_num):
        """Sets the related_edge_num of this AddRsuDTO.

        **参数说明**：RSU可关联的Edge的数量。

        :param related_edge_num: The related_edge_num of this AddRsuDTO.
        :type related_edge_num: int
        """
        self._related_edge_num = related_edge_num

    @property
    def rsu_model_id(self):
        """Gets the rsu_model_id of this AddRsuDTO.

        **参数说明**：RSU型号ID，用于唯一标识一个RSU型号，在平台创建RSU型号后由平台分配获得，获取方法可参见 [创建RSU型号](https://support.huaweicloud.com/api-v2x/v2x_04_0020.html)。  **取值范围**：长度不低于1不超过36，只允许字母、数字、连接符（-）的组合。  **该字段仅供使用MQTT协议RSU设备的用户输入。使用websocket协议RSU设备的用户需忽略此字段。**

        :return: The rsu_model_id of this AddRsuDTO.
        :rtype: str
        """
        return self._rsu_model_id

    @rsu_model_id.setter
    def rsu_model_id(self, rsu_model_id):
        """Sets the rsu_model_id of this AddRsuDTO.

        **参数说明**：RSU型号ID，用于唯一标识一个RSU型号，在平台创建RSU型号后由平台分配获得，获取方法可参见 [创建RSU型号](https://support.huaweicloud.com/api-v2x/v2x_04_0020.html)。  **取值范围**：长度不低于1不超过36，只允许字母、数字、连接符（-）的组合。  **该字段仅供使用MQTT协议RSU设备的用户输入。使用websocket协议RSU设备的用户需忽略此字段。**

        :param rsu_model_id: The rsu_model_id of this AddRsuDTO.
        :type rsu_model_id: str
        """
        self._rsu_model_id = rsu_model_id

    @property
    def intersection_id(self):
        """Gets the intersection_id of this AddRsuDTO.

        **参数说明**：在地图中，rsu所在区域对应的路口ID，也即区域ID拼接路口ID，格式为：region-node_id。其中路网最基本的构成即节点和节点之间连接的路段。节点可以是路口，也可以是一条 路的端点。一个节点的ID在同一个区域内是唯一的。

        :return: The intersection_id of this AddRsuDTO.
        :rtype: str
        """
        return self._intersection_id

    @intersection_id.setter
    def intersection_id(self, intersection_id):
        """Sets the intersection_id of this AddRsuDTO.

        **参数说明**：在地图中，rsu所在区域对应的路口ID，也即区域ID拼接路口ID，格式为：region-node_id。其中路网最基本的构成即节点和节点之间连接的路段。节点可以是路口，也可以是一条 路的端点。一个节点的ID在同一个区域内是唯一的。

        :param intersection_id: The intersection_id of this AddRsuDTO.
        :type intersection_id: str
        """
        self._intersection_id = intersection_id

    @property
    def secret(self):
        """Gets the secret of this AddRsuDTO.

        **参数说明**：MQTT协议RSU密钥，若携带了rsu_model_id参数，则该字段必填。RSU创建后该字段无法修改，查询RSU及查询RSU列表时该字段均不返回。  **取值范围**：只允许数字、小写字母a-f、大写字母A-F的组合。

        :return: The secret of this AddRsuDTO.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this AddRsuDTO.

        **参数说明**：MQTT协议RSU密钥，若携带了rsu_model_id参数，则该字段必填。RSU创建后该字段无法修改，查询RSU及查询RSU列表时该字段均不返回。  **取值范围**：只允许数字、小写字母a-f、大写字母A-F的组合。

        :param secret: The secret of this AddRsuDTO.
        :type secret: str
        """
        self._secret = secret

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
        if not isinstance(other, AddRsuDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
