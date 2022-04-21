# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CollectKeyWordsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'keywords': 'list[KeyWordsStat]'
    }

    attribute_map = {
        'keywords': 'keywords'
    }

    def __init__(self, keywords=None):
        """CollectKeyWordsResponse

        The model defined in huaweicloud sdk

        :param keywords: 指定时间范围内，用户问关键词列表。
        :type keywords: list[:class:`huaweicloudsdkcbs.v1.KeyWordsStat`]
        """
        
        super(CollectKeyWordsResponse, self).__init__()

        self._keywords = None
        self.discriminator = None

        if keywords is not None:
            self.keywords = keywords

    @property
    def keywords(self):
        """Gets the keywords of this CollectKeyWordsResponse.

        指定时间范围内，用户问关键词列表。

        :return: The keywords of this CollectKeyWordsResponse.
        :rtype: list[:class:`huaweicloudsdkcbs.v1.KeyWordsStat`]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this CollectKeyWordsResponse.

        指定时间范围内，用户问关键词列表。

        :param keywords: The keywords of this CollectKeyWordsResponse.
        :type keywords: list[:class:`huaweicloudsdkcbs.v1.KeyWordsStat`]
        """
        self._keywords = keywords

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
        if not isinstance(other, CollectKeyWordsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
