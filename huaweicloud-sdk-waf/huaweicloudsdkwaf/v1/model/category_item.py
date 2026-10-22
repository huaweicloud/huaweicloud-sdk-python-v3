# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CategoryItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'name': 'str',
        'subcategories': 'list[SubcategoryItem]'
    }

    attribute_map = {
        'category': 'category',
        'name': 'name',
        'subcategories': 'subcategories'
    }

    def __init__(self, category=None, name=None, subcategories=None):
        r"""CategoryItem

        The model defined in huaweicloud sdk

        :param category: 分类标识
        :type category: str
        :param name: 分类名称
        :type name: str
        :param subcategories: 子分类列表
        :type subcategories: list[:class:`huaweicloudsdkwaf.v1.SubcategoryItem`]
        """
        
        

        self._category = None
        self._name = None
        self._subcategories = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if name is not None:
            self.name = name
        if subcategories is not None:
            self.subcategories = subcategories

    @property
    def category(self):
        r"""Gets the category of this CategoryItem.

        分类标识

        :return: The category of this CategoryItem.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this CategoryItem.

        分类标识

        :param category: The category of this CategoryItem.
        :type category: str
        """
        self._category = category

    @property
    def name(self):
        r"""Gets the name of this CategoryItem.

        分类名称

        :return: The name of this CategoryItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CategoryItem.

        分类名称

        :param name: The name of this CategoryItem.
        :type name: str
        """
        self._name = name

    @property
    def subcategories(self):
        r"""Gets the subcategories of this CategoryItem.

        子分类列表

        :return: The subcategories of this CategoryItem.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.SubcategoryItem`]
        """
        return self._subcategories

    @subcategories.setter
    def subcategories(self, subcategories):
        r"""Sets the subcategories of this CategoryItem.

        子分类列表

        :param subcategories: The subcategories of this CategoryItem.
        :type subcategories: list[:class:`huaweicloudsdkwaf.v1.SubcategoryItem`]
        """
        self._subcategories = subcategories

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
        if not isinstance(other, CategoryItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
