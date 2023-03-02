# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageWisedesignInpaintingResponseResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_base64': 'str',
        'action': 'str',
        'task_id': 'str'
    }

    attribute_map = {
        'image_base64': 'image_base64',
        'action': 'action',
        'task_id': 'task_id'
    }

    def __init__(self, image_base64=None, action=None, task_id=None):
        """ImageWisedesignInpaintingResponseResult

        The model defined in huaweicloud sdk

        :param image_base64: 修复结果图片base64
        :type image_base64: str
        :param action: 请求类型
        :type action: str
        :param task_id: 请求的任务id
        :type task_id: str
        """
        
        

        self._image_base64 = None
        self._action = None
        self._task_id = None
        self.discriminator = None

        if image_base64 is not None:
            self.image_base64 = image_base64
        if action is not None:
            self.action = action
        if task_id is not None:
            self.task_id = task_id

    @property
    def image_base64(self):
        """Gets the image_base64 of this ImageWisedesignInpaintingResponseResult.

        修复结果图片base64

        :return: The image_base64 of this ImageWisedesignInpaintingResponseResult.
        :rtype: str
        """
        return self._image_base64

    @image_base64.setter
    def image_base64(self, image_base64):
        """Sets the image_base64 of this ImageWisedesignInpaintingResponseResult.

        修复结果图片base64

        :param image_base64: The image_base64 of this ImageWisedesignInpaintingResponseResult.
        :type image_base64: str
        """
        self._image_base64 = image_base64

    @property
    def action(self):
        """Gets the action of this ImageWisedesignInpaintingResponseResult.

        请求类型

        :return: The action of this ImageWisedesignInpaintingResponseResult.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ImageWisedesignInpaintingResponseResult.

        请求类型

        :param action: The action of this ImageWisedesignInpaintingResponseResult.
        :type action: str
        """
        self._action = action

    @property
    def task_id(self):
        """Gets the task_id of this ImageWisedesignInpaintingResponseResult.

        请求的任务id

        :return: The task_id of this ImageWisedesignInpaintingResponseResult.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ImageWisedesignInpaintingResponseResult.

        请求的任务id

        :param task_id: The task_id of this ImageWisedesignInpaintingResponseResult.
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
        if not isinstance(other, ImageWisedesignInpaintingResponseResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
