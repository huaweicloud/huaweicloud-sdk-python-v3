# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteSubtitle:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'language': 'str'
    }

    attribute_map = {
        'type': 'type',
        'language': 'language'
    }

    def __init__(self, type=None, language=None):
        """DeleteSubtitle

        The model defined in huaweicloud sdk

        :param type: 字幕类型，字幕封装当前仅支持VTT
        :type type: str
        :param language: 字幕语言
        :type language: str
        """
        
        

        self._type = None
        self._language = None
        self.discriminator = None

        self.type = type
        self.language = language

    @property
    def type(self):
        """Gets the type of this DeleteSubtitle.

        字幕类型，字幕封装当前仅支持VTT

        :return: The type of this DeleteSubtitle.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeleteSubtitle.

        字幕类型，字幕封装当前仅支持VTT

        :param type: The type of this DeleteSubtitle.
        :type type: str
        """
        self._type = type

    @property
    def language(self):
        """Gets the language of this DeleteSubtitle.

        字幕语言

        :return: The language of this DeleteSubtitle.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this DeleteSubtitle.

        字幕语言

        :param language: The language of this DeleteSubtitle.
        :type language: str
        """
        self._language = language

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
        if not isinstance(other, DeleteSubtitle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
