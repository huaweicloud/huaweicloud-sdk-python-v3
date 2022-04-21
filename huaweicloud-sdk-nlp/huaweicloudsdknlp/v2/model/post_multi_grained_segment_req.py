# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostMultiGrainedSegmentReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'text': 'str',
        'lang': 'str',
        'granularity': 'int'
    }

    attribute_map = {
        'text': 'text',
        'lang': 'lang',
        'granularity': 'granularity'
    }

    def __init__(self, text=None, lang=None, granularity=None):
        """PostMultiGrainedSegmentReq

        The model defined in huaweicloud sdk

        :param text: 待分词文本，长度为1~64，文本编码为UTF-8。
        :type text: str
        :param lang: 支持的文本语言类型，目前只支持中文，默认为zh。
        :type lang: str
        :param granularity: 分词粒度，1为最细粒度，2为最粗粒度，其它情况默认返回全部粒度分词树结果。
        :type granularity: int
        """
        
        

        self._text = None
        self._lang = None
        self._granularity = None
        self.discriminator = None

        self.text = text
        if lang is not None:
            self.lang = lang
        if granularity is not None:
            self.granularity = granularity

    @property
    def text(self):
        """Gets the text of this PostMultiGrainedSegmentReq.

        待分词文本，长度为1~64，文本编码为UTF-8。

        :return: The text of this PostMultiGrainedSegmentReq.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this PostMultiGrainedSegmentReq.

        待分词文本，长度为1~64，文本编码为UTF-8。

        :param text: The text of this PostMultiGrainedSegmentReq.
        :type text: str
        """
        self._text = text

    @property
    def lang(self):
        """Gets the lang of this PostMultiGrainedSegmentReq.

        支持的文本语言类型，目前只支持中文，默认为zh。

        :return: The lang of this PostMultiGrainedSegmentReq.
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        """Sets the lang of this PostMultiGrainedSegmentReq.

        支持的文本语言类型，目前只支持中文，默认为zh。

        :param lang: The lang of this PostMultiGrainedSegmentReq.
        :type lang: str
        """
        self._lang = lang

    @property
    def granularity(self):
        """Gets the granularity of this PostMultiGrainedSegmentReq.

        分词粒度，1为最细粒度，2为最粗粒度，其它情况默认返回全部粒度分词树结果。

        :return: The granularity of this PostMultiGrainedSegmentReq.
        :rtype: int
        """
        return self._granularity

    @granularity.setter
    def granularity(self, granularity):
        """Sets the granularity of this PostMultiGrainedSegmentReq.

        分词粒度，1为最细粒度，2为最粗粒度，其它情况默认返回全部粒度分词树结果。

        :param granularity: The granularity of this PostMultiGrainedSegmentReq.
        :type granularity: int
        """
        self._granularity = granularity

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
        if not isinstance(other, PostMultiGrainedSegmentReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
