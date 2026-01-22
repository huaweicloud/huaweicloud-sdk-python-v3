# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeletePullTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'task_id': 'str'
    }

    attribute_map = {
        'region': 'region',
        'task_id': 'task_id'
    }

    def __init__(self, region=None, task_id=None):
        r"""DeletePullTaskRequest

        The model defined in huaweicloud sdk

        :param region: 任务执行区域
        :type region: str
        :param task_id: 任务id
        :type task_id: str
        """
        
        

        self._region = None
        self._task_id = None
        self.discriminator = None

        if region is not None:
            self.region = region
        self.task_id = task_id

    @property
    def region(self):
        r"""Gets the region of this DeletePullTaskRequest.

        任务执行区域

        :return: The region of this DeletePullTaskRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this DeletePullTaskRequest.

        任务执行区域

        :param region: The region of this DeletePullTaskRequest.
        :type region: str
        """
        self._region = region

    @property
    def task_id(self):
        r"""Gets the task_id of this DeletePullTaskRequest.

        任务id

        :return: The task_id of this DeletePullTaskRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this DeletePullTaskRequest.

        任务id

        :param task_id: The task_id of this DeletePullTaskRequest.
        :type task_id: str
        """
        self._task_id = task_id

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
        if not isinstance(other, DeletePullTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
