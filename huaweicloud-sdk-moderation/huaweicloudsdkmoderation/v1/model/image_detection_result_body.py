# coding: utf-8

import pprint
import re

import six





class ImageDetectionResultBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'detail': 'ImageDetectionResultDetail',
        'suggestion': 'str',
        'category_suggestion': 'object'
    }

    attribute_map = {
        'detail': 'detail',
        'suggestion': 'suggestion',
        'category_suggestion': 'category_suggestion'
    }

    def __init__(self, detail=None, suggestion=None, category_suggestion=None):
        """ImageDetectionResultBody - a model defined in huaweicloud sdk"""
        
        

        self._detail = None
        self._suggestion = None
        self._category_suggestion = None
        self.discriminator = None

        if detail is not None:
            self.detail = detail
        if suggestion is not None:
            self.suggestion = suggestion
        if category_suggestion is not None:
            self.category_suggestion = category_suggestion

    @property
    def detail(self):
        """Gets the detail of this ImageDetectionResultBody.


        :return: The detail of this ImageDetectionResultBody.
        :rtype: ImageDetectionResultDetail
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ImageDetectionResultBody.


        :param detail: The detail of this ImageDetectionResultBody.
        :type: ImageDetectionResultDetail
        """
        self._detail = detail

    @property
    def suggestion(self):
        """Gets the suggestion of this ImageDetectionResultBody.

        检测结果是否通过。 block：包含敏感信息，不通过 pass：不包含敏感信息，通过 review：需要人工复检 > 说明： 当同时检测多个场景时，suggestion的值以最可能包含敏感信息的场景为准。即任一场景出现了block则总的suggestion为block，所有场景都pass时suggestion为pass，这两种情况之外则一定有场景需要review，此时suggestion为review。 

        :return: The suggestion of this ImageDetectionResultBody.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this ImageDetectionResultBody.

        检测结果是否通过。 block：包含敏感信息，不通过 pass：不包含敏感信息，通过 review：需要人工复检 > 说明： 当同时检测多个场景时，suggestion的值以最可能包含敏感信息的场景为准。即任一场景出现了block则总的suggestion为block，所有场景都pass时suggestion为pass，这两种情况之外则一定有场景需要review，此时suggestion为review。 

        :param suggestion: The suggestion of this ImageDetectionResultBody.
        :type: str
        """
        self._suggestion = suggestion

    @property
    def category_suggestion(self):
        """Gets the category_suggestion of this ImageDetectionResultBody.

        具体每个场景的检测结果。  block：包含敏感信息，不通过  pass：不包含敏感信息，通过  review：需要人工复检 

        :return: The category_suggestion of this ImageDetectionResultBody.
        :rtype: object
        """
        return self._category_suggestion

    @category_suggestion.setter
    def category_suggestion(self, category_suggestion):
        """Sets the category_suggestion of this ImageDetectionResultBody.

        具体每个场景的检测结果。  block：包含敏感信息，不通过  pass：不包含敏感信息，通过  review：需要人工复检 

        :param category_suggestion: The category_suggestion of this ImageDetectionResultBody.
        :type: object
        """
        self._category_suggestion = category_suggestion

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
        if not isinstance(other, ImageDetectionResultBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
