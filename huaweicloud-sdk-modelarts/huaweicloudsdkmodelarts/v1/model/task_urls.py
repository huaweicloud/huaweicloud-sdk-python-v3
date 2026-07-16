# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskUrls:

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
        'url': 'str'
    }

    attribute_map = {
        'task': 'task',
        'url': 'url'
    }

    def __init__(self, task=None, url=None):
        r"""TaskUrls

        The model defined in huaweicloud sdk

        :param task: 训练作业的任务ID。
        :type task: str
        :param url: 训练作业SSH连接地址。
        :type url: str
        """
        
        

        self._task = None
        self._url = None
        self.discriminator = None

        if task is not None:
            self.task = task
        if url is not None:
            self.url = url

    @property
    def task(self):
        r"""Gets the task of this TaskUrls.

        训练作业的任务ID。

        :return: The task of this TaskUrls.
        :rtype: str
        """
        return self._task

    @task.setter
    def task(self, task):
        r"""Sets the task of this TaskUrls.

        训练作业的任务ID。

        :param task: The task of this TaskUrls.
        :type task: str
        """
        self._task = task

    @property
    def url(self):
        r"""Gets the url of this TaskUrls.

        训练作业SSH连接地址。

        :return: The url of this TaskUrls.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this TaskUrls.

        训练作业SSH连接地址。

        :param url: The url of this TaskUrls.
        :type url: str
        """
        self._url = url

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
        if not isinstance(other, TaskUrls):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
