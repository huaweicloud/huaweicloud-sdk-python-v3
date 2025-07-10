# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Content:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'en': 'str',
        'ch': 'str'
    }

    attribute_map = {
        'en': 'en',
        'ch': 'ch'
    }

    def __init__(self, en=None, ch=None):
        r"""Content

        The model defined in huaweicloud sdk

        :param en: 英文策略内容。
        :type en: str
        :param ch: 中文策略内容。
        :type ch: str
        """
        
        

        self._en = None
        self._ch = None
        self.discriminator = None

        if en is not None:
            self.en = en
        if ch is not None:
            self.ch = ch

    @property
    def en(self):
        r"""Gets the en of this Content.

        英文策略内容。

        :return: The en of this Content.
        :rtype: str
        """
        return self._en

    @en.setter
    def en(self, en):
        r"""Sets the en of this Content.

        英文策略内容。

        :param en: The en of this Content.
        :type en: str
        """
        self._en = en

    @property
    def ch(self):
        r"""Gets the ch of this Content.

        中文策略内容。

        :return: The ch of this Content.
        :rtype: str
        """
        return self._ch

    @ch.setter
    def ch(self, ch):
        r"""Sets the ch of this Content.

        中文策略内容。

        :param ch: The ch of this Content.
        :type ch: str
        """
        self._ch = ch

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
        if not isinstance(other, Content):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
