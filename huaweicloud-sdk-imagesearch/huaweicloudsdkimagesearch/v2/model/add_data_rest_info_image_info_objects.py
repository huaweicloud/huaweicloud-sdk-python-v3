# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddDataRestInfoImageInfoObjects:

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
        'category_name': 'str'
    }

    attribute_map = {
        'box': 'box',
        'category': 'category',
        'category_name': 'category_name'
    }

    def __init__(self, box=None, category=None, category_name=None):
        """AddDataRestInfoImageInfoObjects

        The model defined in huaweicloud sdk

        :param box: 主体目标框。
        :type box: str
        :param category: 主体类目序号。
        :type category: int
        :param category_name: 主体类目名称。
        :type category_name: str
        """
        
        

        self._box = None
        self._category = None
        self._category_name = None
        self.discriminator = None

        if box is not None:
            self.box = box
        if category is not None:
            self.category = category
        if category_name is not None:
            self.category_name = category_name

    @property
    def box(self):
        """Gets the box of this AddDataRestInfoImageInfoObjects.

        主体目标框。

        :return: The box of this AddDataRestInfoImageInfoObjects.
        :rtype: str
        """
        return self._box

    @box.setter
    def box(self, box):
        """Sets the box of this AddDataRestInfoImageInfoObjects.

        主体目标框。

        :param box: The box of this AddDataRestInfoImageInfoObjects.
        :type box: str
        """
        self._box = box

    @property
    def category(self):
        """Gets the category of this AddDataRestInfoImageInfoObjects.

        主体类目序号。

        :return: The category of this AddDataRestInfoImageInfoObjects.
        :rtype: int
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this AddDataRestInfoImageInfoObjects.

        主体类目序号。

        :param category: The category of this AddDataRestInfoImageInfoObjects.
        :type category: int
        """
        self._category = category

    @property
    def category_name(self):
        """Gets the category_name of this AddDataRestInfoImageInfoObjects.

        主体类目名称。

        :return: The category_name of this AddDataRestInfoImageInfoObjects.
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """Sets the category_name of this AddDataRestInfoImageInfoObjects.

        主体类目名称。

        :param category_name: The category_name of this AddDataRestInfoImageInfoObjects.
        :type category_name: str
        """
        self._category_name = category_name

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
        if not isinstance(other, AddDataRestInfoImageInfoObjects):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
