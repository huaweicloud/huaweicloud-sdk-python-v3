# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTasksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'id': 'str',
        'instance_id': 'str',
        'order_id': 'str',
        'name': 'str',
        'status': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'id': 'id',
        'instance_id': 'instance_id',
        'order_id': 'order_id',
        'name': 'name',
        'status': 'status',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, offset=None, limit=None, id=None, instance_id=None, order_id=None, name=None, status=None, start_time=None, end_time=None):
        r"""ListTasksRequest

        The model defined in huaweicloud sdk

        :param offset: 索引位置，偏移量。  从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询记录数。默认为10，不能为负数，最小值为1，最大值为50。
        :type limit: int
        :param id: 任务ID，按任务ID过滤。
        :type id: str
        :param instance_id: 实例ID，按实例ID过滤。
        :type instance_id: str
        :param order_id: 订单ID，按订单ID过滤。
        :type order_id: str
        :param name: 任务名称，按任务名称称过滤。
        :type name: str
        :param status: 任务状态，按任务状态过滤。 Running:运行中 Completed:已完成 Failed:已失败
        :type status: str
        :param start_time: 任务的创建时间，按时间范围进行过滤，“start_time”有值时，“end_time”必选。格式为UTC时间戳。
        :type start_time: str
        :param end_time: 任务的结束时间，按时间范围进行过滤，“start_time”有值时，“end_time”必选。格式为UTC时间戳。
        :type end_time: str
        """
        
        

        self._offset = None
        self._limit = None
        self._id = None
        self._instance_id = None
        self._order_id = None
        self._name = None
        self._status = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if id is not None:
            self.id = id
        if instance_id is not None:
            self.instance_id = instance_id
        if order_id is not None:
            self.order_id = order_id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def offset(self):
        r"""Gets the offset of this ListTasksRequest.

        索引位置，偏移量。  从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ListTasksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTasksRequest.

        索引位置，偏移量。  从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ListTasksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListTasksRequest.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为50。

        :return: The limit of this ListTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTasksRequest.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为50。

        :param limit: The limit of this ListTasksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def id(self):
        r"""Gets the id of this ListTasksRequest.

        任务ID，按任务ID过滤。

        :return: The id of this ListTasksRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListTasksRequest.

        任务ID，按任务ID过滤。

        :param id: The id of this ListTasksRequest.
        :type id: str
        """
        self._id = id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListTasksRequest.

        实例ID，按实例ID过滤。

        :return: The instance_id of this ListTasksRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListTasksRequest.

        实例ID，按实例ID过滤。

        :param instance_id: The instance_id of this ListTasksRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def order_id(self):
        r"""Gets the order_id of this ListTasksRequest.

        订单ID，按订单ID过滤。

        :return: The order_id of this ListTasksRequest.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this ListTasksRequest.

        订单ID，按订单ID过滤。

        :param order_id: The order_id of this ListTasksRequest.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def name(self):
        r"""Gets the name of this ListTasksRequest.

        任务名称，按任务名称称过滤。

        :return: The name of this ListTasksRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListTasksRequest.

        任务名称，按任务名称称过滤。

        :param name: The name of this ListTasksRequest.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ListTasksRequest.

        任务状态，按任务状态过滤。 Running:运行中 Completed:已完成 Failed:已失败

        :return: The status of this ListTasksRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListTasksRequest.

        任务状态，按任务状态过滤。 Running:运行中 Completed:已完成 Failed:已失败

        :param status: The status of this ListTasksRequest.
        :type status: str
        """
        self._status = status

    @property
    def start_time(self):
        r"""Gets the start_time of this ListTasksRequest.

        任务的创建时间，按时间范围进行过滤，“start_time”有值时，“end_time”必选。格式为UTC时间戳。

        :return: The start_time of this ListTasksRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListTasksRequest.

        任务的创建时间，按时间范围进行过滤，“start_time”有值时，“end_time”必选。格式为UTC时间戳。

        :param start_time: The start_time of this ListTasksRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListTasksRequest.

        任务的结束时间，按时间范围进行过滤，“start_time”有值时，“end_time”必选。格式为UTC时间戳。

        :return: The end_time of this ListTasksRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListTasksRequest.

        任务的结束时间，按时间范围进行过滤，“start_time”有值时，“end_time”必选。格式为UTC时间戳。

        :param end_time: The end_time of this ListTasksRequest.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ListTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
