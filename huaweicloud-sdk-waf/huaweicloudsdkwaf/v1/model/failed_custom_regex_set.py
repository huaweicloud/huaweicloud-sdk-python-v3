# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FailedCustomRegexSet:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'regex_set_id': 'str',
        'reason': 'str'
    }

    attribute_map = {
        'regex_set_id': 'regex_set_id',
        'reason': 'reason'
    }

    def __init__(self, regex_set_id=None, reason=None):
        r"""FailedCustomRegexSet

        The model defined in huaweicloud sdk

        :param regex_set_id: 失败的正则库ID
        :type regex_set_id: str
        :param reason: 失败原因
        :type reason: str
        """
        
        

        self._regex_set_id = None
        self._reason = None
        self.discriminator = None

        if regex_set_id is not None:
            self.regex_set_id = regex_set_id
        if reason is not None:
            self.reason = reason

    @property
    def regex_set_id(self):
        r"""Gets the regex_set_id of this FailedCustomRegexSet.

        失败的正则库ID

        :return: The regex_set_id of this FailedCustomRegexSet.
        :rtype: str
        """
        return self._regex_set_id

    @regex_set_id.setter
    def regex_set_id(self, regex_set_id):
        r"""Sets the regex_set_id of this FailedCustomRegexSet.

        失败的正则库ID

        :param regex_set_id: The regex_set_id of this FailedCustomRegexSet.
        :type regex_set_id: str
        """
        self._regex_set_id = regex_set_id

    @property
    def reason(self):
        r"""Gets the reason of this FailedCustomRegexSet.

        失败原因

        :return: The reason of this FailedCustomRegexSet.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this FailedCustomRegexSet.

        失败原因

        :param reason: The reason of this FailedCustomRegexSet.
        :type reason: str
        """
        self._reason = reason

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
        if not isinstance(other, FailedCustomRegexSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
