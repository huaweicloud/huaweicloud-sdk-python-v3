# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Subtitle:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'type': 'str',
        'language': 'str',
        'md5': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'language': 'language',
        'md5': 'md5',
        'description': 'description'
    }

    def __init__(self, id=None, type=None, language=None, md5=None, description=None):
        """Subtitle

        The model defined in huaweicloud sdk

        :param id: 字幕id。  取值范围：[1,8]。
        :type id: int
        :param type: 字幕文件类型，目前暂只支持“SRT”。
        :type type: str
        :param language: 字幕语言类型。  取值如下： - CN：表示中文字幕。 - EN：表示英文字幕。
        :type language: str
        :param md5: 字幕文件的MD5值。
        :type md5: str
        :param description: 字幕描述。
        :type description: str
        """
        
        

        self._id = None
        self._type = None
        self._language = None
        self._md5 = None
        self._description = None
        self.discriminator = None

        self.id = id
        self.type = type
        self.language = language
        if md5 is not None:
            self.md5 = md5
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this Subtitle.

        字幕id。  取值范围：[1,8]。

        :return: The id of this Subtitle.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Subtitle.

        字幕id。  取值范围：[1,8]。

        :param id: The id of this Subtitle.
        :type id: int
        """
        self._id = id

    @property
    def type(self):
        """Gets the type of this Subtitle.

        字幕文件类型，目前暂只支持“SRT”。

        :return: The type of this Subtitle.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Subtitle.

        字幕文件类型，目前暂只支持“SRT”。

        :param type: The type of this Subtitle.
        :type type: str
        """
        self._type = type

    @property
    def language(self):
        """Gets the language of this Subtitle.

        字幕语言类型。  取值如下： - CN：表示中文字幕。 - EN：表示英文字幕。

        :return: The language of this Subtitle.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Subtitle.

        字幕语言类型。  取值如下： - CN：表示中文字幕。 - EN：表示英文字幕。

        :param language: The language of this Subtitle.
        :type language: str
        """
        self._language = language

    @property
    def md5(self):
        """Gets the md5 of this Subtitle.

        字幕文件的MD5值。

        :return: The md5 of this Subtitle.
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this Subtitle.

        字幕文件的MD5值。

        :param md5: The md5 of this Subtitle.
        :type md5: str
        """
        self._md5 = md5

    @property
    def description(self):
        """Gets the description of this Subtitle.

        字幕描述。

        :return: The description of this Subtitle.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Subtitle.

        字幕描述。

        :param description: The description of this Subtitle.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, Subtitle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
