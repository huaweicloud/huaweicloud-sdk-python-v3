# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MonitorTaskInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'task_props': 'object'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_props': 'task_props'
    }

    def __init__(self, task_id=None, task_props=None):
        r"""MonitorTaskInfo

        The model defined in huaweicloud sdk

        :param task_id: Flink作业任务ID。
        :type task_id: str
        :param task_props: 任务实时监控指标。
        :type task_props: object
        """
        
        

        self._task_id = None
        self._task_props = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if task_props is not None:
            self.task_props = task_props

    @property
    def task_id(self):
        r"""Gets the task_id of this MonitorTaskInfo.

        Flink作业任务ID。

        :return: The task_id of this MonitorTaskInfo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this MonitorTaskInfo.

        Flink作业任务ID。

        :param task_id: The task_id of this MonitorTaskInfo.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_props(self):
        r"""Gets the task_props of this MonitorTaskInfo.

        任务实时监控指标。

        :return: The task_props of this MonitorTaskInfo.
        :rtype: object
        """
        return self._task_props

    @task_props.setter
    def task_props(self, task_props):
        r"""Sets the task_props of this MonitorTaskInfo.

        任务实时监控指标。

        :param task_props: The task_props of this MonitorTaskInfo.
        :type task_props: object
        """
        self._task_props = task_props

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
        if not isinstance(other, MonitorTaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
