# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CategoryDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'name_zh': 'str',
        'name_en': 'str',
        'sub_categories': 'list[CategoryDto]'
    }

    attribute_map = {
        'key': 'key',
        'name_zh': 'name_zh',
        'name_en': 'name_en',
        'sub_categories': 'sub_categories'
    }

    def __init__(self, key=None, name_zh=None, name_en=None, sub_categories=None):
        r"""CategoryDto

        The model defined in huaweicloud sdk

        :param key: **参数解释：** 检视意见分类key。
        :type key: str
        :param name_zh: **参数解释：** 检视意见分类中文名。
        :type name_zh: str
        :param name_en: **参数解释：** 检视意见分类英文名。
        :type name_en: str
        :param sub_categories: **参数解释：** 子检视意见分类。
        :type sub_categories: list[:class:`huaweicloudsdkcodehub.v4.CategoryDto`]
        """
        
        

        self._key = None
        self._name_zh = None
        self._name_en = None
        self._sub_categories = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if name_zh is not None:
            self.name_zh = name_zh
        if name_en is not None:
            self.name_en = name_en
        if sub_categories is not None:
            self.sub_categories = sub_categories

    @property
    def key(self):
        r"""Gets the key of this CategoryDto.

        **参数解释：** 检视意见分类key。

        :return: The key of this CategoryDto.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this CategoryDto.

        **参数解释：** 检视意见分类key。

        :param key: The key of this CategoryDto.
        :type key: str
        """
        self._key = key

    @property
    def name_zh(self):
        r"""Gets the name_zh of this CategoryDto.

        **参数解释：** 检视意见分类中文名。

        :return: The name_zh of this CategoryDto.
        :rtype: str
        """
        return self._name_zh

    @name_zh.setter
    def name_zh(self, name_zh):
        r"""Sets the name_zh of this CategoryDto.

        **参数解释：** 检视意见分类中文名。

        :param name_zh: The name_zh of this CategoryDto.
        :type name_zh: str
        """
        self._name_zh = name_zh

    @property
    def name_en(self):
        r"""Gets the name_en of this CategoryDto.

        **参数解释：** 检视意见分类英文名。

        :return: The name_en of this CategoryDto.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        r"""Sets the name_en of this CategoryDto.

        **参数解释：** 检视意见分类英文名。

        :param name_en: The name_en of this CategoryDto.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def sub_categories(self):
        r"""Gets the sub_categories of this CategoryDto.

        **参数解释：** 子检视意见分类。

        :return: The sub_categories of this CategoryDto.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.CategoryDto`]
        """
        return self._sub_categories

    @sub_categories.setter
    def sub_categories(self, sub_categories):
        r"""Sets the sub_categories of this CategoryDto.

        **参数解释：** 子检视意见分类。

        :param sub_categories: The sub_categories of this CategoryDto.
        :type sub_categories: list[:class:`huaweicloudsdkcodehub.v4.CategoryDto`]
        """
        self._sub_categories = sub_categories

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
        if not isinstance(other, CategoryDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
