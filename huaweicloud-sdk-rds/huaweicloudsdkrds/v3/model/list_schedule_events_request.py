# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScheduleEventsRequest:

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
        'instance_id': 'str',
        'status': 'str',
        'type': 'str',
        'level': 'str',
        'sort_field': 'str',
        'order': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'id': 'id',
        'instance_id': 'instance_id',
        'status': 'status',
        'type': 'type',
        'level': 'level',
        'sort_field': 'sort_field',
        'order': 'order',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, id=None, instance_id=None, status=None, type=None, level=None, sort_field=None, order=None, offset=None, limit=None):
        r"""ListScheduleEventsRequest

        The model defined in huaweicloud sdk

        :param id: **参数解释**：  事件ID。  **约束限制**：  不涉及。
        :type id: str
        :param instance_id: **参数解释**：  实例ID。  **约束限制**：  不涉及。
        :type instance_id: str
        :param status: **参数解释**：  事件状态  **约束限制**：  不涉及。  **取值范围**：  枚举值：WAITING 等待中；INQUIRING 待授权; SCHEDULED 待执行; EXECUTING 执行中; COMPLETED 已完成; FAILED 失败; CANCELED 已取消。
        :type status: str
        :param type: **参数解释**：  事件类型  **约束限制**：  不涉及。  **取值范围**：  枚举值：RESTAT_NODE 重启实例节点。
        :type type: str
        :param level: **参数解释**：  事件级别  **约束限制**：  不涉及。  **取值范围**：  CRITICAL 紧急；MAJOR 重要；MINOR 一般；INFO 提示。
        :type level: str
        :param sort_field: **参数解释**：  排序字段，支持planned_execution_time、created_time、latest_execution_time。  **约束限制**：  不涉及。
        :type sort_field: str
        :param order: **参数解释**：  排序顺序  **约束限制**：  不涉及。  **取值范围**：  DESC 降序；ASC升序   **默认取值**：  DESC 降序
        :type order: str
        :param offset: **参数解释**：  索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。  **约束限制**：  不涉及。  **取值范围**：  不涉及  **默认取值**：  0
        :type offset: int
        :param limit: **参数解释**：  查询记录数。默认为10，不能为负数，最小值为1，最大值为100。  **约束限制**：  不涉及。  **取值范围**：  不涉及  **默认取值**：  10
        :type limit: int
        """
        
        

        self._id = None
        self._instance_id = None
        self._status = None
        self._type = None
        self._level = None
        self._sort_field = None
        self._order = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if instance_id is not None:
            self.instance_id = instance_id
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if level is not None:
            self.level = level
        if sort_field is not None:
            self.sort_field = sort_field
        if order is not None:
            self.order = order
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def id(self):
        r"""Gets the id of this ListScheduleEventsRequest.

        **参数解释**：  事件ID。  **约束限制**：  不涉及。

        :return: The id of this ListScheduleEventsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListScheduleEventsRequest.

        **参数解释**：  事件ID。  **约束限制**：  不涉及。

        :param id: The id of this ListScheduleEventsRequest.
        :type id: str
        """
        self._id = id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListScheduleEventsRequest.

        **参数解释**：  实例ID。  **约束限制**：  不涉及。

        :return: The instance_id of this ListScheduleEventsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListScheduleEventsRequest.

        **参数解释**：  实例ID。  **约束限制**：  不涉及。

        :param instance_id: The instance_id of this ListScheduleEventsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def status(self):
        r"""Gets the status of this ListScheduleEventsRequest.

        **参数解释**：  事件状态  **约束限制**：  不涉及。  **取值范围**：  枚举值：WAITING 等待中；INQUIRING 待授权; SCHEDULED 待执行; EXECUTING 执行中; COMPLETED 已完成; FAILED 失败; CANCELED 已取消。

        :return: The status of this ListScheduleEventsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListScheduleEventsRequest.

        **参数解释**：  事件状态  **约束限制**：  不涉及。  **取值范围**：  枚举值：WAITING 等待中；INQUIRING 待授权; SCHEDULED 待执行; EXECUTING 执行中; COMPLETED 已完成; FAILED 失败; CANCELED 已取消。

        :param status: The status of this ListScheduleEventsRequest.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this ListScheduleEventsRequest.

        **参数解释**：  事件类型  **约束限制**：  不涉及。  **取值范围**：  枚举值：RESTAT_NODE 重启实例节点。

        :return: The type of this ListScheduleEventsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListScheduleEventsRequest.

        **参数解释**：  事件类型  **约束限制**：  不涉及。  **取值范围**：  枚举值：RESTAT_NODE 重启实例节点。

        :param type: The type of this ListScheduleEventsRequest.
        :type type: str
        """
        self._type = type

    @property
    def level(self):
        r"""Gets the level of this ListScheduleEventsRequest.

        **参数解释**：  事件级别  **约束限制**：  不涉及。  **取值范围**：  CRITICAL 紧急；MAJOR 重要；MINOR 一般；INFO 提示。

        :return: The level of this ListScheduleEventsRequest.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this ListScheduleEventsRequest.

        **参数解释**：  事件级别  **约束限制**：  不涉及。  **取值范围**：  CRITICAL 紧急；MAJOR 重要；MINOR 一般；INFO 提示。

        :param level: The level of this ListScheduleEventsRequest.
        :type level: str
        """
        self._level = level

    @property
    def sort_field(self):
        r"""Gets the sort_field of this ListScheduleEventsRequest.

        **参数解释**：  排序字段，支持planned_execution_time、created_time、latest_execution_time。  **约束限制**：  不涉及。

        :return: The sort_field of this ListScheduleEventsRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this ListScheduleEventsRequest.

        **参数解释**：  排序字段，支持planned_execution_time、created_time、latest_execution_time。  **约束限制**：  不涉及。

        :param sort_field: The sort_field of this ListScheduleEventsRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def order(self):
        r"""Gets the order of this ListScheduleEventsRequest.

        **参数解释**：  排序顺序  **约束限制**：  不涉及。  **取值范围**：  DESC 降序；ASC升序   **默认取值**：  DESC 降序

        :return: The order of this ListScheduleEventsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListScheduleEventsRequest.

        **参数解释**：  排序顺序  **约束限制**：  不涉及。  **取值范围**：  DESC 降序；ASC升序   **默认取值**：  DESC 降序

        :param order: The order of this ListScheduleEventsRequest.
        :type order: str
        """
        self._order = order

    @property
    def offset(self):
        r"""Gets the offset of this ListScheduleEventsRequest.

        **参数解释**：  索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。  **约束限制**：  不涉及。  **取值范围**：  不涉及  **默认取值**：  0

        :return: The offset of this ListScheduleEventsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListScheduleEventsRequest.

        **参数解释**：  索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。  **约束限制**：  不涉及。  **取值范围**：  不涉及  **默认取值**：  0

        :param offset: The offset of this ListScheduleEventsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListScheduleEventsRequest.

        **参数解释**：  查询记录数。默认为10，不能为负数，最小值为1，最大值为100。  **约束限制**：  不涉及。  **取值范围**：  不涉及  **默认取值**：  10

        :return: The limit of this ListScheduleEventsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListScheduleEventsRequest.

        **参数解释**：  查询记录数。默认为10，不能为负数，最小值为1，最大值为100。  **约束限制**：  不涉及。  **取值范围**：  不涉及  **默认取值**：  10

        :param limit: The limit of this ListScheduleEventsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListScheduleEventsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
