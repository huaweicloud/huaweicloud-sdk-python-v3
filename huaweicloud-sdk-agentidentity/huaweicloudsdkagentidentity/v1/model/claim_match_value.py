# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClaimMatchValue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'match_value_string': 'str',
        'match_value_string_list': 'list[str]'
    }

    attribute_map = {
        'match_value_string': 'match_value_string',
        'match_value_string_list': 'match_value_string_list'
    }

    def __init__(self, match_value_string=None, match_value_string_list=None):
        r"""ClaimMatchValue

        The model defined in huaweicloud sdk

        :param match_value_string: The string value to match for.
        :type match_value_string: str
        :param match_value_string_list: 
        :type match_value_string_list: list[str]
        """
        
        

        self._match_value_string = None
        self._match_value_string_list = None
        self.discriminator = None

        if match_value_string is not None:
            self.match_value_string = match_value_string
        if match_value_string_list is not None:
            self.match_value_string_list = match_value_string_list

    @property
    def match_value_string(self):
        r"""Gets the match_value_string of this ClaimMatchValue.

        The string value to match for.

        :return: The match_value_string of this ClaimMatchValue.
        :rtype: str
        """
        return self._match_value_string

    @match_value_string.setter
    def match_value_string(self, match_value_string):
        r"""Sets the match_value_string of this ClaimMatchValue.

        The string value to match for.

        :param match_value_string: The match_value_string of this ClaimMatchValue.
        :type match_value_string: str
        """
        self._match_value_string = match_value_string

    @property
    def match_value_string_list(self):
        r"""Gets the match_value_string_list of this ClaimMatchValue.

        :return: The match_value_string_list of this ClaimMatchValue.
        :rtype: list[str]
        """
        return self._match_value_string_list

    @match_value_string_list.setter
    def match_value_string_list(self, match_value_string_list):
        r"""Sets the match_value_string_list of this ClaimMatchValue.

        :param match_value_string_list: The match_value_string_list of this ClaimMatchValue.
        :type match_value_string_list: list[str]
        """
        self._match_value_string_list = match_value_string_list

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
        if not isinstance(other, ClaimMatchValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
