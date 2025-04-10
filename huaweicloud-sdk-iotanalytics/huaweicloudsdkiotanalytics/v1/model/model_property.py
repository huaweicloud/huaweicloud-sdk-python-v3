# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelProperty:

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
        'type': 'str',
        'description': 'str',
        'unit': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'unit': 'unit'
    }

    def __init__(self, name=None, type=None, description=None, unit=None):
        r"""ModelProperty

        The model defined in huaweicloud sdk

        :param name: 属性名称
        :type name: str
        :param type: 属性值类型
        :type type: str
        :param description: 属性描述
        :type description: str
        :param unit: 属性单位
        :type unit: str
        """
        
        

        self._name = None
        self._type = None
        self._description = None
        self._unit = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if unit is not None:
            self.unit = unit

    @property
    def name(self):
        r"""Gets the name of this ModelProperty.

        属性名称

        :return: The name of this ModelProperty.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ModelProperty.

        属性名称

        :param name: The name of this ModelProperty.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this ModelProperty.

        属性值类型

        :return: The type of this ModelProperty.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ModelProperty.

        属性值类型

        :param type: The type of this ModelProperty.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this ModelProperty.

        属性描述

        :return: The description of this ModelProperty.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ModelProperty.

        属性描述

        :param description: The description of this ModelProperty.
        :type description: str
        """
        self._description = description

    @property
    def unit(self):
        r"""Gets the unit of this ModelProperty.

        属性单位

        :return: The unit of this ModelProperty.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this ModelProperty.

        属性单位

        :param unit: The unit of this ModelProperty.
        :type unit: str
        """
        self._unit = unit

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
        if not isinstance(other, ModelProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
