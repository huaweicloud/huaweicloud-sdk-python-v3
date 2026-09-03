# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduleEventInfo:

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
        'category': 'str',
        'impact': 'str',
        'status': 'str',
        'reason': 'str',
        'level': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'db_type': 'str',
        'created_time': 'str',
        'updated_time': 'str',
        'type': 'str',
        'extend_info': 'str',
        'execute_time': 'str',
        'execution_time_window': 'ExecuteWindow',
        'event_entities': 'list[EventEntity]'
    }

    attribute_map = {
        'id': 'id',
        'category': 'category',
        'impact': 'impact',
        'status': 'status',
        'reason': 'reason',
        'level': 'level',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'db_type': 'db_type',
        'created_time': 'created_time',
        'updated_time': 'updated_time',
        'type': 'type',
        'extend_info': 'extend_info',
        'execute_time': 'execute_time',
        'execution_time_window': 'execution_time_window',
        'event_entities': 'event_entities'
    }

    def __init__(self, id=None, category=None, impact=None, status=None, reason=None, level=None, instance_id=None, instance_name=None, db_type=None, created_time=None, updated_time=None, type=None, extend_info=None, execute_time=None, execution_time_window=None, event_entities=None):
        r"""ScheduleEventInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释**：  事件ID。  **取值范围**：  只能由英文字母、数字组成，前面为UUID，后缀为ev07，长度为36个字符。
        :type id: str
        :param category: **参数解释**：  事件类别。  **取值范围**：  Maintenance：计划内运维事件。
        :type category: str
        :param impact: **参数解释**：  事件影响。  **取值范围**：  不涉及。
        :type impact: str
        :param status: **参数解释**：  事件状态。  **取值范围**：    - inquiring：待授权。   - scheduled：待执行。   - executing：执行中。   - completed：执行完成。   - canceled：事件关闭。   - failed：执行失败。
        :type status: str
        :param reason: **参数解释**：  事件原因。  **取值范围**：  不涉及。
        :type reason: str
        :param level: **参数解释**：  事件级别。  **取值范围**：  - critical：紧急。 - major：重要。 - minor：一般。 - info：提示。
        :type level: str
        :param instance_id: **参数解释**：  实例ID。  **取值范围**：  只能由英文字母、数字组成，前面为UUID，后缀为in07，长度为36个字符。
        :type instance_id: str
        :param instance_name: **参数解释**：  实例名称。  **取值范围**：  最小为4个字符，最大为64个字符且不超过64个字节（注意：一个中文字符占用3个字节），必须以字母或中文开头，区分大小写，可以包含字母、数字、中划线、下划线或中文，不能包含其他特殊字符。
        :type instance_name: str
        :param db_type: **参数解释**：  引擎名称。  **取值范围**：  taurus：TaurusDB企业版。
        :type db_type: str
        :param created_time: **参数解释**：  创建时间。UTC，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。  **取值范围**：  不涉及。
        :type created_time: str
        :param updated_time: **参数解释**：  更新时间。UTC，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。  **取值范围**：  不涉及。
        :type updated_time: str
        :param type: **参数解释**：  事件类型。  **取值范围**：  - system.lifecycle.rebuild_node：备机重建事件。 - system.lifecycle.db_upgrade：数据库内核小版本升级事件。 - system.scheduled_event.high_cpu_memory：实例CPU或内存高负载事件，需要变更实例规格。
        :type type: str
        :param extend_info: **参数解释**：  扩展信息。  **取值范围**：  不涉及。
        :type extend_info: str
        :param execute_time: **参数解释**：  事件的执行时间。UTC，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。  **取值范围**：  不涉及。
        :type execute_time: str
        :param execution_time_window: 
        :type execution_time_window: :class:`huaweicloudsdkgaussdb.v3.ExecuteWindow`
        :param event_entities: **参数解释**：  事件对象信息列表，包含事件对象ID和事件对象的执行状态
        :type event_entities: list[:class:`huaweicloudsdkgaussdb.v3.EventEntity`]
        """
        
        

        self._id = None
        self._category = None
        self._impact = None
        self._status = None
        self._reason = None
        self._level = None
        self._instance_id = None
        self._instance_name = None
        self._db_type = None
        self._created_time = None
        self._updated_time = None
        self._type = None
        self._extend_info = None
        self._execute_time = None
        self._execution_time_window = None
        self._event_entities = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if category is not None:
            self.category = category
        if impact is not None:
            self.impact = impact
        if status is not None:
            self.status = status
        if reason is not None:
            self.reason = reason
        if level is not None:
            self.level = level
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if db_type is not None:
            self.db_type = db_type
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time
        if type is not None:
            self.type = type
        if extend_info is not None:
            self.extend_info = extend_info
        if execute_time is not None:
            self.execute_time = execute_time
        if execution_time_window is not None:
            self.execution_time_window = execution_time_window
        if event_entities is not None:
            self.event_entities = event_entities

    @property
    def id(self):
        r"""Gets the id of this ScheduleEventInfo.

        **参数解释**：  事件ID。  **取值范围**：  只能由英文字母、数字组成，前面为UUID，后缀为ev07，长度为36个字符。

        :return: The id of this ScheduleEventInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ScheduleEventInfo.

        **参数解释**：  事件ID。  **取值范围**：  只能由英文字母、数字组成，前面为UUID，后缀为ev07，长度为36个字符。

        :param id: The id of this ScheduleEventInfo.
        :type id: str
        """
        self._id = id

    @property
    def category(self):
        r"""Gets the category of this ScheduleEventInfo.

        **参数解释**：  事件类别。  **取值范围**：  Maintenance：计划内运维事件。

        :return: The category of this ScheduleEventInfo.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ScheduleEventInfo.

        **参数解释**：  事件类别。  **取值范围**：  Maintenance：计划内运维事件。

        :param category: The category of this ScheduleEventInfo.
        :type category: str
        """
        self._category = category

    @property
    def impact(self):
        r"""Gets the impact of this ScheduleEventInfo.

        **参数解释**：  事件影响。  **取值范围**：  不涉及。

        :return: The impact of this ScheduleEventInfo.
        :rtype: str
        """
        return self._impact

    @impact.setter
    def impact(self, impact):
        r"""Sets the impact of this ScheduleEventInfo.

        **参数解释**：  事件影响。  **取值范围**：  不涉及。

        :param impact: The impact of this ScheduleEventInfo.
        :type impact: str
        """
        self._impact = impact

    @property
    def status(self):
        r"""Gets the status of this ScheduleEventInfo.

        **参数解释**：  事件状态。  **取值范围**：    - inquiring：待授权。   - scheduled：待执行。   - executing：执行中。   - completed：执行完成。   - canceled：事件关闭。   - failed：执行失败。

        :return: The status of this ScheduleEventInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ScheduleEventInfo.

        **参数解释**：  事件状态。  **取值范围**：    - inquiring：待授权。   - scheduled：待执行。   - executing：执行中。   - completed：执行完成。   - canceled：事件关闭。   - failed：执行失败。

        :param status: The status of this ScheduleEventInfo.
        :type status: str
        """
        self._status = status

    @property
    def reason(self):
        r"""Gets the reason of this ScheduleEventInfo.

        **参数解释**：  事件原因。  **取值范围**：  不涉及。

        :return: The reason of this ScheduleEventInfo.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this ScheduleEventInfo.

        **参数解释**：  事件原因。  **取值范围**：  不涉及。

        :param reason: The reason of this ScheduleEventInfo.
        :type reason: str
        """
        self._reason = reason

    @property
    def level(self):
        r"""Gets the level of this ScheduleEventInfo.

        **参数解释**：  事件级别。  **取值范围**：  - critical：紧急。 - major：重要。 - minor：一般。 - info：提示。

        :return: The level of this ScheduleEventInfo.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this ScheduleEventInfo.

        **参数解释**：  事件级别。  **取值范围**：  - critical：紧急。 - major：重要。 - minor：一般。 - info：提示。

        :param level: The level of this ScheduleEventInfo.
        :type level: str
        """
        self._level = level

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ScheduleEventInfo.

        **参数解释**：  实例ID。  **取值范围**：  只能由英文字母、数字组成，前面为UUID，后缀为in07，长度为36个字符。

        :return: The instance_id of this ScheduleEventInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ScheduleEventInfo.

        **参数解释**：  实例ID。  **取值范围**：  只能由英文字母、数字组成，前面为UUID，后缀为in07，长度为36个字符。

        :param instance_id: The instance_id of this ScheduleEventInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ScheduleEventInfo.

        **参数解释**：  实例名称。  **取值范围**：  最小为4个字符，最大为64个字符且不超过64个字节（注意：一个中文字符占用3个字节），必须以字母或中文开头，区分大小写，可以包含字母、数字、中划线、下划线或中文，不能包含其他特殊字符。

        :return: The instance_name of this ScheduleEventInfo.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ScheduleEventInfo.

        **参数解释**：  实例名称。  **取值范围**：  最小为4个字符，最大为64个字符且不超过64个字节（注意：一个中文字符占用3个字节），必须以字母或中文开头，区分大小写，可以包含字母、数字、中划线、下划线或中文，不能包含其他特殊字符。

        :param instance_name: The instance_name of this ScheduleEventInfo.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def db_type(self):
        r"""Gets the db_type of this ScheduleEventInfo.

        **参数解释**：  引擎名称。  **取值范围**：  taurus：TaurusDB企业版。

        :return: The db_type of this ScheduleEventInfo.
        :rtype: str
        """
        return self._db_type

    @db_type.setter
    def db_type(self, db_type):
        r"""Sets the db_type of this ScheduleEventInfo.

        **参数解释**：  引擎名称。  **取值范围**：  taurus：TaurusDB企业版。

        :param db_type: The db_type of this ScheduleEventInfo.
        :type db_type: str
        """
        self._db_type = db_type

    @property
    def created_time(self):
        r"""Gets the created_time of this ScheduleEventInfo.

        **参数解释**：  创建时间。UTC，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。  **取值范围**：  不涉及。

        :return: The created_time of this ScheduleEventInfo.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this ScheduleEventInfo.

        **参数解释**：  创建时间。UTC，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。  **取值范围**：  不涉及。

        :param created_time: The created_time of this ScheduleEventInfo.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        r"""Gets the updated_time of this ScheduleEventInfo.

        **参数解释**：  更新时间。UTC，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。  **取值范围**：  不涉及。

        :return: The updated_time of this ScheduleEventInfo.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        r"""Sets the updated_time of this ScheduleEventInfo.

        **参数解释**：  更新时间。UTC，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。  **取值范围**：  不涉及。

        :param updated_time: The updated_time of this ScheduleEventInfo.
        :type updated_time: str
        """
        self._updated_time = updated_time

    @property
    def type(self):
        r"""Gets the type of this ScheduleEventInfo.

        **参数解释**：  事件类型。  **取值范围**：  - system.lifecycle.rebuild_node：备机重建事件。 - system.lifecycle.db_upgrade：数据库内核小版本升级事件。 - system.scheduled_event.high_cpu_memory：实例CPU或内存高负载事件，需要变更实例规格。

        :return: The type of this ScheduleEventInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ScheduleEventInfo.

        **参数解释**：  事件类型。  **取值范围**：  - system.lifecycle.rebuild_node：备机重建事件。 - system.lifecycle.db_upgrade：数据库内核小版本升级事件。 - system.scheduled_event.high_cpu_memory：实例CPU或内存高负载事件，需要变更实例规格。

        :param type: The type of this ScheduleEventInfo.
        :type type: str
        """
        self._type = type

    @property
    def extend_info(self):
        r"""Gets the extend_info of this ScheduleEventInfo.

        **参数解释**：  扩展信息。  **取值范围**：  不涉及。

        :return: The extend_info of this ScheduleEventInfo.
        :rtype: str
        """
        return self._extend_info

    @extend_info.setter
    def extend_info(self, extend_info):
        r"""Sets the extend_info of this ScheduleEventInfo.

        **参数解释**：  扩展信息。  **取值范围**：  不涉及。

        :param extend_info: The extend_info of this ScheduleEventInfo.
        :type extend_info: str
        """
        self._extend_info = extend_info

    @property
    def execute_time(self):
        r"""Gets the execute_time of this ScheduleEventInfo.

        **参数解释**：  事件的执行时间。UTC，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。  **取值范围**：  不涉及。

        :return: The execute_time of this ScheduleEventInfo.
        :rtype: str
        """
        return self._execute_time

    @execute_time.setter
    def execute_time(self, execute_time):
        r"""Sets the execute_time of this ScheduleEventInfo.

        **参数解释**：  事件的执行时间。UTC，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。  **取值范围**：  不涉及。

        :param execute_time: The execute_time of this ScheduleEventInfo.
        :type execute_time: str
        """
        self._execute_time = execute_time

    @property
    def execution_time_window(self):
        r"""Gets the execution_time_window of this ScheduleEventInfo.

        :return: The execution_time_window of this ScheduleEventInfo.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ExecuteWindow`
        """
        return self._execution_time_window

    @execution_time_window.setter
    def execution_time_window(self, execution_time_window):
        r"""Sets the execution_time_window of this ScheduleEventInfo.

        :param execution_time_window: The execution_time_window of this ScheduleEventInfo.
        :type execution_time_window: :class:`huaweicloudsdkgaussdb.v3.ExecuteWindow`
        """
        self._execution_time_window = execution_time_window

    @property
    def event_entities(self):
        r"""Gets the event_entities of this ScheduleEventInfo.

        **参数解释**：  事件对象信息列表，包含事件对象ID和事件对象的执行状态

        :return: The event_entities of this ScheduleEventInfo.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.EventEntity`]
        """
        return self._event_entities

    @event_entities.setter
    def event_entities(self, event_entities):
        r"""Sets the event_entities of this ScheduleEventInfo.

        **参数解释**：  事件对象信息列表，包含事件对象ID和事件对象的执行状态

        :param event_entities: The event_entities of this ScheduleEventInfo.
        :type event_entities: list[:class:`huaweicloudsdkgaussdb.v3.EventEntity`]
        """
        self._event_entities = event_entities

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
        if not isinstance(other, ScheduleEventInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
