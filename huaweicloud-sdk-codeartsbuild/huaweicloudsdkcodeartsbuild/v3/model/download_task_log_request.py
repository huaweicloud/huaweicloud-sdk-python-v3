# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadTaskLogRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'record_id': 'str',
        'task_name': 'str',
        'log_level': 'str'
    }

    attribute_map = {
        'record_id': 'record_id',
        'task_name': 'task_name',
        'log_level': 'log_level'
    }

    def __init__(self, record_id=None, task_name=None, log_level=None):
        """DownloadTaskLogRequest

        The model defined in huaweicloud sdk

        :param record_id: 记录ID,36位数字、小写字母、&#39;-&#39;组组合。
        :type record_id: str
        :param task_name: 步骤名称
        :type task_name: str
        :param log_level: 日志等级 值为INFO | DEBUG。
        :type log_level: str
        """
        
        

        self._record_id = None
        self._task_name = None
        self._log_level = None
        self.discriminator = None

        self.record_id = record_id
        self.task_name = task_name
        if log_level is not None:
            self.log_level = log_level

    @property
    def record_id(self):
        """Gets the record_id of this DownloadTaskLogRequest.

        记录ID,36位数字、小写字母、'-'组组合。

        :return: The record_id of this DownloadTaskLogRequest.
        :rtype: str
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        """Sets the record_id of this DownloadTaskLogRequest.

        记录ID,36位数字、小写字母、'-'组组合。

        :param record_id: The record_id of this DownloadTaskLogRequest.
        :type record_id: str
        """
        self._record_id = record_id

    @property
    def task_name(self):
        """Gets the task_name of this DownloadTaskLogRequest.

        步骤名称

        :return: The task_name of this DownloadTaskLogRequest.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this DownloadTaskLogRequest.

        步骤名称

        :param task_name: The task_name of this DownloadTaskLogRequest.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def log_level(self):
        """Gets the log_level of this DownloadTaskLogRequest.

        日志等级 值为INFO | DEBUG。

        :return: The log_level of this DownloadTaskLogRequest.
        :rtype: str
        """
        return self._log_level

    @log_level.setter
    def log_level(self, log_level):
        """Sets the log_level of this DownloadTaskLogRequest.

        日志等级 值为INFO | DEBUG。

        :param log_level: The log_level of this DownloadTaskLogRequest.
        :type log_level: str
        """
        self._log_level = log_level

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DownloadTaskLogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
