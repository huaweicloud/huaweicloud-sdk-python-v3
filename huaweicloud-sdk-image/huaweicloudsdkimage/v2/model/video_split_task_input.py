# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoSplitTaskInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'data': 'list[VideoSplitTaskInputData]'
    }

    attribute_map = {
        'type': 'type',
        'data': 'data'
    }

    def __init__(self, type=None, data=None):
        """VideoSplitTaskInput

        The model defined in huaweicloud sdk

        :param type: 任务的输入类型。可选类型有obs（对象存储服务存储的文件），url（指定的文件地址）
        :type type: str
        :param data: 任务的输入详情。针对不同的输入类型有不同的配置。
        :type data: list[:class:`huaweicloudsdkimage.v2.VideoSplitTaskInputData`]
        """
        
        

        self._type = None
        self._data = None
        self.discriminator = None

        self.type = type
        self.data = data

    @property
    def type(self):
        """Gets the type of this VideoSplitTaskInput.

        任务的输入类型。可选类型有obs（对象存储服务存储的文件），url（指定的文件地址）

        :return: The type of this VideoSplitTaskInput.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VideoSplitTaskInput.

        任务的输入类型。可选类型有obs（对象存储服务存储的文件），url（指定的文件地址）

        :param type: The type of this VideoSplitTaskInput.
        :type type: str
        """
        self._type = type

    @property
    def data(self):
        """Gets the data of this VideoSplitTaskInput.

        任务的输入详情。针对不同的输入类型有不同的配置。

        :return: The data of this VideoSplitTaskInput.
        :rtype: list[:class:`huaweicloudsdkimage.v2.VideoSplitTaskInputData`]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this VideoSplitTaskInput.

        任务的输入详情。针对不同的输入类型有不同的配置。

        :param data: The data of this VideoSplitTaskInput.
        :type data: list[:class:`huaweicloudsdkimage.v2.VideoSplitTaskInputData`]
        """
        self._data = data

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
        if not isinstance(other, VideoSplitTaskInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
