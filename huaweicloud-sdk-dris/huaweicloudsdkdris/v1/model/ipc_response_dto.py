# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpcResponseDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'camera_id': 'str',
        'v2x_edge_id': 'str',
        'name': 'str',
        'cross_id': 'str',
        'focal_type': 'str',
        'parent_connect_code': 'str',
        'connect_code': 'str',
        'description': 'str',
        'esn': 'str',
        'ip': 'str',
        'status': 'str',
        'created_time': 'datetime',
        'last_modified_time': 'datetime',
        'last_online_time': 'datetime'
    }

    attribute_map = {
        'camera_id': 'camera_id',
        'v2x_edge_id': 'v2x_edge_id',
        'name': 'name',
        'cross_id': 'cross_id',
        'focal_type': 'focal_type',
        'parent_connect_code': 'parent_connect_code',
        'connect_code': 'connect_code',
        'description': 'description',
        'esn': 'esn',
        'ip': 'ip',
        'status': 'status',
        'created_time': 'created_time',
        'last_modified_time': 'last_modified_time',
        'last_online_time': 'last_online_time'
    }

    def __init__(self, camera_id=None, v2x_edge_id=None, name=None, cross_id=None, focal_type=None, parent_connect_code=None, connect_code=None, description=None, esn=None, ip=None, status=None, created_time=None, last_modified_time=None, last_online_time=None):
        r"""IpcResponseDTO

        The model defined in huaweicloud sdk

        :param camera_id: **参数说明**：摄像头ID，console界面查询摄像头IPC列表中的设备Id。
        :type camera_id: str
        :param v2x_edge_id: **参数说明**：Edge ID，用于唯一标识一个Edge，创建Edge后获得。方法参见 [创建Edge](https://support.huaweicloud.com/api-v2x/v2x_04_0078.html)。
        :type v2x_edge_id: str
        :param name: **参数说明**：摄像头名称。
        :type name: str
        :param cross_id: **参数说明**：摄像头所感知的路口或者路段的Id。
        :type cross_id: str
        :param focal_type: **参数说明**：摄像头聚焦类型。  - long：长焦  - short：短焦
        :type focal_type: str
        :param parent_connect_code: **参数说明**：摄像头连接的ITS800的互联编码。
        :type parent_connect_code: str
        :param connect_code: **参数说明**：摄像头的互联编码。
        :type connect_code: str
        :param description: **参数说明**：描述。
        :type description: str
        :param esn: **参数说明**：IPC的设备编码。
        :type esn: str
        :param ip: **参数说明**：该摄像头的ip地址。
        :type ip: str
        :param status: **参数说明**：摄像机的状态。  **取值范围**：  - ONLINE：在线   - OFFLINE：离线  - INITIAL：初始化  - UNKNOWN：未知   - SLEEP：休眠
        :type status: str
        :param created_time: **参数说明**：创建时间。            格式：yyyy-MM-dd&#39;&#39;T&#39;&#39;HH:mm:ss&#39;&#39;Z&#39;&#39;。  例如 2020-09-01T01:37:01Z。
        :type created_time: datetime
        :param last_modified_time: **参数说明**：最后修改时间。            格式：yyyy-MM-dd&#39;&#39;T&#39;&#39;HH:mm:ss&#39;&#39;Z&#39;&#39;。  例如 2020-09-01T01:37:01Z。
        :type last_modified_time: datetime
        :param last_online_time: **参数说明**：最后在线时间。          格式：yyyy-MM-dd&#39;&#39;T&#39;&#39;HH:mm:ss&#39;&#39;Z&#39;&#39;。  例如 2020-09-01T01:37:01Z。
        :type last_online_time: datetime
        """
        
        

        self._camera_id = None
        self._v2x_edge_id = None
        self._name = None
        self._cross_id = None
        self._focal_type = None
        self._parent_connect_code = None
        self._connect_code = None
        self._description = None
        self._esn = None
        self._ip = None
        self._status = None
        self._created_time = None
        self._last_modified_time = None
        self._last_online_time = None
        self.discriminator = None

        if camera_id is not None:
            self.camera_id = camera_id
        if v2x_edge_id is not None:
            self.v2x_edge_id = v2x_edge_id
        if name is not None:
            self.name = name
        if cross_id is not None:
            self.cross_id = cross_id
        if focal_type is not None:
            self.focal_type = focal_type
        if parent_connect_code is not None:
            self.parent_connect_code = parent_connect_code
        if connect_code is not None:
            self.connect_code = connect_code
        if description is not None:
            self.description = description
        if esn is not None:
            self.esn = esn
        if ip is not None:
            self.ip = ip
        if status is not None:
            self.status = status
        if created_time is not None:
            self.created_time = created_time
        if last_modified_time is not None:
            self.last_modified_time = last_modified_time
        if last_online_time is not None:
            self.last_online_time = last_online_time

    @property
    def camera_id(self):
        r"""Gets the camera_id of this IpcResponseDTO.

        **参数说明**：摄像头ID，console界面查询摄像头IPC列表中的设备Id。

        :return: The camera_id of this IpcResponseDTO.
        :rtype: str
        """
        return self._camera_id

    @camera_id.setter
    def camera_id(self, camera_id):
        r"""Sets the camera_id of this IpcResponseDTO.

        **参数说明**：摄像头ID，console界面查询摄像头IPC列表中的设备Id。

        :param camera_id: The camera_id of this IpcResponseDTO.
        :type camera_id: str
        """
        self._camera_id = camera_id

    @property
    def v2x_edge_id(self):
        r"""Gets the v2x_edge_id of this IpcResponseDTO.

        **参数说明**：Edge ID，用于唯一标识一个Edge，创建Edge后获得。方法参见 [创建Edge](https://support.huaweicloud.com/api-v2x/v2x_04_0078.html)。

        :return: The v2x_edge_id of this IpcResponseDTO.
        :rtype: str
        """
        return self._v2x_edge_id

    @v2x_edge_id.setter
    def v2x_edge_id(self, v2x_edge_id):
        r"""Sets the v2x_edge_id of this IpcResponseDTO.

        **参数说明**：Edge ID，用于唯一标识一个Edge，创建Edge后获得。方法参见 [创建Edge](https://support.huaweicloud.com/api-v2x/v2x_04_0078.html)。

        :param v2x_edge_id: The v2x_edge_id of this IpcResponseDTO.
        :type v2x_edge_id: str
        """
        self._v2x_edge_id = v2x_edge_id

    @property
    def name(self):
        r"""Gets the name of this IpcResponseDTO.

        **参数说明**：摄像头名称。

        :return: The name of this IpcResponseDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this IpcResponseDTO.

        **参数说明**：摄像头名称。

        :param name: The name of this IpcResponseDTO.
        :type name: str
        """
        self._name = name

    @property
    def cross_id(self):
        r"""Gets the cross_id of this IpcResponseDTO.

        **参数说明**：摄像头所感知的路口或者路段的Id。

        :return: The cross_id of this IpcResponseDTO.
        :rtype: str
        """
        return self._cross_id

    @cross_id.setter
    def cross_id(self, cross_id):
        r"""Sets the cross_id of this IpcResponseDTO.

        **参数说明**：摄像头所感知的路口或者路段的Id。

        :param cross_id: The cross_id of this IpcResponseDTO.
        :type cross_id: str
        """
        self._cross_id = cross_id

    @property
    def focal_type(self):
        r"""Gets the focal_type of this IpcResponseDTO.

        **参数说明**：摄像头聚焦类型。  - long：长焦  - short：短焦

        :return: The focal_type of this IpcResponseDTO.
        :rtype: str
        """
        return self._focal_type

    @focal_type.setter
    def focal_type(self, focal_type):
        r"""Sets the focal_type of this IpcResponseDTO.

        **参数说明**：摄像头聚焦类型。  - long：长焦  - short：短焦

        :param focal_type: The focal_type of this IpcResponseDTO.
        :type focal_type: str
        """
        self._focal_type = focal_type

    @property
    def parent_connect_code(self):
        r"""Gets the parent_connect_code of this IpcResponseDTO.

        **参数说明**：摄像头连接的ITS800的互联编码。

        :return: The parent_connect_code of this IpcResponseDTO.
        :rtype: str
        """
        return self._parent_connect_code

    @parent_connect_code.setter
    def parent_connect_code(self, parent_connect_code):
        r"""Sets the parent_connect_code of this IpcResponseDTO.

        **参数说明**：摄像头连接的ITS800的互联编码。

        :param parent_connect_code: The parent_connect_code of this IpcResponseDTO.
        :type parent_connect_code: str
        """
        self._parent_connect_code = parent_connect_code

    @property
    def connect_code(self):
        r"""Gets the connect_code of this IpcResponseDTO.

        **参数说明**：摄像头的互联编码。

        :return: The connect_code of this IpcResponseDTO.
        :rtype: str
        """
        return self._connect_code

    @connect_code.setter
    def connect_code(self, connect_code):
        r"""Sets the connect_code of this IpcResponseDTO.

        **参数说明**：摄像头的互联编码。

        :param connect_code: The connect_code of this IpcResponseDTO.
        :type connect_code: str
        """
        self._connect_code = connect_code

    @property
    def description(self):
        r"""Gets the description of this IpcResponseDTO.

        **参数说明**：描述。

        :return: The description of this IpcResponseDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this IpcResponseDTO.

        **参数说明**：描述。

        :param description: The description of this IpcResponseDTO.
        :type description: str
        """
        self._description = description

    @property
    def esn(self):
        r"""Gets the esn of this IpcResponseDTO.

        **参数说明**：IPC的设备编码。

        :return: The esn of this IpcResponseDTO.
        :rtype: str
        """
        return self._esn

    @esn.setter
    def esn(self, esn):
        r"""Sets the esn of this IpcResponseDTO.

        **参数说明**：IPC的设备编码。

        :param esn: The esn of this IpcResponseDTO.
        :type esn: str
        """
        self._esn = esn

    @property
    def ip(self):
        r"""Gets the ip of this IpcResponseDTO.

        **参数说明**：该摄像头的ip地址。

        :return: The ip of this IpcResponseDTO.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this IpcResponseDTO.

        **参数说明**：该摄像头的ip地址。

        :param ip: The ip of this IpcResponseDTO.
        :type ip: str
        """
        self._ip = ip

    @property
    def status(self):
        r"""Gets the status of this IpcResponseDTO.

        **参数说明**：摄像机的状态。  **取值范围**：  - ONLINE：在线   - OFFLINE：离线  - INITIAL：初始化  - UNKNOWN：未知   - SLEEP：休眠

        :return: The status of this IpcResponseDTO.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this IpcResponseDTO.

        **参数说明**：摄像机的状态。  **取值范围**：  - ONLINE：在线   - OFFLINE：离线  - INITIAL：初始化  - UNKNOWN：未知   - SLEEP：休眠

        :param status: The status of this IpcResponseDTO.
        :type status: str
        """
        self._status = status

    @property
    def created_time(self):
        r"""Gets the created_time of this IpcResponseDTO.

        **参数说明**：创建时间。            格式：yyyy-MM-dd''T''HH:mm:ss''Z''。  例如 2020-09-01T01:37:01Z。

        :return: The created_time of this IpcResponseDTO.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this IpcResponseDTO.

        **参数说明**：创建时间。            格式：yyyy-MM-dd''T''HH:mm:ss''Z''。  例如 2020-09-01T01:37:01Z。

        :param created_time: The created_time of this IpcResponseDTO.
        :type created_time: datetime
        """
        self._created_time = created_time

    @property
    def last_modified_time(self):
        r"""Gets the last_modified_time of this IpcResponseDTO.

        **参数说明**：最后修改时间。            格式：yyyy-MM-dd''T''HH:mm:ss''Z''。  例如 2020-09-01T01:37:01Z。

        :return: The last_modified_time of this IpcResponseDTO.
        :rtype: datetime
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        r"""Sets the last_modified_time of this IpcResponseDTO.

        **参数说明**：最后修改时间。            格式：yyyy-MM-dd''T''HH:mm:ss''Z''。  例如 2020-09-01T01:37:01Z。

        :param last_modified_time: The last_modified_time of this IpcResponseDTO.
        :type last_modified_time: datetime
        """
        self._last_modified_time = last_modified_time

    @property
    def last_online_time(self):
        r"""Gets the last_online_time of this IpcResponseDTO.

        **参数说明**：最后在线时间。          格式：yyyy-MM-dd''T''HH:mm:ss''Z''。  例如 2020-09-01T01:37:01Z。

        :return: The last_online_time of this IpcResponseDTO.
        :rtype: datetime
        """
        return self._last_online_time

    @last_online_time.setter
    def last_online_time(self, last_online_time):
        r"""Sets the last_online_time of this IpcResponseDTO.

        **参数说明**：最后在线时间。          格式：yyyy-MM-dd''T''HH:mm:ss''Z''。  例如 2020-09-01T01:37:01Z。

        :param last_online_time: The last_online_time of this IpcResponseDTO.
        :type last_online_time: datetime
        """
        self._last_online_time = last_online_time

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
        if not isinstance(other, IpcResponseDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
