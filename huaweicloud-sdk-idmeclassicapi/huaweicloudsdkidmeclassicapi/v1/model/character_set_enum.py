# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CharacterSetEnum:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cn_name': 'str',
        'code': 'str',
        'en_name': 'str'
    }

    attribute_map = {
        'cn_name': 'cnName',
        'code': 'code',
        'en_name': 'enName'
    }

    def __init__(self, cn_name=None, code=None, en_name=None):
        r"""CharacterSetEnum

        The model defined in huaweicloud sdk

        :param cn_name: **参数解释：**  中文名。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type cn_name: str
        :param code: **参数解释：**  编码。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type code: str
        :param en_name: **参数解释：**  英文名。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type en_name: str
        """
        
        

        self._cn_name = None
        self._code = None
        self._en_name = None
        self.discriminator = None

        if cn_name is not None:
            self.cn_name = cn_name
        if code is not None:
            self.code = code
        if en_name is not None:
            self.en_name = en_name

    @property
    def cn_name(self):
        r"""Gets the cn_name of this CharacterSetEnum.

        **参数解释：**  中文名。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The cn_name of this CharacterSetEnum.
        :rtype: str
        """
        return self._cn_name

    @cn_name.setter
    def cn_name(self, cn_name):
        r"""Sets the cn_name of this CharacterSetEnum.

        **参数解释：**  中文名。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param cn_name: The cn_name of this CharacterSetEnum.
        :type cn_name: str
        """
        self._cn_name = cn_name

    @property
    def code(self):
        r"""Gets the code of this CharacterSetEnum.

        **参数解释：**  编码。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The code of this CharacterSetEnum.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this CharacterSetEnum.

        **参数解释：**  编码。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param code: The code of this CharacterSetEnum.
        :type code: str
        """
        self._code = code

    @property
    def en_name(self):
        r"""Gets the en_name of this CharacterSetEnum.

        **参数解释：**  英文名。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The en_name of this CharacterSetEnum.
        :rtype: str
        """
        return self._en_name

    @en_name.setter
    def en_name(self, en_name):
        r"""Sets the en_name of this CharacterSetEnum.

        **参数解释：**  英文名。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param en_name: The en_name of this CharacterSetEnum.
        :type en_name: str
        """
        self._en_name = en_name

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
        if not isinstance(other, CharacterSetEnum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
