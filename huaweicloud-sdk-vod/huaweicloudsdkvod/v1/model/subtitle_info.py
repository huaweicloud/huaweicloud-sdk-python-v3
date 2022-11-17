# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubtitleInfo:

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
        'id': 'int',
        'type': 'str',
        'language': 'str'
    }

    attribute_map = {
        'url': 'url',
        'id': 'id',
        'type': 'type',
        'language': 'language'
    }

    def __init__(self, url=None, id=None, type=None, language=None):
        """SubtitleInfo

        The model defined in huaweicloud sdk

        :param url: 字幕文件的下载地址 
        :type url: str
        :param id: 字幕文件id 
        :type id: int
        :param type: 字幕文件类型 
        :type type: str
        :param language: 字幕文件语言种类 
        :type language: str
        """
        
        

        self._url = None
        self._id = None
        self._type = None
        self._language = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if language is not None:
            self.language = language

    @property
    def url(self):
        """Gets the url of this SubtitleInfo.

        字幕文件的下载地址 

        :return: The url of this SubtitleInfo.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SubtitleInfo.

        字幕文件的下载地址 

        :param url: The url of this SubtitleInfo.
        :type url: str
        """
        self._url = url

    @property
    def id(self):
        """Gets the id of this SubtitleInfo.

        字幕文件id 

        :return: The id of this SubtitleInfo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubtitleInfo.

        字幕文件id 

        :param id: The id of this SubtitleInfo.
        :type id: int
        """
        self._id = id

    @property
    def type(self):
        """Gets the type of this SubtitleInfo.

        字幕文件类型 

        :return: The type of this SubtitleInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SubtitleInfo.

        字幕文件类型 

        :param type: The type of this SubtitleInfo.
        :type type: str
        """
        self._type = type

    @property
    def language(self):
        """Gets the language of this SubtitleInfo.

        字幕文件语言种类 

        :return: The language of this SubtitleInfo.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this SubtitleInfo.

        字幕文件语言种类 

        :param language: The language of this SubtitleInfo.
        :type language: str
        """
        self._language = language

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
        if not isinstance(other, SubtitleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
