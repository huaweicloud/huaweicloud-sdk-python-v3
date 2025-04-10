# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TagOperationDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_id': 'str',
        'tag_id': 'str',
        'modifier': 'str'
    }

    attribute_map = {
        'object_id': 'objectId',
        'tag_id': 'tagId',
        'modifier': 'modifier'
    }

    def __init__(self, object_id=None, tag_id=None, modifier=None):
        r"""TagOperationDTO

        The model defined in huaweicloud sdk

        :param object_id: **参数解释：**  数据实例ID。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type object_id: str
        :param tag_id: **参数解释：**  标签ID。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 
        :type tag_id: str
        :param modifier: **参数解释：**  修改人。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type modifier: str
        """
        
        

        self._object_id = None
        self._tag_id = None
        self._modifier = None
        self.discriminator = None

        self.object_id = object_id
        self.tag_id = tag_id
        if modifier is not None:
            self.modifier = modifier

    @property
    def object_id(self):
        r"""Gets the object_id of this TagOperationDTO.

        **参数解释：**  数据实例ID。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The object_id of this TagOperationDTO.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this TagOperationDTO.

        **参数解释：**  数据实例ID。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param object_id: The object_id of this TagOperationDTO.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def tag_id(self):
        r"""Gets the tag_id of this TagOperationDTO.

        **参数解释：**  标签ID。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 

        :return: The tag_id of this TagOperationDTO.
        :rtype: str
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        r"""Sets the tag_id of this TagOperationDTO.

        **参数解释：**  标签ID。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 

        :param tag_id: The tag_id of this TagOperationDTO.
        :type tag_id: str
        """
        self._tag_id = tag_id

    @property
    def modifier(self):
        r"""Gets the modifier of this TagOperationDTO.

        **参数解释：**  修改人。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The modifier of this TagOperationDTO.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        r"""Sets the modifier of this TagOperationDTO.

        **参数解释：**  修改人。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param modifier: The modifier of this TagOperationDTO.
        :type modifier: str
        """
        self._modifier = modifier

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
        if not isinstance(other, TagOperationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
