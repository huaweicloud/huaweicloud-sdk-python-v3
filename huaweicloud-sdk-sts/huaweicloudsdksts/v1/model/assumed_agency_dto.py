# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssumedAgencyDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'urn': 'str',
        'id': 'str'
    }

    attribute_map = {
        'urn': 'urn',
        'id': 'id'
    }

    def __init__(self, urn=None, id=None):
        r"""AssumedAgencyDto

        The model defined in huaweicloud sdk

        :param urn: **参数解释**： 委托会话或信任委托会话的URN。  **取值范围**： 不涉及。 
        :type urn: str
        :param id: **参数解释**： 委托会话或信任委托会话的唯一标识，包含了委托ID和委托会话名称信息。  **取值范围**： 不涉及。 
        :type id: str
        """
        
        

        self._urn = None
        self._id = None
        self.discriminator = None

        self.urn = urn
        self.id = id

    @property
    def urn(self):
        r"""Gets the urn of this AssumedAgencyDto.

        **参数解释**： 委托会话或信任委托会话的URN。  **取值范围**： 不涉及。 

        :return: The urn of this AssumedAgencyDto.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        r"""Sets the urn of this AssumedAgencyDto.

        **参数解释**： 委托会话或信任委托会话的URN。  **取值范围**： 不涉及。 

        :param urn: The urn of this AssumedAgencyDto.
        :type urn: str
        """
        self._urn = urn

    @property
    def id(self):
        r"""Gets the id of this AssumedAgencyDto.

        **参数解释**： 委托会话或信任委托会话的唯一标识，包含了委托ID和委托会话名称信息。  **取值范围**： 不涉及。 

        :return: The id of this AssumedAgencyDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AssumedAgencyDto.

        **参数解释**： 委托会话或信任委托会话的唯一标识，包含了委托ID和委托会话名称信息。  **取值范围**： 不涉及。 

        :param id: The id of this AssumedAgencyDto.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, AssumedAgencyDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
