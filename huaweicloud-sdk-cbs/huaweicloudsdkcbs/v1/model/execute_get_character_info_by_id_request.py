# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteGetCharacterInfoByIdRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'character_id': 'str'
    }

    attribute_map = {
        'character_id': 'character_id'
    }

    def __init__(self, character_id=None):
        r"""ExecuteGetCharacterInfoByIdRequest

        The model defined in huaweicloud sdk

        :param character_id: 形象id
        :type character_id: str
        """
        
        

        self._character_id = None
        self.discriminator = None

        self.character_id = character_id

    @property
    def character_id(self):
        r"""Gets the character_id of this ExecuteGetCharacterInfoByIdRequest.

        形象id

        :return: The character_id of this ExecuteGetCharacterInfoByIdRequest.
        :rtype: str
        """
        return self._character_id

    @character_id.setter
    def character_id(self, character_id):
        r"""Sets the character_id of this ExecuteGetCharacterInfoByIdRequest.

        形象id

        :param character_id: The character_id of this ExecuteGetCharacterInfoByIdRequest.
        :type character_id: str
        """
        self._character_id = character_id

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
        if not isinstance(other, ExecuteGetCharacterInfoByIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
