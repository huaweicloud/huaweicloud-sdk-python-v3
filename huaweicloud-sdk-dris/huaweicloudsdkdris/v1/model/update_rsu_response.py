# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRsuResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rsu_id': 'str',
        'name': 'str',
        'description': 'str',
        'esn': 'str',
        'last_modified_time': 'datetime',
        'created_time': 'datetime',
        'last_online_time': 'datetime',
        'ip': 'str',
        'position_description': 'str',
        'location': 'RsuLocation',
        'status': 'str',
        'rsu_model_id': 'str',
        'intersection_id': 'str',
        'related_edge_num': 'int',
        'software_version': 'str'
    }

    attribute_map = {
        'rsu_id': 'rsu_id',
        'name': 'name',
        'description': 'description',
        'esn': 'esn',
        'last_modified_time': 'last_modified_time',
        'created_time': 'created_time',
        'last_online_time': 'last_online_time',
        'ip': 'ip',
        'position_description': 'position_description',
        'location': 'location',
        'status': 'status',
        'rsu_model_id': 'rsu_model_id',
        'intersection_id': 'intersection_id',
        'related_edge_num': 'related_edge_num',
        'software_version': 'software_version'
    }

    def __init__(self, rsu_id=None, name=None, description=None, esn=None, last_modified_time=None, created_time=None, last_online_time=None, ip=None, position_description=None, location=None, status=None, rsu_model_id=None, intersection_id=None, related_edge_num=None, software_version=None):
        """UpdateRsuResponse

        The model defined in huaweicloud sdk

        :param rsu_id: **参数说明**：RSU的唯一标识符，在平台创建RSU时由平台生成。
        :type rsu_id: str
        :param name: **参数说明**：RSU的名字。  **取值范围**：长度不低于1不超过128，只允许中文、字母、数字、下划线（_）、连接符（-）的组合。
        :type name: str
        :param description: **参数说明**：RSU的描述。  **取值范围**：只允许中文、字母、数字、下划线（_）、中文分号（；）、中文冒号（：）、中文问号（？）、中文感叹号（！）中文逗号（，）、中文句号（。）、英文分号（;）、英文冒号（:）、英文逗号（,）、英文句号（.）、英文问号（?）、英文感叹号（!）、顿号（、）、连接符（-）的组合。
        :type description: str
        :param esn: **参数说明**：RSU的设备序列号。  **取值范围**：只允许字母、数字、下划线（_）的组合。
        :type esn: str
        :param last_modified_time: **参数说明**：最后修改的时间。  格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;  例如 2020-09-01T01:37:01Z
        :type last_modified_time: datetime
        :param created_time: **参数说明**：创建的时间。  格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;  例如 2020-09-01T01:37:01Z
        :type created_time: datetime
        :param last_online_time: **参数说明**：最后的在线时间。  格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;  例如 2020-09-01T01:37:01Z
        :type last_online_time: datetime
        :param ip: **参数说明**：RSU的IP。满足IP的格式，例如127.0.0.1。
        :type ip: str
        :param position_description: **参数说明**：安装位置编码，由用户自定义。  **取值范围**：长度不低于1不超过128，只允许字母、数字、下划线（_）的组合。
        :type position_description: str
        :param location: 
        :type location: :class:`huaweicloudsdkdris.v1.RsuLocation`
        :param status: **参数说明**：RSU设备状态。  **取值范围**：  - ONLINE：在线  - OFFLINE：离线  - INITIAL：初始化  - UNKNOWN：未知
        :type status: str
        :param rsu_model_id: **参数说明**：RSU型号ID，用于唯一标识一个RSU型号，在平台创建RSU型号后由平台分配获得，获取方法可参见 [创建RSU型号](https://support.huaweicloud.com/api-v2x/v2x_04_0020.html)。  **取值范围**：长度不低于1不超过36，只允许字母、数字、连接符（-）的组合。  **该字段仅供使用MQTT协议RSU设备的用户输入。使用websocket协议RSU设备的用户需忽略此字段。**
        :type rsu_model_id: str
        :param intersection_id: **参数说明**：在地图中，rsu所在区域对应的路口ID，也即区域ID拼接路口ID，格式为：region-node_id。其中路网最基本的构成即节点和节点之间连接的路段。节点可以是路口，也可以是一条 路的端点。一个节点的ID在同一个区域内是唯一的。
        :type intersection_id: str
        :param related_edge_num: **参数说明**：RSU可关联的Edge的数量。
        :type related_edge_num: int
        :param software_version: **参数说明**：RSU的软件版本，由RSU上报其软件版本。
        :type software_version: str
        """
        
        super(UpdateRsuResponse, self).__init__()

        self._rsu_id = None
        self._name = None
        self._description = None
        self._esn = None
        self._last_modified_time = None
        self._created_time = None
        self._last_online_time = None
        self._ip = None
        self._position_description = None
        self._location = None
        self._status = None
        self._rsu_model_id = None
        self._intersection_id = None
        self._related_edge_num = None
        self._software_version = None
        self.discriminator = None

        if rsu_id is not None:
            self.rsu_id = rsu_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if esn is not None:
            self.esn = esn
        if last_modified_time is not None:
            self.last_modified_time = last_modified_time
        if created_time is not None:
            self.created_time = created_time
        if last_online_time is not None:
            self.last_online_time = last_online_time
        if ip is not None:
            self.ip = ip
        if position_description is not None:
            self.position_description = position_description
        if location is not None:
            self.location = location
        if status is not None:
            self.status = status
        if rsu_model_id is not None:
            self.rsu_model_id = rsu_model_id
        if intersection_id is not None:
            self.intersection_id = intersection_id
        if related_edge_num is not None:
            self.related_edge_num = related_edge_num
        if software_version is not None:
            self.software_version = software_version

    @property
    def rsu_id(self):
        """Gets the rsu_id of this UpdateRsuResponse.

        **参数说明**：RSU的唯一标识符，在平台创建RSU时由平台生成。

        :return: The rsu_id of this UpdateRsuResponse.
        :rtype: str
        """
        return self._rsu_id

    @rsu_id.setter
    def rsu_id(self, rsu_id):
        """Sets the rsu_id of this UpdateRsuResponse.

        **参数说明**：RSU的唯一标识符，在平台创建RSU时由平台生成。

        :param rsu_id: The rsu_id of this UpdateRsuResponse.
        :type rsu_id: str
        """
        self._rsu_id = rsu_id

    @property
    def name(self):
        """Gets the name of this UpdateRsuResponse.

        **参数说明**：RSU的名字。  **取值范围**：长度不低于1不超过128，只允许中文、字母、数字、下划线（_）、连接符（-）的组合。

        :return: The name of this UpdateRsuResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateRsuResponse.

        **参数说明**：RSU的名字。  **取值范围**：长度不低于1不超过128，只允许中文、字母、数字、下划线（_）、连接符（-）的组合。

        :param name: The name of this UpdateRsuResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateRsuResponse.

        **参数说明**：RSU的描述。  **取值范围**：只允许中文、字母、数字、下划线（_）、中文分号（；）、中文冒号（：）、中文问号（？）、中文感叹号（！）中文逗号（，）、中文句号（。）、英文分号（;）、英文冒号（:）、英文逗号（,）、英文句号（.）、英文问号（?）、英文感叹号（!）、顿号（、）、连接符（-）的组合。

        :return: The description of this UpdateRsuResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateRsuResponse.

        **参数说明**：RSU的描述。  **取值范围**：只允许中文、字母、数字、下划线（_）、中文分号（；）、中文冒号（：）、中文问号（？）、中文感叹号（！）中文逗号（，）、中文句号（。）、英文分号（;）、英文冒号（:）、英文逗号（,）、英文句号（.）、英文问号（?）、英文感叹号（!）、顿号（、）、连接符（-）的组合。

        :param description: The description of this UpdateRsuResponse.
        :type description: str
        """
        self._description = description

    @property
    def esn(self):
        """Gets the esn of this UpdateRsuResponse.

        **参数说明**：RSU的设备序列号。  **取值范围**：只允许字母、数字、下划线（_）的组合。

        :return: The esn of this UpdateRsuResponse.
        :rtype: str
        """
        return self._esn

    @esn.setter
    def esn(self, esn):
        """Sets the esn of this UpdateRsuResponse.

        **参数说明**：RSU的设备序列号。  **取值范围**：只允许字母、数字、下划线（_）的组合。

        :param esn: The esn of this UpdateRsuResponse.
        :type esn: str
        """
        self._esn = esn

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this UpdateRsuResponse.

        **参数说明**：最后修改的时间。  格式：yyyy-MM-dd'T'HH:mm:ss'Z'  例如 2020-09-01T01:37:01Z

        :return: The last_modified_time of this UpdateRsuResponse.
        :rtype: datetime
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this UpdateRsuResponse.

        **参数说明**：最后修改的时间。  格式：yyyy-MM-dd'T'HH:mm:ss'Z'  例如 2020-09-01T01:37:01Z

        :param last_modified_time: The last_modified_time of this UpdateRsuResponse.
        :type last_modified_time: datetime
        """
        self._last_modified_time = last_modified_time

    @property
    def created_time(self):
        """Gets the created_time of this UpdateRsuResponse.

        **参数说明**：创建的时间。  格式：yyyy-MM-dd'T'HH:mm:ss'Z'  例如 2020-09-01T01:37:01Z

        :return: The created_time of this UpdateRsuResponse.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this UpdateRsuResponse.

        **参数说明**：创建的时间。  格式：yyyy-MM-dd'T'HH:mm:ss'Z'  例如 2020-09-01T01:37:01Z

        :param created_time: The created_time of this UpdateRsuResponse.
        :type created_time: datetime
        """
        self._created_time = created_time

    @property
    def last_online_time(self):
        """Gets the last_online_time of this UpdateRsuResponse.

        **参数说明**：最后的在线时间。  格式：yyyy-MM-dd'T'HH:mm:ss'Z'  例如 2020-09-01T01:37:01Z

        :return: The last_online_time of this UpdateRsuResponse.
        :rtype: datetime
        """
        return self._last_online_time

    @last_online_time.setter
    def last_online_time(self, last_online_time):
        """Sets the last_online_time of this UpdateRsuResponse.

        **参数说明**：最后的在线时间。  格式：yyyy-MM-dd'T'HH:mm:ss'Z'  例如 2020-09-01T01:37:01Z

        :param last_online_time: The last_online_time of this UpdateRsuResponse.
        :type last_online_time: datetime
        """
        self._last_online_time = last_online_time

    @property
    def ip(self):
        """Gets the ip of this UpdateRsuResponse.

        **参数说明**：RSU的IP。满足IP的格式，例如127.0.0.1。

        :return: The ip of this UpdateRsuResponse.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this UpdateRsuResponse.

        **参数说明**：RSU的IP。满足IP的格式，例如127.0.0.1。

        :param ip: The ip of this UpdateRsuResponse.
        :type ip: str
        """
        self._ip = ip

    @property
    def position_description(self):
        """Gets the position_description of this UpdateRsuResponse.

        **参数说明**：安装位置编码，由用户自定义。  **取值范围**：长度不低于1不超过128，只允许字母、数字、下划线（_）的组合。

        :return: The position_description of this UpdateRsuResponse.
        :rtype: str
        """
        return self._position_description

    @position_description.setter
    def position_description(self, position_description):
        """Sets the position_description of this UpdateRsuResponse.

        **参数说明**：安装位置编码，由用户自定义。  **取值范围**：长度不低于1不超过128，只允许字母、数字、下划线（_）的组合。

        :param position_description: The position_description of this UpdateRsuResponse.
        :type position_description: str
        """
        self._position_description = position_description

    @property
    def location(self):
        """Gets the location of this UpdateRsuResponse.

        :return: The location of this UpdateRsuResponse.
        :rtype: :class:`huaweicloudsdkdris.v1.RsuLocation`
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this UpdateRsuResponse.

        :param location: The location of this UpdateRsuResponse.
        :type location: :class:`huaweicloudsdkdris.v1.RsuLocation`
        """
        self._location = location

    @property
    def status(self):
        """Gets the status of this UpdateRsuResponse.

        **参数说明**：RSU设备状态。  **取值范围**：  - ONLINE：在线  - OFFLINE：离线  - INITIAL：初始化  - UNKNOWN：未知

        :return: The status of this UpdateRsuResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateRsuResponse.

        **参数说明**：RSU设备状态。  **取值范围**：  - ONLINE：在线  - OFFLINE：离线  - INITIAL：初始化  - UNKNOWN：未知

        :param status: The status of this UpdateRsuResponse.
        :type status: str
        """
        self._status = status

    @property
    def rsu_model_id(self):
        """Gets the rsu_model_id of this UpdateRsuResponse.

        **参数说明**：RSU型号ID，用于唯一标识一个RSU型号，在平台创建RSU型号后由平台分配获得，获取方法可参见 [创建RSU型号](https://support.huaweicloud.com/api-v2x/v2x_04_0020.html)。  **取值范围**：长度不低于1不超过36，只允许字母、数字、连接符（-）的组合。  **该字段仅供使用MQTT协议RSU设备的用户输入。使用websocket协议RSU设备的用户需忽略此字段。**

        :return: The rsu_model_id of this UpdateRsuResponse.
        :rtype: str
        """
        return self._rsu_model_id

    @rsu_model_id.setter
    def rsu_model_id(self, rsu_model_id):
        """Sets the rsu_model_id of this UpdateRsuResponse.

        **参数说明**：RSU型号ID，用于唯一标识一个RSU型号，在平台创建RSU型号后由平台分配获得，获取方法可参见 [创建RSU型号](https://support.huaweicloud.com/api-v2x/v2x_04_0020.html)。  **取值范围**：长度不低于1不超过36，只允许字母、数字、连接符（-）的组合。  **该字段仅供使用MQTT协议RSU设备的用户输入。使用websocket协议RSU设备的用户需忽略此字段。**

        :param rsu_model_id: The rsu_model_id of this UpdateRsuResponse.
        :type rsu_model_id: str
        """
        self._rsu_model_id = rsu_model_id

    @property
    def intersection_id(self):
        """Gets the intersection_id of this UpdateRsuResponse.

        **参数说明**：在地图中，rsu所在区域对应的路口ID，也即区域ID拼接路口ID，格式为：region-node_id。其中路网最基本的构成即节点和节点之间连接的路段。节点可以是路口，也可以是一条 路的端点。一个节点的ID在同一个区域内是唯一的。

        :return: The intersection_id of this UpdateRsuResponse.
        :rtype: str
        """
        return self._intersection_id

    @intersection_id.setter
    def intersection_id(self, intersection_id):
        """Sets the intersection_id of this UpdateRsuResponse.

        **参数说明**：在地图中，rsu所在区域对应的路口ID，也即区域ID拼接路口ID，格式为：region-node_id。其中路网最基本的构成即节点和节点之间连接的路段。节点可以是路口，也可以是一条 路的端点。一个节点的ID在同一个区域内是唯一的。

        :param intersection_id: The intersection_id of this UpdateRsuResponse.
        :type intersection_id: str
        """
        self._intersection_id = intersection_id

    @property
    def related_edge_num(self):
        """Gets the related_edge_num of this UpdateRsuResponse.

        **参数说明**：RSU可关联的Edge的数量。

        :return: The related_edge_num of this UpdateRsuResponse.
        :rtype: int
        """
        return self._related_edge_num

    @related_edge_num.setter
    def related_edge_num(self, related_edge_num):
        """Sets the related_edge_num of this UpdateRsuResponse.

        **参数说明**：RSU可关联的Edge的数量。

        :param related_edge_num: The related_edge_num of this UpdateRsuResponse.
        :type related_edge_num: int
        """
        self._related_edge_num = related_edge_num

    @property
    def software_version(self):
        """Gets the software_version of this UpdateRsuResponse.

        **参数说明**：RSU的软件版本，由RSU上报其软件版本。

        :return: The software_version of this UpdateRsuResponse.
        :rtype: str
        """
        return self._software_version

    @software_version.setter
    def software_version(self, software_version):
        """Sets the software_version of this UpdateRsuResponse.

        **参数说明**：RSU的软件版本，由RSU上报其软件版本。

        :param software_version: The software_version of this UpdateRsuResponse.
        :type software_version: str
        """
        self._software_version = software_version

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
        if not isinstance(other, UpdateRsuResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
