# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchRestInfoImageInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'box': 'str',
        'category': 'int',
        'category_name': 'str',
        'objects': 'list[AddDataRestInfoImageInfoObjects]'
    }

    attribute_map = {
        'box': 'box',
        'category': 'category',
        'category_name': 'category_name',
        'objects': 'objects'
    }

    def __init__(self, box=None, category=None, category_name=None, objects=None):
        r"""SearchRestInfoImageInfo

        The model defined in huaweicloud sdk

        :param box: 用于搜索的主体目标框。
        :type box: str
        :param category: 用于搜索的主体类目序号。
        :type category: int
        :param category_name: 用于搜索的主体类目名称。
        :type category_name: str
        :param objects: 搜索图像中的所有主体列表。
        :type objects: list[:class:`huaweicloudsdkimagesearch.v2.AddDataRestInfoImageInfoObjects`]
        """
        
        

        self._box = None
        self._category = None
        self._category_name = None
        self._objects = None
        self.discriminator = None

        if box is not None:
            self.box = box
        if category is not None:
            self.category = category
        if category_name is not None:
            self.category_name = category_name
        if objects is not None:
            self.objects = objects

    @property
    def box(self):
        r"""Gets the box of this SearchRestInfoImageInfo.

        用于搜索的主体目标框。

        :return: The box of this SearchRestInfoImageInfo.
        :rtype: str
        """
        return self._box

    @box.setter
    def box(self, box):
        r"""Sets the box of this SearchRestInfoImageInfo.

        用于搜索的主体目标框。

        :param box: The box of this SearchRestInfoImageInfo.
        :type box: str
        """
        self._box = box

    @property
    def category(self):
        r"""Gets the category of this SearchRestInfoImageInfo.

        用于搜索的主体类目序号。

        :return: The category of this SearchRestInfoImageInfo.
        :rtype: int
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this SearchRestInfoImageInfo.

        用于搜索的主体类目序号。

        :param category: The category of this SearchRestInfoImageInfo.
        :type category: int
        """
        self._category = category

    @property
    def category_name(self):
        r"""Gets the category_name of this SearchRestInfoImageInfo.

        用于搜索的主体类目名称。

        :return: The category_name of this SearchRestInfoImageInfo.
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        r"""Sets the category_name of this SearchRestInfoImageInfo.

        用于搜索的主体类目名称。

        :param category_name: The category_name of this SearchRestInfoImageInfo.
        :type category_name: str
        """
        self._category_name = category_name

    @property
    def objects(self):
        r"""Gets the objects of this SearchRestInfoImageInfo.

        搜索图像中的所有主体列表。

        :return: The objects of this SearchRestInfoImageInfo.
        :rtype: list[:class:`huaweicloudsdkimagesearch.v2.AddDataRestInfoImageInfoObjects`]
        """
        return self._objects

    @objects.setter
    def objects(self, objects):
        r"""Sets the objects of this SearchRestInfoImageInfo.

        搜索图像中的所有主体列表。

        :param objects: The objects of this SearchRestInfoImageInfo.
        :type objects: list[:class:`huaweicloudsdkimagesearch.v2.AddDataRestInfoImageInfoObjects`]
        """
        self._objects = objects

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
        if not isinstance(other, SearchRestInfoImageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
