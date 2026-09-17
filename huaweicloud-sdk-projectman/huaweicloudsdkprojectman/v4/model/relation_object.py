# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RelationObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_type': 'str',
        'categories': 'list[str]'
    }

    attribute_map = {
        'object_type': 'object_type',
        'categories': 'categories'
    }

    def __init__(self, object_type=None, categories=None):
        r"""RelationObject

        The model defined in huaweicloud sdk

        :param object_type: **参数解释**： 实体的种类。 **取值范围**： 不涉及。
        :type object_type: str
        :param categories: **参数解释**： 类型列表。 **取值范围**： 不涉及。
        :type categories: list[str]
        """
        
        

        self._object_type = None
        self._categories = None
        self.discriminator = None

        if object_type is not None:
            self.object_type = object_type
        if categories is not None:
            self.categories = categories

    @property
    def object_type(self):
        r"""Gets the object_type of this RelationObject.

        **参数解释**： 实体的种类。 **取值范围**： 不涉及。

        :return: The object_type of this RelationObject.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        r"""Sets the object_type of this RelationObject.

        **参数解释**： 实体的种类。 **取值范围**： 不涉及。

        :param object_type: The object_type of this RelationObject.
        :type object_type: str
        """
        self._object_type = object_type

    @property
    def categories(self):
        r"""Gets the categories of this RelationObject.

        **参数解释**： 类型列表。 **取值范围**： 不涉及。

        :return: The categories of this RelationObject.
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        r"""Sets the categories of this RelationObject.

        **参数解释**： 类型列表。 **取值范围**： 不涉及。

        :param categories: The categories of this RelationObject.
        :type categories: list[str]
        """
        self._categories = categories

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
        if not isinstance(other, RelationObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
