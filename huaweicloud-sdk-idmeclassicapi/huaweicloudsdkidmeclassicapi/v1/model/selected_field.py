# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SelectedField:

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
        'name_as': 'str'
    }

    attribute_map = {
        'name': 'name',
        'name_as': 'nameAs'
    }

    def __init__(self, name=None, name_as=None):
        r"""SelectedField

        The model defined in huaweicloud sdk

        :param name: **参数解释：**  字段名称，如果是子参考对象的属性，则为“参考对象.属性名称”，例如：“master.name”。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type name: str
        :param name_as: **参数解释：**  字段别名。如果不填，默认使用name参数的值。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type name_as: str
        """
        
        

        self._name = None
        self._name_as = None
        self.discriminator = None

        self.name = name
        if name_as is not None:
            self.name_as = name_as

    @property
    def name(self):
        r"""Gets the name of this SelectedField.

        **参数解释：**  字段名称，如果是子参考对象的属性，则为“参考对象.属性名称”，例如：“master.name”。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The name of this SelectedField.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SelectedField.

        **参数解释：**  字段名称，如果是子参考对象的属性，则为“参考对象.属性名称”，例如：“master.name”。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param name: The name of this SelectedField.
        :type name: str
        """
        self._name = name

    @property
    def name_as(self):
        r"""Gets the name_as of this SelectedField.

        **参数解释：**  字段别名。如果不填，默认使用name参数的值。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The name_as of this SelectedField.
        :rtype: str
        """
        return self._name_as

    @name_as.setter
    def name_as(self, name_as):
        r"""Sets the name_as of this SelectedField.

        **参数解释：**  字段别名。如果不填，默认使用name参数的值。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param name_as: The name_as of this SelectedField.
        :type name_as: str
        """
        self._name_as = name_as

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
        if not isinstance(other, SelectedField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
