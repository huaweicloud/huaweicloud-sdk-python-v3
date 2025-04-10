# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObjectReferenceViewDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'clazz': 'str',
        'id': 'str'
    }

    attribute_map = {
        'clazz': 'clazz',
        'id': 'id'
    }

    def __init__(self, clazz=None, id=None):
        r"""ObjectReferenceViewDTO

        The model defined in huaweicloud sdk

        :param clazz: **参数解释：**  类名。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type clazz: str
        :param id: **参数解释：**  唯一标识。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 
        :type id: str
        """
        
        

        self._clazz = None
        self._id = None
        self.discriminator = None

        if clazz is not None:
            self.clazz = clazz
        self.id = id

    @property
    def clazz(self):
        r"""Gets the clazz of this ObjectReferenceViewDTO.

        **参数解释：**  类名。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The clazz of this ObjectReferenceViewDTO.
        :rtype: str
        """
        return self._clazz

    @clazz.setter
    def clazz(self, clazz):
        r"""Sets the clazz of this ObjectReferenceViewDTO.

        **参数解释：**  类名。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param clazz: The clazz of this ObjectReferenceViewDTO.
        :type clazz: str
        """
        self._clazz = clazz

    @property
    def id(self):
        r"""Gets the id of this ObjectReferenceViewDTO.

        **参数解释：**  唯一标识。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 

        :return: The id of this ObjectReferenceViewDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ObjectReferenceViewDTO.

        **参数解释：**  唯一标识。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 

        :param id: The id of this ObjectReferenceViewDTO.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, ObjectReferenceViewDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
