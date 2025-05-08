# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObjectTaskResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_type': 'str',
        'transcode_task': 'TranscodeTask',
        'thumbnail_task': 'ThumbnailTask',
        'image_sprite_task': 'ImageSpriteTask'
    }

    attribute_map = {
        'task_type': 'task_type',
        'transcode_task': 'transcode_task',
        'thumbnail_task': 'thumbnail_task',
        'image_sprite_task': 'image_sprite_task'
    }

    def __init__(self, task_type=None, transcode_task=None, thumbnail_task=None, image_sprite_task=None):
        r"""ObjectTaskResult

        The model defined in huaweicloud sdk

        :param task_type: 工作流中任务类型
        :type task_type: str
        :param transcode_task: 
        :type transcode_task: :class:`huaweicloudsdkvod.v1.TranscodeTask`
        :param thumbnail_task: 
        :type thumbnail_task: :class:`huaweicloudsdkvod.v1.ThumbnailTask`
        :param image_sprite_task: 
        :type image_sprite_task: :class:`huaweicloudsdkvod.v1.ImageSpriteTask`
        """
        
        

        self._task_type = None
        self._transcode_task = None
        self._thumbnail_task = None
        self._image_sprite_task = None
        self.discriminator = None

        if task_type is not None:
            self.task_type = task_type
        if transcode_task is not None:
            self.transcode_task = transcode_task
        if thumbnail_task is not None:
            self.thumbnail_task = thumbnail_task
        if image_sprite_task is not None:
            self.image_sprite_task = image_sprite_task

    @property
    def task_type(self):
        r"""Gets the task_type of this ObjectTaskResult.

        工作流中任务类型

        :return: The task_type of this ObjectTaskResult.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ObjectTaskResult.

        工作流中任务类型

        :param task_type: The task_type of this ObjectTaskResult.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def transcode_task(self):
        r"""Gets the transcode_task of this ObjectTaskResult.

        :return: The transcode_task of this ObjectTaskResult.
        :rtype: :class:`huaweicloudsdkvod.v1.TranscodeTask`
        """
        return self._transcode_task

    @transcode_task.setter
    def transcode_task(self, transcode_task):
        r"""Sets the transcode_task of this ObjectTaskResult.

        :param transcode_task: The transcode_task of this ObjectTaskResult.
        :type transcode_task: :class:`huaweicloudsdkvod.v1.TranscodeTask`
        """
        self._transcode_task = transcode_task

    @property
    def thumbnail_task(self):
        r"""Gets the thumbnail_task of this ObjectTaskResult.

        :return: The thumbnail_task of this ObjectTaskResult.
        :rtype: :class:`huaweicloudsdkvod.v1.ThumbnailTask`
        """
        return self._thumbnail_task

    @thumbnail_task.setter
    def thumbnail_task(self, thumbnail_task):
        r"""Sets the thumbnail_task of this ObjectTaskResult.

        :param thumbnail_task: The thumbnail_task of this ObjectTaskResult.
        :type thumbnail_task: :class:`huaweicloudsdkvod.v1.ThumbnailTask`
        """
        self._thumbnail_task = thumbnail_task

    @property
    def image_sprite_task(self):
        r"""Gets the image_sprite_task of this ObjectTaskResult.

        :return: The image_sprite_task of this ObjectTaskResult.
        :rtype: :class:`huaweicloudsdkvod.v1.ImageSpriteTask`
        """
        return self._image_sprite_task

    @image_sprite_task.setter
    def image_sprite_task(self, image_sprite_task):
        r"""Sets the image_sprite_task of this ObjectTaskResult.

        :param image_sprite_task: The image_sprite_task of this ObjectTaskResult.
        :type image_sprite_task: :class:`huaweicloudsdkvod.v1.ImageSpriteTask`
        """
        self._image_sprite_task = image_sprite_task

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
        if not isinstance(other, ObjectTaskResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
