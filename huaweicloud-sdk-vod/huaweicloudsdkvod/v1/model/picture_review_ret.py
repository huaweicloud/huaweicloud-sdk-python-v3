# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        """PictureReviewRet

        The model defined in huaweicloud sdk

        :param suggestion: 检测结果是否通过。  取值如下： - block：包含敏感信息，不通过。 - pass：不包含敏感信息，通过。 - review：需要人工复检。
        :type suggestion: str
        :param offset: 截图在视频中的时间偏移值。封面不涉及此字段  单位：秒。
        :type offset: int
        :param url: 对应截图/封面的访问URL。
        :type url: str
        :param politics: 政治因素审核结果。
        :type politics: list[:class:`huaweicloudsdkvod.v1.ReviewDetail`]
        :param terrorism: 暴恐元素审核结果。
        :type terrorism: list[:class:`huaweicloudsdkvod.v1.ReviewDetail`]
        :param porn: 涉黄内容审核结果。
        :type porn: list[:class:`huaweicloudsdkvod.v1.ReviewDetail`]
        """
        
        

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

        检测结果是否通过。  取值如下： - block：包含敏感信息，不通过。 - pass：不包含敏感信息，通过。 - review：需要人工复检。

        :return: The suggestion of this PictureReviewRet.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this PictureReviewRet.

        检测结果是否通过。  取值如下： - block：包含敏感信息，不通过。 - pass：不包含敏感信息，通过。 - review：需要人工复检。

        :param suggestion: The suggestion of this PictureReviewRet.
        :type suggestion: str
        """
        self._suggestion = suggestion

    @property
    def offset(self):
        """Gets the offset of this PictureReviewRet.

        截图在视频中的时间偏移值。封面不涉及此字段  单位：秒。

        :return: The offset of this PictureReviewRet.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this PictureReviewRet.

        截图在视频中的时间偏移值。封面不涉及此字段  单位：秒。

        :param offset: The offset of this PictureReviewRet.
        :type offset: int
        """
        self._offset = offset

    @property
    def url(self):
        """Gets the url of this PictureReviewRet.

        对应截图/封面的访问URL。

        :return: The url of this PictureReviewRet.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PictureReviewRet.

        对应截图/封面的访问URL。

        :param url: The url of this PictureReviewRet.
        :type url: str
        """
        self._url = url

    @property
    def politics(self):
        """Gets the politics of this PictureReviewRet.

        政治因素审核结果。

        :return: The politics of this PictureReviewRet.
        :rtype: list[:class:`huaweicloudsdkvod.v1.ReviewDetail`]
        """
        return self._politics

    @politics.setter
    def politics(self, politics):
        """Sets the politics of this PictureReviewRet.

        政治因素审核结果。

        :param politics: The politics of this PictureReviewRet.
        :type politics: list[:class:`huaweicloudsdkvod.v1.ReviewDetail`]
        """
        self._politics = politics

    @property
    def terrorism(self):
        """Gets the terrorism of this PictureReviewRet.

        暴恐元素审核结果。

        :return: The terrorism of this PictureReviewRet.
        :rtype: list[:class:`huaweicloudsdkvod.v1.ReviewDetail`]
        """
        return self._terrorism

    @terrorism.setter
    def terrorism(self, terrorism):
        """Sets the terrorism of this PictureReviewRet.

        暴恐元素审核结果。

        :param terrorism: The terrorism of this PictureReviewRet.
        :type terrorism: list[:class:`huaweicloudsdkvod.v1.ReviewDetail`]
        """
        self._terrorism = terrorism

    @property
    def porn(self):
        """Gets the porn of this PictureReviewRet.

        涉黄内容审核结果。

        :return: The porn of this PictureReviewRet.
        :rtype: list[:class:`huaweicloudsdkvod.v1.ReviewDetail`]
        """
        return self._porn

    @porn.setter
    def porn(self, porn):
        """Sets the porn of this PictureReviewRet.

        涉黄内容审核结果。

        :param porn: The porn of this PictureReviewRet.
        :type porn: list[:class:`huaweicloudsdkvod.v1.ReviewDetail`]
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
        if not isinstance(other, PictureReviewRet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
