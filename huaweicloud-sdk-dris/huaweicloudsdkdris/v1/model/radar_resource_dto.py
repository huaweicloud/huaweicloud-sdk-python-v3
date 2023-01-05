# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RadarResourceDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'radar_id': 'str',
        'name': 'str',
        'v2x_edge_id': 'str',
        'ip': 'str',
        'status': 'str',
        'esn': 'str',
        'position_description': 'str',
        'created_time': 'datetime',
        'last_modified_time': 'datetime',
        'last_online_time': 'datetime'
    }

    attribute_map = {
        'radar_id': 'radar_id',
        'name': 'name',
        'v2x_edge_id': 'v2x_edge_id',
        'ip': 'ip',
        'status': 'status',
        'esn': 'esn',
        'position_description': 'position_description',
        'created_time': 'created_time',
        'last_modified_time': 'last_modified_time',
        'last_online_time': 'last_online_time'
    }

    def __init__(self, radar_id=None, name=None, v2x_edge_id=None, ip=None, status=None, esn=None, position_description=None, created_time=None, last_modified_time=None, last_online_time=None):
        """RadarResourceDTO

        The model defined in huaweicloud sdk

        :param radar_id: **参数说明**：雷达ID 
        :type radar_id: str
        :param name: **参数说明**：名称  **取值范围**：长度不小于1，不大于128的汉字、英文字母、数字、下划线（_）和横杠（-）的组合。 
        :type name: str
        :param v2x_edge_id: **参数说明**：所属的EdgeId  **取值范围**：长度不小于1，不大于128的英文字母、数字、下划线（_）和横杠（-）的组合。 
        :type v2x_edge_id: str
        :param ip: **参数说明**：设备IP 
        :type ip: str
        :param status: **参数说明**：状态值  **取值范围**：   - ONLINE：在线   - OFFLINE：离线   - UNKNOWN：未知   - SLEEP：睡眠 
        :type status: str
        :param esn: **参数说明**：设备编号  **取值范围**：长度不小于1，不大于64的英文字母、数字和下划线（_）的组合。 
        :type esn: str
        :param position_description: **参数说明**：位置描述  **取值范围**：长度不小于1，不大于128的英文字母、数字和下划线（_）的组合。 
        :type position_description: str
        :param created_time: **参数说明**：最后修改的时间。格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39; 例如 2020-09-01T01:37:01Z 
        :type created_time: datetime
        :param last_modified_time: **参数说明**：最后修改时间。格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39; 例如 2020-09-01T01:37:01Z 
        :type last_modified_time: datetime
        :param last_online_time: **参数说明**：最后的在线时间。格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39; 例如 2020-09-01T01:37:01Z 
        :type last_online_time: datetime
        """
        
        

        self._radar_id = None
        self._name = None
        self._v2x_edge_id = None
        self._ip = None
        self._status = None
        self._esn = None
        self._position_description = None
        self._created_time = None
        self._last_modified_time = None
        self._last_online_time = None
        self.discriminator = None

        if radar_id is not None:
            self.radar_id = radar_id
        if name is not None:
            self.name = name
        if v2x_edge_id is not None:
            self.v2x_edge_id = v2x_edge_id
        if ip is not None:
            self.ip = ip
        if status is not None:
            self.status = status
        if esn is not None:
            self.esn = esn
        if position_description is not None:
            self.position_description = position_description
        if created_time is not None:
            self.created_time = created_time
        if last_modified_time is not None:
            self.last_modified_time = last_modified_time
        if last_online_time is not None:
            self.last_online_time = last_online_time

    @property
    def radar_id(self):
        """Gets the radar_id of this RadarResourceDTO.

        **参数说明**：雷达ID 

        :return: The radar_id of this RadarResourceDTO.
        :rtype: str
        """
        return self._radar_id

    @radar_id.setter
    def radar_id(self, radar_id):
        """Sets the radar_id of this RadarResourceDTO.

        **参数说明**：雷达ID 

        :param radar_id: The radar_id of this RadarResourceDTO.
        :type radar_id: str
        """
        self._radar_id = radar_id

    @property
    def name(self):
        """Gets the name of this RadarResourceDTO.

        **参数说明**：名称  **取值范围**：长度不小于1，不大于128的汉字、英文字母、数字、下划线（_）和横杠（-）的组合。 

        :return: The name of this RadarResourceDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RadarResourceDTO.

        **参数说明**：名称  **取值范围**：长度不小于1，不大于128的汉字、英文字母、数字、下划线（_）和横杠（-）的组合。 

        :param name: The name of this RadarResourceDTO.
        :type name: str
        """
        self._name = name

    @property
    def v2x_edge_id(self):
        """Gets the v2x_edge_id of this RadarResourceDTO.

        **参数说明**：所属的EdgeId  **取值范围**：长度不小于1，不大于128的英文字母、数字、下划线（_）和横杠（-）的组合。 

        :return: The v2x_edge_id of this RadarResourceDTO.
        :rtype: str
        """
        return self._v2x_edge_id

    @v2x_edge_id.setter
    def v2x_edge_id(self, v2x_edge_id):
        """Sets the v2x_edge_id of this RadarResourceDTO.

        **参数说明**：所属的EdgeId  **取值范围**：长度不小于1，不大于128的英文字母、数字、下划线（_）和横杠（-）的组合。 

        :param v2x_edge_id: The v2x_edge_id of this RadarResourceDTO.
        :type v2x_edge_id: str
        """
        self._v2x_edge_id = v2x_edge_id

    @property
    def ip(self):
        """Gets the ip of this RadarResourceDTO.

        **参数说明**：设备IP 

        :return: The ip of this RadarResourceDTO.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this RadarResourceDTO.

        **参数说明**：设备IP 

        :param ip: The ip of this RadarResourceDTO.
        :type ip: str
        """
        self._ip = ip

    @property
    def status(self):
        """Gets the status of this RadarResourceDTO.

        **参数说明**：状态值  **取值范围**：   - ONLINE：在线   - OFFLINE：离线   - UNKNOWN：未知   - SLEEP：睡眠 

        :return: The status of this RadarResourceDTO.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RadarResourceDTO.

        **参数说明**：状态值  **取值范围**：   - ONLINE：在线   - OFFLINE：离线   - UNKNOWN：未知   - SLEEP：睡眠 

        :param status: The status of this RadarResourceDTO.
        :type status: str
        """
        self._status = status

    @property
    def esn(self):
        """Gets the esn of this RadarResourceDTO.

        **参数说明**：设备编号  **取值范围**：长度不小于1，不大于64的英文字母、数字和下划线（_）的组合。 

        :return: The esn of this RadarResourceDTO.
        :rtype: str
        """
        return self._esn

    @esn.setter
    def esn(self, esn):
        """Sets the esn of this RadarResourceDTO.

        **参数说明**：设备编号  **取值范围**：长度不小于1，不大于64的英文字母、数字和下划线（_）的组合。 

        :param esn: The esn of this RadarResourceDTO.
        :type esn: str
        """
        self._esn = esn

    @property
    def position_description(self):
        """Gets the position_description of this RadarResourceDTO.

        **参数说明**：位置描述  **取值范围**：长度不小于1，不大于128的英文字母、数字和下划线（_）的组合。 

        :return: The position_description of this RadarResourceDTO.
        :rtype: str
        """
        return self._position_description

    @position_description.setter
    def position_description(self, position_description):
        """Sets the position_description of this RadarResourceDTO.

        **参数说明**：位置描述  **取值范围**：长度不小于1，不大于128的英文字母、数字和下划线（_）的组合。 

        :param position_description: The position_description of this RadarResourceDTO.
        :type position_description: str
        """
        self._position_description = position_description

    @property
    def created_time(self):
        """Gets the created_time of this RadarResourceDTO.

        **参数说明**：最后修改的时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z' 例如 2020-09-01T01:37:01Z 

        :return: The created_time of this RadarResourceDTO.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this RadarResourceDTO.

        **参数说明**：最后修改的时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z' 例如 2020-09-01T01:37:01Z 

        :param created_time: The created_time of this RadarResourceDTO.
        :type created_time: datetime
        """
        self._created_time = created_time

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this RadarResourceDTO.

        **参数说明**：最后修改时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z' 例如 2020-09-01T01:37:01Z 

        :return: The last_modified_time of this RadarResourceDTO.
        :rtype: datetime
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this RadarResourceDTO.

        **参数说明**：最后修改时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z' 例如 2020-09-01T01:37:01Z 

        :param last_modified_time: The last_modified_time of this RadarResourceDTO.
        :type last_modified_time: datetime
        """
        self._last_modified_time = last_modified_time

    @property
    def last_online_time(self):
        """Gets the last_online_time of this RadarResourceDTO.

        **参数说明**：最后的在线时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z' 例如 2020-09-01T01:37:01Z 

        :return: The last_online_time of this RadarResourceDTO.
        :rtype: datetime
        """
        return self._last_online_time

    @last_online_time.setter
    def last_online_time(self, last_online_time):
        """Sets the last_online_time of this RadarResourceDTO.

        **参数说明**：最后的在线时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z' 例如 2020-09-01T01:37:01Z 

        :param last_online_time: The last_online_time of this RadarResourceDTO.
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
        if not isinstance(other, RadarResourceDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
