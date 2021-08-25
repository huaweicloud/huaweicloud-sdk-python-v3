# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'detail': 'ImageDetectionResultDetail',
        'category_suggestions': 'dict(str, str)'
    }

    attribute_map = {
        'url': 'url',
        'suggestion': 'suggestion',
        'detail': 'detail',
        'category_suggestions': 'category_suggestions'
    }

    def __init__(self, url=None, suggestion=None, detail=None, category_suggestions=None):
        """CheckResultItemsBody - a model defined in huaweicloud sdk"""
        
        

        self._url = None
        self._suggestion = None
        self._detail = None
        self._category_suggestions = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if suggestion is not None:
            self.suggestion = suggestion
        if detail is not None:
            self.detail = detail
        if category_suggestions is not None:
            self.category_suggestions = category_suggestions

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

        检测结果是否通过。 - block：包含敏感信息，不通过 - pass：不包含敏感信息，通过 - review：需要人工复检 > 当同时检测多个场景时，suggestion的值以最可能包含敏感信息的场景为准。即任一场景出现了block则总的suggestion为block，所有场景都pass时suggestion为pass，这两种情况之外则一定有场景需要review，此时suggestion为review。 

        :return: The suggestion of this CheckResultItemsBody.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this CheckResultItemsBody.

        检测结果是否通过。 - block：包含敏感信息，不通过 - pass：不包含敏感信息，通过 - review：需要人工复检 > 当同时检测多个场景时，suggestion的值以最可能包含敏感信息的场景为准。即任一场景出现了block则总的suggestion为block，所有场景都pass时suggestion为pass，这两种情况之外则一定有场景需要review，此时suggestion为review。 

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

    @property
    def category_suggestions(self):
        """Gets the category_suggestions of this CheckResultItemsBody.

        具体每个场景的检测结果。  block：包含敏感信息，不通过  pass：不包含敏感信息，通过  review：需要人工复检 

        :return: The category_suggestions of this CheckResultItemsBody.
        :rtype: dict(str, str)
        """
        return self._category_suggestions

    @category_suggestions.setter
    def category_suggestions(self, category_suggestions):
        """Sets the category_suggestions of this CheckResultItemsBody.

        具体每个场景的检测结果。  block：包含敏感信息，不通过  pass：不包含敏感信息，通过  review：需要人工复检 

        :param category_suggestions: The category_suggestions of this CheckResultItemsBody.
        :type: dict(str, str)
        """
        self._category_suggestions = category_suggestions

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
        if not isinstance(other, CheckResultItemsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
