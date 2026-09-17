# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOperationalTaskDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'category': 'str',
        'task_id': 'str',
        'status': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'category': 'category',
        'task_id': 'task_id',
        'status': 'status',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, cluster_id=None, category=None, task_id=None, status=None, start_time=None, end_time=None, limit=None, offset=None):
        r"""ListOperationalTaskDetailRequest

        The model defined in huaweicloud sdk

        :param cluster_id: **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type cluster_id: str
        :param category: **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： VacuumFull **默认取值**： VacuumFull
        :type category: str
        :param task_id: **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type task_id: str
        :param status: **参数解释**： 状态。 **约束限制**： 不涉及。 **取值范围**： running、waiting、finished、canceled **默认取值**： 不涉及。
        :type status: str
        :param start_time: **参数解释**： 开始日期。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type start_time: str
        :param end_time: **参数解释**： 结束日期。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type end_time: str
        :param limit: **参数解释**： 分页查询，每页大小。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 100
        :type limit: int
        :param offset: **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0 **默认取值**： 0
        :type offset: int
        """
        
        

        self._cluster_id = None
        self._category = None
        self._task_id = None
        self._status = None
        self._start_time = None
        self._end_time = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if category is not None:
            self.category = category
        if task_id is not None:
            self.task_id = task_id
        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListOperationalTaskDetailRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The cluster_id of this ListOperationalTaskDetailRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListOperationalTaskDetailRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param cluster_id: The cluster_id of this ListOperationalTaskDetailRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def category(self):
        r"""Gets the category of this ListOperationalTaskDetailRequest.

        **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： VacuumFull **默认取值**： VacuumFull

        :return: The category of this ListOperationalTaskDetailRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListOperationalTaskDetailRequest.

        **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： VacuumFull **默认取值**： VacuumFull

        :param category: The category of this ListOperationalTaskDetailRequest.
        :type category: str
        """
        self._category = category

    @property
    def task_id(self):
        r"""Gets the task_id of this ListOperationalTaskDetailRequest.

        **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The task_id of this ListOperationalTaskDetailRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ListOperationalTaskDetailRequest.

        **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param task_id: The task_id of this ListOperationalTaskDetailRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def status(self):
        r"""Gets the status of this ListOperationalTaskDetailRequest.

        **参数解释**： 状态。 **约束限制**： 不涉及。 **取值范围**： running、waiting、finished、canceled **默认取值**： 不涉及。

        :return: The status of this ListOperationalTaskDetailRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListOperationalTaskDetailRequest.

        **参数解释**： 状态。 **约束限制**： 不涉及。 **取值范围**： running、waiting、finished、canceled **默认取值**： 不涉及。

        :param status: The status of this ListOperationalTaskDetailRequest.
        :type status: str
        """
        self._status = status

    @property
    def start_time(self):
        r"""Gets the start_time of this ListOperationalTaskDetailRequest.

        **参数解释**： 开始日期。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The start_time of this ListOperationalTaskDetailRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListOperationalTaskDetailRequest.

        **参数解释**： 开始日期。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param start_time: The start_time of this ListOperationalTaskDetailRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListOperationalTaskDetailRequest.

        **参数解释**： 结束日期。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The end_time of this ListOperationalTaskDetailRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListOperationalTaskDetailRequest.

        **参数解释**： 结束日期。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param end_time: The end_time of this ListOperationalTaskDetailRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def limit(self):
        r"""Gets the limit of this ListOperationalTaskDetailRequest.

        **参数解释**： 分页查询，每页大小。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 100

        :return: The limit of this ListOperationalTaskDetailRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListOperationalTaskDetailRequest.

        **参数解释**： 分页查询，每页大小。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 100

        :param limit: The limit of this ListOperationalTaskDetailRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListOperationalTaskDetailRequest.

        **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0 **默认取值**： 0

        :return: The offset of this ListOperationalTaskDetailRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListOperationalTaskDetailRequest.

        **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0 **默认取值**： 0

        :param offset: The offset of this ListOperationalTaskDetailRequest.
        :type offset: int
        """
        self._offset = offset

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListOperationalTaskDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
