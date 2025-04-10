# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AudioStreamCreateRequestData:

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
        'language': 'str',
        'return_all_results': 'bool'
    }

    attribute_map = {
        'url': 'url',
        'language': 'language',
        'return_all_results': 'return_all_results'
    }

    def __init__(self, url=None, language=None, return_all_results=None):
        r"""AudioStreamCreateRequestData

        The model defined in huaweicloud sdk

        :param url: 音频流url地址，支持rtmp、rtmps、hls、http、https等主流协议。
        :type url: str
        :param language: 指定音频流中语种类型 zh: 中文,默认值为zh
        :type language: str
        :param return_all_results: 返回音频片段结果的策略。可选值如下： false：返回风险等级为非pass的音频片段结果 true：返回所有风险等级的音频片段结果 说明： 1. 默认值为false； 2. 每隔10秒返回一次最近10秒音频流的审核结果。
        :type return_all_results: bool
        """
        
        

        self._url = None
        self._language = None
        self._return_all_results = None
        self.discriminator = None

        self.url = url
        if language is not None:
            self.language = language
        if return_all_results is not None:
            self.return_all_results = return_all_results

    @property
    def url(self):
        r"""Gets the url of this AudioStreamCreateRequestData.

        音频流url地址，支持rtmp、rtmps、hls、http、https等主流协议。

        :return: The url of this AudioStreamCreateRequestData.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this AudioStreamCreateRequestData.

        音频流url地址，支持rtmp、rtmps、hls、http、https等主流协议。

        :param url: The url of this AudioStreamCreateRequestData.
        :type url: str
        """
        self._url = url

    @property
    def language(self):
        r"""Gets the language of this AudioStreamCreateRequestData.

        指定音频流中语种类型 zh: 中文,默认值为zh

        :return: The language of this AudioStreamCreateRequestData.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this AudioStreamCreateRequestData.

        指定音频流中语种类型 zh: 中文,默认值为zh

        :param language: The language of this AudioStreamCreateRequestData.
        :type language: str
        """
        self._language = language

    @property
    def return_all_results(self):
        r"""Gets the return_all_results of this AudioStreamCreateRequestData.

        返回音频片段结果的策略。可选值如下： false：返回风险等级为非pass的音频片段结果 true：返回所有风险等级的音频片段结果 说明： 1. 默认值为false； 2. 每隔10秒返回一次最近10秒音频流的审核结果。

        :return: The return_all_results of this AudioStreamCreateRequestData.
        :rtype: bool
        """
        return self._return_all_results

    @return_all_results.setter
    def return_all_results(self, return_all_results):
        r"""Sets the return_all_results of this AudioStreamCreateRequestData.

        返回音频片段结果的策略。可选值如下： false：返回风险等级为非pass的音频片段结果 true：返回所有风险等级的音频片段结果 说明： 1. 默认值为false； 2. 每隔10秒返回一次最近10秒音频流的审核结果。

        :param return_all_results: The return_all_results of this AudioStreamCreateRequestData.
        :type return_all_results: bool
        """
        self._return_all_results = return_all_results

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
        if not isinstance(other, AudioStreamCreateRequestData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
