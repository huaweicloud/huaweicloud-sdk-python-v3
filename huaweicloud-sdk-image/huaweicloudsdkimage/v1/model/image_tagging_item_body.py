# coding: utf-8

import pprint
import re

import six





class ImageTaggingItemBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'confidence': 'str',
        'type': 'str',
        'tag': 'str',
        'i18n_tag': 'ImageTaggingI18nTag'
    }

    attribute_map = {
        'confidence': 'confidence',
        'type': 'type',
        'tag': 'tag',
        'i18n_tag': 'i18n_tag'
    }

    def __init__(self, confidence=None, type=None, tag=None, i18n_tag=None):
        """ImageTaggingItemBody - a model defined in huaweicloud sdk"""
        
        

        self._confidence = None
        self._type = None
        self._tag = None
        self._i18n_tag = None
        self.discriminator = None

        if confidence is not None:
            self.confidence = confidence
        if type is not None:
            self.type = type
        if tag is not None:
            self.tag = tag
        if i18n_tag is not None:
            self.i18n_tag = i18n_tag

    @property
    def confidence(self):
        """Gets the confidence of this ImageTaggingItemBody.

        置信度，取值范围：0-100。

        :return: The confidence of this ImageTaggingItemBody.
        :rtype: str
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this ImageTaggingItemBody.

        置信度，取值范围：0-100。

        :param confidence: The confidence of this ImageTaggingItemBody.
        :type: str
        """
        self._confidence = confidence

    @property
    def type(self):
        """Gets the type of this ImageTaggingItemBody.

        标签的类别 object：实体标签 scene：场景标签 concept：概念标签

        :return: The type of this ImageTaggingItemBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ImageTaggingItemBody.

        标签的类别 object：实体标签 scene：场景标签 concept：概念标签

        :param type: The type of this ImageTaggingItemBody.
        :type: str
        """
        self._type = type

    @property
    def tag(self):
        """Gets the tag of this ImageTaggingItemBody.

        标签名称。

        :return: The tag of this ImageTaggingItemBody.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ImageTaggingItemBody.

        标签名称。

        :param tag: The tag of this ImageTaggingItemBody.
        :type: str
        """
        self._tag = tag

    @property
    def i18n_tag(self):
        """Gets the i18n_tag of this ImageTaggingItemBody.


        :return: The i18n_tag of this ImageTaggingItemBody.
        :rtype: ImageTaggingI18nTag
        """
        return self._i18n_tag

    @i18n_tag.setter
    def i18n_tag(self, i18n_tag):
        """Sets the i18n_tag of this ImageTaggingItemBody.


        :param i18n_tag: The i18n_tag of this ImageTaggingItemBody.
        :type: ImageTaggingI18nTag
        """
        self._i18n_tag = i18n_tag

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImageTaggingItemBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
