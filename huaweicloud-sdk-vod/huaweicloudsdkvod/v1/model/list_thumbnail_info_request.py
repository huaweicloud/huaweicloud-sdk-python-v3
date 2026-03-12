# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListThumbnailInfoRequest:

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
        'task_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'task_id': 'task_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, asset_id=None, task_id=None, offset=None, limit=None):
        r"""ListThumbnailInfoRequest

        The model defined in huaweicloud sdk

        :param asset_id: 截图对应媒资id的截图，只支持单个媒资。
        :type asset_id: str
        :param task_id: 截图对应的任务id，只支持单个任务查询。
        :type task_id: str
        :param offset: 查询偏移量。取值范围[0,20000]，默认值：0。
        :type offset: int
        :param limit: 查询一页返回数。取值范围[1,100]，默认值：10。
        :type limit: int
        """
        
        

        self._asset_id = None
        self._task_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if asset_id is not None:
            self.asset_id = asset_id
        if task_id is not None:
            self.task_id = task_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def asset_id(self):
        r"""Gets the asset_id of this ListThumbnailInfoRequest.

        截图对应媒资id的截图，只支持单个媒资。

        :return: The asset_id of this ListThumbnailInfoRequest.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this ListThumbnailInfoRequest.

        截图对应媒资id的截图，只支持单个媒资。

        :param asset_id: The asset_id of this ListThumbnailInfoRequest.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def task_id(self):
        r"""Gets the task_id of this ListThumbnailInfoRequest.

        截图对应的任务id，只支持单个任务查询。

        :return: The task_id of this ListThumbnailInfoRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ListThumbnailInfoRequest.

        截图对应的任务id，只支持单个任务查询。

        :param task_id: The task_id of this ListThumbnailInfoRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def offset(self):
        r"""Gets the offset of this ListThumbnailInfoRequest.

        查询偏移量。取值范围[0,20000]，默认值：0。

        :return: The offset of this ListThumbnailInfoRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListThumbnailInfoRequest.

        查询偏移量。取值范围[0,20000]，默认值：0。

        :param offset: The offset of this ListThumbnailInfoRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListThumbnailInfoRequest.

        查询一页返回数。取值范围[1,100]，默认值：10。

        :return: The limit of this ListThumbnailInfoRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListThumbnailInfoRequest.

        查询一页返回数。取值范围[1,100]，默认值：10。

        :param limit: The limit of this ListThumbnailInfoRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListThumbnailInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
