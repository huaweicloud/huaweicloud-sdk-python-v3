# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PersistObjectIdsDecryptDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'decrypt': 'bool',
        'ids': 'list[str]'
    }

    attribute_map = {
        'decrypt': 'decrypt',
        'ids': 'ids'
    }

    def __init__(self, decrypt=None, ids=None):
        r"""PersistObjectIdsDecryptDTO

        The model defined in huaweicloud sdk

        :param decrypt: **参数解释：**  是否加密。  **约束限制：**  不涉及。  **取值范围：**  - true：加密。 - false：不加密。  **默认取值：**  false。 
        :type decrypt: bool
        :param ids: **参数解释：**  ID列表。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type ids: list[str]
        """
        
        

        self._decrypt = None
        self._ids = None
        self.discriminator = None

        if decrypt is not None:
            self.decrypt = decrypt
        self.ids = ids

    @property
    def decrypt(self):
        r"""Gets the decrypt of this PersistObjectIdsDecryptDTO.

        **参数解释：**  是否加密。  **约束限制：**  不涉及。  **取值范围：**  - true：加密。 - false：不加密。  **默认取值：**  false。 

        :return: The decrypt of this PersistObjectIdsDecryptDTO.
        :rtype: bool
        """
        return self._decrypt

    @decrypt.setter
    def decrypt(self, decrypt):
        r"""Sets the decrypt of this PersistObjectIdsDecryptDTO.

        **参数解释：**  是否加密。  **约束限制：**  不涉及。  **取值范围：**  - true：加密。 - false：不加密。  **默认取值：**  false。 

        :param decrypt: The decrypt of this PersistObjectIdsDecryptDTO.
        :type decrypt: bool
        """
        self._decrypt = decrypt

    @property
    def ids(self):
        r"""Gets the ids of this PersistObjectIdsDecryptDTO.

        **参数解释：**  ID列表。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The ids of this PersistObjectIdsDecryptDTO.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this PersistObjectIdsDecryptDTO.

        **参数解释：**  ID列表。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param ids: The ids of this PersistObjectIdsDecryptDTO.
        :type ids: list[str]
        """
        self._ids = ids

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
        if not isinstance(other, PersistObjectIdsDecryptDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
