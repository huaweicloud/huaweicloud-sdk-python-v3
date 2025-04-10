# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductRequest:

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
        'description': 'str',
        'attributes': 'dict(str, ProductAttributes)',
        'tags': 'list[Attributes]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'attributes': 'attributes',
        'tags': 'tags'
    }

    def __init__(self, name=None, description=None, attributes=None, tags=None):
        r"""ProductRequest

        The model defined in huaweicloud sdk

        :param name: 产品名称，允许输入小写字母，数字，中划线，不能以中划线开头或结尾，最大长度为26位
        :type name: str
        :param description: 产品描述
        :type description: str
        :param attributes: 产品属性值
        :type attributes: dict(str, ProductAttributes)
        :param tags: 产品标签
        :type tags: list[:class:`huaweicloudsdkief.v1.Attributes`]
        """
        
        

        self._name = None
        self._description = None
        self._attributes = None
        self._tags = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if attributes is not None:
            self.attributes = attributes
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        r"""Gets the name of this ProductRequest.

        产品名称，允许输入小写字母，数字，中划线，不能以中划线开头或结尾，最大长度为26位

        :return: The name of this ProductRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ProductRequest.

        产品名称，允许输入小写字母，数字，中划线，不能以中划线开头或结尾，最大长度为26位

        :param name: The name of this ProductRequest.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ProductRequest.

        产品描述

        :return: The description of this ProductRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ProductRequest.

        产品描述

        :param description: The description of this ProductRequest.
        :type description: str
        """
        self._description = description

    @property
    def attributes(self):
        r"""Gets the attributes of this ProductRequest.

        产品属性值

        :return: The attributes of this ProductRequest.
        :rtype: dict(str, ProductAttributes)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        r"""Sets the attributes of this ProductRequest.

        产品属性值

        :param attributes: The attributes of this ProductRequest.
        :type attributes: dict(str, ProductAttributes)
        """
        self._attributes = attributes

    @property
    def tags(self):
        r"""Gets the tags of this ProductRequest.

        产品标签

        :return: The tags of this ProductRequest.
        :rtype: list[:class:`huaweicloudsdkief.v1.Attributes`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ProductRequest.

        产品标签

        :param tags: The tags of this ProductRequest.
        :type tags: list[:class:`huaweicloudsdkief.v1.Attributes`]
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
        if not isinstance(other, ProductRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
