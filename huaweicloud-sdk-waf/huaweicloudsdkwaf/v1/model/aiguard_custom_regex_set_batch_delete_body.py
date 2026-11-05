# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AiguardCustomRegexSetBatchDeleteBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'regex_set_ids': 'list[str]'
    }

    attribute_map = {
        'regex_set_ids': 'regex_set_ids'
    }

    def __init__(self, regex_set_ids=None):
        r"""AiguardCustomRegexSetBatchDeleteBody

        The model defined in huaweicloud sdk

        :param regex_set_ids: 正则库ID列表
        :type regex_set_ids: list[str]
        """
        
        

        self._regex_set_ids = None
        self.discriminator = None

        self.regex_set_ids = regex_set_ids

    @property
    def regex_set_ids(self):
        r"""Gets the regex_set_ids of this AiguardCustomRegexSetBatchDeleteBody.

        正则库ID列表

        :return: The regex_set_ids of this AiguardCustomRegexSetBatchDeleteBody.
        :rtype: list[str]
        """
        return self._regex_set_ids

    @regex_set_ids.setter
    def regex_set_ids(self, regex_set_ids):
        r"""Sets the regex_set_ids of this AiguardCustomRegexSetBatchDeleteBody.

        正则库ID列表

        :param regex_set_ids: The regex_set_ids of this AiguardCustomRegexSetBatchDeleteBody.
        :type regex_set_ids: list[str]
        """
        self._regex_set_ids = regex_set_ids

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
        if not isinstance(other, AiguardCustomRegexSetBatchDeleteBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
