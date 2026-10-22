# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserTagDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'match_field': 'str',
        'match_field_index': 'str'
    }

    attribute_map = {
        'match_field': 'match_field',
        'match_field_index': 'match_field_index'
    }

    def __init__(self, match_field=None, match_field_index=None):
        r"""UserTagDTO

        The model defined in huaweicloud sdk

        :param match_field: 
        :type match_field: str
        :param match_field_index: 
        :type match_field_index: str
        """
        
        

        self._match_field = None
        self._match_field_index = None
        self.discriminator = None

        if match_field is not None:
            self.match_field = match_field
        if match_field_index is not None:
            self.match_field_index = match_field_index

    @property
    def match_field(self):
        r"""Gets the match_field of this UserTagDTO.

        :return: The match_field of this UserTagDTO.
        :rtype: str
        """
        return self._match_field

    @match_field.setter
    def match_field(self, match_field):
        r"""Sets the match_field of this UserTagDTO.

        :param match_field: The match_field of this UserTagDTO.
        :type match_field: str
        """
        self._match_field = match_field

    @property
    def match_field_index(self):
        r"""Gets the match_field_index of this UserTagDTO.

        :return: The match_field_index of this UserTagDTO.
        :rtype: str
        """
        return self._match_field_index

    @match_field_index.setter
    def match_field_index(self, match_field_index):
        r"""Sets the match_field_index of this UserTagDTO.

        :param match_field_index: The match_field_index of this UserTagDTO.
        :type match_field_index: str
        """
        self._match_field_index = match_field_index

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
        if not isinstance(other, UserTagDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
