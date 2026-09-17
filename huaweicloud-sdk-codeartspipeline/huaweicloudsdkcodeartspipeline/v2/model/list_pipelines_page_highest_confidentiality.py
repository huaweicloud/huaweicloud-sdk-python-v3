# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPipelinesPageHighestConfidentiality:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'code': 'str',
        'reserve_1': 'str',
        'value': 'str',
        'value_en': 'str',
        'sequence': 'int'
    }

    attribute_map = {
        'id': 'id',
        'code': 'code',
        'reserve_1': 'reserve_1',
        'value': 'value',
        'value_en': 'value_en',
        'sequence': 'sequence'
    }

    def __init__(self, id=None, code=None, reserve_1=None, value=None, value_en=None, sequence=None):
        r"""ListPipelinesPageHighestConfidentiality

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 密级ID。 **取值范围**： 不涉及。 
        :type id: str
        :param code: **参数解释**： 密级等级逻辑ID。 **取值范围**： 不涉及。 
        :type code: str
        :param reserve_1: **参数解释**： 预留字段。 **取值范围**： 不涉及。 
        :type reserve_1: str
        :param value: **参数解释**： 密级等级中文名。 **取值范围**： 不涉及。 
        :type value: str
        :param value_en: **参数解释**： 密级等级英文名。 **取值范围**： 不涉及。 
        :type value_en: str
        :param sequence: **参数解释**： 密级等级序号，密级越高数字越大。 **取值范围**： 正整数。 
        :type sequence: int
        """
        
        

        self._id = None
        self._code = None
        self._reserve_1 = None
        self._value = None
        self._value_en = None
        self._sequence = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if code is not None:
            self.code = code
        if reserve_1 is not None:
            self.reserve_1 = reserve_1
        if value is not None:
            self.value = value
        if value_en is not None:
            self.value_en = value_en
        if sequence is not None:
            self.sequence = sequence

    @property
    def id(self):
        r"""Gets the id of this ListPipelinesPageHighestConfidentiality.

        **参数解释**： 密级ID。 **取值范围**： 不涉及。 

        :return: The id of this ListPipelinesPageHighestConfidentiality.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListPipelinesPageHighestConfidentiality.

        **参数解释**： 密级ID。 **取值范围**： 不涉及。 

        :param id: The id of this ListPipelinesPageHighestConfidentiality.
        :type id: str
        """
        self._id = id

    @property
    def code(self):
        r"""Gets the code of this ListPipelinesPageHighestConfidentiality.

        **参数解释**： 密级等级逻辑ID。 **取值范围**： 不涉及。 

        :return: The code of this ListPipelinesPageHighestConfidentiality.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ListPipelinesPageHighestConfidentiality.

        **参数解释**： 密级等级逻辑ID。 **取值范围**： 不涉及。 

        :param code: The code of this ListPipelinesPageHighestConfidentiality.
        :type code: str
        """
        self._code = code

    @property
    def reserve_1(self):
        r"""Gets the reserve_1 of this ListPipelinesPageHighestConfidentiality.

        **参数解释**： 预留字段。 **取值范围**： 不涉及。 

        :return: The reserve_1 of this ListPipelinesPageHighestConfidentiality.
        :rtype: str
        """
        return self._reserve_1

    @reserve_1.setter
    def reserve_1(self, reserve_1):
        r"""Sets the reserve_1 of this ListPipelinesPageHighestConfidentiality.

        **参数解释**： 预留字段。 **取值范围**： 不涉及。 

        :param reserve_1: The reserve_1 of this ListPipelinesPageHighestConfidentiality.
        :type reserve_1: str
        """
        self._reserve_1 = reserve_1

    @property
    def value(self):
        r"""Gets the value of this ListPipelinesPageHighestConfidentiality.

        **参数解释**： 密级等级中文名。 **取值范围**： 不涉及。 

        :return: The value of this ListPipelinesPageHighestConfidentiality.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ListPipelinesPageHighestConfidentiality.

        **参数解释**： 密级等级中文名。 **取值范围**： 不涉及。 

        :param value: The value of this ListPipelinesPageHighestConfidentiality.
        :type value: str
        """
        self._value = value

    @property
    def value_en(self):
        r"""Gets the value_en of this ListPipelinesPageHighestConfidentiality.

        **参数解释**： 密级等级英文名。 **取值范围**： 不涉及。 

        :return: The value_en of this ListPipelinesPageHighestConfidentiality.
        :rtype: str
        """
        return self._value_en

    @value_en.setter
    def value_en(self, value_en):
        r"""Sets the value_en of this ListPipelinesPageHighestConfidentiality.

        **参数解释**： 密级等级英文名。 **取值范围**： 不涉及。 

        :param value_en: The value_en of this ListPipelinesPageHighestConfidentiality.
        :type value_en: str
        """
        self._value_en = value_en

    @property
    def sequence(self):
        r"""Gets the sequence of this ListPipelinesPageHighestConfidentiality.

        **参数解释**： 密级等级序号，密级越高数字越大。 **取值范围**： 正整数。 

        :return: The sequence of this ListPipelinesPageHighestConfidentiality.
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        r"""Sets the sequence of this ListPipelinesPageHighestConfidentiality.

        **参数解释**： 密级等级序号，密级越高数字越大。 **取值范围**： 正整数。 

        :param sequence: The sequence of this ListPipelinesPageHighestConfidentiality.
        :type sequence: int
        """
        self._sequence = sequence

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
        if not isinstance(other, ListPipelinesPageHighestConfidentiality):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
