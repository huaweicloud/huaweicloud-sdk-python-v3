# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskHistory:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task': 'str',
        'ip': 'str',
        'host_ip': 'str',
        'schedule_count': 'int'
    }

    attribute_map = {
        'task': 'task',
        'ip': 'ip',
        'host_ip': 'host_ip',
        'schedule_count': 'schedule_count'
    }

    def __init__(self, task=None, ip=None, host_ip=None, schedule_count=None):
        r"""TaskHistory

        The model defined in huaweicloud sdk

        :param task: **参数解释**：实例名。 **取值范围**：不涉及。
        :type task: str
        :param ip: **参数解释**：实例IP。 **取值范围**：不涉及。
        :type ip: str
        :param host_ip: **参数解释**：实例所在的节点IP。 **取值范围**：不涉及。
        :type host_ip: str
        :param schedule_count: **参数解释**：该实例归属于第几次调度。 **取值范围**：不涉及。
        :type schedule_count: int
        """
        
        

        self._task = None
        self._ip = None
        self._host_ip = None
        self._schedule_count = None
        self.discriminator = None

        if task is not None:
            self.task = task
        if ip is not None:
            self.ip = ip
        if host_ip is not None:
            self.host_ip = host_ip
        if schedule_count is not None:
            self.schedule_count = schedule_count

    @property
    def task(self):
        r"""Gets the task of this TaskHistory.

        **参数解释**：实例名。 **取值范围**：不涉及。

        :return: The task of this TaskHistory.
        :rtype: str
        """
        return self._task

    @task.setter
    def task(self, task):
        r"""Sets the task of this TaskHistory.

        **参数解释**：实例名。 **取值范围**：不涉及。

        :param task: The task of this TaskHistory.
        :type task: str
        """
        self._task = task

    @property
    def ip(self):
        r"""Gets the ip of this TaskHistory.

        **参数解释**：实例IP。 **取值范围**：不涉及。

        :return: The ip of this TaskHistory.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this TaskHistory.

        **参数解释**：实例IP。 **取值范围**：不涉及。

        :param ip: The ip of this TaskHistory.
        :type ip: str
        """
        self._ip = ip

    @property
    def host_ip(self):
        r"""Gets the host_ip of this TaskHistory.

        **参数解释**：实例所在的节点IP。 **取值范围**：不涉及。

        :return: The host_ip of this TaskHistory.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this TaskHistory.

        **参数解释**：实例所在的节点IP。 **取值范围**：不涉及。

        :param host_ip: The host_ip of this TaskHistory.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def schedule_count(self):
        r"""Gets the schedule_count of this TaskHistory.

        **参数解释**：该实例归属于第几次调度。 **取值范围**：不涉及。

        :return: The schedule_count of this TaskHistory.
        :rtype: int
        """
        return self._schedule_count

    @schedule_count.setter
    def schedule_count(self, schedule_count):
        r"""Sets the schedule_count of this TaskHistory.

        **参数解释**：该实例归属于第几次调度。 **取值范围**：不涉及。

        :param schedule_count: The schedule_count of this TaskHistory.
        :type schedule_count: int
        """
        self._schedule_count = schedule_count

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
        if not isinstance(other, TaskHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
