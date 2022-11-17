# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageTaggingItemBodyI18nType:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'zh': 'str',
        'en': 'str'
    }

    attribute_map = {
        'zh': 'zh',
        'en': 'en'
    }

    def __init__(self, zh=None, en=None):
        """ImageTaggingItemBodyI18nType

        The model defined in huaweicloud sdk

        :param zh: 中文标签类别
        :type zh: str
        :param en: 英文标签类别
        :type en: str
        """
        
        

        self._zh = None
        self._en = None
        self.discriminator = None

        if zh is not None:
            self.zh = zh
        if en is not None:
            self.en = en

    @property
    def zh(self):
        """Gets the zh of this ImageTaggingItemBodyI18nType.

        中文标签类别

        :return: The zh of this ImageTaggingItemBodyI18nType.
        :rtype: str
        """
        return self._zh

    @zh.setter
    def zh(self, zh):
        """Sets the zh of this ImageTaggingItemBodyI18nType.

        中文标签类别

        :param zh: The zh of this ImageTaggingItemBodyI18nType.
        :type zh: str
        """
        self._zh = zh

    @property
    def en(self):
        """Gets the en of this ImageTaggingItemBodyI18nType.

        英文标签类别

        :return: The en of this ImageTaggingItemBodyI18nType.
        :rtype: str
        """
        return self._en

    @en.setter
    def en(self, en):
        """Sets the en of this ImageTaggingItemBodyI18nType.

        英文标签类别

        :param en: The en of this ImageTaggingItemBodyI18nType.
        :type en: str
        """
        self._en = en

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
        if not isinstance(other, ImageTaggingItemBodyI18nType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
