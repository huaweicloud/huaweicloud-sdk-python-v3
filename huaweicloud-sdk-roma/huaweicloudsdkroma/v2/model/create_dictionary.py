# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDictionary:

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
        'code': 'str',
        'order': 'int',
        'extend_one': 'str',
        'extend_two': 'str',
        'parent_code': 'str'
    }

    attribute_map = {
        'name': 'name',
        'remark': 'remark',
        'code': 'code',
        'order': 'order',
        'extend_one': 'extend_one',
        'extend_two': 'extend_two',
        'parent_code': 'parent_code'
    }

    def __init__(self, name=None, remark=None, code=None, order=None, extend_one=None, extend_two=None, parent_code=None):
        """CreateDictionary

        The model defined in huaweicloud sdk

        :param name: 字典名称 - 字符集：中文、英文字母、数字、下划线和空格 - 约束：实例下唯一
        :type name: str
        :param remark: 字典描述
        :type remark: str
        :param code: 字典编码 - 字符集：英文字母、数字、下划线和空格 - 约束：实例下唯一
        :type code: str
        :param order: 字典排序，值越小顺序越靠前
        :type order: int
        :param extend_one: 字典扩展字段1 - 字符集：中文、英文字母、数字、下划线和空格
        :type extend_one: str
        :param extend_two: 字典扩展字段2 - 字符集：中文、英文字母、数字、下划线和空格
        :type extend_two: str
        :param parent_code: 父字典编码,为空时代表自身就是最顶级字典
        :type parent_code: str
        """
        
        

        self._name = None
        self._remark = None
        self._code = None
        self._order = None
        self._extend_one = None
        self._extend_two = None
        self._parent_code = None
        self.discriminator = None

        self.name = name
        if remark is not None:
            self.remark = remark
        self.code = code
        if order is not None:
            self.order = order
        if extend_one is not None:
            self.extend_one = extend_one
        if extend_two is not None:
            self.extend_two = extend_two
        if parent_code is not None:
            self.parent_code = parent_code

    @property
    def name(self):
        """Gets the name of this CreateDictionary.

        字典名称 - 字符集：中文、英文字母、数字、下划线和空格 - 约束：实例下唯一

        :return: The name of this CreateDictionary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateDictionary.

        字典名称 - 字符集：中文、英文字母、数字、下划线和空格 - 约束：实例下唯一

        :param name: The name of this CreateDictionary.
        :type name: str
        """
        self._name = name

    @property
    def remark(self):
        """Gets the remark of this CreateDictionary.

        字典描述

        :return: The remark of this CreateDictionary.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this CreateDictionary.

        字典描述

        :param remark: The remark of this CreateDictionary.
        :type remark: str
        """
        self._remark = remark

    @property
    def code(self):
        """Gets the code of this CreateDictionary.

        字典编码 - 字符集：英文字母、数字、下划线和空格 - 约束：实例下唯一

        :return: The code of this CreateDictionary.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CreateDictionary.

        字典编码 - 字符集：英文字母、数字、下划线和空格 - 约束：实例下唯一

        :param code: The code of this CreateDictionary.
        :type code: str
        """
        self._code = code

    @property
    def order(self):
        """Gets the order of this CreateDictionary.

        字典排序，值越小顺序越靠前

        :return: The order of this CreateDictionary.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this CreateDictionary.

        字典排序，值越小顺序越靠前

        :param order: The order of this CreateDictionary.
        :type order: int
        """
        self._order = order

    @property
    def extend_one(self):
        """Gets the extend_one of this CreateDictionary.

        字典扩展字段1 - 字符集：中文、英文字母、数字、下划线和空格

        :return: The extend_one of this CreateDictionary.
        :rtype: str
        """
        return self._extend_one

    @extend_one.setter
    def extend_one(self, extend_one):
        """Sets the extend_one of this CreateDictionary.

        字典扩展字段1 - 字符集：中文、英文字母、数字、下划线和空格

        :param extend_one: The extend_one of this CreateDictionary.
        :type extend_one: str
        """
        self._extend_one = extend_one

    @property
    def extend_two(self):
        """Gets the extend_two of this CreateDictionary.

        字典扩展字段2 - 字符集：中文、英文字母、数字、下划线和空格

        :return: The extend_two of this CreateDictionary.
        :rtype: str
        """
        return self._extend_two

    @extend_two.setter
    def extend_two(self, extend_two):
        """Sets the extend_two of this CreateDictionary.

        字典扩展字段2 - 字符集：中文、英文字母、数字、下划线和空格

        :param extend_two: The extend_two of this CreateDictionary.
        :type extend_two: str
        """
        self._extend_two = extend_two

    @property
    def parent_code(self):
        """Gets the parent_code of this CreateDictionary.

        父字典编码,为空时代表自身就是最顶级字典

        :return: The parent_code of this CreateDictionary.
        :rtype: str
        """
        return self._parent_code

    @parent_code.setter
    def parent_code(self, parent_code):
        """Sets the parent_code of this CreateDictionary.

        父字典编码,为空时代表自身就是最顶级字典

        :param parent_code: The parent_code of this CreateDictionary.
        :type parent_code: str
        """
        self._parent_code = parent_code

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
        if not isinstance(other, CreateDictionary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
