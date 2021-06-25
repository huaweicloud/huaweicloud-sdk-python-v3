# coding: utf-8

import pprint
import re

import six





class PictureReviewRet:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'suggestion': 'str',
        'offset': 'int',
        'url': 'str',
        'politics': 'list[ReviewDetail]',
        'terrorism': 'list[ReviewDetail]',
        'porn': 'list[ReviewDetail]'
    }

    attribute_map = {
        'suggestion': 'suggestion',
        'offset': 'offset',
        'url': 'url',
        'politics': 'politics',
        'terrorism': 'terrorism',
        'porn': 'porn'
    }

    def __init__(self, suggestion=None, offset=None, url=None, politics=None, terrorism=None, porn=None):
        """PictureReviewRet - a model defined in huaweicloud sdk"""
        
        

        self._suggestion = None
        self._offset = None
        self._url = None
        self._politics = None
        self._terrorism = None
        self._porn = None
        self.discriminator = None

        if suggestion is not None:
            self.suggestion = suggestion
        if offset is not None:
            self.offset = offset
        self.url = url
        if politics is not None:
            self.politics = politics
        if terrorism is not None:
            self.terrorism = terrorism
        if porn is not None:
            self.porn = porn

    @property
    def suggestion(self):
        """Gets the suggestion of this PictureReviewRet.

        检测结果是否通过。 block：包含敏感信息，不通过。 pass：不包含敏感信息，通过。 review：需要人工复查。 

        :return: The suggestion of this PictureReviewRet.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this PictureReviewRet.

        检测结果是否通过。 block：包含敏感信息，不通过。 pass：不包含敏感信息，通过。 review：需要人工复查。 

        :param suggestion: The suggestion of this PictureReviewRet.
        :type: str
        """
        self._suggestion = suggestion

    @property
    def offset(self):
        """Gets the offset of this PictureReviewRet.

        截图在视频中的时间偏移值，单位为秒。封面不涉及此字段

        :return: The offset of this PictureReviewRet.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this PictureReviewRet.

        截图在视频中的时间偏移值，单位为秒。封面不涉及此字段

        :param offset: The offset of this PictureReviewRet.
        :type: int
        """
        self._offset = offset

    @property
    def url(self):
        """Gets the url of this PictureReviewRet.

        对应截图/封面的的访问url

        :return: The url of this PictureReviewRet.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PictureReviewRet.

        对应截图/封面的的访问url

        :param url: The url of this PictureReviewRet.
        :type: str
        """
        self._url = url

    @property
    def politics(self):
        """Gets the politics of this PictureReviewRet.


        :return: The politics of this PictureReviewRet.
        :rtype: list[ReviewDetail]
        """
        return self._politics

    @politics.setter
    def politics(self, politics):
        """Sets the politics of this PictureReviewRet.


        :param politics: The politics of this PictureReviewRet.
        :type: list[ReviewDetail]
        """
        self._politics = politics

    @property
    def terrorism(self):
        """Gets the terrorism of this PictureReviewRet.


        :return: The terrorism of this PictureReviewRet.
        :rtype: list[ReviewDetail]
        """
        return self._terrorism

    @terrorism.setter
    def terrorism(self, terrorism):
        """Sets the terrorism of this PictureReviewRet.


        :param terrorism: The terrorism of this PictureReviewRet.
        :type: list[ReviewDetail]
        """
        self._terrorism = terrorism

    @property
    def porn(self):
        """Gets the porn of this PictureReviewRet.


        :return: The porn of this PictureReviewRet.
        :rtype: list[ReviewDetail]
        """
        return self._porn

    @porn.setter
    def porn(self, porn):
        """Sets the porn of this PictureReviewRet.


        :param porn: The porn of this PictureReviewRet.
        :type: list[ReviewDetail]
        """
        self._porn = porn

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
        if not isinstance(other, PictureReviewRet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other