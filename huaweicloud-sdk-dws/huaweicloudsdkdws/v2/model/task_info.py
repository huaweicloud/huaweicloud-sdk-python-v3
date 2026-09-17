# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_name': 'str',
        'description': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'white_list': 'list[DateInfo]',
        'type': 'str',
        'vacuum_mode': 'str',
        'vacuum_target': 'str',
        'vacuum_threshold': 'str',
        'vacuum_retrieving_space': 'str',
        'vacuum_priority': 'str',
        'time_zone': 'str',
        'priority': 'list[TableInfoOpen]',
        'category': 'str'
    }

    attribute_map = {
        'task_name': 'task_name',
        'description': 'description',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'white_list': 'white_list',
        'type': 'type',
        'vacuum_mode': 'vacuum_mode',
        'vacuum_target': 'vacuum_target',
        'vacuum_threshold': 'vacuum_threshold',
        'vacuum_retrieving_space': 'vacuum_retrieving_space',
        'vacuum_priority': 'vacuum_priority',
        'time_zone': 'time_zone',
        'priority': 'priority',
        'category': 'category'
    }

    def __init__(self, task_name=None, description=None, start_time=None, end_time=None, white_list=None, type=None, vacuum_mode=None, vacuum_target=None, vacuum_threshold=None, vacuum_retrieving_space=None, vacuum_priority=None, time_zone=None, priority=None, category=None):
        r"""TaskInfo

        The model defined in huaweicloud sdk

        :param task_name: **参数解释**： 任务名称。 **约束限制**： 不涉及。 **取值范围**： 非null。 **默认取值**： 不涉及。
        :type task_name: str
        :param description: **参数解释**： 描述信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type description: str
        :param start_time: **参数解释**： 开始时间。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type start_time: str
        :param end_time: **参数解释**： 结束时间。 **约束限制**： 不涉及。 **取值范围**： 非null。 **默认取值**： 不涉及。
        :type end_time: str
        :param white_list: **参数解释**： 执行计划。 **约束限制**： 不涉及。 **取值范围**： 非null。 **默认取值**： 不涉及。
        :type white_list: list[:class:`huaweicloudsdkdws.v2.DateInfo`]
        :param type: **参数解释**： 任务类型。 **约束限制**： 不涉及。 **取值范围**： Date：单次型任务； Window：周期型任务； **默认取值**： 不涉及。
        :type type: str
        :param vacuum_mode: **参数解释**： 任务模式。 **约束限制**： 不涉及。 **取值范围**： 非null。 **默认取值**： 不涉及。
        :type vacuum_mode: str
        :param vacuum_target: **参数解释**： 自动Vacuum目标。 **约束限制**： 不涉及。 **取值范围**： user_vacuumfull：用户表VacuumFull； system_vacuum：系统表VacuumFull； **默认取值**： 不涉及。
        :type vacuum_target: str
        :param vacuum_threshold: **参数解释**： 膨胀率，单位为百分比。 **约束限制**： 不涉及。 **取值范围**： 建议设置为当前集群空间使用率+10%，且最大不超过80%。 **默认取值**： 不涉及。
        :type vacuum_threshold: str
        :param vacuum_retrieving_space: **参数解释**： 目标表可回收空间。 **约束限制**： 不涉及。 **取值范围**： 非null。 **默认取值**： 不涉及。
        :type vacuum_retrieving_space: str
        :param vacuum_priority: **参数解释**： 优先级。 **约束限制**： 不涉及。 **取值范围**： 非null。 **默认取值**： 不涉及。
        :type vacuum_priority: str
        :param time_zone: **参数解释**： 时区偏移信息。 **约束限制**： 不涉及。 **取值范围**： -2659~+2459 **默认取值**： 不涉及。
        :type time_zone: str
        :param priority: **参数解释**： 优先级表信息。 **默认取值**： 不涉及。
        :type priority: list[:class:`huaweicloudsdkdws.v2.TableInfoOpen`]
        :param category: **参数解释**： 分类信息。 **默认取值**： Vacuum
        :type category: str
        """
        
        

        self._task_name = None
        self._description = None
        self._start_time = None
        self._end_time = None
        self._white_list = None
        self._type = None
        self._vacuum_mode = None
        self._vacuum_target = None
        self._vacuum_threshold = None
        self._vacuum_retrieving_space = None
        self._vacuum_priority = None
        self._time_zone = None
        self._priority = None
        self._category = None
        self.discriminator = None

        if task_name is not None:
            self.task_name = task_name
        if description is not None:
            self.description = description
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if white_list is not None:
            self.white_list = white_list
        if type is not None:
            self.type = type
        if vacuum_mode is not None:
            self.vacuum_mode = vacuum_mode
        if vacuum_target is not None:
            self.vacuum_target = vacuum_target
        if vacuum_threshold is not None:
            self.vacuum_threshold = vacuum_threshold
        if vacuum_retrieving_space is not None:
            self.vacuum_retrieving_space = vacuum_retrieving_space
        if vacuum_priority is not None:
            self.vacuum_priority = vacuum_priority
        if time_zone is not None:
            self.time_zone = time_zone
        if priority is not None:
            self.priority = priority
        if category is not None:
            self.category = category

    @property
    def task_name(self):
        r"""Gets the task_name of this TaskInfo.

        **参数解释**： 任务名称。 **约束限制**： 不涉及。 **取值范围**： 非null。 **默认取值**： 不涉及。

        :return: The task_name of this TaskInfo.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this TaskInfo.

        **参数解释**： 任务名称。 **约束限制**： 不涉及。 **取值范围**： 非null。 **默认取值**： 不涉及。

        :param task_name: The task_name of this TaskInfo.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def description(self):
        r"""Gets the description of this TaskInfo.

        **参数解释**： 描述信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The description of this TaskInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TaskInfo.

        **参数解释**： 描述信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param description: The description of this TaskInfo.
        :type description: str
        """
        self._description = description

    @property
    def start_time(self):
        r"""Gets the start_time of this TaskInfo.

        **参数解释**： 开始时间。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The start_time of this TaskInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this TaskInfo.

        **参数解释**： 开始时间。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param start_time: The start_time of this TaskInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this TaskInfo.

        **参数解释**： 结束时间。 **约束限制**： 不涉及。 **取值范围**： 非null。 **默认取值**： 不涉及。

        :return: The end_time of this TaskInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this TaskInfo.

        **参数解释**： 结束时间。 **约束限制**： 不涉及。 **取值范围**： 非null。 **默认取值**： 不涉及。

        :param end_time: The end_time of this TaskInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def white_list(self):
        r"""Gets the white_list of this TaskInfo.

        **参数解释**： 执行计划。 **约束限制**： 不涉及。 **取值范围**： 非null。 **默认取值**： 不涉及。

        :return: The white_list of this TaskInfo.
        :rtype: list[:class:`huaweicloudsdkdws.v2.DateInfo`]
        """
        return self._white_list

    @white_list.setter
    def white_list(self, white_list):
        r"""Sets the white_list of this TaskInfo.

        **参数解释**： 执行计划。 **约束限制**： 不涉及。 **取值范围**： 非null。 **默认取值**： 不涉及。

        :param white_list: The white_list of this TaskInfo.
        :type white_list: list[:class:`huaweicloudsdkdws.v2.DateInfo`]
        """
        self._white_list = white_list

    @property
    def type(self):
        r"""Gets the type of this TaskInfo.

        **参数解释**： 任务类型。 **约束限制**： 不涉及。 **取值范围**： Date：单次型任务； Window：周期型任务； **默认取值**： 不涉及。

        :return: The type of this TaskInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this TaskInfo.

        **参数解释**： 任务类型。 **约束限制**： 不涉及。 **取值范围**： Date：单次型任务； Window：周期型任务； **默认取值**： 不涉及。

        :param type: The type of this TaskInfo.
        :type type: str
        """
        self._type = type

    @property
    def vacuum_mode(self):
        r"""Gets the vacuum_mode of this TaskInfo.

        **参数解释**： 任务模式。 **约束限制**： 不涉及。 **取值范围**： 非null。 **默认取值**： 不涉及。

        :return: The vacuum_mode of this TaskInfo.
        :rtype: str
        """
        return self._vacuum_mode

    @vacuum_mode.setter
    def vacuum_mode(self, vacuum_mode):
        r"""Sets the vacuum_mode of this TaskInfo.

        **参数解释**： 任务模式。 **约束限制**： 不涉及。 **取值范围**： 非null。 **默认取值**： 不涉及。

        :param vacuum_mode: The vacuum_mode of this TaskInfo.
        :type vacuum_mode: str
        """
        self._vacuum_mode = vacuum_mode

    @property
    def vacuum_target(self):
        r"""Gets the vacuum_target of this TaskInfo.

        **参数解释**： 自动Vacuum目标。 **约束限制**： 不涉及。 **取值范围**： user_vacuumfull：用户表VacuumFull； system_vacuum：系统表VacuumFull； **默认取值**： 不涉及。

        :return: The vacuum_target of this TaskInfo.
        :rtype: str
        """
        return self._vacuum_target

    @vacuum_target.setter
    def vacuum_target(self, vacuum_target):
        r"""Sets the vacuum_target of this TaskInfo.

        **参数解释**： 自动Vacuum目标。 **约束限制**： 不涉及。 **取值范围**： user_vacuumfull：用户表VacuumFull； system_vacuum：系统表VacuumFull； **默认取值**： 不涉及。

        :param vacuum_target: The vacuum_target of this TaskInfo.
        :type vacuum_target: str
        """
        self._vacuum_target = vacuum_target

    @property
    def vacuum_threshold(self):
        r"""Gets the vacuum_threshold of this TaskInfo.

        **参数解释**： 膨胀率，单位为百分比。 **约束限制**： 不涉及。 **取值范围**： 建议设置为当前集群空间使用率+10%，且最大不超过80%。 **默认取值**： 不涉及。

        :return: The vacuum_threshold of this TaskInfo.
        :rtype: str
        """
        return self._vacuum_threshold

    @vacuum_threshold.setter
    def vacuum_threshold(self, vacuum_threshold):
        r"""Sets the vacuum_threshold of this TaskInfo.

        **参数解释**： 膨胀率，单位为百分比。 **约束限制**： 不涉及。 **取值范围**： 建议设置为当前集群空间使用率+10%，且最大不超过80%。 **默认取值**： 不涉及。

        :param vacuum_threshold: The vacuum_threshold of this TaskInfo.
        :type vacuum_threshold: str
        """
        self._vacuum_threshold = vacuum_threshold

    @property
    def vacuum_retrieving_space(self):
        r"""Gets the vacuum_retrieving_space of this TaskInfo.

        **参数解释**： 目标表可回收空间。 **约束限制**： 不涉及。 **取值范围**： 非null。 **默认取值**： 不涉及。

        :return: The vacuum_retrieving_space of this TaskInfo.
        :rtype: str
        """
        return self._vacuum_retrieving_space

    @vacuum_retrieving_space.setter
    def vacuum_retrieving_space(self, vacuum_retrieving_space):
        r"""Sets the vacuum_retrieving_space of this TaskInfo.

        **参数解释**： 目标表可回收空间。 **约束限制**： 不涉及。 **取值范围**： 非null。 **默认取值**： 不涉及。

        :param vacuum_retrieving_space: The vacuum_retrieving_space of this TaskInfo.
        :type vacuum_retrieving_space: str
        """
        self._vacuum_retrieving_space = vacuum_retrieving_space

    @property
    def vacuum_priority(self):
        r"""Gets the vacuum_priority of this TaskInfo.

        **参数解释**： 优先级。 **约束限制**： 不涉及。 **取值范围**： 非null。 **默认取值**： 不涉及。

        :return: The vacuum_priority of this TaskInfo.
        :rtype: str
        """
        return self._vacuum_priority

    @vacuum_priority.setter
    def vacuum_priority(self, vacuum_priority):
        r"""Sets the vacuum_priority of this TaskInfo.

        **参数解释**： 优先级。 **约束限制**： 不涉及。 **取值范围**： 非null。 **默认取值**： 不涉及。

        :param vacuum_priority: The vacuum_priority of this TaskInfo.
        :type vacuum_priority: str
        """
        self._vacuum_priority = vacuum_priority

    @property
    def time_zone(self):
        r"""Gets the time_zone of this TaskInfo.

        **参数解释**： 时区偏移信息。 **约束限制**： 不涉及。 **取值范围**： -2659~+2459 **默认取值**： 不涉及。

        :return: The time_zone of this TaskInfo.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this TaskInfo.

        **参数解释**： 时区偏移信息。 **约束限制**： 不涉及。 **取值范围**： -2659~+2459 **默认取值**： 不涉及。

        :param time_zone: The time_zone of this TaskInfo.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def priority(self):
        r"""Gets the priority of this TaskInfo.

        **参数解释**： 优先级表信息。 **默认取值**： 不涉及。

        :return: The priority of this TaskInfo.
        :rtype: list[:class:`huaweicloudsdkdws.v2.TableInfoOpen`]
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this TaskInfo.

        **参数解释**： 优先级表信息。 **默认取值**： 不涉及。

        :param priority: The priority of this TaskInfo.
        :type priority: list[:class:`huaweicloudsdkdws.v2.TableInfoOpen`]
        """
        self._priority = priority

    @property
    def category(self):
        r"""Gets the category of this TaskInfo.

        **参数解释**： 分类信息。 **默认取值**： Vacuum

        :return: The category of this TaskInfo.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this TaskInfo.

        **参数解释**： 分类信息。 **默认取值**： Vacuum

        :param category: The category of this TaskInfo.
        :type category: str
        """
        self._category = category

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
        if not isinstance(other, TaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
