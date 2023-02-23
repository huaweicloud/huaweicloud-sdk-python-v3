# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchPictureItem:

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
        'sim': 'float',
        'tags': 'object'
    }

    attribute_map = {
        'path': 'path',
        'sim': 'sim',
        'tags': 'tags'
    }

    def __init__(self, path=None, sim=None, tags=None):
        """SearchPictureItem

        The model defined in huaweicloud sdk

        :param path: 被搜索图片的路径。
        :type path: str
        :param sim: 查询图片和被搜索图片的相似度，值越接近1表示越相似。
        :type sim: float
        :param tags: 自定义的标签名称和标签内容。
        :type tags: object
        """
        
        

        self._path = None
        self._sim = None
        self._tags = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if sim is not None:
            self.sim = sim
        if tags is not None:
            self.tags = tags

    @property
    def path(self):
        """Gets the path of this SearchPictureItem.

        被搜索图片的路径。

        :return: The path of this SearchPictureItem.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this SearchPictureItem.

        被搜索图片的路径。

        :param path: The path of this SearchPictureItem.
        :type path: str
        """
        self._path = path

    @property
    def sim(self):
        """Gets the sim of this SearchPictureItem.

        查询图片和被搜索图片的相似度，值越接近1表示越相似。

        :return: The sim of this SearchPictureItem.
        :rtype: float
        """
        return self._sim

    @sim.setter
    def sim(self, sim):
        """Sets the sim of this SearchPictureItem.

        查询图片和被搜索图片的相似度，值越接近1表示越相似。

        :param sim: The sim of this SearchPictureItem.
        :type sim: float
        """
        self._sim = sim

    @property
    def tags(self):
        """Gets the tags of this SearchPictureItem.

        自定义的标签名称和标签内容。

        :return: The tags of this SearchPictureItem.
        :rtype: object
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SearchPictureItem.

        自定义的标签名称和标签内容。

        :param tags: The tags of this SearchPictureItem.
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
        if not isinstance(other, SearchPictureItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
