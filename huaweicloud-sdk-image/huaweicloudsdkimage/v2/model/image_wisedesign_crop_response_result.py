# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageWisedesignCropResponseResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'box': 'list[int]',
        'image_base64': 'str',
        'task_id': 'str'
    }

    attribute_map = {
        'box': 'box',
        'image_base64': 'image_base64',
        'task_id': 'task_id'
    }

    def __init__(self, box=None, image_base64=None, task_id=None):
        """ImageWisedesignCropResponseResult

        The model defined in huaweicloud sdk

        :param box: 裁剪结果框，有四个整型数值，分别代表左上角横坐标、左上角纵坐标、右下角横坐标、右下角纵坐标，示例：[x_min, y_min, x_max, y_max]
        :type box: list[int]
        :param image_base64: 裁剪后图像的64位编码
        :type image_base64: str
        :param task_id: 请求的任务id
        :type task_id: str
        """
        
        

        self._box = None
        self._image_base64 = None
        self._task_id = None
        self.discriminator = None

        if box is not None:
            self.box = box
        if image_base64 is not None:
            self.image_base64 = image_base64
        if task_id is not None:
            self.task_id = task_id

    @property
    def box(self):
        """Gets the box of this ImageWisedesignCropResponseResult.

        裁剪结果框，有四个整型数值，分别代表左上角横坐标、左上角纵坐标、右下角横坐标、右下角纵坐标，示例：[x_min, y_min, x_max, y_max]

        :return: The box of this ImageWisedesignCropResponseResult.
        :rtype: list[int]
        """
        return self._box

    @box.setter
    def box(self, box):
        """Sets the box of this ImageWisedesignCropResponseResult.

        裁剪结果框，有四个整型数值，分别代表左上角横坐标、左上角纵坐标、右下角横坐标、右下角纵坐标，示例：[x_min, y_min, x_max, y_max]

        :param box: The box of this ImageWisedesignCropResponseResult.
        :type box: list[int]
        """
        self._box = box

    @property
    def image_base64(self):
        """Gets the image_base64 of this ImageWisedesignCropResponseResult.

        裁剪后图像的64位编码

        :return: The image_base64 of this ImageWisedesignCropResponseResult.
        :rtype: str
        """
        return self._image_base64

    @image_base64.setter
    def image_base64(self, image_base64):
        """Sets the image_base64 of this ImageWisedesignCropResponseResult.

        裁剪后图像的64位编码

        :param image_base64: The image_base64 of this ImageWisedesignCropResponseResult.
        :type image_base64: str
        """
        self._image_base64 = image_base64

    @property
    def task_id(self):
        """Gets the task_id of this ImageWisedesignCropResponseResult.

        请求的任务id

        :return: The task_id of this ImageWisedesignCropResponseResult.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ImageWisedesignCropResponseResult.

        请求的任务id

        :param task_id: The task_id of this ImageWisedesignCropResponseResult.
        :type task_id: str
        """
        self._task_id = task_id

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
        if not isinstance(other, ImageWisedesignCropResponseResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
