# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSlowLogsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'start_date': 'str',
        'end_date': 'str',
        'node_id': 'str',
        'type': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'node_id': 'node_id',
        'type': 'type',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, start_date=None, end_date=None, node_id=None, type=None, offset=None, limit=None):
        r"""ListSlowLogsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。
        :type instance_id: str
        :param start_date: 开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type start_date: str
        :param end_date: 结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。只能查询当前时间前一个月内的慢日志。注：结束时间不能晚于当前时间。
        :type end_date: str
        :param node_id: 节点ID，取空值，表示查询实例下所有允许查询的节点。 使用请参考《DDS API参考》的“查询实例列表和详情”响应消息表“nodes 数据结构说明”的“id”。允许查询的节点如下： - 集群实例下面的 shard节点 - 副本集、单节点实例下面的所有节点
        :type node_id: str
        :param type: 语句类型，取空值，表示查询所有语句类型，也可指定如下日志类型： - INSERT - QUERY - UPDATE - REMOVE - GETMORE - COMMAND - KILLCURSORS
        :type type: str
        :param offset: 索引位置，偏移量。取值范围为 [0, 1999]。 从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询记录数。取值范围[1, 100]，默认10 （表示默认返回10条数据）。 注意： limit 与 offset 的和需要满足 &lt;&#x3D; 2000的条件。
        :type limit: int
        """
        
        

        self._instance_id = None
        self._start_date = None
        self._end_date = None
        self._node_id = None
        self._type = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        self.start_date = start_date
        self.end_date = end_date
        if node_id is not None:
            self.node_id = node_id
        if type is not None:
            self.type = type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListSlowLogsRequest.

        实例ID，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。

        :return: The instance_id of this ListSlowLogsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListSlowLogsRequest.

        实例ID，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。

        :param instance_id: The instance_id of this ListSlowLogsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def start_date(self):
        r"""Gets the start_date of this ListSlowLogsRequest.

        开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The start_date of this ListSlowLogsRequest.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        r"""Sets the start_date of this ListSlowLogsRequest.

        开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param start_date: The start_date of this ListSlowLogsRequest.
        :type start_date: str
        """
        self._start_date = start_date

    @property
    def end_date(self):
        r"""Gets the end_date of this ListSlowLogsRequest.

        结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。只能查询当前时间前一个月内的慢日志。注：结束时间不能晚于当前时间。

        :return: The end_date of this ListSlowLogsRequest.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        r"""Sets the end_date of this ListSlowLogsRequest.

        结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。只能查询当前时间前一个月内的慢日志。注：结束时间不能晚于当前时间。

        :param end_date: The end_date of this ListSlowLogsRequest.
        :type end_date: str
        """
        self._end_date = end_date

    @property
    def node_id(self):
        r"""Gets the node_id of this ListSlowLogsRequest.

        节点ID，取空值，表示查询实例下所有允许查询的节点。 使用请参考《DDS API参考》的“查询实例列表和详情”响应消息表“nodes 数据结构说明”的“id”。允许查询的节点如下： - 集群实例下面的 shard节点 - 副本集、单节点实例下面的所有节点

        :return: The node_id of this ListSlowLogsRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ListSlowLogsRequest.

        节点ID，取空值，表示查询实例下所有允许查询的节点。 使用请参考《DDS API参考》的“查询实例列表和详情”响应消息表“nodes 数据结构说明”的“id”。允许查询的节点如下： - 集群实例下面的 shard节点 - 副本集、单节点实例下面的所有节点

        :param node_id: The node_id of this ListSlowLogsRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def type(self):
        r"""Gets the type of this ListSlowLogsRequest.

        语句类型，取空值，表示查询所有语句类型，也可指定如下日志类型： - INSERT - QUERY - UPDATE - REMOVE - GETMORE - COMMAND - KILLCURSORS

        :return: The type of this ListSlowLogsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListSlowLogsRequest.

        语句类型，取空值，表示查询所有语句类型，也可指定如下日志类型： - INSERT - QUERY - UPDATE - REMOVE - GETMORE - COMMAND - KILLCURSORS

        :param type: The type of this ListSlowLogsRequest.
        :type type: str
        """
        self._type = type

    @property
    def offset(self):
        r"""Gets the offset of this ListSlowLogsRequest.

        索引位置，偏移量。取值范围为 [0, 1999]。 从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ListSlowLogsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSlowLogsRequest.

        索引位置，偏移量。取值范围为 [0, 1999]。 从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ListSlowLogsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSlowLogsRequest.

        查询记录数。取值范围[1, 100]，默认10 （表示默认返回10条数据）。 注意： limit 与 offset 的和需要满足 <= 2000的条件。

        :return: The limit of this ListSlowLogsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSlowLogsRequest.

        查询记录数。取值范围[1, 100]，默认10 （表示默认返回10条数据）。 注意： limit 与 offset 的和需要满足 <= 2000的条件。

        :param limit: The limit of this ListSlowLogsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListSlowLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
