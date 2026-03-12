# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryThumbnailInfo:

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
        'thumbnail_para': 'Thumbnail',
        'thumbnail_count': 'int'
    }

    attribute_map = {
        'task_id': 'task_id',
        'thumbnail_para': 'thumbnail_para',
        'thumbnail_count': 'thumbnail_count'
    }

    def __init__(self, task_id=None, thumbnail_para=None, thumbnail_count=None):
        r"""QueryThumbnailInfo

        The model defined in huaweicloud sdk

        :param task_id: 截图任务 
        :type task_id: str
        :param thumbnail_para: 
        :type thumbnail_para: :class:`huaweicloudsdkvod.v1.Thumbnail`
        :param thumbnail_count: 视频截图个数。
        :type thumbnail_count: int
        """
        
        

        self._task_id = None
        self._thumbnail_para = None
        self._thumbnail_count = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if thumbnail_para is not None:
            self.thumbnail_para = thumbnail_para
        if thumbnail_count is not None:
            self.thumbnail_count = thumbnail_count

    @property
    def task_id(self):
        r"""Gets the task_id of this QueryThumbnailInfo.

        截图任务 

        :return: The task_id of this QueryThumbnailInfo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this QueryThumbnailInfo.

        截图任务 

        :param task_id: The task_id of this QueryThumbnailInfo.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def thumbnail_para(self):
        r"""Gets the thumbnail_para of this QueryThumbnailInfo.

        :return: The thumbnail_para of this QueryThumbnailInfo.
        :rtype: :class:`huaweicloudsdkvod.v1.Thumbnail`
        """
        return self._thumbnail_para

    @thumbnail_para.setter
    def thumbnail_para(self, thumbnail_para):
        r"""Sets the thumbnail_para of this QueryThumbnailInfo.

        :param thumbnail_para: The thumbnail_para of this QueryThumbnailInfo.
        :type thumbnail_para: :class:`huaweicloudsdkvod.v1.Thumbnail`
        """
        self._thumbnail_para = thumbnail_para

    @property
    def thumbnail_count(self):
        r"""Gets the thumbnail_count of this QueryThumbnailInfo.

        视频截图个数。

        :return: The thumbnail_count of this QueryThumbnailInfo.
        :rtype: int
        """
        return self._thumbnail_count

    @thumbnail_count.setter
    def thumbnail_count(self, thumbnail_count):
        r"""Sets the thumbnail_count of this QueryThumbnailInfo.

        视频截图个数。

        :param thumbnail_count: The thumbnail_count of this QueryThumbnailInfo.
        :type thumbnail_count: int
        """
        self._thumbnail_count = thumbnail_count

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
        if not isinstance(other, QueryThumbnailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
