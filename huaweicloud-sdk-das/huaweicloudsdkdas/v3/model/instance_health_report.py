# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceHealthReport:

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
        'instance_id': 'str',
        'instance_name': 'str',
        'start_at': 'int',
        'end_at': 'int'
    }

    attribute_map = {
        'task_id': 'task_id',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'start_at': 'start_at',
        'end_at': 'end_at'
    }

    def __init__(self, task_id=None, instance_id=None, instance_name=None, start_at=None, end_at=None):
        r"""InstanceHealthReport

        The model defined in huaweicloud sdk

        :param task_id: 报告ID
        :type task_id: str
        :param instance_id: 实例ID
        :type instance_id: str
        :param instance_name: 实例名称
        :type instance_name: str
        :param start_at: 诊断起始时间（Unix timestamp），单位：毫秒。
        :type start_at: int
        :param end_at: 诊断终止时间（Unix timestamp），单位：毫秒。
        :type end_at: int
        """
        
        

        self._task_id = None
        self._instance_id = None
        self._instance_name = None
        self._start_at = None
        self._end_at = None
        self.discriminator = None

        self.task_id = task_id
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.start_at = start_at
        self.end_at = end_at

    @property
    def task_id(self):
        r"""Gets the task_id of this InstanceHealthReport.

        报告ID

        :return: The task_id of this InstanceHealthReport.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this InstanceHealthReport.

        报告ID

        :param task_id: The task_id of this InstanceHealthReport.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this InstanceHealthReport.

        实例ID

        :return: The instance_id of this InstanceHealthReport.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this InstanceHealthReport.

        实例ID

        :param instance_id: The instance_id of this InstanceHealthReport.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this InstanceHealthReport.

        实例名称

        :return: The instance_name of this InstanceHealthReport.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this InstanceHealthReport.

        实例名称

        :param instance_name: The instance_name of this InstanceHealthReport.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def start_at(self):
        r"""Gets the start_at of this InstanceHealthReport.

        诊断起始时间（Unix timestamp），单位：毫秒。

        :return: The start_at of this InstanceHealthReport.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this InstanceHealthReport.

        诊断起始时间（Unix timestamp），单位：毫秒。

        :param start_at: The start_at of this InstanceHealthReport.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        r"""Gets the end_at of this InstanceHealthReport.

        诊断终止时间（Unix timestamp），单位：毫秒。

        :return: The end_at of this InstanceHealthReport.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this InstanceHealthReport.

        诊断终止时间（Unix timestamp），单位：毫秒。

        :param end_at: The end_at of this InstanceHealthReport.
        :type end_at: int
        """
        self._end_at = end_at

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
        if not isinstance(other, InstanceHealthReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
