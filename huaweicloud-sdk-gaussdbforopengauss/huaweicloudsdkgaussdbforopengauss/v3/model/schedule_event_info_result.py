# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduleEventInfoResult:

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
        'instance_name': 'str',
        'db_type': 'str',
        'created_time': 'str',
        'update_time': 'str',
        'type': 'str',
        'impact': 'str',
        'status': 'str',
        'reason': 'str',
        'execution_time_window': 'ExecuteWindowResult',
        'level': 'str',
        'execute_time': 'str',
        'latest_execution_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'db_type': 'db_type',
        'created_time': 'created_time',
        'update_time': 'update_time',
        'type': 'type',
        'impact': 'impact',
        'status': 'status',
        'reason': 'reason',
        'execution_time_window': 'execution_time_window',
        'level': 'level',
        'execute_time': 'execute_time',
        'latest_execution_time': 'latest_execution_time'
    }

    def __init__(self, id=None, instance_id=None, instance_name=None, db_type=None, created_time=None, update_time=None, type=None, impact=None, status=None, reason=None, execution_time_window=None, level=None, execute_time=None, latest_execution_time=None):
        r"""ScheduleEventInfoResult

        The model defined in huaweicloud sdk

        :param id: **参数解释**: 事件ID。 **取值范围**: 不涉及。
        :type id: str
        :param instance_id: **参数解释**: 实例ID。 **取值范围**: 不涉及。
        :type instance_id: str
        :param instance_name: **参数解释**: 实例名称。 **取值范围**: 不涉及。
        :type instance_name: str
        :param db_type: **参数解释**: 数据库类型。 **取值范围**: 不涉及。
        :type db_type: str
        :param created_time: **参数解释**: 创建时间，格式为\&quot;yyyy-mm-ddThh:mm:ssZ\&quot;。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**: 不涉及。
        :type created_time: str
        :param update_time: **参数解释**: 更新时间，格式为\&quot;yyyy-mm-ddThh:mm:ssZ\&quot;。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**: 不涉及。
        :type update_time: str
        :param type: **参数解释**: 事件类型。 **取值范围**: - RESTAT_NODE：重启实例节点
        :type type: str
        :param impact: **参数解释**: 事件对业务的影响。 **取值范围**: 不涉及。
        :type impact: str
        :param status: **参数解释**: 事件状态。 **取值范围**: - WAITING：等待中 - INQUIRING：待授权 - SCHEDULED：待执行 - EXECUTING：执行中 - COMPLETED：已完成 - FAILED：失败 - CANCELED：已取消
        :type status: str
        :param reason: **参数解释**: 事件发生的原因。 **取值范围**: 不涉及。
        :type reason: str
        :param execution_time_window: 
        :type execution_time_window: :class:`huaweicloudsdkgaussdbforopengauss.v3.ExecuteWindowResult`
        :param level: **参数解释**: 事件级别。 **取值范围**: - CRITICAL：紧急 - MAJOR：重要 - MINOR：一般 - INFO：提示
        :type level: str
        :param execute_time: **参数解释**: 事件执行时间，格式为\&quot;yyyy-mm-ddThh:mm:ssZ\&quot;。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**: 不涉及。
        :type execute_time: str
        :param latest_execution_time: **参数解释**: 最晚执行时间，事件将在该时间之前执行。格式为\&quot;yyyy-mm-ddThh:mm:ssZ\&quot;。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**: 不涉及。
        :type latest_execution_time: str
        """
        
        

        self._id = None
        self._instance_id = None
        self._instance_name = None
        self._db_type = None
        self._created_time = None
        self._update_time = None
        self._type = None
        self._impact = None
        self._status = None
        self._reason = None
        self._execution_time_window = None
        self._level = None
        self._execute_time = None
        self._latest_execution_time = None
        self.discriminator = None

        self.id = id
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.db_type = db_type
        self.created_time = created_time
        self.update_time = update_time
        self.type = type
        self.impact = impact
        self.status = status
        self.reason = reason
        self.execution_time_window = execution_time_window
        self.level = level
        if execute_time is not None:
            self.execute_time = execute_time
        if latest_execution_time is not None:
            self.latest_execution_time = latest_execution_time

    @property
    def id(self):
        r"""Gets the id of this ScheduleEventInfoResult.

        **参数解释**: 事件ID。 **取值范围**: 不涉及。

        :return: The id of this ScheduleEventInfoResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ScheduleEventInfoResult.

        **参数解释**: 事件ID。 **取值范围**: 不涉及。

        :param id: The id of this ScheduleEventInfoResult.
        :type id: str
        """
        self._id = id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ScheduleEventInfoResult.

        **参数解释**: 实例ID。 **取值范围**: 不涉及。

        :return: The instance_id of this ScheduleEventInfoResult.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ScheduleEventInfoResult.

        **参数解释**: 实例ID。 **取值范围**: 不涉及。

        :param instance_id: The instance_id of this ScheduleEventInfoResult.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ScheduleEventInfoResult.

        **参数解释**: 实例名称。 **取值范围**: 不涉及。

        :return: The instance_name of this ScheduleEventInfoResult.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ScheduleEventInfoResult.

        **参数解释**: 实例名称。 **取值范围**: 不涉及。

        :param instance_name: The instance_name of this ScheduleEventInfoResult.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def db_type(self):
        r"""Gets the db_type of this ScheduleEventInfoResult.

        **参数解释**: 数据库类型。 **取值范围**: 不涉及。

        :return: The db_type of this ScheduleEventInfoResult.
        :rtype: str
        """
        return self._db_type

    @db_type.setter
    def db_type(self, db_type):
        r"""Sets the db_type of this ScheduleEventInfoResult.

        **参数解释**: 数据库类型。 **取值范围**: 不涉及。

        :param db_type: The db_type of this ScheduleEventInfoResult.
        :type db_type: str
        """
        self._db_type = db_type

    @property
    def created_time(self):
        r"""Gets the created_time of this ScheduleEventInfoResult.

        **参数解释**: 创建时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**: 不涉及。

        :return: The created_time of this ScheduleEventInfoResult.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this ScheduleEventInfoResult.

        **参数解释**: 创建时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**: 不涉及。

        :param created_time: The created_time of this ScheduleEventInfoResult.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ScheduleEventInfoResult.

        **参数解释**: 更新时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**: 不涉及。

        :return: The update_time of this ScheduleEventInfoResult.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ScheduleEventInfoResult.

        **参数解释**: 更新时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**: 不涉及。

        :param update_time: The update_time of this ScheduleEventInfoResult.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def type(self):
        r"""Gets the type of this ScheduleEventInfoResult.

        **参数解释**: 事件类型。 **取值范围**: - RESTAT_NODE：重启实例节点

        :return: The type of this ScheduleEventInfoResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ScheduleEventInfoResult.

        **参数解释**: 事件类型。 **取值范围**: - RESTAT_NODE：重启实例节点

        :param type: The type of this ScheduleEventInfoResult.
        :type type: str
        """
        self._type = type

    @property
    def impact(self):
        r"""Gets the impact of this ScheduleEventInfoResult.

        **参数解释**: 事件对业务的影响。 **取值范围**: 不涉及。

        :return: The impact of this ScheduleEventInfoResult.
        :rtype: str
        """
        return self._impact

    @impact.setter
    def impact(self, impact):
        r"""Sets the impact of this ScheduleEventInfoResult.

        **参数解释**: 事件对业务的影响。 **取值范围**: 不涉及。

        :param impact: The impact of this ScheduleEventInfoResult.
        :type impact: str
        """
        self._impact = impact

    @property
    def status(self):
        r"""Gets the status of this ScheduleEventInfoResult.

        **参数解释**: 事件状态。 **取值范围**: - WAITING：等待中 - INQUIRING：待授权 - SCHEDULED：待执行 - EXECUTING：执行中 - COMPLETED：已完成 - FAILED：失败 - CANCELED：已取消

        :return: The status of this ScheduleEventInfoResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ScheduleEventInfoResult.

        **参数解释**: 事件状态。 **取值范围**: - WAITING：等待中 - INQUIRING：待授权 - SCHEDULED：待执行 - EXECUTING：执行中 - COMPLETED：已完成 - FAILED：失败 - CANCELED：已取消

        :param status: The status of this ScheduleEventInfoResult.
        :type status: str
        """
        self._status = status

    @property
    def reason(self):
        r"""Gets the reason of this ScheduleEventInfoResult.

        **参数解释**: 事件发生的原因。 **取值范围**: 不涉及。

        :return: The reason of this ScheduleEventInfoResult.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this ScheduleEventInfoResult.

        **参数解释**: 事件发生的原因。 **取值范围**: 不涉及。

        :param reason: The reason of this ScheduleEventInfoResult.
        :type reason: str
        """
        self._reason = reason

    @property
    def execution_time_window(self):
        r"""Gets the execution_time_window of this ScheduleEventInfoResult.

        :return: The execution_time_window of this ScheduleEventInfoResult.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ExecuteWindowResult`
        """
        return self._execution_time_window

    @execution_time_window.setter
    def execution_time_window(self, execution_time_window):
        r"""Sets the execution_time_window of this ScheduleEventInfoResult.

        :param execution_time_window: The execution_time_window of this ScheduleEventInfoResult.
        :type execution_time_window: :class:`huaweicloudsdkgaussdbforopengauss.v3.ExecuteWindowResult`
        """
        self._execution_time_window = execution_time_window

    @property
    def level(self):
        r"""Gets the level of this ScheduleEventInfoResult.

        **参数解释**: 事件级别。 **取值范围**: - CRITICAL：紧急 - MAJOR：重要 - MINOR：一般 - INFO：提示

        :return: The level of this ScheduleEventInfoResult.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this ScheduleEventInfoResult.

        **参数解释**: 事件级别。 **取值范围**: - CRITICAL：紧急 - MAJOR：重要 - MINOR：一般 - INFO：提示

        :param level: The level of this ScheduleEventInfoResult.
        :type level: str
        """
        self._level = level

    @property
    def execute_time(self):
        r"""Gets the execute_time of this ScheduleEventInfoResult.

        **参数解释**: 事件执行时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**: 不涉及。

        :return: The execute_time of this ScheduleEventInfoResult.
        :rtype: str
        """
        return self._execute_time

    @execute_time.setter
    def execute_time(self, execute_time):
        r"""Sets the execute_time of this ScheduleEventInfoResult.

        **参数解释**: 事件执行时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**: 不涉及。

        :param execute_time: The execute_time of this ScheduleEventInfoResult.
        :type execute_time: str
        """
        self._execute_time = execute_time

    @property
    def latest_execution_time(self):
        r"""Gets the latest_execution_time of this ScheduleEventInfoResult.

        **参数解释**: 最晚执行时间，事件将在该时间之前执行。格式为\"yyyy-mm-ddThh:mm:ssZ\"。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**: 不涉及。

        :return: The latest_execution_time of this ScheduleEventInfoResult.
        :rtype: str
        """
        return self._latest_execution_time

    @latest_execution_time.setter
    def latest_execution_time(self, latest_execution_time):
        r"""Sets the latest_execution_time of this ScheduleEventInfoResult.

        **参数解释**: 最晚执行时间，事件将在该时间之前执行。格式为\"yyyy-mm-ddThh:mm:ssZ\"。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**: 不涉及。

        :param latest_execution_time: The latest_execution_time of this ScheduleEventInfoResult.
        :type latest_execution_time: str
        """
        self._latest_execution_time = latest_execution_time

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
        if not isinstance(other, ScheduleEventInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
