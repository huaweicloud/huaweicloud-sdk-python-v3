# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskInfoVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'description': 'str',
        'type': 'str',
        'task_id': 'str',
        'task_name': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'white_list': 'list[DateInfo]',
        'vacuum_mode': 'str',
        'vacuum_target': 'str',
        'is_paused': 'int',
        'vacuum_threshold': 'str',
        'vacuum_retrieving_space': 'str',
        'vacuum_priority': 'list[TableInfoOpen]',
        'time_zone': 'str'
    }

    attribute_map = {
        'category': 'category',
        'description': 'description',
        'type': 'type',
        'task_id': 'task_id',
        'task_name': 'task_name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'white_list': 'white_list',
        'vacuum_mode': 'vacuum_mode',
        'vacuum_target': 'vacuum_target',
        'is_paused': 'is_paused',
        'vacuum_threshold': 'vacuum_threshold',
        'vacuum_retrieving_space': 'vacuum_retrieving_space',
        'vacuum_priority': 'vacuum_priority',
        'time_zone': 'time_zone'
    }

    def __init__(self, category=None, description=None, type=None, task_id=None, task_name=None, start_time=None, end_time=None, white_list=None, vacuum_mode=None, vacuum_target=None, is_paused=None, vacuum_threshold=None, vacuum_retrieving_space=None, vacuum_priority=None, time_zone=None):
        r"""TaskInfoVo

        The model defined in huaweicloud sdk

        :param category: **参数解释**： 分类。 **默认取值**： VacuumFull
        :type category: str
        :param description: **参数解释**： 描述信息。 **默认取值**： 不涉及。
        :type description: str
        :param type: **参数解释**： 任务类型。 **默认取值**： Window：周期型任务； Date：单次型任务；
        :type type: str
        :param task_id: **参数解释**： 任务ID。 **默认取值**： 不涉及。
        :type task_id: str
        :param task_name: **参数解释**： 任务名称。 **默认取值**： 不涉及。
        :type task_name: str
        :param start_time: **参数解释**： 任务开始时间。 **默认取值**： 不涉及。
        :type start_time: str
        :param end_time: **参数解释**： 任务结束时间。 **默认取值**： 不涉及。
        :type end_time: str
        :param white_list: **参数解释**： 任务时间窗。 **默认取值**： 不涉及。
        :type white_list: list[:class:`huaweicloudsdkdws.v2.DateInfo`]
        :param vacuum_mode: **参数解释**： 任务模式。 **默认取值**： manual：指定目标； auto：自动；
        :type vacuum_mode: str
        :param vacuum_target: **参数解释**： 自动Vacuum目标。 **默认取值**： user_vacuumfull：用户表VacuumFull； system_vacuum：系统表VacuumFull；
        :type vacuum_target: str
        :param is_paused: **参数解释**： 是否暂停。 **默认取值**： 0：否； 1：是；
        :type is_paused: int
        :param vacuum_threshold: **参数解释**： 膨胀率，单位为百分比。 **默认取值**： 不涉及。
        :type vacuum_threshold: str
        :param vacuum_retrieving_space: **参数解释**： 目标表可回收空间。 **默认取值**： 不涉及。
        :type vacuum_retrieving_space: str
        :param vacuum_priority: **参数解释**： 优先Vacuum目标。 **默认取值**： 不涉及。
        :type vacuum_priority: list[:class:`huaweicloudsdkdws.v2.TableInfoOpen`]
        :param time_zone: **参数解释**： 时区信息。 **默认取值**： 一般为null。
        :type time_zone: str
        """
        
        

        self._category = None
        self._description = None
        self._type = None
        self._task_id = None
        self._task_name = None
        self._start_time = None
        self._end_time = None
        self._white_list = None
        self._vacuum_mode = None
        self._vacuum_target = None
        self._is_paused = None
        self._vacuum_threshold = None
        self._vacuum_retrieving_space = None
        self._vacuum_priority = None
        self._time_zone = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if white_list is not None:
            self.white_list = white_list
        if vacuum_mode is not None:
            self.vacuum_mode = vacuum_mode
        if vacuum_target is not None:
            self.vacuum_target = vacuum_target
        if is_paused is not None:
            self.is_paused = is_paused
        if vacuum_threshold is not None:
            self.vacuum_threshold = vacuum_threshold
        if vacuum_retrieving_space is not None:
            self.vacuum_retrieving_space = vacuum_retrieving_space
        if vacuum_priority is not None:
            self.vacuum_priority = vacuum_priority
        if time_zone is not None:
            self.time_zone = time_zone

    @property
    def category(self):
        r"""Gets the category of this TaskInfoVo.

        **参数解释**： 分类。 **默认取值**： VacuumFull

        :return: The category of this TaskInfoVo.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this TaskInfoVo.

        **参数解释**： 分类。 **默认取值**： VacuumFull

        :param category: The category of this TaskInfoVo.
        :type category: str
        """
        self._category = category

    @property
    def description(self):
        r"""Gets the description of this TaskInfoVo.

        **参数解释**： 描述信息。 **默认取值**： 不涉及。

        :return: The description of this TaskInfoVo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TaskInfoVo.

        **参数解释**： 描述信息。 **默认取值**： 不涉及。

        :param description: The description of this TaskInfoVo.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this TaskInfoVo.

        **参数解释**： 任务类型。 **默认取值**： Window：周期型任务； Date：单次型任务；

        :return: The type of this TaskInfoVo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this TaskInfoVo.

        **参数解释**： 任务类型。 **默认取值**： Window：周期型任务； Date：单次型任务；

        :param type: The type of this TaskInfoVo.
        :type type: str
        """
        self._type = type

    @property
    def task_id(self):
        r"""Gets the task_id of this TaskInfoVo.

        **参数解释**： 任务ID。 **默认取值**： 不涉及。

        :return: The task_id of this TaskInfoVo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this TaskInfoVo.

        **参数解释**： 任务ID。 **默认取值**： 不涉及。

        :param task_id: The task_id of this TaskInfoVo.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        r"""Gets the task_name of this TaskInfoVo.

        **参数解释**： 任务名称。 **默认取值**： 不涉及。

        :return: The task_name of this TaskInfoVo.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this TaskInfoVo.

        **参数解释**： 任务名称。 **默认取值**： 不涉及。

        :param task_name: The task_name of this TaskInfoVo.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def start_time(self):
        r"""Gets the start_time of this TaskInfoVo.

        **参数解释**： 任务开始时间。 **默认取值**： 不涉及。

        :return: The start_time of this TaskInfoVo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this TaskInfoVo.

        **参数解释**： 任务开始时间。 **默认取值**： 不涉及。

        :param start_time: The start_time of this TaskInfoVo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this TaskInfoVo.

        **参数解释**： 任务结束时间。 **默认取值**： 不涉及。

        :return: The end_time of this TaskInfoVo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this TaskInfoVo.

        **参数解释**： 任务结束时间。 **默认取值**： 不涉及。

        :param end_time: The end_time of this TaskInfoVo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def white_list(self):
        r"""Gets the white_list of this TaskInfoVo.

        **参数解释**： 任务时间窗。 **默认取值**： 不涉及。

        :return: The white_list of this TaskInfoVo.
        :rtype: list[:class:`huaweicloudsdkdws.v2.DateInfo`]
        """
        return self._white_list

    @white_list.setter
    def white_list(self, white_list):
        r"""Sets the white_list of this TaskInfoVo.

        **参数解释**： 任务时间窗。 **默认取值**： 不涉及。

        :param white_list: The white_list of this TaskInfoVo.
        :type white_list: list[:class:`huaweicloudsdkdws.v2.DateInfo`]
        """
        self._white_list = white_list

    @property
    def vacuum_mode(self):
        r"""Gets the vacuum_mode of this TaskInfoVo.

        **参数解释**： 任务模式。 **默认取值**： manual：指定目标； auto：自动；

        :return: The vacuum_mode of this TaskInfoVo.
        :rtype: str
        """
        return self._vacuum_mode

    @vacuum_mode.setter
    def vacuum_mode(self, vacuum_mode):
        r"""Sets the vacuum_mode of this TaskInfoVo.

        **参数解释**： 任务模式。 **默认取值**： manual：指定目标； auto：自动；

        :param vacuum_mode: The vacuum_mode of this TaskInfoVo.
        :type vacuum_mode: str
        """
        self._vacuum_mode = vacuum_mode

    @property
    def vacuum_target(self):
        r"""Gets the vacuum_target of this TaskInfoVo.

        **参数解释**： 自动Vacuum目标。 **默认取值**： user_vacuumfull：用户表VacuumFull； system_vacuum：系统表VacuumFull；

        :return: The vacuum_target of this TaskInfoVo.
        :rtype: str
        """
        return self._vacuum_target

    @vacuum_target.setter
    def vacuum_target(self, vacuum_target):
        r"""Sets the vacuum_target of this TaskInfoVo.

        **参数解释**： 自动Vacuum目标。 **默认取值**： user_vacuumfull：用户表VacuumFull； system_vacuum：系统表VacuumFull；

        :param vacuum_target: The vacuum_target of this TaskInfoVo.
        :type vacuum_target: str
        """
        self._vacuum_target = vacuum_target

    @property
    def is_paused(self):
        r"""Gets the is_paused of this TaskInfoVo.

        **参数解释**： 是否暂停。 **默认取值**： 0：否； 1：是；

        :return: The is_paused of this TaskInfoVo.
        :rtype: int
        """
        return self._is_paused

    @is_paused.setter
    def is_paused(self, is_paused):
        r"""Sets the is_paused of this TaskInfoVo.

        **参数解释**： 是否暂停。 **默认取值**： 0：否； 1：是；

        :param is_paused: The is_paused of this TaskInfoVo.
        :type is_paused: int
        """
        self._is_paused = is_paused

    @property
    def vacuum_threshold(self):
        r"""Gets the vacuum_threshold of this TaskInfoVo.

        **参数解释**： 膨胀率，单位为百分比。 **默认取值**： 不涉及。

        :return: The vacuum_threshold of this TaskInfoVo.
        :rtype: str
        """
        return self._vacuum_threshold

    @vacuum_threshold.setter
    def vacuum_threshold(self, vacuum_threshold):
        r"""Sets the vacuum_threshold of this TaskInfoVo.

        **参数解释**： 膨胀率，单位为百分比。 **默认取值**： 不涉及。

        :param vacuum_threshold: The vacuum_threshold of this TaskInfoVo.
        :type vacuum_threshold: str
        """
        self._vacuum_threshold = vacuum_threshold

    @property
    def vacuum_retrieving_space(self):
        r"""Gets the vacuum_retrieving_space of this TaskInfoVo.

        **参数解释**： 目标表可回收空间。 **默认取值**： 不涉及。

        :return: The vacuum_retrieving_space of this TaskInfoVo.
        :rtype: str
        """
        return self._vacuum_retrieving_space

    @vacuum_retrieving_space.setter
    def vacuum_retrieving_space(self, vacuum_retrieving_space):
        r"""Sets the vacuum_retrieving_space of this TaskInfoVo.

        **参数解释**： 目标表可回收空间。 **默认取值**： 不涉及。

        :param vacuum_retrieving_space: The vacuum_retrieving_space of this TaskInfoVo.
        :type vacuum_retrieving_space: str
        """
        self._vacuum_retrieving_space = vacuum_retrieving_space

    @property
    def vacuum_priority(self):
        r"""Gets the vacuum_priority of this TaskInfoVo.

        **参数解释**： 优先Vacuum目标。 **默认取值**： 不涉及。

        :return: The vacuum_priority of this TaskInfoVo.
        :rtype: list[:class:`huaweicloudsdkdws.v2.TableInfoOpen`]
        """
        return self._vacuum_priority

    @vacuum_priority.setter
    def vacuum_priority(self, vacuum_priority):
        r"""Sets the vacuum_priority of this TaskInfoVo.

        **参数解释**： 优先Vacuum目标。 **默认取值**： 不涉及。

        :param vacuum_priority: The vacuum_priority of this TaskInfoVo.
        :type vacuum_priority: list[:class:`huaweicloudsdkdws.v2.TableInfoOpen`]
        """
        self._vacuum_priority = vacuum_priority

    @property
    def time_zone(self):
        r"""Gets the time_zone of this TaskInfoVo.

        **参数解释**： 时区信息。 **默认取值**： 一般为null。

        :return: The time_zone of this TaskInfoVo.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this TaskInfoVo.

        **参数解释**： 时区信息。 **默认取值**： 一般为null。

        :param time_zone: The time_zone of this TaskInfoVo.
        :type time_zone: str
        """
        self._time_zone = time_zone

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
        if not isinstance(other, TaskInfoVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
