# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DecServiceFlavorItemDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type_code': 'str',
        'code': 'str'
    }

    attribute_map = {
        'type_code': 'type_code',
        'code': 'code'
    }

    def __init__(self, type_code=None, code=None):
        r"""DecServiceFlavorItemDetail

        The model defined in huaweicloud sdk

        :param type_code: **参数解释**: 类型编码。 **取值范围**: 不涉及。
        :type type_code: str
        :param code: **参数解释**: 规格编码。 **取值范围**: 不涉及。
        :type code: str
        """
        
        

        self._type_code = None
        self._code = None
        self.discriminator = None

        if type_code is not None:
            self.type_code = type_code
        if code is not None:
            self.code = code

    @property
    def type_code(self):
        r"""Gets the type_code of this DecServiceFlavorItemDetail.

        **参数解释**: 类型编码。 **取值范围**: 不涉及。

        :return: The type_code of this DecServiceFlavorItemDetail.
        :rtype: str
        """
        return self._type_code

    @type_code.setter
    def type_code(self, type_code):
        r"""Sets the type_code of this DecServiceFlavorItemDetail.

        **参数解释**: 类型编码。 **取值范围**: 不涉及。

        :param type_code: The type_code of this DecServiceFlavorItemDetail.
        :type type_code: str
        """
        self._type_code = type_code

    @property
    def code(self):
        r"""Gets the code of this DecServiceFlavorItemDetail.

        **参数解释**: 规格编码。 **取值范围**: 不涉及。

        :return: The code of this DecServiceFlavorItemDetail.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this DecServiceFlavorItemDetail.

        **参数解释**: 规格编码。 **取值范围**: 不涉及。

        :param code: The code of this DecServiceFlavorItemDetail.
        :type code: str
        """
        self._code = code

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
        if not isinstance(other, DecServiceFlavorItemDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
