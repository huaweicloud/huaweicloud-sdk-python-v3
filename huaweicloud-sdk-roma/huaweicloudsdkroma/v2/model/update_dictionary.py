# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDictionary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'remark': 'str',
        'order': 'int',
        'extend_one': 'str',
        'extend_two': 'str'
    }

    attribute_map = {
        'name': 'name',
        'remark': 'remark',
        'order': 'order',
        'extend_one': 'extend_one',
        'extend_two': 'extend_two'
    }

    def __init__(self, name=None, remark=None, order=None, extend_one=None, extend_two=None):
        r"""UpdateDictionary

        The model defined in huaweicloud sdk

        :param name: 字典名称 - 字符集：中文、英文字母、数字、下划线和空格 - 约束：实例下唯一
        :type name: str
        :param remark: 字典描述
        :type remark: str
        :param order: 字典排序，值越小顺序越靠前
        :type order: int
        :param extend_one: 字典扩展字段1 - 字符集：中文、英文字母、数字、下划线和空格
        :type extend_one: str
        :param extend_two: 字典扩展字段2 - 字符集：中文、英文字母、数字、下划线和空格
        :type extend_two: str
        """
        
        

        self._name = None
        self._remark = None
        self._order = None
        self._extend_one = None
        self._extend_two = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if remark is not None:
            self.remark = remark
        if order is not None:
            self.order = order
        if extend_one is not None:
            self.extend_one = extend_one
        if extend_two is not None:
            self.extend_two = extend_two

    @property
    def name(self):
        r"""Gets the name of this UpdateDictionary.

        字典名称 - 字符集：中文、英文字母、数字、下划线和空格 - 约束：实例下唯一

        :return: The name of this UpdateDictionary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateDictionary.

        字典名称 - 字符集：中文、英文字母、数字、下划线和空格 - 约束：实例下唯一

        :param name: The name of this UpdateDictionary.
        :type name: str
        """
        self._name = name

    @property
    def remark(self):
        r"""Gets the remark of this UpdateDictionary.

        字典描述

        :return: The remark of this UpdateDictionary.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this UpdateDictionary.

        字典描述

        :param remark: The remark of this UpdateDictionary.
        :type remark: str
        """
        self._remark = remark

    @property
    def order(self):
        r"""Gets the order of this UpdateDictionary.

        字典排序，值越小顺序越靠前

        :return: The order of this UpdateDictionary.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this UpdateDictionary.

        字典排序，值越小顺序越靠前

        :param order: The order of this UpdateDictionary.
        :type order: int
        """
        self._order = order

    @property
    def extend_one(self):
        r"""Gets the extend_one of this UpdateDictionary.

        字典扩展字段1 - 字符集：中文、英文字母、数字、下划线和空格

        :return: The extend_one of this UpdateDictionary.
        :rtype: str
        """
        return self._extend_one

    @extend_one.setter
    def extend_one(self, extend_one):
        r"""Sets the extend_one of this UpdateDictionary.

        字典扩展字段1 - 字符集：中文、英文字母、数字、下划线和空格

        :param extend_one: The extend_one of this UpdateDictionary.
        :type extend_one: str
        """
        self._extend_one = extend_one

    @property
    def extend_two(self):
        r"""Gets the extend_two of this UpdateDictionary.

        字典扩展字段2 - 字符集：中文、英文字母、数字、下划线和空格

        :return: The extend_two of this UpdateDictionary.
        :rtype: str
        """
        return self._extend_two

    @extend_two.setter
    def extend_two(self, extend_two):
        r"""Sets the extend_two of this UpdateDictionary.

        字典扩展字段2 - 字符集：中文、英文字母、数字、下划线和空格

        :param extend_two: The extend_two of this UpdateDictionary.
        :type extend_two: str
        """
        self._extend_two = extend_two

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
        if not isinstance(other, UpdateDictionary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
