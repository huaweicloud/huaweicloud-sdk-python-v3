# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceScheduleEventsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'id': 'str',
        'instance_id': 'str',
        'status': 'str',
        'type': 'str',
        'level': 'str',
        'sort_field': 'str',
        'order': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'id': 'id',
        'instance_id': 'instance_id',
        'status': 'status',
        'type': 'type',
        'level': 'level',
        'sort_field': 'sort_field',
        'order': 'order',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, x_language=None, id=None, instance_id=None, status=None, type=None, level=None, sort_field=None, order=None, limit=None, offset=None):
        r"""ShowInstanceScheduleEventsRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释**：              请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us：英文。 - zh-cn：中文。  **默认取值**：  en-us。
        :type x_language: str
        :param id: **参数解释**：  事件ID。  您可以登录管理控制台，在事件管理列表中查看事件ID。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，前面为UUID，后缀为ev07，长度为36个字符。  **默认取值**：  不涉及。
        :type id: str
        :param instance_id: **参数解释**：  实例ID，此参数是实例的唯一标识。  获取方法请参见[查询实例列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlInstancesUnifyStatus.html)。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。  **默认取值**：  不涉及。
        :type instance_id: str
        :param status: **参数解释**：  事件状态。  **约束限制**：  不涉及。  **取值范围**：  - inquiring：待授权。 - scheduled：待执行。 - executing：执行中。 - completed：执行完成。 - canceled：事件关闭。 - failed：执行失败。  **默认取值**：  不涉及。
        :type status: str
        :param type: **参数解释**：  事件类型。  **约束限制**：  不涉及。  **取值范围**：  - system.lifecycle.rebuild_node：备机重建事件。 - system.lifecycle.db_upgrade：数据库内核小版本升级事件。 - system.scheduled_event.high_cpu_memory：实例CPU或内存高负载事件，需要变更实例规格。  **默认取值**：  不涉及。
        :type type: str
        :param level: **参数解释**：  事件级别。  **约束限制**：  不涉及。  **取值范围**：  - critical：紧急。 - major：重要。 - minor：一般。 - info：提示。  **默认取值**：  不涉及。
        :type level: str
        :param sort_field: **参数解释**：  响应列表排序字段。  **约束限制**：  不涉及。  **取值范围**：  - created_time：创建时间。 - updated_time：更新时间。 - execution_time_window：执行时间窗。 - execute_time： 执行时间。  **默认取值**：  不涉及。
        :type sort_field: str
        :param order: **参数解释**：  响应列表根据sort_field字段的排序方式（升序/降序）。  **约束限制**：  sort_field不为空时生效。  **取值范围**：  - asc：升序排列。 - desc：降序排列。  **默认取值**：  不涉及。
        :type order: str
        :param limit: **参数解释**：              查询记录数。  **约束限制**：  必须为整数，不能为负数。  **取值范围**：  1-100。  **默认取值**：  10。
        :type limit: int
        :param offset: **参数解释**：              索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。  **约束限制**：  必须为整数，不能为负数。  **取值范围**：  ≥0  **默认取值**：  0。
        :type offset: int
        """
        
        

        self._x_language = None
        self._id = None
        self._instance_id = None
        self._status = None
        self._type = None
        self._level = None
        self._sort_field = None
        self._order = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
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
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowInstanceScheduleEventsRequest.

        **参数解释**：              请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us：英文。 - zh-cn：中文。  **默认取值**：  en-us。

        :return: The x_language of this ShowInstanceScheduleEventsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowInstanceScheduleEventsRequest.

        **参数解释**：              请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us：英文。 - zh-cn：中文。  **默认取值**：  en-us。

        :param x_language: The x_language of this ShowInstanceScheduleEventsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def id(self):
        r"""Gets the id of this ShowInstanceScheduleEventsRequest.

        **参数解释**：  事件ID。  您可以登录管理控制台，在事件管理列表中查看事件ID。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，前面为UUID，后缀为ev07，长度为36个字符。  **默认取值**：  不涉及。

        :return: The id of this ShowInstanceScheduleEventsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowInstanceScheduleEventsRequest.

        **参数解释**：  事件ID。  您可以登录管理控制台，在事件管理列表中查看事件ID。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，前面为UUID，后缀为ev07，长度为36个字符。  **默认取值**：  不涉及。

        :param id: The id of this ShowInstanceScheduleEventsRequest.
        :type id: str
        """
        self._id = id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowInstanceScheduleEventsRequest.

        **参数解释**：  实例ID，此参数是实例的唯一标识。  获取方法请参见[查询实例列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlInstancesUnifyStatus.html)。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。  **默认取值**：  不涉及。

        :return: The instance_id of this ShowInstanceScheduleEventsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowInstanceScheduleEventsRequest.

        **参数解释**：  实例ID，此参数是实例的唯一标识。  获取方法请参见[查询实例列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlInstancesUnifyStatus.html)。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。  **默认取值**：  不涉及。

        :param instance_id: The instance_id of this ShowInstanceScheduleEventsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def status(self):
        r"""Gets the status of this ShowInstanceScheduleEventsRequest.

        **参数解释**：  事件状态。  **约束限制**：  不涉及。  **取值范围**：  - inquiring：待授权。 - scheduled：待执行。 - executing：执行中。 - completed：执行完成。 - canceled：事件关闭。 - failed：执行失败。  **默认取值**：  不涉及。

        :return: The status of this ShowInstanceScheduleEventsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowInstanceScheduleEventsRequest.

        **参数解释**：  事件状态。  **约束限制**：  不涉及。  **取值范围**：  - inquiring：待授权。 - scheduled：待执行。 - executing：执行中。 - completed：执行完成。 - canceled：事件关闭。 - failed：执行失败。  **默认取值**：  不涉及。

        :param status: The status of this ShowInstanceScheduleEventsRequest.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this ShowInstanceScheduleEventsRequest.

        **参数解释**：  事件类型。  **约束限制**：  不涉及。  **取值范围**：  - system.lifecycle.rebuild_node：备机重建事件。 - system.lifecycle.db_upgrade：数据库内核小版本升级事件。 - system.scheduled_event.high_cpu_memory：实例CPU或内存高负载事件，需要变更实例规格。  **默认取值**：  不涉及。

        :return: The type of this ShowInstanceScheduleEventsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowInstanceScheduleEventsRequest.

        **参数解释**：  事件类型。  **约束限制**：  不涉及。  **取值范围**：  - system.lifecycle.rebuild_node：备机重建事件。 - system.lifecycle.db_upgrade：数据库内核小版本升级事件。 - system.scheduled_event.high_cpu_memory：实例CPU或内存高负载事件，需要变更实例规格。  **默认取值**：  不涉及。

        :param type: The type of this ShowInstanceScheduleEventsRequest.
        :type type: str
        """
        self._type = type

    @property
    def level(self):
        r"""Gets the level of this ShowInstanceScheduleEventsRequest.

        **参数解释**：  事件级别。  **约束限制**：  不涉及。  **取值范围**：  - critical：紧急。 - major：重要。 - minor：一般。 - info：提示。  **默认取值**：  不涉及。

        :return: The level of this ShowInstanceScheduleEventsRequest.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this ShowInstanceScheduleEventsRequest.

        **参数解释**：  事件级别。  **约束限制**：  不涉及。  **取值范围**：  - critical：紧急。 - major：重要。 - minor：一般。 - info：提示。  **默认取值**：  不涉及。

        :param level: The level of this ShowInstanceScheduleEventsRequest.
        :type level: str
        """
        self._level = level

    @property
    def sort_field(self):
        r"""Gets the sort_field of this ShowInstanceScheduleEventsRequest.

        **参数解释**：  响应列表排序字段。  **约束限制**：  不涉及。  **取值范围**：  - created_time：创建时间。 - updated_time：更新时间。 - execution_time_window：执行时间窗。 - execute_time： 执行时间。  **默认取值**：  不涉及。

        :return: The sort_field of this ShowInstanceScheduleEventsRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this ShowInstanceScheduleEventsRequest.

        **参数解释**：  响应列表排序字段。  **约束限制**：  不涉及。  **取值范围**：  - created_time：创建时间。 - updated_time：更新时间。 - execution_time_window：执行时间窗。 - execute_time： 执行时间。  **默认取值**：  不涉及。

        :param sort_field: The sort_field of this ShowInstanceScheduleEventsRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def order(self):
        r"""Gets the order of this ShowInstanceScheduleEventsRequest.

        **参数解释**：  响应列表根据sort_field字段的排序方式（升序/降序）。  **约束限制**：  sort_field不为空时生效。  **取值范围**：  - asc：升序排列。 - desc：降序排列。  **默认取值**：  不涉及。

        :return: The order of this ShowInstanceScheduleEventsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ShowInstanceScheduleEventsRequest.

        **参数解释**：  响应列表根据sort_field字段的排序方式（升序/降序）。  **约束限制**：  sort_field不为空时生效。  **取值范围**：  - asc：升序排列。 - desc：降序排列。  **默认取值**：  不涉及。

        :param order: The order of this ShowInstanceScheduleEventsRequest.
        :type order: str
        """
        self._order = order

    @property
    def limit(self):
        r"""Gets the limit of this ShowInstanceScheduleEventsRequest.

        **参数解释**：              查询记录数。  **约束限制**：  必须为整数，不能为负数。  **取值范围**：  1-100。  **默认取值**：  10。

        :return: The limit of this ShowInstanceScheduleEventsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowInstanceScheduleEventsRequest.

        **参数解释**：              查询记录数。  **约束限制**：  必须为整数，不能为负数。  **取值范围**：  1-100。  **默认取值**：  10。

        :param limit: The limit of this ShowInstanceScheduleEventsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowInstanceScheduleEventsRequest.

        **参数解释**：              索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。  **约束限制**：  必须为整数，不能为负数。  **取值范围**：  ≥0  **默认取值**：  0。

        :return: The offset of this ShowInstanceScheduleEventsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowInstanceScheduleEventsRequest.

        **参数解释**：              索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。  **约束限制**：  必须为整数，不能为负数。  **取值范围**：  ≥0  **默认取值**：  0。

        :param offset: The offset of this ShowInstanceScheduleEventsRequest.
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
        if not isinstance(other, ShowInstanceScheduleEventsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
