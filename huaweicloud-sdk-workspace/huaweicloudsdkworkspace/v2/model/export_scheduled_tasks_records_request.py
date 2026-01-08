# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportScheduledTasksRecordsRequest:

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
        'language': 'str',
        'time_zone': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'language': 'language',
        'time_zone': 'time_zone'
    }

    def __init__(self, task_id=None, language=None, time_zone=None):
        r"""ExportScheduledTasksRecordsRequest

        The model defined in huaweicloud sdk

        :param task_id: 任务ID。
        :type task_id: str
        :param language: 语言。
        :type language: str
        :param time_zone: 时区。
        :type time_zone: str
        """
        
        

        self._task_id = None
        self._language = None
        self._time_zone = None
        self.discriminator = None

        self.task_id = task_id
        if language is not None:
            self.language = language
        if time_zone is not None:
            self.time_zone = time_zone

    @property
    def task_id(self):
        r"""Gets the task_id of this ExportScheduledTasksRecordsRequest.

        任务ID。

        :return: The task_id of this ExportScheduledTasksRecordsRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ExportScheduledTasksRecordsRequest.

        任务ID。

        :param task_id: The task_id of this ExportScheduledTasksRecordsRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def language(self):
        r"""Gets the language of this ExportScheduledTasksRecordsRequest.

        语言。

        :return: The language of this ExportScheduledTasksRecordsRequest.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ExportScheduledTasksRecordsRequest.

        语言。

        :param language: The language of this ExportScheduledTasksRecordsRequest.
        :type language: str
        """
        self._language = language

    @property
    def time_zone(self):
        r"""Gets the time_zone of this ExportScheduledTasksRecordsRequest.

        时区。

        :return: The time_zone of this ExportScheduledTasksRecordsRequest.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this ExportScheduledTasksRecordsRequest.

        时区。

        :param time_zone: The time_zone of this ExportScheduledTasksRecordsRequest.
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
        if not isinstance(other, ExportScheduledTasksRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
