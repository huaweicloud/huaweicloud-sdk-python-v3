# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTrafficMirrorFilterRulesRequest:

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
        'description': 'str',
        'traffic_mirror_filter_id': 'str',
        'direction': 'str',
        'protocol': 'str',
        'source_cidr_block': 'str',
        'destination_cidr_block': 'str',
        'source_port_range': 'str',
        'destination_port_range': 'str',
        'action': 'str',
        'priority': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'traffic_mirror_filter_id': 'traffic_mirror_filter_id',
        'direction': 'direction',
        'protocol': 'protocol',
        'source_cidr_block': 'source_cidr_block',
        'destination_cidr_block': 'destination_cidr_block',
        'source_port_range': 'source_port_range',
        'destination_port_range': 'destination_port_range',
        'action': 'action',
        'priority': 'priority',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, id=None, description=None, traffic_mirror_filter_id=None, direction=None, protocol=None, source_cidr_block=None, destination_cidr_block=None, source_port_range=None, destination_port_range=None, action=None, priority=None, limit=None, marker=None):
        """ListTrafficMirrorFilterRulesRequest

        The model defined in huaweicloud sdk

        :param id: 使用规则ID过滤或排序
        :type id: str
        :param description: 使用规则描述过滤
        :type description: str
        :param traffic_mirror_filter_id: 使用筛选条件ID过滤
        :type traffic_mirror_filter_id: str
        :param direction: 使用规则方向过滤
        :type direction: str
        :param protocol: 使用规则协议过滤
        :type protocol: str
        :param source_cidr_block: 使用规则源网段过滤
        :type source_cidr_block: str
        :param destination_cidr_block: 使用规则目的网段过滤
        :type destination_cidr_block: str
        :param source_port_range: 使用规则源端口范围过滤
        :type source_port_range: str
        :param destination_port_range: 使用规则目的端口范围过滤
        :type destination_port_range: str
        :param action: 使用规则action过滤
        :type action: str
        :param priority: 使用规则优先级过滤
        :type priority: str
        :param limit: 功能说明：每页返回的个数 取值范围：0-2000
        :type limit: int
        :param marker: 分页查询起始的资源ID，为空时查询第一页
        :type marker: str
        """
        
        

        self._id = None
        self._description = None
        self._traffic_mirror_filter_id = None
        self._direction = None
        self._protocol = None
        self._source_cidr_block = None
        self._destination_cidr_block = None
        self._source_port_range = None
        self._destination_port_range = None
        self._action = None
        self._priority = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        if traffic_mirror_filter_id is not None:
            self.traffic_mirror_filter_id = traffic_mirror_filter_id
        if direction is not None:
            self.direction = direction
        if protocol is not None:
            self.protocol = protocol
        if source_cidr_block is not None:
            self.source_cidr_block = source_cidr_block
        if destination_cidr_block is not None:
            self.destination_cidr_block = destination_cidr_block
        if source_port_range is not None:
            self.source_port_range = source_port_range
        if destination_port_range is not None:
            self.destination_port_range = destination_port_range
        if action is not None:
            self.action = action
        if priority is not None:
            self.priority = priority
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def id(self):
        """Gets the id of this ListTrafficMirrorFilterRulesRequest.

        使用规则ID过滤或排序

        :return: The id of this ListTrafficMirrorFilterRulesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListTrafficMirrorFilterRulesRequest.

        使用规则ID过滤或排序

        :param id: The id of this ListTrafficMirrorFilterRulesRequest.
        :type id: str
        """
        self._id = id

    @property
    def description(self):
        """Gets the description of this ListTrafficMirrorFilterRulesRequest.

        使用规则描述过滤

        :return: The description of this ListTrafficMirrorFilterRulesRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListTrafficMirrorFilterRulesRequest.

        使用规则描述过滤

        :param description: The description of this ListTrafficMirrorFilterRulesRequest.
        :type description: str
        """
        self._description = description

    @property
    def traffic_mirror_filter_id(self):
        """Gets the traffic_mirror_filter_id of this ListTrafficMirrorFilterRulesRequest.

        使用筛选条件ID过滤

        :return: The traffic_mirror_filter_id of this ListTrafficMirrorFilterRulesRequest.
        :rtype: str
        """
        return self._traffic_mirror_filter_id

    @traffic_mirror_filter_id.setter
    def traffic_mirror_filter_id(self, traffic_mirror_filter_id):
        """Sets the traffic_mirror_filter_id of this ListTrafficMirrorFilterRulesRequest.

        使用筛选条件ID过滤

        :param traffic_mirror_filter_id: The traffic_mirror_filter_id of this ListTrafficMirrorFilterRulesRequest.
        :type traffic_mirror_filter_id: str
        """
        self._traffic_mirror_filter_id = traffic_mirror_filter_id

    @property
    def direction(self):
        """Gets the direction of this ListTrafficMirrorFilterRulesRequest.

        使用规则方向过滤

        :return: The direction of this ListTrafficMirrorFilterRulesRequest.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this ListTrafficMirrorFilterRulesRequest.

        使用规则方向过滤

        :param direction: The direction of this ListTrafficMirrorFilterRulesRequest.
        :type direction: str
        """
        self._direction = direction

    @property
    def protocol(self):
        """Gets the protocol of this ListTrafficMirrorFilterRulesRequest.

        使用规则协议过滤

        :return: The protocol of this ListTrafficMirrorFilterRulesRequest.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ListTrafficMirrorFilterRulesRequest.

        使用规则协议过滤

        :param protocol: The protocol of this ListTrafficMirrorFilterRulesRequest.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def source_cidr_block(self):
        """Gets the source_cidr_block of this ListTrafficMirrorFilterRulesRequest.

        使用规则源网段过滤

        :return: The source_cidr_block of this ListTrafficMirrorFilterRulesRequest.
        :rtype: str
        """
        return self._source_cidr_block

    @source_cidr_block.setter
    def source_cidr_block(self, source_cidr_block):
        """Sets the source_cidr_block of this ListTrafficMirrorFilterRulesRequest.

        使用规则源网段过滤

        :param source_cidr_block: The source_cidr_block of this ListTrafficMirrorFilterRulesRequest.
        :type source_cidr_block: str
        """
        self._source_cidr_block = source_cidr_block

    @property
    def destination_cidr_block(self):
        """Gets the destination_cidr_block of this ListTrafficMirrorFilterRulesRequest.

        使用规则目的网段过滤

        :return: The destination_cidr_block of this ListTrafficMirrorFilterRulesRequest.
        :rtype: str
        """
        return self._destination_cidr_block

    @destination_cidr_block.setter
    def destination_cidr_block(self, destination_cidr_block):
        """Sets the destination_cidr_block of this ListTrafficMirrorFilterRulesRequest.

        使用规则目的网段过滤

        :param destination_cidr_block: The destination_cidr_block of this ListTrafficMirrorFilterRulesRequest.
        :type destination_cidr_block: str
        """
        self._destination_cidr_block = destination_cidr_block

    @property
    def source_port_range(self):
        """Gets the source_port_range of this ListTrafficMirrorFilterRulesRequest.

        使用规则源端口范围过滤

        :return: The source_port_range of this ListTrafficMirrorFilterRulesRequest.
        :rtype: str
        """
        return self._source_port_range

    @source_port_range.setter
    def source_port_range(self, source_port_range):
        """Sets the source_port_range of this ListTrafficMirrorFilterRulesRequest.

        使用规则源端口范围过滤

        :param source_port_range: The source_port_range of this ListTrafficMirrorFilterRulesRequest.
        :type source_port_range: str
        """
        self._source_port_range = source_port_range

    @property
    def destination_port_range(self):
        """Gets the destination_port_range of this ListTrafficMirrorFilterRulesRequest.

        使用规则目的端口范围过滤

        :return: The destination_port_range of this ListTrafficMirrorFilterRulesRequest.
        :rtype: str
        """
        return self._destination_port_range

    @destination_port_range.setter
    def destination_port_range(self, destination_port_range):
        """Sets the destination_port_range of this ListTrafficMirrorFilterRulesRequest.

        使用规则目的端口范围过滤

        :param destination_port_range: The destination_port_range of this ListTrafficMirrorFilterRulesRequest.
        :type destination_port_range: str
        """
        self._destination_port_range = destination_port_range

    @property
    def action(self):
        """Gets the action of this ListTrafficMirrorFilterRulesRequest.

        使用规则action过滤

        :return: The action of this ListTrafficMirrorFilterRulesRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ListTrafficMirrorFilterRulesRequest.

        使用规则action过滤

        :param action: The action of this ListTrafficMirrorFilterRulesRequest.
        :type action: str
        """
        self._action = action

    @property
    def priority(self):
        """Gets the priority of this ListTrafficMirrorFilterRulesRequest.

        使用规则优先级过滤

        :return: The priority of this ListTrafficMirrorFilterRulesRequest.
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this ListTrafficMirrorFilterRulesRequest.

        使用规则优先级过滤

        :param priority: The priority of this ListTrafficMirrorFilterRulesRequest.
        :type priority: str
        """
        self._priority = priority

    @property
    def limit(self):
        """Gets the limit of this ListTrafficMirrorFilterRulesRequest.

        功能说明：每页返回的个数 取值范围：0-2000

        :return: The limit of this ListTrafficMirrorFilterRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTrafficMirrorFilterRulesRequest.

        功能说明：每页返回的个数 取值范围：0-2000

        :param limit: The limit of this ListTrafficMirrorFilterRulesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListTrafficMirrorFilterRulesRequest.

        分页查询起始的资源ID，为空时查询第一页

        :return: The marker of this ListTrafficMirrorFilterRulesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListTrafficMirrorFilterRulesRequest.

        分页查询起始的资源ID，为空时查询第一页

        :param marker: The marker of this ListTrafficMirrorFilterRulesRequest.
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
        if not isinstance(other, ListTrafficMirrorFilterRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
