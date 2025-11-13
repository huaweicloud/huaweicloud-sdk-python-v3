# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubTaskInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sub_task_name': 'str',
        'percent': 'str',
        'status': 'str',
        'remaining_time': 'str'
    }

    attribute_map = {
        'sub_task_name': 'sub_task_name',
        'percent': 'percent',
        'status': 'status',
        'remaining_time': 'remaining_time'
    }

    def __init__(self, sub_task_name=None, percent=None, status=None, remaining_time=None):
        r"""SubTaskInfo

        The model defined in huaweicloud sdk

        :param sub_task_name: **参数解释**：  子任务名。  **取值范围**：  不涉及。
        :type sub_task_name: str
        :param percent: **参数解释**：  子任务进度百分比。  **取值范围**：  0-100。
        :type percent: str
        :param status: **参数解释**：  子任务状态。  **取值范围**：  - Pending：表示待执行。 - Running：表示运行中。 - Completed：表示已完成。
        :type status: str
        :param remaining_time: **参数解释**：  剩余时间，单位为秒。  **取值范围**：  不涉及。
        :type remaining_time: str
        """
        
        

        self._sub_task_name = None
        self._percent = None
        self._status = None
        self._remaining_time = None
        self.discriminator = None

        if sub_task_name is not None:
            self.sub_task_name = sub_task_name
        if percent is not None:
            self.percent = percent
        if status is not None:
            self.status = status
        if remaining_time is not None:
            self.remaining_time = remaining_time

    @property
    def sub_task_name(self):
        r"""Gets the sub_task_name of this SubTaskInfo.

        **参数解释**：  子任务名。  **取值范围**：  不涉及。

        :return: The sub_task_name of this SubTaskInfo.
        :rtype: str
        """
        return self._sub_task_name

    @sub_task_name.setter
    def sub_task_name(self, sub_task_name):
        r"""Sets the sub_task_name of this SubTaskInfo.

        **参数解释**：  子任务名。  **取值范围**：  不涉及。

        :param sub_task_name: The sub_task_name of this SubTaskInfo.
        :type sub_task_name: str
        """
        self._sub_task_name = sub_task_name

    @property
    def percent(self):
        r"""Gets the percent of this SubTaskInfo.

        **参数解释**：  子任务进度百分比。  **取值范围**：  0-100。

        :return: The percent of this SubTaskInfo.
        :rtype: str
        """
        return self._percent

    @percent.setter
    def percent(self, percent):
        r"""Sets the percent of this SubTaskInfo.

        **参数解释**：  子任务进度百分比。  **取值范围**：  0-100。

        :param percent: The percent of this SubTaskInfo.
        :type percent: str
        """
        self._percent = percent

    @property
    def status(self):
        r"""Gets the status of this SubTaskInfo.

        **参数解释**：  子任务状态。  **取值范围**：  - Pending：表示待执行。 - Running：表示运行中。 - Completed：表示已完成。

        :return: The status of this SubTaskInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SubTaskInfo.

        **参数解释**：  子任务状态。  **取值范围**：  - Pending：表示待执行。 - Running：表示运行中。 - Completed：表示已完成。

        :param status: The status of this SubTaskInfo.
        :type status: str
        """
        self._status = status

    @property
    def remaining_time(self):
        r"""Gets the remaining_time of this SubTaskInfo.

        **参数解释**：  剩余时间，单位为秒。  **取值范围**：  不涉及。

        :return: The remaining_time of this SubTaskInfo.
        :rtype: str
        """
        return self._remaining_time

    @remaining_time.setter
    def remaining_time(self, remaining_time):
        r"""Sets the remaining_time of this SubTaskInfo.

        **参数解释**：  剩余时间，单位为秒。  **取值范围**：  不涉及。

        :param remaining_time: The remaining_time of this SubTaskInfo.
        :type remaining_time: str
        """
        self._remaining_time = remaining_time

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
        if not isinstance(other, SubTaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
