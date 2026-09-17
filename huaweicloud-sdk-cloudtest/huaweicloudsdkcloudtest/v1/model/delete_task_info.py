# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteTaskInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version_uri': 'str',
        'task_uris': 'list[str]'
    }

    attribute_map = {
        'version_uri': 'version_uri',
        'task_uris': 'task_uris'
    }

    def __init__(self, version_uri=None, task_uris=None):
        r"""DeleteTaskInfo

        The model defined in huaweicloud sdk

        :param version_uri: 分支/迭代id
        :type version_uri: str
        :param task_uris: 任务id数组
        :type task_uris: list[str]
        """
        
        

        self._version_uri = None
        self._task_uris = None
        self.discriminator = None

        if version_uri is not None:
            self.version_uri = version_uri
        if task_uris is not None:
            self.task_uris = task_uris

    @property
    def version_uri(self):
        r"""Gets the version_uri of this DeleteTaskInfo.

        分支/迭代id

        :return: The version_uri of this DeleteTaskInfo.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        r"""Sets the version_uri of this DeleteTaskInfo.

        分支/迭代id

        :param version_uri: The version_uri of this DeleteTaskInfo.
        :type version_uri: str
        """
        self._version_uri = version_uri

    @property
    def task_uris(self):
        r"""Gets the task_uris of this DeleteTaskInfo.

        任务id数组

        :return: The task_uris of this DeleteTaskInfo.
        :rtype: list[str]
        """
        return self._task_uris

    @task_uris.setter
    def task_uris(self, task_uris):
        r"""Sets the task_uris of this DeleteTaskInfo.

        任务id数组

        :param task_uris: The task_uris of this DeleteTaskInfo.
        :type task_uris: list[str]
        """
        self._task_uris = task_uris

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
        if not isinstance(other, DeleteTaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
