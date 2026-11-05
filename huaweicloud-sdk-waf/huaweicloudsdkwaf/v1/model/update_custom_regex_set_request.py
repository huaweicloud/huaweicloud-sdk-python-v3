# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCustomRegexSetRequest:

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
        'body': 'AiguardCustomRegexSetUpdateBody'
    }

    attribute_map = {
        'regex_set_id': 'regex_set_id',
        'body': 'body'
    }

    def __init__(self, regex_set_id=None, body=None):
        r"""UpdateCustomRegexSetRequest

        The model defined in huaweicloud sdk

        :param regex_set_id: 正则库ID
        :type regex_set_id: str
        :param body: Body of the UpdateCustomRegexSetRequest
        :type body: :class:`huaweicloudsdkwaf.v1.AiguardCustomRegexSetUpdateBody`
        """
        
        

        self._regex_set_id = None
        self._body = None
        self.discriminator = None

        self.regex_set_id = regex_set_id
        if body is not None:
            self.body = body

    @property
    def regex_set_id(self):
        r"""Gets the regex_set_id of this UpdateCustomRegexSetRequest.

        正则库ID

        :return: The regex_set_id of this UpdateCustomRegexSetRequest.
        :rtype: str
        """
        return self._regex_set_id

    @regex_set_id.setter
    def regex_set_id(self, regex_set_id):
        r"""Sets the regex_set_id of this UpdateCustomRegexSetRequest.

        正则库ID

        :param regex_set_id: The regex_set_id of this UpdateCustomRegexSetRequest.
        :type regex_set_id: str
        """
        self._regex_set_id = regex_set_id

    @property
    def body(self):
        r"""Gets the body of this UpdateCustomRegexSetRequest.

        :return: The body of this UpdateCustomRegexSetRequest.
        :rtype: :class:`huaweicloudsdkwaf.v1.AiguardCustomRegexSetUpdateBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateCustomRegexSetRequest.

        :param body: The body of this UpdateCustomRegexSetRequest.
        :type body: :class:`huaweicloudsdkwaf.v1.AiguardCustomRegexSetUpdateBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateCustomRegexSetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
