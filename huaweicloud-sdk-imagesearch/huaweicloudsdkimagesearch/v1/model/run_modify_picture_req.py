# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunModifyPictureReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'path': 'str',
        'tags': 'object'
    }

    attribute_map = {
        'path': 'path',
        'tags': 'tags'
    }

    def __init__(self, path=None, tags=None):
        """RunModifyPictureReq

        The model defined in huaweicloud sdk

        :param path: 图片URL路径，作为图片库中索引图片的ID。
        :type path: str
        :param tags: 自定义标签，格式为key:value对，其中： - 标签名（key值）须存在于实例中； - 标签内容（value值）为自定义标签值。 
        :type tags: object
        """
        
        

        self._path = None
        self._tags = None
        self.discriminator = None

        self.path = path
        self.tags = tags

    @property
    def path(self):
        """Gets the path of this RunModifyPictureReq.

        图片URL路径，作为图片库中索引图片的ID。

        :return: The path of this RunModifyPictureReq.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this RunModifyPictureReq.

        图片URL路径，作为图片库中索引图片的ID。

        :param path: The path of this RunModifyPictureReq.
        :type path: str
        """
        self._path = path

    @property
    def tags(self):
        """Gets the tags of this RunModifyPictureReq.

        自定义标签，格式为key:value对，其中： - 标签名（key值）须存在于实例中； - 标签内容（value值）为自定义标签值。 

        :return: The tags of this RunModifyPictureReq.
        :rtype: object
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this RunModifyPictureReq.

        自定义标签，格式为key:value对，其中： - 标签名（key值）须存在于实例中； - 标签内容（value值）为自定义标签值。 

        :param tags: The tags of this RunModifyPictureReq.
        :type tags: object
        """
        self._tags = tags

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
        if not isinstance(other, RunModifyPictureReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
