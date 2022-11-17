# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TranscriberResult:

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
        'analysis_info': 'AnalysisInfoResult',
        'word_info': 'list[WordInfo]'
    }

    attribute_map = {
        'text': 'text',
        'analysis_info': 'analysis_info',
        'word_info': 'word_info'
    }

    def __init__(self, text=None, analysis_info=None, word_info=None):
        """TranscriberResult

        The model defined in huaweicloud sdk

        :param text: 识别结果文本。
        :type text: str
        :param analysis_info: 
        :type analysis_info: :class:`huaweicloudsdksis.v1.AnalysisInfoResult`
        :param word_info: 分词输出列表
        :type word_info: list[:class:`huaweicloudsdksis.v1.WordInfo`]
        """
        
        

        self._text = None
        self._analysis_info = None
        self._word_info = None
        self.discriminator = None

        self.text = text
        if analysis_info is not None:
            self.analysis_info = analysis_info
        if word_info is not None:
            self.word_info = word_info

    @property
    def text(self):
        """Gets the text of this TranscriberResult.

        识别结果文本。

        :return: The text of this TranscriberResult.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this TranscriberResult.

        识别结果文本。

        :param text: The text of this TranscriberResult.
        :type text: str
        """
        self._text = text

    @property
    def analysis_info(self):
        """Gets the analysis_info of this TranscriberResult.

        :return: The analysis_info of this TranscriberResult.
        :rtype: :class:`huaweicloudsdksis.v1.AnalysisInfoResult`
        """
        return self._analysis_info

    @analysis_info.setter
    def analysis_info(self, analysis_info):
        """Sets the analysis_info of this TranscriberResult.

        :param analysis_info: The analysis_info of this TranscriberResult.
        :type analysis_info: :class:`huaweicloudsdksis.v1.AnalysisInfoResult`
        """
        self._analysis_info = analysis_info

    @property
    def word_info(self):
        """Gets the word_info of this TranscriberResult.

        分词输出列表

        :return: The word_info of this TranscriberResult.
        :rtype: list[:class:`huaweicloudsdksis.v1.WordInfo`]
        """
        return self._word_info

    @word_info.setter
    def word_info(self, word_info):
        """Sets the word_info of this TranscriberResult.

        分词输出列表

        :param word_info: The word_info of this TranscriberResult.
        :type word_info: list[:class:`huaweicloudsdksis.v1.WordInfo`]
        """
        self._word_info = word_info

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
        if not isinstance(other, TranscriberResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
