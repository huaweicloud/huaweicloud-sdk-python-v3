# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IntelligentKillSessionHistory:

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
        'start_time': 'int',
        'end_time': 'int',
        'download_link': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'download_link': 'download_link'
    }

    def __init__(self, task_id=None, start_time=None, end_time=None, download_link=None):
        r"""IntelligentKillSessionHistory

        The model defined in huaweicloud sdk

        :param task_id: **参数解释**：  智能Kill会话动作任务ID。  **取值范围**：  不涉及。
        :type task_id: str
        :param start_time: **参数解释**：  智能Kill会话动作起始时间。  **取值范围**：  开始执行智能Kill会话动作时刻的秒级时间戳。
        :type start_time: int
        :param end_time: **参数解释**：  智能Kill会话动作结束时间。  **取值范围**：  结束执行智能Kill会话动作时刻的秒级时间戳。
        :type end_time: int
        :param download_link: **参数解释**：  智能Kill会话历史记录下载链接。  **取值范围**：  不涉及。
        :type download_link: str
        """
        
        

        self._task_id = None
        self._start_time = None
        self._end_time = None
        self._download_link = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if download_link is not None:
            self.download_link = download_link

    @property
    def task_id(self):
        r"""Gets the task_id of this IntelligentKillSessionHistory.

        **参数解释**：  智能Kill会话动作任务ID。  **取值范围**：  不涉及。

        :return: The task_id of this IntelligentKillSessionHistory.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this IntelligentKillSessionHistory.

        **参数解释**：  智能Kill会话动作任务ID。  **取值范围**：  不涉及。

        :param task_id: The task_id of this IntelligentKillSessionHistory.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def start_time(self):
        r"""Gets the start_time of this IntelligentKillSessionHistory.

        **参数解释**：  智能Kill会话动作起始时间。  **取值范围**：  开始执行智能Kill会话动作时刻的秒级时间戳。

        :return: The start_time of this IntelligentKillSessionHistory.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this IntelligentKillSessionHistory.

        **参数解释**：  智能Kill会话动作起始时间。  **取值范围**：  开始执行智能Kill会话动作时刻的秒级时间戳。

        :param start_time: The start_time of this IntelligentKillSessionHistory.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this IntelligentKillSessionHistory.

        **参数解释**：  智能Kill会话动作结束时间。  **取值范围**：  结束执行智能Kill会话动作时刻的秒级时间戳。

        :return: The end_time of this IntelligentKillSessionHistory.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this IntelligentKillSessionHistory.

        **参数解释**：  智能Kill会话动作结束时间。  **取值范围**：  结束执行智能Kill会话动作时刻的秒级时间戳。

        :param end_time: The end_time of this IntelligentKillSessionHistory.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def download_link(self):
        r"""Gets the download_link of this IntelligentKillSessionHistory.

        **参数解释**：  智能Kill会话历史记录下载链接。  **取值范围**：  不涉及。

        :return: The download_link of this IntelligentKillSessionHistory.
        :rtype: str
        """
        return self._download_link

    @download_link.setter
    def download_link(self, download_link):
        r"""Sets the download_link of this IntelligentKillSessionHistory.

        **参数解释**：  智能Kill会话历史记录下载链接。  **取值范围**：  不涉及。

        :param download_link: The download_link of this IntelligentKillSessionHistory.
        :type download_link: str
        """
        self._download_link = download_link

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
        if not isinstance(other, IntelligentKillSessionHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
