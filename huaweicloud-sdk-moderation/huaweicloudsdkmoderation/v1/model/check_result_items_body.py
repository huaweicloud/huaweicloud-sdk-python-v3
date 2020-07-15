# coding: utf-8

import pprint
import re

import six





class CheckResultItemsBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'suggestion': 'str',
        'detail': 'ImageDetectionResultDetail'
    }

    attribute_map = {
        'url': 'url',
        'suggestion': 'suggestion',
        'detail': 'detail'
    }

    def __init__(self, url=None, suggestion=None, detail=None):
        """CheckResultItemsBody - a model defined in huaweicloud sdk"""
        
        

        self._url = None
        self._suggestion = None
        self._detail = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if suggestion is not None:
            self.suggestion = suggestion
        if detail is not None:
            self.detail = detail

    @property
    def url(self):
        """Gets the url of this CheckResultItemsBody.

        图片的URL路径。

        :return: The url of this CheckResultItemsBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CheckResultItemsBody.

        图片的URL路径。

        :param url: The url of this CheckResultItemsBody.
        :type: str
        """
        self._url = url

    @property
    def suggestion(self):
        """Gets the suggestion of this CheckResultItemsBody.

        请参见[表2](https://support.huaweicloud.com/api-moderation/moderation_03_0019.html#moderation_03_0019__zh-cn_topic_0087142444_table663805019540)中suggestion字段说明。

        :return: The suggestion of this CheckResultItemsBody.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this CheckResultItemsBody.

        请参见[表2](https://support.huaweicloud.com/api-moderation/moderation_03_0019.html#moderation_03_0019__zh-cn_topic_0087142444_table663805019540)中suggestion字段说明。

        :param suggestion: The suggestion of this CheckResultItemsBody.
        :type: str
        """
        self._suggestion = suggestion

    @property
    def detail(self):
        """Gets the detail of this CheckResultItemsBody.


        :return: The detail of this CheckResultItemsBody.
        :rtype: ImageDetectionResultDetail
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this CheckResultItemsBody.


        :param detail: The detail of this CheckResultItemsBody.
        :type: ImageDetectionResultDetail
        """
        self._detail = detail

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
        if not isinstance(other, CheckResultItemsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
