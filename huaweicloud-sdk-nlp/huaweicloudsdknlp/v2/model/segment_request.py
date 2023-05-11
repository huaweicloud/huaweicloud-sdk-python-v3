# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SegmentRequest:

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
        'pos_switch': 'int',
        'lang': 'str',
        'criterion': 'str'
    }

    attribute_map = {
        'text': 'text',
        'pos_switch': 'pos_switch',
        'lang': 'lang',
        'criterion': 'criterion'
    }

    def __init__(self, text=None, pos_switch=None, lang=None, criterion=None):
        """SegmentRequest

        The model defined in huaweicloud sdk

        :param text: 待分词文本，长度为1~512，文本编码为UTF-8。
        :type text: str
        :param pos_switch: 是否开启词性标注功能，1为开启，0为关闭，默认为关闭。
        :type pos_switch: int
        :param lang: 支持的文本语言类型，目前支持中文（zh）和英文（en），默认为中文。
        :type lang: str
        :param criterion: 支持的分词规范。 中文分词标准目前支持PKU（北大分词标准）、CTB（宾州中文树库标准），默认为PKU。 英文分词标准默认为Penn TreeBank（宾州树库标准），不需要传入该参数。
        :type criterion: str
        """
        
        

        self._text = None
        self._pos_switch = None
        self._lang = None
        self._criterion = None
        self.discriminator = None

        self.text = text
        if pos_switch is not None:
            self.pos_switch = pos_switch
        if lang is not None:
            self.lang = lang
        if criterion is not None:
            self.criterion = criterion

    @property
    def text(self):
        """Gets the text of this SegmentRequest.

        待分词文本，长度为1~512，文本编码为UTF-8。

        :return: The text of this SegmentRequest.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this SegmentRequest.

        待分词文本，长度为1~512，文本编码为UTF-8。

        :param text: The text of this SegmentRequest.
        :type text: str
        """
        self._text = text

    @property
    def pos_switch(self):
        """Gets the pos_switch of this SegmentRequest.

        是否开启词性标注功能，1为开启，0为关闭，默认为关闭。

        :return: The pos_switch of this SegmentRequest.
        :rtype: int
        """
        return self._pos_switch

    @pos_switch.setter
    def pos_switch(self, pos_switch):
        """Sets the pos_switch of this SegmentRequest.

        是否开启词性标注功能，1为开启，0为关闭，默认为关闭。

        :param pos_switch: The pos_switch of this SegmentRequest.
        :type pos_switch: int
        """
        self._pos_switch = pos_switch

    @property
    def lang(self):
        """Gets the lang of this SegmentRequest.

        支持的文本语言类型，目前支持中文（zh）和英文（en），默认为中文。

        :return: The lang of this SegmentRequest.
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        """Sets the lang of this SegmentRequest.

        支持的文本语言类型，目前支持中文（zh）和英文（en），默认为中文。

        :param lang: The lang of this SegmentRequest.
        :type lang: str
        """
        self._lang = lang

    @property
    def criterion(self):
        """Gets the criterion of this SegmentRequest.

        支持的分词规范。 中文分词标准目前支持PKU（北大分词标准）、CTB（宾州中文树库标准），默认为PKU。 英文分词标准默认为Penn TreeBank（宾州树库标准），不需要传入该参数。

        :return: The criterion of this SegmentRequest.
        :rtype: str
        """
        return self._criterion

    @criterion.setter
    def criterion(self, criterion):
        """Sets the criterion of this SegmentRequest.

        支持的分词规范。 中文分词标准目前支持PKU（北大分词标准）、CTB（宾州中文树库标准），默认为PKU。 英文分词标准默认为Penn TreeBank（宾州树库标准），不需要传入该参数。

        :param criterion: The criterion of this SegmentRequest.
        :type criterion: str
        """
        self._criterion = criterion

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
        if not isinstance(other, SegmentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
