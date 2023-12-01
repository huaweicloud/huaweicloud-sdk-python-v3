# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTrafficMirrorSessionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'traffic_mirror_filter_id': 'str',
        'traffic_mirror_target_id': 'str',
        'traffic_mirror_target_type': 'str',
        'virtual_network_id': 'str',
        'packet_length': 'str',
        'priority': 'str',
        'enabled': 'str',
        'type': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'traffic_mirror_filter_id': 'traffic_mirror_filter_id',
        'traffic_mirror_target_id': 'traffic_mirror_target_id',
        'traffic_mirror_target_type': 'traffic_mirror_target_type',
        'virtual_network_id': 'virtual_network_id',
        'packet_length': 'packet_length',
        'priority': 'priority',
        'enabled': 'enabled',
        'type': 'type',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, id=None, name=None, description=None, traffic_mirror_filter_id=None, traffic_mirror_target_id=None, traffic_mirror_target_type=None, virtual_network_id=None, packet_length=None, priority=None, enabled=None, type=None, created_at=None, updated_at=None, limit=None, marker=None):
        """ListTrafficMirrorSessionsRequest

        The model defined in huaweicloud sdk

        :param id: 使用镜像会话ID过滤或排序
        :type id: str
        :param name: 使用镜像会话名称过滤或排序
        :type name: str
        :param description: 使用镜像会话描述过滤
        :type description: str
        :param traffic_mirror_filter_id: 使用筛选条件ID过滤
        :type traffic_mirror_filter_id: str
        :param traffic_mirror_target_id: 使用镜像目的ID过滤
        :type traffic_mirror_target_id: str
        :param traffic_mirror_target_type: 使用镜像目的类型过滤
        :type traffic_mirror_target_type: str
        :param virtual_network_id: 使用VNI过滤
        :type virtual_network_id: str
        :param packet_length: 使用最大传输单元MTU过滤
        :type packet_length: str
        :param priority: 使用镜像会话优先级过滤
        :type priority: str
        :param enabled: 使用enabled过滤
        :type enabled: str
        :param type: 使用镜像源类型过滤
        :type type: str
        :param created_at: 使用创建时间戳排序
        :type created_at: str
        :param updated_at: 使用更新时间戳排序
        :type updated_at: str
        :param limit: 功能说明：每页返回的个数 取值范围：0-2000
        :type limit: int
        :param marker: 分页查询起始的资源ID，为空时查询第一页
        :type marker: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._traffic_mirror_filter_id = None
        self._traffic_mirror_target_id = None
        self._traffic_mirror_target_type = None
        self._virtual_network_id = None
        self._packet_length = None
        self._priority = None
        self._enabled = None
        self._type = None
        self._created_at = None
        self._updated_at = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if traffic_mirror_filter_id is not None:
            self.traffic_mirror_filter_id = traffic_mirror_filter_id
        if traffic_mirror_target_id is not None:
            self.traffic_mirror_target_id = traffic_mirror_target_id
        if traffic_mirror_target_type is not None:
            self.traffic_mirror_target_type = traffic_mirror_target_type
        if virtual_network_id is not None:
            self.virtual_network_id = virtual_network_id
        if packet_length is not None:
            self.packet_length = packet_length
        if priority is not None:
            self.priority = priority
        if enabled is not None:
            self.enabled = enabled
        if type is not None:
            self.type = type
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def id(self):
        """Gets the id of this ListTrafficMirrorSessionsRequest.

        使用镜像会话ID过滤或排序

        :return: The id of this ListTrafficMirrorSessionsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListTrafficMirrorSessionsRequest.

        使用镜像会话ID过滤或排序

        :param id: The id of this ListTrafficMirrorSessionsRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListTrafficMirrorSessionsRequest.

        使用镜像会话名称过滤或排序

        :return: The name of this ListTrafficMirrorSessionsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListTrafficMirrorSessionsRequest.

        使用镜像会话名称过滤或排序

        :param name: The name of this ListTrafficMirrorSessionsRequest.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ListTrafficMirrorSessionsRequest.

        使用镜像会话描述过滤

        :return: The description of this ListTrafficMirrorSessionsRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListTrafficMirrorSessionsRequest.

        使用镜像会话描述过滤

        :param description: The description of this ListTrafficMirrorSessionsRequest.
        :type description: str
        """
        self._description = description

    @property
    def traffic_mirror_filter_id(self):
        """Gets the traffic_mirror_filter_id of this ListTrafficMirrorSessionsRequest.

        使用筛选条件ID过滤

        :return: The traffic_mirror_filter_id of this ListTrafficMirrorSessionsRequest.
        :rtype: str
        """
        return self._traffic_mirror_filter_id

    @traffic_mirror_filter_id.setter
    def traffic_mirror_filter_id(self, traffic_mirror_filter_id):
        """Sets the traffic_mirror_filter_id of this ListTrafficMirrorSessionsRequest.

        使用筛选条件ID过滤

        :param traffic_mirror_filter_id: The traffic_mirror_filter_id of this ListTrafficMirrorSessionsRequest.
        :type traffic_mirror_filter_id: str
        """
        self._traffic_mirror_filter_id = traffic_mirror_filter_id

    @property
    def traffic_mirror_target_id(self):
        """Gets the traffic_mirror_target_id of this ListTrafficMirrorSessionsRequest.

        使用镜像目的ID过滤

        :return: The traffic_mirror_target_id of this ListTrafficMirrorSessionsRequest.
        :rtype: str
        """
        return self._traffic_mirror_target_id

    @traffic_mirror_target_id.setter
    def traffic_mirror_target_id(self, traffic_mirror_target_id):
        """Sets the traffic_mirror_target_id of this ListTrafficMirrorSessionsRequest.

        使用镜像目的ID过滤

        :param traffic_mirror_target_id: The traffic_mirror_target_id of this ListTrafficMirrorSessionsRequest.
        :type traffic_mirror_target_id: str
        """
        self._traffic_mirror_target_id = traffic_mirror_target_id

    @property
    def traffic_mirror_target_type(self):
        """Gets the traffic_mirror_target_type of this ListTrafficMirrorSessionsRequest.

        使用镜像目的类型过滤

        :return: The traffic_mirror_target_type of this ListTrafficMirrorSessionsRequest.
        :rtype: str
        """
        return self._traffic_mirror_target_type

    @traffic_mirror_target_type.setter
    def traffic_mirror_target_type(self, traffic_mirror_target_type):
        """Sets the traffic_mirror_target_type of this ListTrafficMirrorSessionsRequest.

        使用镜像目的类型过滤

        :param traffic_mirror_target_type: The traffic_mirror_target_type of this ListTrafficMirrorSessionsRequest.
        :type traffic_mirror_target_type: str
        """
        self._traffic_mirror_target_type = traffic_mirror_target_type

    @property
    def virtual_network_id(self):
        """Gets the virtual_network_id of this ListTrafficMirrorSessionsRequest.

        使用VNI过滤

        :return: The virtual_network_id of this ListTrafficMirrorSessionsRequest.
        :rtype: str
        """
        return self._virtual_network_id

    @virtual_network_id.setter
    def virtual_network_id(self, virtual_network_id):
        """Sets the virtual_network_id of this ListTrafficMirrorSessionsRequest.

        使用VNI过滤

        :param virtual_network_id: The virtual_network_id of this ListTrafficMirrorSessionsRequest.
        :type virtual_network_id: str
        """
        self._virtual_network_id = virtual_network_id

    @property
    def packet_length(self):
        """Gets the packet_length of this ListTrafficMirrorSessionsRequest.

        使用最大传输单元MTU过滤

        :return: The packet_length of this ListTrafficMirrorSessionsRequest.
        :rtype: str
        """
        return self._packet_length

    @packet_length.setter
    def packet_length(self, packet_length):
        """Sets the packet_length of this ListTrafficMirrorSessionsRequest.

        使用最大传输单元MTU过滤

        :param packet_length: The packet_length of this ListTrafficMirrorSessionsRequest.
        :type packet_length: str
        """
        self._packet_length = packet_length

    @property
    def priority(self):
        """Gets the priority of this ListTrafficMirrorSessionsRequest.

        使用镜像会话优先级过滤

        :return: The priority of this ListTrafficMirrorSessionsRequest.
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this ListTrafficMirrorSessionsRequest.

        使用镜像会话优先级过滤

        :param priority: The priority of this ListTrafficMirrorSessionsRequest.
        :type priority: str
        """
        self._priority = priority

    @property
    def enabled(self):
        """Gets the enabled of this ListTrafficMirrorSessionsRequest.

        使用enabled过滤

        :return: The enabled of this ListTrafficMirrorSessionsRequest.
        :rtype: str
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ListTrafficMirrorSessionsRequest.

        使用enabled过滤

        :param enabled: The enabled of this ListTrafficMirrorSessionsRequest.
        :type enabled: str
        """
        self._enabled = enabled

    @property
    def type(self):
        """Gets the type of this ListTrafficMirrorSessionsRequest.

        使用镜像源类型过滤

        :return: The type of this ListTrafficMirrorSessionsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListTrafficMirrorSessionsRequest.

        使用镜像源类型过滤

        :param type: The type of this ListTrafficMirrorSessionsRequest.
        :type type: str
        """
        self._type = type

    @property
    def created_at(self):
        """Gets the created_at of this ListTrafficMirrorSessionsRequest.

        使用创建时间戳排序

        :return: The created_at of this ListTrafficMirrorSessionsRequest.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ListTrafficMirrorSessionsRequest.

        使用创建时间戳排序

        :param created_at: The created_at of this ListTrafficMirrorSessionsRequest.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ListTrafficMirrorSessionsRequest.

        使用更新时间戳排序

        :return: The updated_at of this ListTrafficMirrorSessionsRequest.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ListTrafficMirrorSessionsRequest.

        使用更新时间戳排序

        :param updated_at: The updated_at of this ListTrafficMirrorSessionsRequest.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def limit(self):
        """Gets the limit of this ListTrafficMirrorSessionsRequest.

        功能说明：每页返回的个数 取值范围：0-2000

        :return: The limit of this ListTrafficMirrorSessionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTrafficMirrorSessionsRequest.

        功能说明：每页返回的个数 取值范围：0-2000

        :param limit: The limit of this ListTrafficMirrorSessionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListTrafficMirrorSessionsRequest.

        分页查询起始的资源ID，为空时查询第一页

        :return: The marker of this ListTrafficMirrorSessionsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListTrafficMirrorSessionsRequest.

        分页查询起始的资源ID，为空时查询第一页

        :param marker: The marker of this ListTrafficMirrorSessionsRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListTrafficMirrorSessionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
