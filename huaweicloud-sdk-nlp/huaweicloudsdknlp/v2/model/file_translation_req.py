# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FileTranslationReq:

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
        '_from': 'str',
        'to': 'str',
        'type': 'str'
    }

    attribute_map = {
        'url': 'url',
        '_from': 'from',
        'to': 'to',
        'type': 'type'
    }

    def __init__(self, url=None, _from=None, to=None, type=None):
        """FileTranslationReq

        The model defined in huaweicloud sdk

        :param url: 存放在OBS的文档文件路径，私密文件推荐使用临时授权URL调用服务，如何获取OBS文件URL和临时授权URL请参见配置OBS访问权限（https://support.huaweicloud.com/api-nlp/nlp_03_0080.html）。OBS的region要和请求服务的region保持一致，region不一致则OBS不可用，即使obs是公开访问权限。
        :type url: str
        :param _from: 翻译原语言，文档翻译服务当前仅支持中英互译。
        :type _from: str
        :param to: 翻译目标语言，文档翻译服务当前仅支持中英互译。
        :type to: str
        :param type: 文档格式，当前仅支持翻译“docx”、“pptx”和“txt”格式的文档。
        :type type: str
        """
        
        

        self._url = None
        self.__from = None
        self._to = None
        self._type = None
        self.discriminator = None

        self.url = url
        self._from = _from
        self.to = to
        self.type = type

    @property
    def url(self):
        """Gets the url of this FileTranslationReq.

        存放在OBS的文档文件路径，私密文件推荐使用临时授权URL调用服务，如何获取OBS文件URL和临时授权URL请参见配置OBS访问权限（https://support.huaweicloud.com/api-nlp/nlp_03_0080.html）。OBS的region要和请求服务的region保持一致，region不一致则OBS不可用，即使obs是公开访问权限。

        :return: The url of this FileTranslationReq.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this FileTranslationReq.

        存放在OBS的文档文件路径，私密文件推荐使用临时授权URL调用服务，如何获取OBS文件URL和临时授权URL请参见配置OBS访问权限（https://support.huaweicloud.com/api-nlp/nlp_03_0080.html）。OBS的region要和请求服务的region保持一致，region不一致则OBS不可用，即使obs是公开访问权限。

        :param url: The url of this FileTranslationReq.
        :type url: str
        """
        self._url = url

    @property
    def _from(self):
        """Gets the _from of this FileTranslationReq.

        翻译原语言，文档翻译服务当前仅支持中英互译。

        :return: The _from of this FileTranslationReq.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this FileTranslationReq.

        翻译原语言，文档翻译服务当前仅支持中英互译。

        :param _from: The _from of this FileTranslationReq.
        :type _from: str
        """
        self.__from = _from

    @property
    def to(self):
        """Gets the to of this FileTranslationReq.

        翻译目标语言，文档翻译服务当前仅支持中英互译。

        :return: The to of this FileTranslationReq.
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this FileTranslationReq.

        翻译目标语言，文档翻译服务当前仅支持中英互译。

        :param to: The to of this FileTranslationReq.
        :type to: str
        """
        self._to = to

    @property
    def type(self):
        """Gets the type of this FileTranslationReq.

        文档格式，当前仅支持翻译“docx”、“pptx”和“txt”格式的文档。

        :return: The type of this FileTranslationReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FileTranslationReq.

        文档格式，当前仅支持翻译“docx”、“pptx”和“txt”格式的文档。

        :param type: The type of this FileTranslationReq.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, FileTranslationReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
