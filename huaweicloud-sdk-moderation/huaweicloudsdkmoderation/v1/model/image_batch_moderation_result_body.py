# coding: utf-8

import pprint
import re

import six


class ImageBatchModerationResultBody(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'url': 'str',
        'suggestion': 'str',
        'detail': 'object',
        'confidence': 'float',
        'face_detail': 'object',
        'label': 'str'
    }

    attribute_map = {
        'url': 'url',
        'suggestion': 'suggestion',
        'detail': 'detail',
        'confidence': 'confidence',
        'face_detail': 'face_detail',
        'label': 'label'
    }

    def __init__(self, url=None, suggestion=None, detail=None, confidence=None, face_detail=None, label=None):  # noqa: E501
        """ImageBatchModerationResultBody - a model defined in huaweicloud sdk"""

        self._url = None
        self._suggestion = None
        self._detail = None
        self._confidence = None
        self._face_detail = None
        self._label = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if suggestion is not None:
            self.suggestion = suggestion
        if detail is not None:
            self.detail = detail
        if confidence is not None:
            self.confidence = confidence
        if face_detail is not None:
            self.face_detail = face_detail
        if label is not None:
            self.label = label

    @property
    def url(self):
        """Gets the url of this ImageBatchModerationResultBody.

        图片的URL路径。

        :return: The url of this ImageBatchModerationResultBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ImageBatchModerationResultBody.

        图片的URL路径。

        :param url: The url of this ImageBatchModerationResultBody.
        :type: str
        """
        self._url = url

    @property
    def suggestion(self):
        """Gets the suggestion of this ImageBatchModerationResultBody.

        请参见[表2](https://support.huaweicloud.com/api-moderation/moderation_03_0019.html#moderation_03_0019__zh-cn_topic_0087142444_table663805019540)中suggestion字段说明。

        :return: The suggestion of this ImageBatchModerationResultBody.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this ImageBatchModerationResultBody.

        请参见[表2](https://support.huaweicloud.com/api-moderation/moderation_03_0019.html#moderation_03_0019__zh-cn_topic_0087142444_table663805019540)中suggestion字段说明。

        :param suggestion: The suggestion of this ImageBatchModerationResultBody.
        :type: str
        """
        self._suggestion = suggestion

    @property
    def detail(self):
        """Gets the detail of this ImageBatchModerationResultBody.

        请参见[表2](https://support.huaweicloud.com/api-moderation/moderation_03_0019.html#moderation_03_0019__zh-cn_topic_0087142444_table663805019540)中detail字段说明

        :return: The detail of this ImageBatchModerationResultBody.
        :rtype: object
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ImageBatchModerationResultBody.

        请参见[表2](https://support.huaweicloud.com/api-moderation/moderation_03_0019.html#moderation_03_0019__zh-cn_topic_0087142444_table663805019540)中detail字段说明

        :param detail: The detail of this ImageBatchModerationResultBody.
        :type: object
        """
        self._detail = detail

    @property
    def confidence(self):
        """Gets the confidence of this ImageBatchModerationResultBody.

        请参见[表2](https://support.huaweicloud.com/api-moderation/moderation_03_0019.html#moderation_03_0019__zh-cn_topic_0087142444_table663805019540)中confidence字段说明。

        :return: The confidence of this ImageBatchModerationResultBody.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this ImageBatchModerationResultBody.

        请参见[表2](https://support.huaweicloud.com/api-moderation/moderation_03_0019.html#moderation_03_0019__zh-cn_topic_0087142444_table663805019540)中confidence字段说明。

        :param confidence: The confidence of this ImageBatchModerationResultBody.
        :type: float
        """
        self._confidence = confidence

    @property
    def face_detail(self):
        """Gets the face_detail of this ImageBatchModerationResultBody.

        请参见[表2](https://support.huaweicloud.com/api-moderation/moderation_03_0019.html#moderation_03_0019__zh-cn_topic_0087142444_table663805019540)中face_detail字段说明。

        :return: The face_detail of this ImageBatchModerationResultBody.
        :rtype: object
        """
        return self._face_detail

    @face_detail.setter
    def face_detail(self, face_detail):
        """Sets the face_detail of this ImageBatchModerationResultBody.

        请参见[表2](https://support.huaweicloud.com/api-moderation/moderation_03_0019.html#moderation_03_0019__zh-cn_topic_0087142444_table663805019540)中face_detail字段说明。

        :param face_detail: The face_detail of this ImageBatchModerationResultBody.
        :type: object
        """
        self._face_detail = face_detail

    @property
    def label(self):
        """Gets the label of this ImageBatchModerationResultBody.

        请参见[表2](https://support.huaweicloud.com/api-moderation/moderation_03_0019.html#moderation_03_0019__zh-cn_topic_0087142444_table663805019540)中label字段说明。

        :return: The label of this ImageBatchModerationResultBody.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ImageBatchModerationResultBody.

        请参见[表2](https://support.huaweicloud.com/api-moderation/moderation_03_0019.html#moderation_03_0019__zh-cn_topic_0087142444_table663805019540)中label字段说明。

        :param label: The label of this ImageBatchModerationResultBody.
        :type: str
        """
        self._label = label

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
        if not isinstance(other, ImageBatchModerationResultBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
