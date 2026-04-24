# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventSearchResultV2Events:

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
        'name': 'str',
        'type': 'str',
        'status': 'str',
        'baseline_name': 'str',
        'task_name': 'str',
        'task_id': 'str',
        'task_version': 'int',
        'happen_time': 'int',
        'owner_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'status': 'status',
        'baseline_name': 'baseline_name',
        'task_name': 'task_name',
        'task_id': 'task_id',
        'task_version': 'task_version',
        'happen_time': 'happen_time',
        'owner_name': 'owner_name'
    }

    def __init__(self, id=None, name=None, type=None, status=None, baseline_name=None, task_name=None, task_id=None, task_version=None, happen_time=None, owner_name=None):
        r"""EventSearchResultV2Events

        The model defined in huaweicloud sdk

        :param id: 事件ID。
        :type id: str
        :param name: 事件名称。
        :type name: str
        :param type: 事件类型，取值为ERROR和SLOW_DOWN。
        :type type: str
        :param status: 事件状态，取值为NEW_DISCOVERY、PROCESSING、RESTORED和IGNORED。
        :type status: str
        :param baseline_name: 基线任务名称。
        :type baseline_name: str
        :param task_name: 作业名称。
        :type task_name: str
        :param task_id: 作业ID。
        :type task_id: str
        :param task_version: 作业版本号。
        :type task_version: int
        :param happen_time: 发生时间戳，单位毫秒。
        :type happen_time: int
        :param owner_name: 责任人用户名称。
        :type owner_name: str
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._status = None
        self._baseline_name = None
        self._task_name = None
        self._task_id = None
        self._task_version = None
        self._happen_time = None
        self._owner_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if baseline_name is not None:
            self.baseline_name = baseline_name
        if task_name is not None:
            self.task_name = task_name
        if task_id is not None:
            self.task_id = task_id
        if task_version is not None:
            self.task_version = task_version
        if happen_time is not None:
            self.happen_time = happen_time
        if owner_name is not None:
            self.owner_name = owner_name

    @property
    def id(self):
        r"""Gets the id of this EventSearchResultV2Events.

        事件ID。

        :return: The id of this EventSearchResultV2Events.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this EventSearchResultV2Events.

        事件ID。

        :param id: The id of this EventSearchResultV2Events.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this EventSearchResultV2Events.

        事件名称。

        :return: The name of this EventSearchResultV2Events.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EventSearchResultV2Events.

        事件名称。

        :param name: The name of this EventSearchResultV2Events.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this EventSearchResultV2Events.

        事件类型，取值为ERROR和SLOW_DOWN。

        :return: The type of this EventSearchResultV2Events.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this EventSearchResultV2Events.

        事件类型，取值为ERROR和SLOW_DOWN。

        :param type: The type of this EventSearchResultV2Events.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this EventSearchResultV2Events.

        事件状态，取值为NEW_DISCOVERY、PROCESSING、RESTORED和IGNORED。

        :return: The status of this EventSearchResultV2Events.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this EventSearchResultV2Events.

        事件状态，取值为NEW_DISCOVERY、PROCESSING、RESTORED和IGNORED。

        :param status: The status of this EventSearchResultV2Events.
        :type status: str
        """
        self._status = status

    @property
    def baseline_name(self):
        r"""Gets the baseline_name of this EventSearchResultV2Events.

        基线任务名称。

        :return: The baseline_name of this EventSearchResultV2Events.
        :rtype: str
        """
        return self._baseline_name

    @baseline_name.setter
    def baseline_name(self, baseline_name):
        r"""Sets the baseline_name of this EventSearchResultV2Events.

        基线任务名称。

        :param baseline_name: The baseline_name of this EventSearchResultV2Events.
        :type baseline_name: str
        """
        self._baseline_name = baseline_name

    @property
    def task_name(self):
        r"""Gets the task_name of this EventSearchResultV2Events.

        作业名称。

        :return: The task_name of this EventSearchResultV2Events.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this EventSearchResultV2Events.

        作业名称。

        :param task_name: The task_name of this EventSearchResultV2Events.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_id(self):
        r"""Gets the task_id of this EventSearchResultV2Events.

        作业ID。

        :return: The task_id of this EventSearchResultV2Events.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this EventSearchResultV2Events.

        作业ID。

        :param task_id: The task_id of this EventSearchResultV2Events.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_version(self):
        r"""Gets the task_version of this EventSearchResultV2Events.

        作业版本号。

        :return: The task_version of this EventSearchResultV2Events.
        :rtype: int
        """
        return self._task_version

    @task_version.setter
    def task_version(self, task_version):
        r"""Sets the task_version of this EventSearchResultV2Events.

        作业版本号。

        :param task_version: The task_version of this EventSearchResultV2Events.
        :type task_version: int
        """
        self._task_version = task_version

    @property
    def happen_time(self):
        r"""Gets the happen_time of this EventSearchResultV2Events.

        发生时间戳，单位毫秒。

        :return: The happen_time of this EventSearchResultV2Events.
        :rtype: int
        """
        return self._happen_time

    @happen_time.setter
    def happen_time(self, happen_time):
        r"""Sets the happen_time of this EventSearchResultV2Events.

        发生时间戳，单位毫秒。

        :param happen_time: The happen_time of this EventSearchResultV2Events.
        :type happen_time: int
        """
        self._happen_time = happen_time

    @property
    def owner_name(self):
        r"""Gets the owner_name of this EventSearchResultV2Events.

        责任人用户名称。

        :return: The owner_name of this EventSearchResultV2Events.
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        r"""Sets the owner_name of this EventSearchResultV2Events.

        责任人用户名称。

        :param owner_name: The owner_name of this EventSearchResultV2Events.
        :type owner_name: str
        """
        self._owner_name = owner_name

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
        if not isinstance(other, EventSearchResultV2Events):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
