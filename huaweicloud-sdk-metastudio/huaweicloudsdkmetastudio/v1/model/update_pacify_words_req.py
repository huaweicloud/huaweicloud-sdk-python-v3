# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePacifyWordsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pacify_words': 'str'
    }

    attribute_map = {
        'pacify_words': 'pacify_words'
    }

    def __init__(self, pacify_words=None):
        r"""UpdatePacifyWordsReq

        The model defined in huaweicloud sdk

        :param pacify_words: 安抚话术。
        :type pacify_words: str
        """
        
        

        self._pacify_words = None
        self.discriminator = None

        self.pacify_words = pacify_words

    @property
    def pacify_words(self):
        r"""Gets the pacify_words of this UpdatePacifyWordsReq.

        安抚话术。

        :return: The pacify_words of this UpdatePacifyWordsReq.
        :rtype: str
        """
        return self._pacify_words

    @pacify_words.setter
    def pacify_words(self, pacify_words):
        r"""Sets the pacify_words of this UpdatePacifyWordsReq.

        安抚话术。

        :param pacify_words: The pacify_words of this UpdatePacifyWordsReq.
        :type pacify_words: str
        """
        self._pacify_words = pacify_words

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
        if not isinstance(other, UpdatePacifyWordsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
