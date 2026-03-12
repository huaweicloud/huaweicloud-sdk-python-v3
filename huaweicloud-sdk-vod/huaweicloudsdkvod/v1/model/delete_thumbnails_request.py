# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteThumbnailsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_id': 'str',
        'task_id': 'list[str]'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'task_id': 'task_id'
    }

    def __init__(self, asset_id=None, task_id=None):
        r"""DeleteThumbnailsRequest

        The model defined in huaweicloud sdk

        :param asset_id: 媒资ID
        :type asset_id: str
        :param task_id: 删除指定截图任务的截图结果，一次最多10个
        :type task_id: list[str]
        """
        
        

        self._asset_id = None
        self._task_id = None
        self.discriminator = None

        if asset_id is not None:
            self.asset_id = asset_id
        if task_id is not None:
            self.task_id = task_id

    @property
    def asset_id(self):
        r"""Gets the asset_id of this DeleteThumbnailsRequest.

        媒资ID

        :return: The asset_id of this DeleteThumbnailsRequest.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this DeleteThumbnailsRequest.

        媒资ID

        :param asset_id: The asset_id of this DeleteThumbnailsRequest.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def task_id(self):
        r"""Gets the task_id of this DeleteThumbnailsRequest.

        删除指定截图任务的截图结果，一次最多10个

        :return: The task_id of this DeleteThumbnailsRequest.
        :rtype: list[str]
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this DeleteThumbnailsRequest.

        删除指定截图任务的截图结果，一次最多10个

        :param task_id: The task_id of this DeleteThumbnailsRequest.
        :type task_id: list[str]
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
        if not isinstance(other, DeleteThumbnailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
