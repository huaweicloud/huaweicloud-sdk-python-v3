# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowErrorLogRequest:

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
        'start_time': 'str',
        'end_time': 'str',
        'node_id': 'str',
        'type': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'node_id': 'node_id',
        'type': 'type',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, start_time=None, end_time=None, node_id=None, type=None, offset=None, limit=None):
        """ShowErrorLogRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，可以调用“查询实例列表”接口获取。如果未申请实例，可以调用“创建实例”接口创建。
        :type instance_id: str
        :param start_time: 开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始，Z指时区偏移量，例如北京时间偏移显示为+0800。开始时间不得早于当前时间31天。
        :type start_time: str
        :param end_time: 结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 只能查询当前时间前一个月内的错误日志。结束时间不能晚于当前时间。
        :type end_time: str
        :param node_id: 节点ID，取空值，表示查询实例下所有允许查询的节点。
        :type node_id: str
        :param type: 语句类型，取空值，表示查询所有语句类型，也可指定如下日志类型： - Warning - Error
        :type type: str
        :param offset: 索引位置，偏移量。取值范围为 [0, 1999]。 从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询） - 必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询记录数。取值范围[1, 100]，默认10 （表示默认返回10条数据）。 - limit 与 offset的和需要满足小于等于2000的条件。
        :type limit: int
        """
        
        

        self._instance_id = None
        self._start_time = None
        self._end_time = None
        self._node_id = None
        self._type = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        self.start_time = start_time
        self.end_time = end_time
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
        """Gets the instance_id of this ShowErrorLogRequest.

        实例ID，可以调用“查询实例列表”接口获取。如果未申请实例，可以调用“创建实例”接口创建。

        :return: The instance_id of this ShowErrorLogRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowErrorLogRequest.

        实例ID，可以调用“查询实例列表”接口获取。如果未申请实例，可以调用“创建实例”接口创建。

        :param instance_id: The instance_id of this ShowErrorLogRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def start_time(self):
        """Gets the start_time of this ShowErrorLogRequest.

        开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始，Z指时区偏移量，例如北京时间偏移显示为+0800。开始时间不得早于当前时间31天。

        :return: The start_time of this ShowErrorLogRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowErrorLogRequest.

        开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始，Z指时区偏移量，例如北京时间偏移显示为+0800。开始时间不得早于当前时间31天。

        :param start_time: The start_time of this ShowErrorLogRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowErrorLogRequest.

        结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 只能查询当前时间前一个月内的错误日志。结束时间不能晚于当前时间。

        :return: The end_time of this ShowErrorLogRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowErrorLogRequest.

        结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 只能查询当前时间前一个月内的错误日志。结束时间不能晚于当前时间。

        :param end_time: The end_time of this ShowErrorLogRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def node_id(self):
        """Gets the node_id of this ShowErrorLogRequest.

        节点ID，取空值，表示查询实例下所有允许查询的节点。

        :return: The node_id of this ShowErrorLogRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this ShowErrorLogRequest.

        节点ID，取空值，表示查询实例下所有允许查询的节点。

        :param node_id: The node_id of this ShowErrorLogRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def type(self):
        """Gets the type of this ShowErrorLogRequest.

        语句类型，取空值，表示查询所有语句类型，也可指定如下日志类型： - Warning - Error

        :return: The type of this ShowErrorLogRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowErrorLogRequest.

        语句类型，取空值，表示查询所有语句类型，也可指定如下日志类型： - Warning - Error

        :param type: The type of this ShowErrorLogRequest.
        :type type: str
        """
        self._type = type

    @property
    def offset(self):
        """Gets the offset of this ShowErrorLogRequest.

        索引位置，偏移量。取值范围为 [0, 1999]。 从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询） - 必须为数字，不能为负数。

        :return: The offset of this ShowErrorLogRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowErrorLogRequest.

        索引位置，偏移量。取值范围为 [0, 1999]。 从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询） - 必须为数字，不能为负数。

        :param offset: The offset of this ShowErrorLogRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowErrorLogRequest.

        查询记录数。取值范围[1, 100]，默认10 （表示默认返回10条数据）。 - limit 与 offset的和需要满足小于等于2000的条件。

        :return: The limit of this ShowErrorLogRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowErrorLogRequest.

        查询记录数。取值范围[1, 100]，默认10 （表示默认返回10条数据）。 - limit 与 offset的和需要满足小于等于2000的条件。

        :param limit: The limit of this ShowErrorLogRequest.
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
        if not isinstance(other, ShowErrorLogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
